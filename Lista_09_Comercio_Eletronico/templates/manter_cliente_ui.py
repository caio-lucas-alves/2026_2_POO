import streamlit as st
import pandas as pd
from service.service import Service

class ManterClienteUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de clientes")
        aba = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])

        with aba[0]:
            with st.form("inserir_cliente"):
                nome = st.text_input("Nome")
                email = st.text_input("E-mail")
                fone = st.text_input("Telefone")
                enviar = st.form_submit_button("Cadastrar cliente")
                if enviar:
                    if nome.strip() and email.strip() and fone.strip():
                        Service.cliente_inserir(nome, email, fone)
                        st.success("Cliente cadastrado com sucesso.")
                    else:
                        st.error("Preencha todos os campos.")

        with aba[1]:
            clientes = Service.cliente_listar()
            if clientes:
                dados = [{"ID": c.id, "Nome": c.nome, "E-mail": c.email, "Telefone": c.fone} for c in clientes]
                st.dataframe(pd.DataFrame(dados), use_container_width=True, hide_index=True)
            else:
                st.info("Não existem clientes cadastrados.")

        with aba[2]:
            clientes = Service.cliente_listar()
            if clientes:
                opcoes = {f"{c.id} - {c.nome}": c.id for c in clientes}
                selecionado = st.selectbox("Cliente", list(opcoes.keys()), key="cliente_atualizar")
                cliente = Service.cliente_listar_id(opcoes[selecionado])
                with st.form("atualizar_cliente"):
                    nome = st.text_input("Nome", value=cliente.nome)
                    email = st.text_input("E-mail", value=cliente.email)
                    fone = st.text_input("Telefone", value=cliente.fone)
                    enviar = st.form_submit_button("Salvar alterações")
                    if enviar:
                        if nome.strip() and email.strip() and fone.strip():
                            Service.cliente_atualizar(cliente.id, nome, email, fone)
                            st.success("Cliente atualizado com sucesso.")
                        else:
                            st.error("Preencha todos os campos.")
            else:
                st.info("Não existem clientes cadastrados.")

        with aba[3]:
            clientes = Service.cliente_listar()
            if clientes:
                opcoes = {f"{c.id} - {c.nome}": c.id for c in clientes}
                selecionado = st.selectbox("Cliente", list(opcoes.keys()), key="cliente_excluir")
                if st.button("Excluir cliente"):
                    Service.cliente_excluir(opcoes[selecionado])
                    st.success("Cliente excluído com sucesso.")
            else:
                st.info("Não existem clientes cadastrados.")
