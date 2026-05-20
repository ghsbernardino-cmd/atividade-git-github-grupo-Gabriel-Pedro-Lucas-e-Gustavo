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
    