import coleta_dados as cd
import sys

def coleda_dados_brasil(username, password, universidade = "Todos", campus = "", curso = "Todos", turno = "Todos", grau = "Todos"):

    menu = "/html/body/nav/div/a[2]/i"

    sua_conta = ""
    login = ""

    erro = "/html/body/main/div/div/p"

    dataset = "/html/body/main/section[2]/div/div[2]/a/div"
    botao_seta = "/html/body/main/div/div[2]/div[1]/div/div[1]/div[2]"
    botao_cursos = "/html/body/main/div/div[2]/div[1]/div/div[2]/div/a/b"

    campo_universidade = '//*[@id="data"]/div[1]/div/form/div[1]/div[4]/div/input'
    botao_campus = '//*[@id="data"]/div[1]/div/form/div[1]/div[5]/label'
    campo_campus = '//*[@id="id_campus_nome"]'
    campo_curso = '//*[@id="data"]/div[1]/div/form/div[1]/div[6]/div/input'
    campo_turno = '//*[@id="data"]/div[1]/div/form/div[1]/div[8]/div/input'
    campo_grau = '//*[@id="data"]/div[1]/div/form/div[1]/div[7]/div/input'

    botao_filtrar = '//*[@id="data"]/div[1]/div/form/div[2]/input'
    botao_baixar = '//*[@id="data"]/div[2]/div[1]/a[1]'

    pesquisa = "Cursos e notas de corte do PROUNI 2018"
    download_dir = "downloads"

    coleta = cd.ColetaDados("https://brasil.io/home/", download_dir)

    # Passo 1: Verificar se o menu hambúrguer está visível
    if (coleta.click(menu, 10)):
        sua_conta = '//*[@id="mobile-demo"]/li[1]/a'
        login = '//*[@id="mobile_unauthenticated-dropdown"]/li[2]/a'
    else:
        sua_conta = '/html/body/nav/div/ul/li[1]/a/i'
        login = '//*[@id="desktop_unauthenticated-dropdown"]/li[2]/a'

    try:
        # Passo 2: Clicar na seta "Sua Conta"
        coleta.click(sua_conta, 5)
            
        # Passo 3: Clicar no botão "Login"
        coleta.click(login, 5)
            
        # Passo 4: Preencher o campo de login
        coleta.preenche_campo("id_username", username, 5)
            
        # Passo 5: Preencher o campo de senha (se aplicável)
        coleta.preenche_campo_enter("id_password", password, 5)
            
        # Passo 6: Verificar se o login foi bem-sucedido ou se o erro de login foi exibido
        if(coleta.aparece(erro, 5)):
            print("Usuário ou senha incorretos.")
            
        else:
            print("Login efetuado com sucesso.")

        # Passo 7: Clicar no botão "Dataset"
        coleta.click(dataset, 5)
            
        # Passo 8: Preencher o campo de pesquisa
        coleta.preenche_campo_enter("id_search", pesquisa, 5)

        # Passo 9: Clicar na seta e em "cursos"
        coleta.click(botao_seta, 5)
        coleta.click(botao_cursos, 5)
            
        # Passo 10: Preencher o campos de filtro
        # Filtrando pela universidade
        coleta.preenche_selecao(campo_universidade, universidade, 5)
            
        # Filtrando pelo nome do campus
        if (campus != ""):
            coleta.click(botao_campus, 10)
            coleta.preenche_campo(campo_campus, campus, 10)
        
        # Filtrando pelo curso
        coleta.preenche_selecao(campo_curso, curso, 10)
            
        # Filtrando pelo turno
        coleta.preenche_selecao(campo_turno, turno, 10)
            
        # Filtrando pelo grau
        coleta.preenche_selecao(campo_grau, grau, 10)
            
        # Passo 11: Clicar no botão "filtrar"
        coleta.click(botao_filtrar, 10)

        # Passo 12: Clicar no botão "baixar" para salvar o csv
        coleta.click(botao_baixar, 10)
            
    except Exception as e:
        return e
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