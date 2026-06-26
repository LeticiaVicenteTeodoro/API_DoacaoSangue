from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

URL = "https://hemominas.mg.gov.br"

TIPOS = [
    "O+",
    "O-",
    "A+",
    "A-",
    "B+",
    "B-",
    "AB+",
    "AB-",
]


def coletar_estoque_hemominas():
    options = Options()

    # Mais estável no Windows
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")

    driver = None

    try:
        service = Service()
        driver = webdriver.Chrome(
            service=service,
            options=options
        )

        driver.get(URL)

        time.sleep(5)

        elementos = driver.find_elements(
            By.CSS_SELECTOR,
            "div"
        )

        estoque = {}

        for el in elementos:
            try:
                tipo = el.find_element(
                    By.TAG_NAME,
                    "b"
                ).text.strip()

                status = el.find_element(
                    By.TAG_NAME,
                    "p"
                ).text.strip()

                if tipo in TIPOS:
                    estoque[tipo] = status

            except Exception:
                continue

        print("ESTOQUE COLETADO:", estoque)

        return estoque

    except Exception as e:
        print("ERRO HEMOMINAS:", e)
        return None

    finally:
        if driver:
            driver.quit()