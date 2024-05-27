from start_browser import IniciaNavegador
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class PopulacaoSC:

    @classmethod
    def main(cls):
        driver = IniciaNavegador._start_browser()

        try:
            wait = WebDriverWait(driver, 10)
            acao = ActionChains(driver)
            cls.executar(driver, wait, acao)
            return cls.coletar_dados(wait)
        except Exception as err:
            print(f"Erro {err}")
       
        driver.quit()

    @staticmethod
    def clicar_menu(wait, acao):
        try:
            menu = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="abaMenuLateral"]')))
            acao.click(on_element=menu).perform()
            sleep(1)
        except Exception as e:
            print(f"Erro ao clicar no menu: {e}")

    @staticmethod
    def clicar_estados(wait, acao):
        try:
            estados = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@id="menu__estado"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu__estado"]')))
            acao.click(on_element=estados).perform()
            sleep(1)
        except Exception as e:
            print(f"Erro ao clicar em estados: {e}")

    @staticmethod
    def clicar_sc(wait, acao):
        try:
            sc = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="segunda-coluna"]/ul/li[24]/div')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="segunda-coluna"]/ul/li[24]/div')))
            acao.click(on_element=sc).perform()
            sleep(1)
        except Exception as e:
            print(f"Erro ao clicar em Santa Catarina: {e}")

    @staticmethod
    def coletar_dados(wait):
        try:
            xpath_nome = '//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[2]'
            xpath_numero = '//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[3]/valor-indicador/div/span[1]'
            xpath_unidade = '//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[3]/valor-indicador/div/span[2]'

            dado = wait.until(EC.presence_of_element_located((By.XPATH, xpath_nome))).text
            numero = wait.until(EC.presence_of_element_located((By.XPATH, xpath_numero))).text
            unidade = wait.until(EC.presence_of_element_located((By.XPATH, xpath_unidade))).text.rstrip()

            
            dados = {
                        "dado": dado,
                        "numero": numero,
                        "unidade": unidade
                    }

            print(dados)            

            return dados
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
            return {}
    


    @classmethod
    def executar(cls, driver, wait, acao):
       
        url = "https://cidades.ibge.gov.br/"
        driver.get(url)
        sleep(2)

        cls.clicar_menu(wait, acao)
        cls.clicar_estados(wait, acao)
        cls.clicar_sc(wait, acao)






        

