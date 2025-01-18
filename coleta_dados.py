from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, sys, os

# Definindo a classe
class ColetaDados:
    # Método inicializador (construtor)
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
    
    def __init__(self, url, diretorio_download):
        self.driver = self.definir_diretorio_download(diretorio_download)
        self.driver.get(url)
    
    def click(self, xpath, tempo_espera):
        try:
            elemento = WebDriverWait(self.driver, tempo_espera).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            elemento.click()  # Clique no menu para expandir
            print("Botão clicado!")
        except Exception as e:
            print("Erro ao clicar no botão.")
            raise
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
            raise
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
            raise
        return 1
    
    def preenche_selecao(self, xpath, opcao_desejada, tempo_espera):
        try:
            # Passo 1: Localizar o campo de seleção e clicar
            campo = WebDriverWait(self.driver, tempo_espera).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            campo.click()  # Abre o menu suspenso
            print(f"Campo '{xpath}' clicado!")

            # Passo 2: Localizar as opções correspondentes
            data_target = campo.get_attribute("data-target")  # Obter o identificador da lista de opções
            lista_opcoes_xpath = f'//ul[@id="{data_target}"]/li'
            opcoes = WebDriverWait(self.driver, tempo_espera).until(
                EC.presence_of_all_elements_located((By.XPATH, lista_opcoes_xpath))
            )
            
            # Passo 3: Iterar pelas opções e selecionar a desejada
            for opcao in opcoes:
                if opcao.text == opcao_desejada:
                    opcao.click()
                    print(f"Opção '{opcao_desejada}' selecionada com sucesso!")
                    return True

            print(f"Opção '{opcao_desejada}' não encontrada no campo '{xpath}'.")
            return False
        except Exception as e:
            print(f"Erro ao selecionar opção no campo '{xpath}': {e}")
            raise

    def aparece(self, xpath, tempo_espera):
        try:
            # Espera até que o texto de erro apareça se as credenciais forem inválidas
            WebDriverWait(self.driver, tempo_espera).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except Exception:
            return 0
        return 1
    
    def definir_diretorio_download(self, download_dir):
        download_dir = os.path.join(os.getcwd(), download_dir)
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

        # Iniciar o WebDriver com as opções configuradas
        driver = webdriver.Chrome(options=chrome_options)
        
        return driver

    def encerrar(self):
        time.sleep(5)
        self.driver.quit()  # Fecha o navegador
        sys.exit()  # Encerra o programa