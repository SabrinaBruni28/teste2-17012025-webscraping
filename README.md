<p style="text-align:center" dir="auto">
  <a href="#desafio1">Teste 2</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<h2 id="desafio1" style="text-align:center;border-bottom:none">Teste 2</h2>

Neste teste, você precisa desenvolver uma aplicação para coletar dados do site <a href="https://brasil.io/home/" target="_blank">brasil.io</a>. Seguem as etapas que sua aplicação deve obrigatoriamente seguir ao ser executada:

1) Iniciar pela URL https://brasil.io/home/, simulando sempre a interação de um usuário real.
2) Realizar o login no site antes de qualquer consulta ou extração de dados.
3) Acessar o dataset “Cursos e notas de corte do PROUNI 2018” para os cursos.
4) Filtre pela Universidade, informada como entrada da aplicação.
5) Filtre pelo Nome do Campus, também informado como entrada da aplicação.
6) Filtre pelo Curso, informado como entrada da aplicação.
7) Filtre pelo Turno, informado como entrada da aplicação.
8) Filtre pelo Grau, informado como entrada da aplicação.
9) Baixe o arquivo CSV resultante do filtro.
10) Mova o arquivo CSV baixado para o diretório downloads/ na raiz da aplicação. Se esse diretório não existir, a aplicação deve criá-lo automaticamente.

### Requisitos dos Desafios:
1) Utilize a linguagem Python para desenvolver a solução.
2) No mesmo README, inclua uma seção detalhada que explique claramente os passos necessários para executar o código. Certifique-se de que as instruções sejam precisas, organizadas e fáceis de entender, pois os avaliadores seguirão essa documentação.
3) Faça um fork do repositório.
4) A entrega deve ser realizada por meio de um pull request para o repositório original.
5) Envie seus commits para o GitHub faltando 5 minutos para o prazo final do teste. Não faça antes, pois você pode expor informações do seu teste para os demais participantes.
6) Abra o pull request também faltando 5 minutos para o prazo final da entrega do teste.
7) A entrega deve ser realizada dentro do prazo estabelecido.

## Como executar:
* Para executar é necessário o selenium:
  - Para instalar digite no terminal`sudo pip install selenium`

* Para executar digite:
  - `make teste USERNAME=username PASSWORD=senha UNIVERSIDADE=universidade CAMPUS=campus CURSO=curso TURNO=turno GRAU=grau`
  - Ou `make` para ver como executar
