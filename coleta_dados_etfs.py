import pandas as pd
import json
from time import sleep
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager

from auxiliar_constantes import URL_LINKS_ETFS



def main():
    df_etfs = coletar_dados_todos_etfs_B3()

    PASTA_DE_DADOS = 'dados_coletados'

    NOME_ARQUIVO_ETFS = 'dados_completos_etfs'
    data_mes_hoje = datetime.today().strftime('%Y-%m')

    df_etfs.to_excel('{}\\{}_{}.xlsx'.format(PASTA_DE_DADOS, NOME_ARQUIVO_ETFS, data_mes_hoje), index=False)
    df_etfs.to_pickle('{}\\{}_{}.pickle'.format(PASTA_DE_DADOS, NOME_ARQUIVO_ETFS, data_mes_hoje))

    print(df_etfs)