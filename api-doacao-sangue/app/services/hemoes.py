import requests
from bs4 import BeautifulSoup

URL = "https://hemoes.es.gov.br/"

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]


def coletar_estoque_hemoes():
    try:
        response = requests.get(
            URL,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        print("STATUS HEMOES:", response.status_code)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text(" ", strip=True).lower()

        estoque = {tipo: "Adequado" for tipo in TIPOS}

        if "todos os tipos" in texto and ("baixa" in texto or "crítico" in texto or "critico" in texto):
            for tipo in TIPOS:
                estoque[tipo] = "Alerta"

        if "o+" in texto:
            estoque["O+"] = "Alerta"

        if "o-" in texto:
            estoque["O-"] = "Alerta"

        if "a+" in texto:
            estoque["A+"] = "Alerta"

        if "a-" in texto:
            estoque["A-"] = "Alerta"

        print("ESTOQUE HEMOES:", estoque)

        return estoque

    except Exception as e:
        print("ERRO HEMOES:", e)
        return None