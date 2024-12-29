
import sqlite3
from fastapi import status
from database.criar_tabelas import conectar
from utils.retorna_erro_http import retorna_erro_http

def listar_produtos_service():
    try:
        conexao = conectar()
        conexao.row_factory = sqlite3.Row #retorna os resultados como sqlite3.Row, que permite acessar os dados de cada linha da consulta usando o nome das colunas, como se fosse um dicionário. -> streamlit (qualquer coisa é só apagar)

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conexao.close()
        
        if produtos.count == 0:
            retorna_erro_http("Nenhum não encontrado." + str(e),status.HTTP_404_NOT_FOUND)
        return produtos
    except sqlite3.IntegrityError as e:
        # Caso haja erro de integridade (ex: chave única duplicada)
        raise ValueError("Erro de integridade no banco de dados: " + str(e))
    except sqlite3.OperationalError as e:
        # Erro operacional, como erro de SQL ou banco de dados não encontrado
        raise sqlite3.DatabaseError("Erro operacional no banco de dados: " + str(e))
    except Exception as e:
        # Erros gerais de exceção
        raise Exception("Erro ao processar a solicitação: " + str(e))