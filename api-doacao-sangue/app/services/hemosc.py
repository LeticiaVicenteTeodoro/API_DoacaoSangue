import requests
from bs4 import BeautifulSoup

URL = "https://www.saude.sc.gov.br/index.php/pt/component/content/article/com-aumento-na-demanda-hemosc-chama-populacao-para-repor-estoques-de-sangue?Itemid=101&catid=84"

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]


def coletar_estoque_hemosc():
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text(" ", strip=True).lower()

        estoque = {}

        if "tipos sanguíneos a e o, positivo e negativo" in texto or "a e o, positivo e negativo" in texto:
            estoque = {
                "O+": "Alerta",
                "O-": "Alerta",
                "A+": "Alerta",
                "A-": "Alerta",
                "B+": "Adequado",
                "B-": "Adequado",
                "AB+": "Adequado",
                "AB-": "Adequado",
            }
        else:
            estoque = {
                tipo: "Não informado"
                for tipo in TIPOS
            }

        print("ESTOQUE HEMOSC:", estoque)

        return estoque

    except Exception as e:
        print("ERRO HEMOSC:", e)
        return None