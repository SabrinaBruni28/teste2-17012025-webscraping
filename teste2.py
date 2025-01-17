import coleta_dados as cd
import sys

def coleda_dados_brasil(username, password, universidade, campus, curso, turno, grau):
    coleta = cd.ColetaDados("https://brasil.io/home/")

    menu = "/html/body/nav/div/a[2]/i"

    sua_conta = ""
    login = ""

    erro = "/html/body/main/div/div/p"

    dataset = "/html/body/main/section[2]/div/div[2]/a/div"
    botao_seta = "/html/body/main/div/div[2]/div[1]/div/div[1]/div[2]"
    botao_cursos = "/html/body/main/div/div[2]/div[1]/div/div[2]/div/a/b"

    campo_universidade = '//*[@id="data"]/div[1]/div/form/div[1]/div[4]/div/input'
    campo_campus = '//*[@id="id_campus_nome"]'
    campo_curso = '//*[@id="data"]/div[1]/div/form/div[1]/div[6]/div/input'
    campo_turno = '//*[@id="data"]/div[1]/div/form/div[1]/div[8]/div/input'
    campo_grau = '//*[@id="data"]/div[1]/div/form/div[1]/div[7]/div/input'

    botao_baixar = '//*[@id="data"]/div[2]/div[1]/a[1]'

    pesquisa = "Cursos e notas de corte do PROUNI 2018"
    download_dir = "/downloads/"

    # Passo 1: Verificar se o menu hambúrguer está visível
    if (coleta.click(menu, 10)):
        sua_conta = '//*[@id="mobile-demo"]/li[1]/a'
        login = '//*[@id="mobile_unauthenticated-dropdown"]/li[2]/a'
    else:
        sua_conta = '/html/body/nav/div/ul/li[1]/a/i'
        login = '//*[@id="desktop_unauthenticated-dropdown"]/li[2]/a'

    # Passo 2: Clicar na seta "Sua Conta"
    if (not coleta.click(sua_conta, 5)):
        coleta.encerrar()

    # Passo 3: Clicar no botão "Login"
    if(not coleta.click(login, 5)):
        coleta.encerrar()

    # Passo 3: Preencher o campo de login
    if(not coleta.preenche_campo("id_username", username, 5)):
        coleta.encerrar()

    # Passo 4: Preencher o campo de senha (se aplicável)
    if(not coleta.preenche_campo_enter("id_password", password, 5)):
        coleta.encerrar()

    # Passo 5: Verificar se o login foi bem-sucedido ou se o erro de login foi exibido
    if(coleta.aparece(erro, 5)):
        print("Usuário ou senha incorretos.")
        coleta.encerrar()
    else:
        print("Login efetuado com sucesso.")

    # Passo 6: Clicar no botão "Dataset"
    if(not coleta.click(dataset, 5)):
        coleta.encerrar()

    # Passo 7: Preencher o campo de pesquisa
    if(not coleta.preenche_campo_enter("id_search", pesquisa, 5)):
        coleta.encerrar()

    # Passo 8: Clicar na seta e em "cursos"
    if(not coleta.click(botao_seta, 5)):
        coleta.encerrar()
    if(not coleta.click(botao_cursos, 5)):
        coleta.encerrar()

    # Passo 9: Preencher o campos de filtro
    # Filtrando pela universidade
    if (not coleta.preenche_selecao(campo_universidade, universidade, 5)):
        coleta.encerrar()
    # Filtrando pelo nome do campus
    if (not coleta.preenche_campo(campo_campus, campus, 5)):
        coleta.encerrar()
    # Filtrando pelo curso
    if (not coleta.preenche_selecao(campo_curso, curso, 5)):
        coleta.encerrar()
    # Filtrando pelo turno
    if (not coleta.preenche_selecao(campo_turno, turno, 5)):
        coleta.encerrar()
    # Filtrando pelo grau
    if (not coleta.preenche_selecao(campo_grau, grau, 5)):
        coleta.encerrar()

    # Passo 10: Clicar no botão "baixar" para salvar o csv
    coleta.definir_diretorio_download(download_dir)
    if(not coleta.click(botao_baixar, 5)):
        coleta.encerrar()

    coleta.encerrar()

# Captura os parâmetros da linha de comando
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    universidade = sys.argv[3]
    campus = sys.argv[4]
    curso = sys.argv[5]
    turno = sys.argv[6]
    grau = sys.argv[7]

    coleda_dados_brasil(username, password, universidade, campus, curso, turno, grau)