from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys
import os

# Definindo a classe
class ColetaDados:
    # Método inicializador (construtor)
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
    
    # Método para mostrar informações do carro
    def click(self, xpath, tempo_espera):
        try:
            elemento = WebDriverWait(self.driver, tempo_espera).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            elemento.click()  # Clique no menu para expandir
            print("Botão clicado!")
        except:
            print("Erro ao clicar no botão.")
            return 0
        return 1
    
    def preenche_campo(self, id, informacao, tempo_espera ):
        try:
            input = WebDriverWait(self.driver, tempo_espera).until(
                EC.visibility_of_element_located((By.ID, id))
            )
            input.send_keys(informacao)
            print(f"{id} preenchido!")
        except Exception as e:
            print(f"Erro ao preencher o campo de {id}: {e}")
            return 0
        return 1

    def preenche_campo_enter(self, id, informacao, tempo_espera ):
            try:
                input = WebDriverWait(self.driver, tempo_espera).until(
                    EC.visibility_of_element_located((By.ID, id))
                )
                input.send_keys(informacao)
                input.send_keys(Keys.RETURN)  # Simula pressionamento de Enter
                print(f"{id} preenchido!")
            except Exception as e:
                print(f"Erro ao preencher o campo de {id}: {e}")
                return 0
            return 1
    
    def preenche_selecao(self, xpath, opcao, tempo_espera):
       # Espera até o input (campo de texto) estar presente
        campo_input = WebDriverWait(self.driver, tempo_espera).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        # Passo 1: Clicar no campo de texto para abrir o menu
        campo_input.click()

        # Passo 2: Esperar que as opções apareçam no dropdown
        opcoes_dropdown = WebDriverWait(self.driver, tempo_espera).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

        # Passo 3: Selecionar a opção desejada (por texto)
        for opcao in opcoes_dropdown:
            if opcao.text == opcao:
                opcao.click()
                print(f"Opção '{opcao.text}' selecionada com sucesso!")
                break


    def aparece(self, xpath, tempo_espera):
        try:
            # Espera até que o texto de erro apareça se as credenciais forem inválidas
            WebDriverWait(self.driver, tempo_espera).until(
                EC.visibility_of_element_located((By.XPATH, xpath))  # Substitua pelo texto exato
            )
        except:
            return 0
        return 1
    
    def definir_diretorio_download(download_dir):
        # Garantir que o diretório exista
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Configurar o ChromeOptions para definir o diretório de download
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,  # Define o diretório de download
            "download.prompt_for_download": False,        # Impede o prompt de download
            "directory_upgrade": True                     # Permite substituir arquivos sem aviso
        })

    def encerrar(self):
        time.sleep(5)
        self.driver.quit()  # Fecha o navegador
        sys.exit()  # Encerra o programa