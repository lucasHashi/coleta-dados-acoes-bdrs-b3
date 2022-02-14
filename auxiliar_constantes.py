

# ---------------- ETFS ----------------

URL_LINKS_ETFS = 'https://sistemaswebb3-listados.b3.com.br/fundsPage/3'


# ---------------- FIIS ----------------

URL_LINKS_FIIS = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'


# ---------------- ACOES ----------------

URL_BASE_DADOS_ACAO = 'https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/main/{}/{}/overview?language=pt-br' # .format(codigo_acao, ticker)

URLS_IPOS_POR_ANO = {
    2022: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDIyfQ=='
    ],
    2021: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwieWVhciI6MjAyMX0='
    ],
    2020: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwieWVhciI6MjAyMH0='
    ],
    2019: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE5fQ=='
    ],
    2018: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE4fQ=='
    ],
    2017: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE3fQ=='
    ],
    2016: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE2fQ=='
    ],
    2015: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE1fQ=='
    ],
    2014: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDE0fQ=='
    ],
    2013: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDEzfQ=='
    ],
    2012: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDEyfQ=='
    ],
    2011: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDExfQ=='
    ],
    2010: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDEwfQ=='
    ],
    2009: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA5fQ=='
    ],
    2008: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA4fQ=='
    ],
    2007: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA3fQ=='
    ],
    2006: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA2fQ=='
    ],
    2005: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA1fQ=='
    ],
    2004: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDA0fQ=='
    ],
    2003: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDAzfQ=='
    ],
    2002: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDAyfQ=='
    ],
    2001: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDAxfQ=='
    ],
    2000: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoyMDAwfQ=='
    ],
    1999: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoxOTk5fQ=='
    ],
    1998: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjIwLCJ5ZWFyIjoxOTk4fQ=='
    ],
    1997: [
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwieWVhciI6MTk5N30=',
        'https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetYearListing/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MiwicGFnZVNpemUiOjEyMCwieWVhciI6MTk5N30='
    ]
}