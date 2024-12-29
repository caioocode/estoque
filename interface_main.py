import streamlit as st
import requests
from services.produtos.criar_produtos_service import criar_produto_service
from services.produtos.listar_produtos_service import listar_produtos_service
from services.produtos.deletar_produto_service import deletar_produto_service

# Definindo a classe Produto (caso ainda não tenha)
class Produto:
    def __init__(self, nome, categoria, quantidade_estoque, preco, localizacao_deposito):
        self.nome = nome
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.localizacao_deposito = localizacao_deposito

# Configuração básica do app
st.set_page_config(page_title="Sistema de Estoque", layout="centered")

# Título do aplicativo
st.title("Sistema de Gerenciamento de Estoque")

# Barra lateral para navegação
menu = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto", "Deletar Produto"])

# Injetando CSS para melhorar o visual
#st.markdown(""" coloque aqui sua estilização""", unsafe_allow_html=True)


# Listar produtos
if menu == "Listar Produtos":
    st.header("Lista de Produtos")

    
    try:
        produtos = listar_produtos_service()
        if produtos:
            # Cabeçalho da tabela
            st.write(f"| ID|Nome | Categoria | Quantidade | Preço | Localização | Ação |")
            

            # Iterar pelos produtos e exibir os dados com botão de ação
            for produto in produtos:
                col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
                col1.write(produto["id"])
                col2.write(produto["nome"])
                col3.write(produto["categoria"])
                col4.write(produto["quantidade_estoque"])
                col5.write(f"R${produto['preco']:.2f}")
                col6.write(produto["localizacao_deposito"])
                if col7.button("Remover", key=f"remover_{produto['id']}"):
                    try:
                        deletar_produto_service(produto["id"])
                        st.success(f"Produto {produto['id']} removido com sucesso!")
                    except Exception as e:
                        st.error(f"Erro ao remover produto {produto['id']}: {e}")
        else:
            st.info("Nenhum produto encontrado.")
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
    

# Adicionar produto
elif menu == "Adicionar Produto":
    st.header("Adicionar Novo Produto")
    with st.form("form_add_produto"):
        nome = st.text_input("Nome do Produto")
        categoria = st.text_input("Categoria")
        quantidade = st.number_input("Quantidade em Estoque", min_value=0, step=1)
        preco = st.number_input("Preço", min_value=0.0, step=0.01, format="%.2f")
        localizacao = st.text_input("Localização no Depósito")
        submit = st.form_submit_button("Adicionar Produto")

        if submit:
            try:
                # Criando uma instância do Produto
                produto = Produto(
                    nome=nome,
                    categoria=categoria,
                    quantidade_estoque=int(quantidade),
                    preco=float(preco),
                    localizacao_deposito=localizacao
                )

                # Passando o objeto Produto para a função de serviço
                criar_produto_service(produto)

                st.success("Produto adicionado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar produto: {e}")

# Deletar produto
elif menu == "Deletar Produto":
    st.header("Deletar Produto")
    id_produto = st.number_input("ID do Produto", min_value=1, step=1)
    if st.button("Deletar"):
        try:
            deletar_produto_service(id_produto)
            st.success("Produto deletado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao deletar produto: {e}")

