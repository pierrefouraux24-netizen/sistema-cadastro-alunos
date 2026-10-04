# SISTEMA DE CADASTRO DE ALUNOS
alunos = []

def adicionar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota (0 a 10): "))
    while nota < 0 or nota > 10:
        print("A nota deve ser de 0 a 10.")
        nota = float(input("Nota: "))
    alunos.append({"nome": nome, "idade": idade, "nota": nota})
    print("Aluno cadastrado!")
def listar():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(aluno["nome"], "-", aluno["idade"], "anos - Nota:", aluno["nota"])
def buscar():
    nome = input("Nome para buscar: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])
            return
    print("Aluno não encontrado.")
def remover():
    nome = input("Nome para remover: ")
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            alunos.remove(aluno)
            print("Aluno removido!")
            return
    print("Aluno não encontrado.")
def media():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        total = sum(aluno["nota"] for aluno in alunos)
        print("Média geral:", total / len(alunos))
while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Média geral")
    print("6 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        media()
    elif opcao == "6":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")