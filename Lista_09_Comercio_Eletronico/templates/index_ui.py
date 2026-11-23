import streamlit as st
from templates.manter_cliente_ui import ManterClienteUI
from templates.manter_categoria_ui import ManterCategoriaUI
from templates.manter_produto_ui import ManterProdutoUI
from templates.reajustar_produto_ui import ReajustarProdutoUI

class IndexUI:
    @staticmethod
    def Main():
        st.set_page_config(page_title="Comércio Eletrônico", page_icon="🛒", layout="wide")
        st.sidebar.title("Comércio Eletrônico")
        pagina = st.sidebar.selectbox(
            "Selecione uma página",
            [
                "Início",
                "Manter clientes",
                "Manter categorias",
                "Manter produtos",
                "Reajustar preços"
            ]
        )

        if pagina == "Início":
            st.title("Sistema de Comércio Eletrônico")
            st.write("Selecione uma opção no menu lateral para começar.")
            st.info("Os dados cadastrados são armazenados em um banco de dados SQLite.")
        elif pagina == "Manter clientes":
            ManterClienteUI.Main()
        elif pagina == "Manter categorias":
            ManterCategoriaUI.Main()
        elif pagina == "Manter produtos":
            ManterProdutoUI.Main()
        elif pagina == "Reajustar preços":
            ReajustarProdutoUI.Main()
