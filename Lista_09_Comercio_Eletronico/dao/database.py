import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DADOS_DIR = BASE_DIR / "dados"
DADOS_DIR.mkdir(exist_ok=True)
DB_PATH = DADOS_DIR / "comercio.db"

def conectar():
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                fone TEXT NOT NULL
            )
        """)
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS categoria (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL
            )
        """)
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL,
                idCategoria INTEGER NOT NULL,
                FOREIGN KEY (idCategoria) REFERENCES categoria(id)
                    ON UPDATE CASCADE ON DELETE RESTRICT
            )
        """)

criar_tabelas()
