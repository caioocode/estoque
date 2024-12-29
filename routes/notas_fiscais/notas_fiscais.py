from schemas.schema import NotaFiscal
from database.criar_tabelas import conectar
from fastapi import APIRouter

routes = APIRouter()


# Cadastrar Nota Fiscal
@routes.post("/notas_fiscais/")
def cadastrar_nota_fiscal(nota: NotaFiscal):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Calcular o valor total (se necessário)
    if nota.valor_total is None:
        nota.valor_total = nota.quantidade * nota.preco

    # Inserir a nova nota fiscal
    cursor.execute('''
        INSERT INTO notas_fiscais (numero, nome_produto, quantidade, preco, valor_total, tipo_movimentacao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nota.numero, nota.nome_produto, nota.quantidade, nota.preco, nota.valor_total, nota.tipo_movimentacao))
    
    # Registrar a movimentação
    cursor.execute('''
        INSERT INTO movimentacoes (nome_produto, quantidade, preco, tipo_movimentacao)
        VALUES (?, ?, ?, ?)
    ''', (nota.nome_produto, nota.quantidade, nota.preco, nota.tipo_movimentacao))
    
    conexao.commit()
    conexao.close()
    return {"message": "Nota fiscal cadastrada com sucesso"}
