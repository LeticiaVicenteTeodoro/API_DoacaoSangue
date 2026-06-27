import requests
from bs4 import BeautifulSoup

URL = "https://www.hemopa.pa.gov.br/"

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]


def coletar_estoque_hemopa():
    try:
        response = requests.get(
            URL,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        print("STATUS HEMOPA:", response.status_code)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text(" ", strip=True).lower()

        print("TEXTO HEMOPA:", texto[:1500])

        estoque = {tipo: "Adequado" for tipo in TIPOS}

        if "o negativo" in texto or "o-" in texto:
            estoque["O-"] = "Alerta"

        if "o positivo" in texto or "o+" in texto:
            estoque["O+"] = "Alerta"

        if "a negativo" in texto or "a-" in texto:
            estoque["A-"] = "Alerta"

        if "a positivo" in texto or "a+" in texto:
            estoque["A+"] = "Alerta"

        if "todos os tipos" in texto and (
            "baixo" in texto
            or "baixa" in texto
            or "crítico" in texto
            or "critico" in texto
        ):
            for tipo in TIPOS:
                estoque[tipo] = "Alerta"

        print("ESTOQUE HEMOPA:", estoque)

        return estoque

    except Exception as e:
        print("ERRO HEMOPA:", e)
        return None