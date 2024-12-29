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
# Listar produtos
if menu == "Listar Produtos":
    st.header("Lista de Produtos")
    try:
        produtos = listar_produtos_service()
        if produtos:
            # Criando a estrutura HTML da tabela
            html_table = """
                <table style="border-collapse: collapse; width: 100%;">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Categoria</th>
                            <th>Quantidade</th>
                            <th>Preço</th>
                            <th>Localização</th>
                            <th>Ação</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            for produto in produtos:
                html_table += f"""
                <tr id="produto_{produto['id']}">
                    <td>{produto['id']}</td>
                    <td>{produto['nome']}</td>
                    <td>{produto['categoria']}</td>
                    <td>{produto['quantidade_estoque']}</td>
                    <td>R${produto['preco']:.2f}</td>
                    <td>{produto['localizacao_deposito']}</td>
                    <td><button id="delete_{produto['id']}">Remover</button></td>
                </tr>
                """
            html_table += "</tbody></table>"

            # Renderizando a tabela no Streamlit
            st.markdown(html_table, unsafe_allow_html=True)

            # Adicionando JavaScript para controlar os cliques nos botões
            st.markdown("""
            <script>
                // Função para remover um produto
                async function removerProduto(produtoId) {
                    try {
                        // Chamando a API para remover o produto
                        const response = await fetch(`http://localhost:8000/produtos/${produtoId}`, {
                            method: 'DELETE',
                        });

                        if (response.ok) {
                            const data = await response.json();
                            // Remover o produto da tabela
                            document.getElementById('produto_' + produtoId).remove();
                            alert(data.message); // Exibe a mensagem de sucesso
                        } else {
                            const data = await response.json();
                            alert('Erro ao remover produto: ' + data.detail);
                        }
                    } catch (error) {
                        console.error('Erro:', error);
                        alert('Erro ao conectar ao servidor');
                    }
                }

                // Adicionando event listeners para todos os botões de remover
                const botoesRemover = document.querySelectorAll('button[id^="delete_"]');
                botoesRemover.forEach(botao => {
                    botao.addEventListener('click', () => {
                        const produtoId = botao.id.replace('delete_', '');
                        removerProduto(produtoId);
                    });
                });
            </script>
            """, unsafe_allow_html=True)

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

