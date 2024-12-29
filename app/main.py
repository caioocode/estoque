from fastapi import FastAPI
from database.criar_tabelas import cria_tabelas
from routes.relatorios.relatorio import routes as gerar_relatorio
from routes.produtos.products import routes as produtos
from routes.notas_fiscais.notas_fiscais import routes as notas_fiscais
from routes.solicitacao.solicitacao import routes as solicitacao_compra


# Configuração do FastAPI
app = FastAPI()

# Cria as tabelas de no banco
cria_tabelas()

# Inclui rotas
app.include_router(produtos, prefix="/v1", tags=["Produtos"])
app.include_router(gerar_relatorio, prefix="/v1", tags=["Relatórios"])
app.include_router(notas_fiscais, prefix="/v1", tags=["Notas fiscais"])
app.include_router(solicitacao_compra, prefix="/v1", tags=["Solicitações de compra"])
