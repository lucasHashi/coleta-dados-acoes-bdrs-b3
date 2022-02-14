import pandas as pd
import json
from time import sleep
from datetime import datetime

import requests
requests.adapters.DEFAULT_RETRIES = 5
from requests.packages.urllib3.util.retry import Retry

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

from auxiliar_constantes import URL_BASE_DADOS_ACAO, URLS_IPOS_POR_ANO


def main():
    df_acoes = coletar_dados_todos_acoes_B3()

    PASTA_DE_DADOS = 'dados_coletados'

    NOME_ARQUIVO_ACOES = 'dados_completos_acoes'
    data_mes_hoje = datetime.today().strftime('%Y-%m')

    df_acoes.to_excel('{}\\{}_{}.xlsx'.format(PASTA_DE_DADOS, NOME_ARQUIVO_ACOES, data_mes_hoje), index=False)
    df_acoes.to_pickle('{}\\{}_{}.pickle'.format(PASTA_DE_DADOS, NOME_ARQUIVO_ACOES, data_mes_hoje))

    print(df_acoes)



def coletar_dados_todos_acoes_B3():
    # Iniciar um df vazio pra ser o completo
    df_acoes = pd.DataFrame()

    # Inicia driver

    # ----- TESTE COM O BEAUTIFUL SOUP -----
    # session = requests.Session()
    # session.keep_alive = False
    # retry = Retry(connect=3, backoff_factor=0.5)
    # adapter = HTTPAdapter(max_retries=retry)
    # session.mount('http://', adapter)
    # session.mount('https://', adapter)
    # result_url = session.get(url_atual)
    # soup = BeautifulSoup(result_url.text, 'html.parser')

    # ----- TESTE COM SELENIUM -----
    ua = UserAgent()
    user_agent = ua.random # User aleatorio

    chrome_options = Options()
    chrome_options.add_argument('user-agent={}'.format(user_agent))
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), # Download temporario do webdriver
        chrome_options=chrome_options
    )

    # Para cada ano
    for _, lista_urls in URLS_IPOS_POR_ANO.items():
        # Para cada paginacao
        for url_atual in lista_urls:
            # Pegar json com todas as acoes dessa pagina

            driver.get(url_atual)

            string_json_dados_da_acao = driver.find_element_by_css_selector('body').text
            json_dados_da_acao = json.loads(string_json_dados_da_acao)

            # Passar pra Dataframe
            df_acoes_url_atual = pd.json_normalize(json_dados_da_acao['results'])
            
            # Juntar com o df completo
            df_acoes = df_acoes.append(df_acoes_url_atual)

    driver.close()

    df_acoes.drop('segment', axis=1, inplace=True)

    df_acoes.rename(columns={
        'codeCVM': 'cod_cvm',
        'issuingCompany': 'issuing_company',
        'companyName': 'company_name',
        'tradingName': 'trading_name',
        'cnpj': 'cnpj',
        'marketIndicator': 'market_indicator',
        'typeBDR': 'type_bdr',
        'dateListing': 'date_listing',
        'status': 'status',
        'segmentEng': 'segment_eng',
        'type': 'type',
        'market': 'market'
    }, inplace=True)

    # df_acoes = df_acoes.iloc[:5, :]

    # Coleta dos dados que nao estao aqui
    df_acao_dados_adicionais = coletar_dados_acomplementares_acoes(df_acoes)

    df_acoes = df_acoes.merge(df_acao_dados_adicionais, left_on='cod_cvm', right_on='cod_cvm')

    # Conversao das colunas
    df_acoes['date_listing'] = pd.to_datetime(df_acoes['date_listing'])

    df_acoes['market_indicator'] = pd.to_numeric(df_acoes['market_indicator'])
    df_acoes['type'] = pd.to_numeric(df_acoes['type'])

    # Separa tickers em linhas diferentes
    df_acoes = df_acoes.explode('all_tickers')

    df_acoes[['ticker', 'cod_isin']] = df_acoes['all_tickers'].astype(str).str.split("', '", expand=True)
    df_acoes['ticker'] = df_acoes['ticker'].str[12:]
    df_acoes['cod_isin'] = df_acoes['cod_isin'].str[12:-2]

    return df_acoes

def coletar_dados_acomplementares_acoes(df_acoes):
    ua = UserAgent()
    user_agent = ua.random # User aleatorio

    chrome_options = Options()
    chrome_options.add_argument('user-agent={}'.format(user_agent))
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), # Download temporario do webdriver
        chrome_options=chrome_options
    )

    df_acao_dados_adicionais = pd.DataFrame()
    for _, linha_acao in df_acoes.iterrows():
        cod_cvm, ticker = linha_acao[['cod_cvm', 'issuing_company']]

        # Acessar url com selenium
        url_dados_acao = URL_BASE_DADOS_ACAO.format(cod_cvm, ticker)

        driver.get(url_dados_acao)
        driver.implicitly_wait(5)
        sleep(1)

        lista_dados_adicionais = coletar_dados_extras_acao(driver, cod_cvm)
        nomes_colunas_dados = ['cod_cvm', 'sector', 'subsector', 'segment', 'main_activity', 'all_tickers', 'site', 'bookkeeper']

        linha_dados_edicionais = dict(zip(nomes_colunas_dados, lista_dados_adicionais))

        df_acao_dados_adicionais = df_acao_dados_adicionais.append(linha_dados_edicionais, ignore_index=True)
    
    driver.close()

    return df_acao_dados_adicionais



def coletar_dados_extras_acao(driver, cod_cvm):
    """Dos dados de uma acao, acessa o site e
    coleta alguns que nao foram ainda carregados

    Args:
        linha_acao (DataFrame): Linha dos dados

    Returns:
        List: Dados adicionais
    """

    # Coletar os dados que nao tinha ainda:
    tags_p = driver.find_elements_by_css_selector('div[class="card-body"] p')
    tags_p_textos = [p.text for p in tags_p]

    setor_economico, subsetor, segmento = '', '', ''
    atividade_principal, site, escriturador = '', '', ''
    for index, tag_p in enumerate(tags_p_textos):
        # setor_economico, subsetor, segmento
        if tag_p == 'Classificação Setorial':
            segmento_texto = tags_p_textos[index+1]
            setor_economico, subsetor, segmento = segmento_texto.split(' / ')
        # atividade_principal
        elif tag_p == 'Atividade Principal':
            atividade_principal = tags_p_textos[index+1]
        # site
        elif tag_p == 'Site':
            site = tags_p_textos[index+1]
        # escriturador
        elif tag_p == 'Escriturador':
            escriturador = tags_p_textos[index+1]
            escriturador = escriturador.split(': ')[1]

    # tickers, codigo_isin
    try:
        table_html_tickers = driver.find_element_by_css_selector('div[class="card-body"] div[id="accordion"] div[id="accordionBody2"] div table').get_attribute('outerHTML')
        df_tickers = pd.read_html(table_html_tickers)[0]
        df_tickers = df_tickers.iloc[1:, :]
        df_tickers.columns = ['ticker', 'cod_isin']
        outros_tickers = df_tickers.to_dict('records')
    except NoSuchElementException as er:
        outros_tickers = []

    # Retornar dados extras
    return [cod_cvm, setor_economico, subsetor, segmento, atividade_principal, outros_tickers, site, escriturador]





if __name__ == "__main__":
    main()