import pandas as pd
import os
import getpass
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def initialize_csv():
    if not os.path.exists("db/"):
        os.makedirs("db/")
    if not os.path.exists("db/horarios.csv"):
        pd.DataFrame(columns=["codigo", "dia_da_semana", "horario", "tipo_servico", "valor_servico"]).to_csv("db/horarios.csv", index=False)
    if not os.path.exists("db/funcionarios.csv"):
        pd.DataFrame([
            {"codigo": "001", "nome": "Lucineide"},
            {"codigo": "002", "nome": "Marilucia"},
            {"codigo": "003", "nome": "José Maria"},
            {"codigo": "004", "nome": "Maria José"},
            {"codigo": "005", "nome": "Josefina"}
        ]).to_csv("db/funcionarios.csv", index=False)
    if not os.path.exists("db/movimentacao_caixa.csv"):
        pd.DataFrame(columns=["tipo", "dia_da_semana", "valor", "codigo_funcionario", "justificativa"]).to_csv("db/movimentacao_caixa.csv", index=False)
    if not os.path.exists("db/compras.csv"):
        pd.DataFrame(columns=["produto", "quantidade_necessaria", "status"]).to_csv("db/compras.csv", index=False)
    if not os.path.exists("db/servicos.csv"):
        pd.DataFrame([
            {"servico": "Manicure", "codigo_funcionario": "001", "valor": 20.00},
            {"servico": "Pedicure", "codigo_funcionario": "001", "valor": 20.00},
            {"servico": "Esmaltação em gel", "codigo_funcionario": "001", "valor": 90.00},
            
            {"servico": "Design de sobrancelhas", "codigo_funcionario": "002", "valor": 30.00},
            {"servico": "Henna", "codigo_funcionario": "002", "valor": 40.00},
            {"servico": "Micropigmentação", "codigo_funcionario": "002", "valor": 350.00},
            
            {"servico": "Massagem", "codigo_funcionario": "003", "valor": 100.00},
            {"servico": "Limpeza de pele", "codigo_funcionario": "003", "valor": 120.00},
            {"servico": "Epilação", "codigo_funcionario": "003", "valor": 150.00},
            
            {"servico": "Brow lamination", "codigo_funcionario": "004", "valor": 150.00},
            {"servico": "Extensão de cílios", "codigo_funcionario": "004", "valor": 250.00},
            {"servico": "Lash lifting", "codigo_funcionario": "004", "valor": 180.00},
            
            {"servico": "Tranças", "codigo_funcionario": "005", "valor": 300.00},
            {"servico": "Penteados", "codigo_funcionario": "005", "valor": 80.00},
            {"servico": "Maquiagem", "codigo_funcionario": "005", "valor": 80.00}
        ]).to_csv("db/servicos.csv", index=False)

console = Console(width=65)

# Função principal
def main_menu():
    while True:
        panel_content = Text()
        panel_content.append("\n--- Sistema de Gestão do Salão de Beleza ---\n", style="light_goldenrod3")
        panel_content.append("1. ", style="sandy_brown")
        panel_content.append("Sou Cliente\n")
        panel_content.append("2. ", style="sandy_brown")
        panel_content.append("Sou Funcionário\n")
        panel_content.append("0. ", style="dark_orange3")
        panel_content.append("Sair\n")
        
        console.print(Panel(panel_content, title="Menu Principal", border_style="light_pink3", padding=[0, 9]))
        
        choice = input("Escolha uma opção [0/1/2] (0): ").strip()

        if choice == "1":
            cliente_menu()
        elif choice == "2":
            text = Text("Informe a senha do usuário")
            text.stylize("dark_red")
            console.print(text)
            senha = getpass.getpass(">  ")
            if senha == "funcionario123":
                funcionario_menu()
            else:
                console.print("[red]Senha incorreta![/red]")
        elif choice == "0":
            console.print("[bold green]Saindo do sistema. Até logo![/bold green]")
            break
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")

# Função para o menu do cliente
def cliente_menu():
    while True:
        panel_content = Text()
        panel_content.append("\n        --- Menu do Cliente ---\n", style="light_goldenrod3")
        panel_content.append("1. ", style="sandy_brown")
        panel_content.append("Ver informações de um agendamento\n")
        panel_content.append("2. ", style="sandy_brown")
        panel_content.append("Agendar um horário\n")
        panel_content.append("3. ", style="sandy_brown")
        panel_content.append("Editar um agendamento\n")
        panel_content.append("4. ", style="sandy_brown")
        panel_content.append("Apagar um agendamento\n")
        panel_content.append("0. ", style="dark_orange3")
        panel_content.append("Voltar ao menu principal\n")
        
        console.print(Panel(panel_content, title="Menu do Cliente", border_style="pink3", padding=[0, 12]))
        
        choice = input("Escolha uma opção [0/1/2/3/4] (0): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            ver_agendamento()
        elif choice == "2":
            agendar_horario()
        elif choice == "3":
            editar_agendamento()
        elif choice == "4":
            apagar_agendamento()
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")

# Função para o menu do funcionário
def funcionario_menu():
    while True:
        panel_content = Text()
        panel_content.append("\n--- Menu do Funcionário ---\n", style="light_goldenrod3")
        panel_content.append("1. ", style="sandy_brown")
        panel_content.append("Controle de Caixa\n")
        panel_content.append("2. ", style="sandy_brown")
        panel_content.append("Relatórios\n")
        panel_content.append("3. ", style="sandy_brown")
        panel_content.append("Controle de Estoque\n")
        panel_content.append("0. ", style="dark_orange3")
        panel_content.append("Voltar ao menu principal\n")
        
        console.print(Panel(panel_content, title="Menu do Funcionário", border_style="light_pink3", padding=[0, 18]))

        choice = input("Escolha uma opção [0/1/2/3] (0): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            controle_caixa()
        elif choice == "2":
            gerar_relatorios()
        elif choice == "3":
            controle_estoque()
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")


# Placeholder para funções ainda a serem implementadas
def ver_agendamento():
    print("Função de ver agendamento ainda não implementada.")

def mostrar_servicos():
    while True:
        servicos = pd.read_csv("db/servicos.csv")
        funcionarios = pd.read_csv("db/funcionarios.csv")

        funcionarios_dict = {funcionario["codigo"]: funcionario["nome"] for _, funcionario in funcionarios.iterrows()}

        panel_content = Text()
        panel_content.append(f"--- Escolha o serviço desejado ---\n", style="light_goldenrod3")

        for index, servico in servicos.iterrows():
            panel_content.append(f"{index + 1}. ", style="sandy_brown")
            panel_content.append(f"{servico['servico']} - R${servico['valor']}"
                                f"\nResponsável: {funcionarios_dict.get(servico['codigo_funcionario'], 'Funcionário não encontrado')}\n")
        
        panel_content.append("0. ", style="dark_orange3")
        panel_content.append("Voltar ao menu do cliente\n")

        console.print(Panel(panel_content, title="Serviços Disponíveis", border_style="pink3", padding=[0, 12]))

        choice = input("Escolha uma opção [0/1/2/3] (0): ").strip()

        if choice == "0":
            break
    
def ver_horarios_disponiveis(dia, servico): 
    print("A implementar")
def agendar_horario():
    mostrar_servicos()

def editar_agendamento():
    print("Função de editar agendamento ainda não implementada.")

def apagar_agendamento():
    print("Função de apagar agendamento ainda não implementada.")

def controle_caixa():
    print("Função de controle de caixa ainda não implementada.")

def gerar_relatorios():
    print("Função de gerar relatórios ainda não implementada.")

def controle_estoque():
    print("Função de controle de estoque ainda não implementada.")

# Inicialização do sistema
if __name__ == "__main__":
    initialize_csv()
    main_menu()
