from fastapi import APIRouter
from database.criar_tabelas import conectar
from schemas.schema import SolicitacaoCompra

routes = APIRouter()


# Solicitar Compra
@routes.post("/solicitacoes_compras/")
def solicitar_compra(solicitacao: SolicitacaoCompra):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Inserir a nova solicitação de compra
    cursor.execute('''
        INSERT INTO solicitacoes_compras (nome_produto, quantidade)
        VALUES (?, ?)
    ''', (solicitacao.nome_produto, solicitacao.quantidade))

    #Registrar a movimentação
    cursor.execute('''
    INSERT INTO movimentacoes (nome_produto, quantidade, preco, tipo_movimentacao)
    VALUES (?, ?, ?, ?)
''', (solicitacao.nome_produto, solicitacao.quantidade, 0, 'entrada'))

    conexao.commit()

    conexao.close()
    return {"message": "Solicitação de compra registrada com sucesso"}