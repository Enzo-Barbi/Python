from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class IniciaNavegador:

    @staticmethod
    def _start_browser():
        driver = None
        try:
            print("Iniciando Navegador")
            
            options = webdriver.ChromeOptions()
            options.add_argument("--headless") # <----- If you want see the navigator doing all process, just comment this line
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        
        except Exception as e:
            print(f"Erro ao abrir o navegador: {e}")
        
        return driver