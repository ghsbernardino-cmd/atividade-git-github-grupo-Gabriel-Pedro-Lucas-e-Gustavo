alunos = []

print("SISTEMA DE CADASTRO DE ALUNOS ")

while True:
    aluno = {
        "nome": input("\nNome: "),
        "idade": input("Idade: "),
        "turma": input("Turma: ")
    }
    alunos.append(aluno)
    print("Cadastrado com sucesso!")
    

    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        print("\nCadastro encerrado. Até logo!")

        break