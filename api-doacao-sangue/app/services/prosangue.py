from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import re

URL = "https://www.portal.prosangue.sp.gov.br/fps"

TIPOS = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]


def normalizar_status(texto):
    texto = texto.lower()

    if "crít" in texto or "crit" in texto:
        return "Critico"

    if "alerta" in texto or "baixo" in texto:
        return "Alerta"

    if "estável" in texto or "estavel" in texto:
        return "Estavel"

    if "adequado" in texto or "normal" in texto:
        return "Adequado"

    return texto.title()


def coletar_estoque_prosangue():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9223")
    options.add_argument("--window-size=1920,1080")

    driver = None

    try:
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(URL)
        time.sleep(8)

        texto = driver.find_element(By.TAG_NAME, "body").text

        print("===== TEXTO DA PÁGINA PRÓ-SANGUE =====")
        print(texto[:3000])
        print("===== FIM DO TEXTO =====")

        estoque = {}

        for tipo in TIPOS:
            padrao = rf"{re.escape(tipo)}[\s\S]{{0,80}}?(Crítico|Critico|Alerta|Estável|Estavel|Adequado|Baixo|Normal)"
            resultado = re.search(padrao, texto, re.IGNORECASE)

            if resultado:
                estoque[tipo] = normalizar_status(resultado.group(1))

        print("ESTOQUE PRÓ-SANGUE:", estoque)

        return estoque

    except Exception as e:
        print("ERRO PRÓ-SANGUE:", e)
        return None

    finally:
        if driver:
            driver.quit()