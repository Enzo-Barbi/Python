from start_browser import IniciaNavegador
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from flask import jsonify

from time import sleep

class Pesquisa:

    json_teste = [{"values":["python"],"attribute":"linguagem","operator":"equal"},
                {"values":["Almir Dapper"],"attribute":"nome","operator":"equal"}]
    

    @classmethod
    def main(cls):
        driver = IniciaNavegador._start_browser()
        cls.barra_pesquisa_google(driver)
        sleep(3)
        return cls.retorna_links(driver)
   
    @classmethod
    def barra_pesquisa_google(cls, driver):
        cls.acessa_google(driver)
        barra_pesquisa = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        cls.clica_barra_pesquisa(driver, barra_pesquisa)
        sleep(2)
        cls.pesquisa_dado(barra_pesquisa)

    @staticmethod
    def acessa_google(driver):
        try:
            url = 'https://www.google.com/'
            driver.get(url)
        except:
            print("Erro ao acessar URL")

    @staticmethod
    def clica_barra_pesquisa(driver, elemento):
        action = ActionChains(driver)
        try:
            action.click(on_element=elemento).perform()
        except:
            print("Erro ao clicar no elemento")

    @classmethod
    def pesquisa_dado(cls, barra_pesquisa):
        valor = cls.coleta_dado_json(cls.json_teste)
        barra_pesquisa.send_keys(valor)
        barra_pesquisa.send_keys(Keys.ENTER)

    @classmethod
    def coleta_dado_json(cls, json):
        try:
            return json[0]['values'][0]
        except:
            print("Erro ao retornar dado do JSON")

    @classmethod
    def retorna_links(cls, driver):
        try:
            lista_elementos = driver.find_elements(By.XPATH, '//span/a[@jsname="UWckNb"]')
            dict_links = {}
            for i, link in enumerate(lista_elementos, start=1):
                dict_links[f"link{i}"] = link.get_attribute('href')
                if len(dict_links) >= 5:
                    break
        except:
            print("erro ao coletar links")
        
        return dict_links