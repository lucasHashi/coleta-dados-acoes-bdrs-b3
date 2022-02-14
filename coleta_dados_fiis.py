import pandas as pd
import json
from time import sleep
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

from auxiliar_constantes import URL_LINKS_FIIS



def main():
    df_fiis = coletar_dados_todos_fiis_B3()

    PASTA_DE_DADOS = 'dados_coletados'

    NOME_ARQUIVO_fiis = 'dados_completos_fiis'
    data_mes_hoje = datetime.today().strftime('%Y-%m')

    df_fiis.to_excel('{}\\{}_{}.xlsx'.format(PASTA_DE_DADOS, NOME_ARQUIVO_fiis, data_mes_hoje), index=False)
    df_fiis.to_pickle('{}\\{}_{}.pickle'.format(PASTA_DE_DADOS, NOME_ARQUIVO_fiis, data_mes_hoje))

    print(df_fiis)