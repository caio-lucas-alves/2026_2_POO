import streamlit as st
import pandas as pd
from service.service import Service

class ManterProdutoUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de produtos")
        categorias = Service.categoria_listar()
        aba = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with aba[0]:
            if categorias:
                opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
                with st.form("inserir_produto"):
                    descricao = st.text_input("Descrição")
                    preco = st.number_input("Preço", min_value=0.0, step=0.01, format="%.2f")
                    estoque = st.number_input("Estoque", min_value=0, step=1)
                    categoria = st.selectbox("Categoria", list(opcoes.keys()))
                    enviar = st.form_submit_button("Cadastrar produto")
                    if enviar:
                        if descricao.strip() and preco > 0:
                            Service.produto_inserir(descricao, preco, estoque, opcoes[categoria])
                            st.success("Produto cadastrado com sucesso.")
                        else:
                            st.error("Informe uma descrição e um preço maior que zero.")
            else:
                st.warning("Cadastre uma categoria antes de cadastrar produtos.")

        with aba[1]:
            produtos = Service.produto_listar()
            categorias_por_id = {c.id: c.descricao for c in categorias}
            if produtos:
                dados = [
                    {
                        "ID": p.id,
                        "Descrição": p.descricao,
                        "Preço": f"R$ {p.preco:.2f}",
                        "Estoque": p.estoque,
                        "Categoria": categorias_por_id.get(p.idCategoria, "Não encontrada")
                    }
                    for p in produtos
                ]
                st.dataframe(pd.DataFrame(dados), use_container_width=True, hide_index=True)
            else:
                st.info("Não existem produtos cadastrados.")

        with aba[2]:
            produtos = Service.produto_listar()
            if produtos and categorias:
                produtos_opcoes = {f"{p.id} - {p.descricao}": p.id for p in produtos}
                selecionado = st.selectbox("Produto", list(produtos_opcoes.keys()), key="produto_atualizar")
                produto = Service.produto_listar_id(produtos_opcoes[selecionado])
                categorias_opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
                categoria_atual = next(
                    (nome for nome, id_categoria in categorias_opcoes.items()
                     if id_categoria == produto.idCategoria),
                    list(categorias_opcoes.keys())[0]
                )
                with st.form("atualizar_produto"):
                    descricao = st.text_input("Descrição", value=produto.descricao)
                    preco = st.number_input("Preço", min_value=0.0, value=float(produto.preco), step=0.01, format="%.2f")
                    estoque = st.number_input("Estoque", min_value=0, value=int(produto.estoque), step=1)
                    categoria = st.selectbox("Categoria", list(categorias_opcoes.keys()), index=list(categorias_opcoes.keys()).index(categoria_atual))
                    enviar = st.form_submit_button("Salvar alterações")
                    if enviar:
                        if descricao.strip() and preco > 0:
                            Service.produto_atualizar(produto.id, descricao, preco, estoque, categorias_opcoes[categoria])
                            st.success("Produto atualizado com sucesso.")
                        else:
                            st.error("Informe uma descrição e um preço maior que zero.")
            else:
                st.info("Cadastre produtos e categorias para utilizar esta opção.")

        with aba[3]:
            produtos = Service.produto_listar()
            if produtos:
                opcoes = {f"{p.id} - {p.descricao}": p.id for p in produtos}
                selecionado = st.selectbox("Produto", list(opcoes.keys()), key="produto_excluir")
                if st.button("Excluir produto"):
                    Service.produto_excluir(opcoes[selecionado])
                    st.success("Produto excluído com sucesso.")
            else:
                st.info("Não existem produtos cadastrados.")
