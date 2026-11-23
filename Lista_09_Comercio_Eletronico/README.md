# POO – Lista 09 – Comércio Eletrônico

Projeto em Python com Streamlit, organizado em camadas.

## Estrutura

- `model/`: classes Cliente, Categoria e Produto.
- `dao/`: operações de banco de dados SQLite.
- `service/`: operações utilizadas pelas interfaces.
- `templates/`: IndexUI, ManterClienteUI, ManterCategoriaUI, ManterProdutoUI e ReajustarProdutoUI.
- `app.py`: ponto de entrada da aplicação.
- `dados/comercio.db`: banco de dados criado automaticamente na primeira execução.

## Como executar

1. Abra a pasta do projeto no VS Code.
2. Abra o terminal na pasta `Lista_09_Comercio_Eletronico`.
3. Instale a dependência:

   `pip install -r requirements.txt`

4. Execute:

   `streamlit run app.py`

## Persistência

Os DAOs utilizam SQLite. Os registros são gravados no arquivo `dados/comercio.db` e permanecem salvos após fechar a aplicação.

## Observação

Cadastre uma categoria antes de cadastrar produtos. Uma categoria que possui produtos vinculados não pode ser excluída.
