import locale
import sys
import time
from datetime import date
import pandas as pd
import os
import getpass
from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import random
import string
import db
import matplotlib.pyplot as plt

locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
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
            apagar_agendamento()
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")

def funcionario_menu():
    while True:
        panel_content = Text()
        panel_content.append("\n        --- Menu ---\n", style="light_goldenrod3")
        panel_content.append("1. ", style="sandy_brown")
        panel_content.append("Ver informações de um agendamento\n")
        panel_content.append("2. ", style="sandy_brown")
        panel_content.append("Agendar um horário\n")
        panel_content.append("3. ", style="sandy_brown")
        panel_content.append("Apagar um agendamento\n")
        panel_content.append("4. ", style="sandy_brown")
        panel_content.append("Ver seus agendamentos para um dia\n")
        panel_content.append("5. ", style="sandy_brown")
        panel_content.append("Finalizar serviço\n")
        panel_content.append("6. ", style="sandy_brown")
        panel_content.append("Fazer retirada do caixa\n")
        panel_content.append("7. ", style="sandy_brown")
        panel_content.append("Criar relatórios\n")
        panel_content.append("0. ", style="dark_orange3")
        panel_content.append("Voltar ao menu principal\n")
        
        console.print(Panel(panel_content, title="Menu de funcionário", border_style="pink3", padding=[0, 12]))
        
        choice = input("Escolha uma opção [0/1/2/3/4/5/6/7] (0): ").strip()

        if choice == "0":
            break
        elif choice == "1":
            ver_agendamento()
        elif choice == "2":
            agendar_horario()
        elif choice == "3":
            apagar_agendamento()
        elif choice == "4":
            ver_agendamentos_de_um_dia()
        elif choice == "5":
            finalizar_servico()
        elif choice == "6":
            registrar_retirada_caixa()
        elif choice == "7":
            gerar_relatorios()
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")


def ver_informacoes_agendamento(codigo):
    funcionarios = pd.read_csv("db/funcionarios.csv")
    funcionarios_dict = {str(funcionario["codigo"]): funcionario["nome"] for _, funcionario in funcionarios.iterrows()}    
    horarios = pd.read_csv("db/horarios.csv")
    horario = horarios[horarios['codigo'] == codigo]
    if horario.empty: 
        print("Código inválido. Verifique e tente novamente.")
    else:
        nome_funcionario = funcionarios_dict.get(horario["codigo_funcionario"].to_string(index=False), "Funcionário não encontrado")
        panel_content = Text()
        panel_content.append("\n    --- Digite \"y\" para sair ---\n", style="light_goldenrod3")
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
        console.print(Panel(panel_content, title="Informações do Agendamento", border_style="pink3", padding=[0, 17]))

def ver_agendamento():
    codigo = Prompt.ask("Informe o código do agendamento")
    ver_informacoes_agendamento(codigo)
    while True:
        exit = Confirm.ask("[red]Deseja sair ao menu?[/red]")
        if exit:
            break

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
    funcionarios = pd.read_csv("db/funcionarios.csv", dtype={"codigo": str})
    funcionarios_dict = {funcionario["codigo"].zfill(3): funcionario["nome"] for _, funcionario in funcionarios.iterrows()}

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
        codigo_funcionario = str(servico_selecionado["codigo_funcionario"]).zfill(3)
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

        codigo_agendamento = gerar_codigo_unico()
        db.salvar_agendamento(
            codigo_agendamento,
            dia,
            horario_selecionado,
            nome_servico,
            codigo_funcionario,
            servico_selecionado["valor"]
        )
        console.print(f"[bold green]Agendamento para {nome_servico} às {horario_selecionado} no dia {dia} foi concluído com sucesso![/bold green]"
                      f"[red]\nCÓDIGO DE AGENDAMENTO: {codigo_agendamento}[/red]")
        break


def apagar_agendamento():
    codigo = Prompt.ask("[light_goldenrod3]Informe o código do agendamento[/light_goldenrod3]")
    
    agendamentos = pd.read_csv("db/horarios.csv")
    if not agendamentos[agendamentos["codigo"] == codigo].empty:
        ver_informacoes_agendamento(codigo)
        delete = Confirm.ask("[red]Deseja mesmo cancelar o agendamento?[/red]")
        if delete:
            agendamentos = agendamentos[agendamentos["codigo"]!= codigo]
            agendamentos.to_csv("db/horarios.csv", index=False)
            console.print("[bold green]Agendamento cancelado com sucesso![/bold green]")
    else:
        console.print("[red]Agendamento não encontrado. Tente novamente.[/red]")

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

def ver_agendamentos_de_um_dia():
    codigo = Prompt.ask("[light_goldenrod3]Informe o seu código de funcionário[/light_goldenrod3]")
    funcionarios = pd.read_csv("db/funcionarios.csv", dtype={"codigo": str})
    if funcionarios[funcionarios["codigo"] == codigo].empty:
        console.print("[red]Funcionário não encontrado. Tente novamente.[/red]")
        return
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia = Prompt.ask("[light_goldenrod3]Informe o dia da semana[/light_goldenrod3]", choices=dias_semana)
    agendamentos = pd.read_csv("db/horarios.csv", dtype={"codigo_funcionario": str})
    agendamentos_dia = agendamentos[(agendamentos["dia_da_semana"] == dia) & (agendamentos["codigo_funcionario"] == codigo)]
    agendamentos_dia = agendamentos_dia.sort_values(by="horario")
    if agendamentos_dia.empty:
        console.print("[yellow]Nenhum agendamento encontrado para este dia.[/yellow]")
        return
    console.print(f"[bold green]Agendamentos para o dia {dia}:[/bold green]")
    agendamentos_painel = Text()
    agendamentos_painel.append(f"--- Serviços agendados ---\n", style="light_goldenrod3")
    for _, agendamento in agendamentos_dia.iterrows():
        agendamentos_painel.append(f"\n        {agendamento['horario']} - {agendamento['codigo']}", style="bold green")
    console.print(Panel(agendamentos_painel, title=f"Agendamentos para {dia}", border_style="light_pink3", padding=(0, 16)))
    ver_detalhes = Confirm.ask("[dark_orange3]Deseja ir ver detalhes de um agendamento?[/dark_orange3]")
    if ver_detalhes:
        ver_agendamento()
    
def finalizar_servico():
    codigo = Prompt.ask("[light_goldenrod3]Informe o código do agendamento[/light_goldenrod3]")
    agendamentos = pd.read_csv("db/horarios.csv")
    agendamento = agendamentos[agendamentos["codigo"] == codigo]
    if agendamento.empty:
        console.print("[red]Agendamento não encontrado. Tente novamente.[/red]")
        return
    ver_informacoes_agendamento(codigo)
    valor_pago = float(Prompt.ask("[light_goldenrod3]Informe o valor pago pelo serviço.[/light_goldenrod3]"))
    troco = valor_pago - float(agendamento["valor_servico"].to_string(index=False))
    console.print(f"[bold green]Troco: R${troco}[/bold green]")
    finalizar = Confirm.ask("[dark_orange3]Finalizar serviço?[/dark_orange3]")
    dia_semana = dias_semana[date.today().weekday()]
    if finalizar:
        agendamentos.drop(agendamento.index, inplace=True)
        agendamentos.to_csv("db/horarios.csv", index=False)
        db.registrar_movimentacao(
            "PAGAMENTO",
            dia_semana,
            float(agendamento['valor_servico'].to_string(index=False)),
            agendamento['codigo_funcionario'].to_string(index=False),
            agendamento['tipo_servico'].to_string(index=False),
        )
        console.print("[bold green]Serviço finalizado com sucesso![/bold green]")


def registrar_retirada_caixa():
    codigo = Prompt.ask("[light_goldenrod3]Informe o código do funcionário[/light_goldenrod3]")

    funcionarios = pd.read_csv("db/funcionarios.csv", dtype={"codigo": str})
    funcionario = funcionarios[funcionarios["codigo"] == codigo]
    if funcionario.empty:
        console.print("[dark_orange3]Código errado. Tente novamente.[/dark_orange3]")
        return
    retirada = float(Prompt.ask("[light_goldenrod3]Qual o valor desejado?[/light_goldenrod3]"))
    justificativa = Prompt.ask("[light_goldenrod3]Para quê o valor está sendo retirado?[/light_goldenrod3]")
    dia_semana = dias_semana[date.today().weekday()]
    db.registrar_movimentacao(
        "RETIRADA",
        dia_semana,
        retirada, 
        codigo, 
        justificativa
    )
    console.print("[bold green]Retirada efetuada com sucesso![/bold green]")

def relatorio_diario():
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia_semana = dias_semana[date.today().weekday()]
    print(dia_semana)
    
    df = pd.read_csv("db/movimentacao_caixa.csv")

    funcionarios = pd.read_csv("db/funcionarios.csv")
    funcionarios_dict = {funcionario["codigo"]: funcionario["nome"] for _, funcionario in funcionarios.iterrows()}
    df["nome_funcionario"] = df["codigo_funcionario"].map(funcionarios_dict)
    
    df["dia_da_semana"] = df["dia_da_semana"].str.strip().str.capitalize()

    df_diario = df[(df['dia_da_semana'] == dia_semana) & (df["tipo"] != "RETIRADA")]
    
    lucro_funcionario = df_diario.groupby("nome_funcionario")["valor"].sum()
    total_diario = df[(df["dia_da_semana"] == dia_semana) & (df["tipo"] != "RETIRADA")]["valor"].sum()
    
    fig, ax = plt.subplots()
    lucro_funcionario.plot(kind="bar", ax=ax, color='#006400')
    ax.set_title(f"Faturamento Diário - {dia_semana}")
    ax.axhline(y=total_diario, color='#FFFFFF', linestyle='--', label=f'Total: {total_diario}')
    ax.set_xlabel('Funcionário')
    ax.set_ylabel('Faturamento')

    plt.xticks(rotation=0)
    plt.tight_layout()
    ax.legend()

    plt.savefig(f"relatorios/{dia_semana}.png")
    plt.show()

def relatorio_semanal():
    df = pd.read_csv("db/movimentacao_caixa.csv")
    funcionarios = pd.read_csv("db/funcionarios.csv")
    funcionarios_dict = {funcionario["codigo"]: funcionario["nome"] for _, funcionario in funcionarios.iterrows()}
    df["nome_funcionario"] = df["codigo_funcionario"].map(funcionarios_dict)

    df["tipo"] = df["tipo"].str.strip().str.upper()
    df_semanal = df[df["tipo"] != "RETIRADA"]

    df["dia_da_semana"] = pd.Categorical(df["dia_da_semana"], categories=dias_semana, ordered=True)

    lucro_funcionario_semanal = df_semanal.groupby(["dia_da_semana", "nome_funcionario"])["valor"].sum().unstack(fill_value=0)
    lucro_total_semanal = df_semanal.groupby("dia_da_semana")["valor"].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    lucro_funcionario_semanal.plot(kind="line", ax=ax, marker="o")

    lucro_total_semanal.plot(kind="line", ax=ax, color="black", linestyle="--", label="Total Semanal")
    
    ax.set_title("Faturamento Semanal")
    ax.set_xlabel('Dia da Semana')
    ax.set_ylabel('Faturamento')
    plt.xticks(rotation=45)
    plt.tight_layout()
    ax.legend()

    plt.savefig(f"relatorios/semanal.png")
    plt.show()


def relatorio_servicos():
    df = pd.read_csv("db/movimentacao_caixa.csv")
    df = df[df["tipo"] != "RETIRADA"]
    frequencia_justificativa = df['justificativa'].value_counts()
    plt.figure(figsize=(7, 7))
    plt.pie(frequencia_justificativa, labels=frequencia_justificativa.index, autopct='%1.1f%%', startangle=90)
    plt.title("Frequência movimentação de caixa")
    plt.savefig("relatorios/servicos.png")
    plt.show()

def gerar_relatorios():
    while True:
        relatorio_escolhido = Prompt.ask(
            "Qual relatório deseja gerar?",
            choices=["Diário", "Semanal", "Servicos", "Sair"],
            default="Diário"
        )
        if relatorio_escolhido == "Diário":
            relatorio_diario()
        elif relatorio_escolhido == "Semanal":
            relatorio_semanal()
        elif relatorio_escolhido == "Servicos":
            relatorio_servicos()
        elif relatorio_escolhido == "Sair":
            console.print("Saindo do sistema...")
            break


# Inicialização do sistema
if __name__ == "__main__":
    initialize_csv()
    main_menu()
