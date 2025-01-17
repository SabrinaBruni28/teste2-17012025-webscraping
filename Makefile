# Alvo padrão
help:
	@echo "Uso: make teste USERNAME=<username> PASSWORD=<password> UNIVERSIDADE=<universidade> CAMPUS=<campus> CURSO=<curso> TURNO=<turno> GRAU=<grau>"
	@echo ""
	@echo "Parâmetros:"
	@echo "  USERNAME     - Nome de usuário"
	@echo "  PASSWORD     - Senha"
	@echo "  UNIVERSIDADE - Nome da universidade"
	@echo "  CAMPUS       - Nome do campus"
	@echo "  CURSO        - Nome do curso"
	@echo "  TURNO        - Turno do curso"
	@echo "  GRAU         - Grau do curso"


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
	@PYTHONNOUSERSITE=1 python3 teste2.py $(USERNAME) $(PASSWORD) $(UNIVERSIDADE) $(CAMPUS) $(CURSO) $(TURNO) $(GRAU)
