import pandas as pd
import os
import getpass
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import random
import string

def gerar_codigo_unico(tamanho=4):
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))

def initialize_csv():
    if not os.path.exists("db/"):
        os.makedirs("db/")
    if not os.path.exists("db/horarios.csv"):
        pd.DataFrame(columns=["codigo", "dia_da_semana", "horario", "tipo_servico", "codigo_funcionario", "valor_servico"]).to_csv("db/horarios.csv", index=False)
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
    funcionarios = pd.read_csv("db/funcionarios.csv")
    funcionarios_dict = {str(funcionario["codigo"]): funcionario["nome"] for _, funcionario in funcionarios.iterrows()}    
    codigo = input("Informe o código de agendamento:")
    horarios = pd.read_csv("db/horarios.csv")
    horario = horarios[horarios['codigo'] == codigo]
    if horario.empty: 
        print("Código inválido. Verifique e tente novamente.")
    else:
        nome_funcionario = funcionarios_dict.get(horario["codigo_funcionario"].to_string(index=False), "Funcionário não encontrado")
        panel_content = Text()
        panel_content.append("\n--- Pressione \"Enter\" para sair ---\n", style="light_goldenrod3")
        panel_content.append("CÓDIGO: ", style="sandy_brown")
        panel_content.append(f"{horario['codigo'].to_string(index=False)}\n")
        panel_content.append("DIA DA SEMANA: ", style="sandy_brown")
        panel_content.append(f"{horario['dia_da_semana'].to_string(index=False)}\n")
        panel_content.append("HORÁRIO: ", style="sandy_brown")
        panel_content.append(f"{horario['horario'].to_string(index=False)}\n")
        panel_content.append("TIPO DE SERVIÇO: ", style="sandy_brown")
        panel_content.append(f"{horario['tipo_servico'].to_string(index=False)}\n")
        panel_content.append("RESPONSÁVEL: ", style="sandy_brown")
        panel_content.append(f"{nome_funcionario}\n")
        panel_content.append("VALOR: ", style="sandy_brown")
        panel_content.append(f"R${horario['valor_servico'].to_string(index=False)}\n")
        console.print(Panel(panel_content, title="Informações sobre agendamento", border_style="light_pink3", padding=[0,14]))


def mostrar_servicos():
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

    
def ver_horarios_disponiveis(dia, servico, codigo_funcionario):
    horarios = pd.read_csv("db/horarios.csv")
    horarios_disponiveis = []

    horarios_permitidos = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00"]

    for horario in horarios_permitidos:
        agendamentos = horarios[(horarios["dia_da_semana"] == dia) & (horarios["horario"] == horario)]

        if len(agendamentos) < 2 and not agendamentos["codigo_funcionario"].eq(codigo_funcionario).any():
            horarios_disponiveis.append(horario)

    return horarios_disponiveis


def agendar_horario():
    servicos = pd.read_csv("db/servicos.csv")
    funcionarios = pd.read_csv("db/funcionarios.csv")
    funcionarios_dict = {funcionario["codigo"]: funcionario["nome"] for _, funcionario in funcionarios.iterrows()}

    while True:
        mostrar_servicos()
        try:
            escolha = int(input("Escolha algum serviço (0 para voltar): ").strip())
            if escolha == 0:
                break
            if escolha < 1 or escolha > len(servicos):
                console.print("[red]Opção inválida. Tente novamente.[/red]")
                continue
        except ValueError:
            console.print("[red]Entrada inválida. Digite um número válido.[/red]")
            continue

        servico_selecionado = servicos.iloc[escolha - 1]
        nome_servico = servico_selecionado["servico"]
        codigo_funcionario = servico_selecionado["codigo_funcionario"]
        nome_funcionario = funcionarios_dict.get(codigo_funcionario, "Funcionário não encontrado")
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

        for i, dia in enumerate(dias_semana, start=1):
            print(f"{i} - {dia}")

        
        while True:
            dia_escolhido = int(input("Digite o número correspondente ao dia: "))
            if 1 <= dia_escolhido <= 7:
                dia = dias_semana[dia_escolhido - 1]
                print(f"Você escolheu: {dia}")
                break
            else:
                print("Escolha inválida!")
        horarios_disponiveis = ver_horarios_disponiveis(dia, nome_servico, codigo_funcionario)

        if not horarios_disponiveis:
            console.print("[yellow]Não há horários disponíveis para este dia.[/yellow]")
            continue

        console.print(f"[bold green]Horários disponíveis para {nome_servico} com {nome_funcionario} no dia {dia}:[/bold green]")
        for i, horario in enumerate(horarios_disponiveis, start=1):
            console.print(f"{i}. {horario}")

        while True:
            try:
                escolha_horario = int(input("Escolha o número do horário desejado: ").strip())
                if escolha_horario < 1 or escolha_horario > len(horarios_disponiveis):
                    console.print("[red]Opção inválida. Tente novamente.[/red]")
                break
            except ValueError:
                console.print("[red]Entrada inválida. Digite um número válido.[/red]")
                

        horario_selecionado = horarios_disponiveis[escolha_horario - 1]

        codigo_horario = gerar_codigo_unico()
        # Salvar o agendamento no arquivo CSV
        novo_agendamento = pd.DataFrame([{
            "codigo": codigo_horario,
            "dia_da_semana": dia,
            "horario": horario_selecionado,
            "tipo_servico": nome_servico,
            "codigo_funcionario": codigo_funcionario,
            "valor_servico": servico_selecionado["valor"],
        }])
        novo_agendamento.to_csv("db/horarios.csv", mode='a', header=False, index=False)
        console.print(f"[bold green]Agendamento para {nome_servico} às {horario_selecionado} no dia {dia} foi concluído com sucesso![/bold green]"
                      f"[red]\nCÓDIGO DE AGENDAMENTO: {codigo_horario}[/red]")
        break


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
