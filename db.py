import csv
import os

# Função genérica para adicionar uma linha ao CSV
def adicionar_registro(nome_arquivo, campos, valores):
    arquivo_existe = os.path.isfile(nome_arquivo)
    with open(nome_arquivo, mode='a', newline='') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=campos)
        if not arquivo_existe:
            writer.writeheader() 
        writer.writerow(valores)

# Função para salvar um agendamento em horarios.csv
def salvar_agendamento(codigo, dia_da_semana, horario, tipo_servico, codigo_funcionario, valor_servico):
    campos = ["codigo", "dia_da_semana", "horario", "tipo_servico", "codigo_funcionario", "valor_servico"]
    valores = {
        "codigo": codigo,
        "dia_da_semana": dia_da_semana,
        "horario": horario,
        "tipo_servico": tipo_servico,
        "codigo_funcionario": codigo_funcionario,
        "valor_servico": valor_servico
    }
    adicionar_registro("db/horarios.csv", campos, valores)

# Função para salvar um funcionário em funcionarios.csv
def salvar_funcionario(codigo, nome, servicos_possiveis):
    campos = ["codigo", "nome", "servicos_possiveis"]
    valores = {
        "codigo": codigo,
        "nome": nome,
        "servicos_possiveis": servicos_possiveis
    }
    adicionar_registro("db/funcionarios.csv", campos, valores)

# Função para registrar uma movimentação de caixa em movimentacao_caixa.csv
def registrar_movimentacao(tipo, dia_da_semana, valor, codigo_funcionario, justificativa):
    campos = ["tipo", "dia_da_semana", "valor", "codigo_funcionario", "justificativa"]
    valores = {
        "tipo": tipo,
        "dia_da_semana": dia_da_semana,
        "valor": valor,
        "codigo_funcionario": codigo_funcionario,
        "justificativa": justificativa
    }
    adicionar_registro("db/movimentacao_caixa.csv", campos, valores)

# Função para registrar uma compra em compras.csv
def registrar_compra(produto, quantidade_necessaria):
    campos = ["produto", "quantidade_necessaria"]
    valores = {
        "produto": produto,
        "quantidade_necessaria": quantidade_necessaria
    }
    adicionar_registro("db/compras.csv", campos, valores)
