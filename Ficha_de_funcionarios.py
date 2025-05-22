import os
import csv
from dataclasses import dataclass

# Limpa a tela de forma compatível com diferentes sistemas operacionais
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

limpar_tela()

@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: float

funcionarios = []

def esperar_enter():
    input("\nPressione Enter para continuar...")

def mostrar_menu():
    print("\n--| SEJA BEM-VINDO À DÊNDE TECH |--")
    print("1- Cadastrar funcionário")
    print("2- Listar funcionários")
    print("3- Atualizar funcionário")
    print("4- Excluir funcionário")
    print("5- Salvar dados em CSV")
    print("6- Carregar de CSV")
    print("7- Sair")
    print()

def cadastrar():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")

    while True:
        try:
            salario = float(input("Salário: R$ "))
            break
        except ValueError:
            print("Digite um valor numérico válido para o salário.")

    funcionario = Funcionario(nome, cpf, cargo, salario)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado!")
    esperar_enter()

def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        esperar_enter()
        return

    print("\nLista de Funcionários:")
    for f in funcionarios:
        print(f"{f.nome} | CPF: {f.cpf} | Cargo: {f.cargo} | Salário: R${f.salario:.2f}")
    esperar_enter()

def atualizar():
    cpf = input("Digite o CPF do funcionário: ")
    for f in funcionarios:
        if f.cpf == cpf:
            f.nome = input("Novo nome: ")
            f.cargo = input("Novo cargo: ")

            while True:
                try:
                    f.salario = float(input("Novo salário: R$ "))
                    break
                except ValueError:
                    print("Digite um valor válido para o salário.")

            print("Funcionário atualizado!")
            esperar_enter()
            return

    print("Funcionário não encontrado.")
    esperar_enter()

def deletar():
    cpf = input("Digite o CPF do funcionário: ")
    for f in funcionarios:
        if f.cpf == cpf:
            funcionarios.remove(f)
            print("Funcionário removido!")
            esperar_enter()
            return
    print("Funcionário não encontrado.")
    esperar_enter()

def salvar_csv():
    with open("funcionarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor.writerow(["Nome", "CPF", "Cargo", "Salário"])
        for f in funcionarios:
            escritor.writerow([f.nome, f.cpf, f.cargo, f.salario])
    print("Dados salvos em CSV com sucesso!")
    esperar_enter()

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            salvar_csv()
        elif opcao == "6":
            print("Função de carregar CSV ainda não implementada.")
            esperar_enter()
        elif opcao == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")
            esperar_enter()

if __name__ == "__main__":
    main()
