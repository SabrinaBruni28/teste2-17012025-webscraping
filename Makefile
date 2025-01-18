# Definindo valores padrão
UNIVERSIDADE ?= "Todos"
CAMPUS ?= ""
CURSO ?= "Todos"
TURNO ?= "Todos"
GRAU ?= "Todos"

# Alvo padrão
help:
	@echo "Uso: make teste USERNAME=<username> PASSWORD=<password> UNIVERSIDADE=<universidade> CAMPUS=<campus> CURSO=<curso> TURNO=<turno> GRAU=<grau>"
	@echo ""
	@echo "Parâmetros:"
	@echo "  USERNAME     - Nome de usuário"
	@echo "  PASSWORD     - Senha"
	@echo "  UNIVERSIDADE - Nome da universidade (padrão: $(UNIVERSIDADE))"
	@echo "  CAMPUS       - Nome do campus (padrão: $(CAMPUS))"
	@echo "  CURSO        - Nome do curso (padrão: $(CURSO))"
	@echo "  TURNO        - Turno do curso (padrão: $(TURNO))"
	@echo "  GRAU         - Grau do curso (padrão: $(GRAU))"

# Alvo para rodar o script Python
teste:
	@echo "Iniciando o processo com os seguintes parâmetros:"
	@echo "USERNAME: $(USERNAME)"
	@echo "PASSWORD: $(PASSWORD)"
	@echo "UNIVERSIDADE: $(UNIVERSIDADE)"
	@echo "CAMPUS: $(CAMPUS)"
	@echo "CURSO: $(CURSO)"
	@echo "TURNO: $(TURNO)"
	@echo "GRAU: $(GRAU)"
	@PYTHONDONTWRITEBYTECODE=1 python3 teste2.py "$(USERNAME)" "$(PASSWORD)" "$(UNIVERSIDADE)" "$(CAMPUS)" "$(CURSO)" "$(TURNO)" "$(GRAU)"
