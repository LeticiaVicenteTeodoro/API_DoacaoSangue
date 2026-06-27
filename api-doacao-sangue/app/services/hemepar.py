import requests
from bs4 import BeautifulSoup

URL = "https://www.parana.pr.gov.br/aen/Noticia/Com-queda-nos-estoques-Hemepar-convoca-doadores-de-sangue-tipos-O-e-O"

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]


def coletar_estoque_hemepar():
    try:
        response = requests.get(
            URL,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        print("STATUS HEMEPAR:", response.status_code)
        print("URL FINAL:", response.url)
        print("TRECHO HTML:", response.text[:500])

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text(" ", strip=True).lower()

        print("TEXTO HEMEPAR:", texto[:1500])

        estoque = {tipo: "Adequado" for tipo in TIPOS}

        if "o+" in texto or "tipo o positivo" in texto:
            estoque["O+"] = "Alerta"

        if "o-" in texto or "tipo o negativo" in texto:
            estoque["O-"] = "Alerta"

        print("ESTOQUE HEMEPAR:", estoque)

        return estoque

    except Exception as e:
        print("ERRO HEMEPAR:", e)
        return None