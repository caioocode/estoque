#from database.criar_tabelas import conectar
from schemas.schema import Produto, ProdutoResponse
from typing import List
from services.produtos.criar_produtos_service import criar_produto_service
from services.produtos.deletar_produto_service import deletar_produto_service
from services.produtos.listar_produtos_service import listar_produtos_service
from services.produtos.alterar_produtos_service import alterar_produtos_service

from fastapi import APIRouter, status, HTTPException
from utils.retorna_erro_http import retorna_erro_http
import sqlite3


routes = APIRouter()


# Criar um produto (Create)
@routes.post("/produtos")
async def criar_produto(produto: Produto):
    try:
        criar_produto_service(produto)
        return {"message": "Produto adicionado com sucesso"}
    except ValueError as e:
        retorna_erro_http(str(e),status.HTTP_400_BAD_REQUEST)
    except sqlite3.DatabaseError as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)


# Deletar um produto por NOME (Delete)
@routes.delete("/produtos/{id}")
async def deletar_produto(id: int):
    try:
        deletar_produto_service(id)
        return {"message": "Produto deletado com sucesso"}
    except ValueError as e:
        retorna_erro_http(str(e),status.HTTP_400_BAD_REQUEST)
    except sqlite3.DatabaseError as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)

#listar produtos
@routes.get("/produtos/", response_model=List[ProdutoResponse])
async def listar_produtos():
    try:
        produtos_data = listar_produtos_service()
        produtos = [ProdutoResponse(id=id, nome=nome, categoria=categoria, quantidade_estoque=quantidade_estoque, preco=preco, localizacao_deposito=localizacao_deposito)
            for id, nome, categoria, quantidade_estoque, preco, localizacao_deposito in produtos_data]
        return produtos
    except ValueError as e:
        retorna_erro_http(str(e),status.HTTP_400_BAD_REQUEST)
    except sqlite3.DatabaseError as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
       retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)


#alterar produto
@routes.put("/produtos/")
async def atualizar_produto(id:str, produto: Produto):
    try:
        produto_atualizado = alterar_produtos_service(id, produto)
        return {"message": "Produto atualizado com sucesso", "produto_atualizado": produto_atualizado}
    except ValueError as e:
        retorna_erro_http(str(e),status.HTTP_400_BAD_REQUEST)
    except sqlite3.DatabaseError as e:
        retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
       retorna_erro_http(str(e),status.HTTP_500_INTERNAL_SERVER_ERROR)





