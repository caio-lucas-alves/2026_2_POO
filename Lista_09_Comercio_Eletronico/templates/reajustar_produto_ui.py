import streamlit as st
from service.service import Service

class ReajustarProdutoUI:
    @staticmethod
    def Main():
        st.title("Reajustar preço dos produtos")
        st.write("Informe um percentual positivo para aumentar os preços ou negativo para aplicar uma promoção.")
        percentual = st.number_input(
            "Percentual (%)",
            value=0.0,
            step=1.0,
            format="%.2f"
        )
        if st.button("Aplicar reajuste"):
            produtos = Service.produto_listar()
            if not produtos:
                st.warning("Não existem produtos cadastrados.")
            elif percentual <= -100:
                st.error("O percentual não pode ser igual ou menor que -100%.")
            else:
                Service.produto_reajustar(percentual)
                st.success("Preços atualizados com sucesso.")
