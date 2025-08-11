import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def configurar_re605x_com_selenium(ssid, senha):
    navegador = detectar_navegador()
    if not navegador:
        print("Nenhum navegador compatível encontrado.")
        return

    driver = iniciar_driver(navegador)
    if not driver:
        print("Falha ao iniciar o navegador.")
        return

    try:
        driver.get("http://tplinkrepeater.net")

        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "login-password"))
            )
        except TimeoutException:
            print("Interface do repetidor não está pronta ou não é compatível.")
            driver.quit()
            return

        driver.find_element(By.ID, "login-password").send_keys("admin")
        driver.find_element(By.ID, "login-button").click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ssid-input"))
            )
        except TimeoutException:
            print("Campo de SSID não encontrado após login. Interface pode ter mudado.")
            driver.quit()
            return

        driver.find_element(By.ID, "ssid-input").clear()
        driver.find_element(By.ID, "ssid-input").send_keys(ssid)

        driver.find_element(By.ID, "password-input").clear()
        driver.find_element(By.ID, "password-input").send_keys(senha)

        driver.find_element(By.ID, "confirm-button").click()
        time.sleep(5)

        print("Configuração concluída com sucesso.")
        print("🕶️ O navegador permanecerá aberto para revisão.")
        input("Pressione Enter para fechar o navegador...")
        driver.quit()

    except NoSuchElementException:
        print("Elemento esperado não encontrado. Verifique a versão da interface.")
        driver.quit()
    except Exception as e:
        print("Erro durante a automação:", e)
        driver.quit()

def detectar_navegador():
    if shutil.which("chrome") or shutil.which("google-chrome"):
        return "chrome"
    elif shutil.which("msedge"):
        return "edge"
    elif shutil.which("firefox"):
        return "firefox"
    return None

def iniciar_driver(navegador):
    try:
        if navegador == "chrome":
            options = ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        elif navegador == "edge":
            options = EdgeOptions()
            service = EdgeService(EdgeChromiumDriverManager().install())
            return webdriver.Edge(service=service, options=options)
        elif navegador == "firefox":
            options = FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)
    except Exception as e:
        print(f"Erro ao iniciar {navegador}: {e}")
        return None