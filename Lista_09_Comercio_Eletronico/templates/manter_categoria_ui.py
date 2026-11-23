import streamlit as st
import pandas as pd
from service.service import Service

class ManterCategoriaUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de categorias")
        aba = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with aba[0]:
            with st.form("inserir_categoria"):
                descricao = st.text_input("Descrição")
                enviar = st.form_submit_button("Cadastrar categoria")
                if enviar:
                    if descricao.strip():
                        Service.categoria_inserir(descricao)
                        st.success("Categoria cadastrada com sucesso.")
                    else:
                        st.error("Informe a descrição.")

        with aba[1]:
            categorias = Service.categoria_listar()
            if categorias:
                st.dataframe(
                    pd.DataFrame([{"ID": c.id, "Descrição": c.descricao} for c in categorias]),
                    use_container_width=True, hide_index=True
                )
            else:
                st.info("Não existem categorias cadastradas.")

        with aba[2]:
            categorias = Service.categoria_listar()
            if categorias:
                opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
                selecionado = st.selectbox("Categoria", list(opcoes.keys()), key="categoria_atualizar")
                categoria = Service.categoria_listar_id(opcoes[selecionado])
                with st.form("atualizar_categoria"):
                    descricao = st.text_input("Descrição", value=categoria.descricao)
                    enviar = st.form_submit_button("Salvar alterações")
                    if enviar:
                        if descricao.strip():
                            Service.categoria_atualizar(categoria.id, descricao)
                            st.success("Categoria atualizada com sucesso.")
                        else:
                            st.error("Informe a descrição.")
            else:
                st.info("Não existem categorias cadastradas.")

        with aba[3]:
            categorias = Service.categoria_listar()
            if categorias:
                opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
                selecionado = st.selectbox("Categoria", list(opcoes.keys()), key="categoria_excluir")
                if st.button("Excluir categoria"):
                    try:
                        Service.categoria_excluir(opcoes[selecionado])
                        st.success("Categoria excluída com sucesso.")
                    except Exception:
                        st.error("Não é possível excluir uma categoria que possui produtos.")
            else:
                st.info("Não existem categorias cadastradas.")
