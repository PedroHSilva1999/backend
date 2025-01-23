from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import os

app = FastAPI(title="API de Filmes", version="1.0.0")

class Filme(BaseModel):
    titulo: str
    diretor: str
    ano: int
    genero: str

class FilmeResponse(Filme):
    id: int

def get_db():
    db = sqlite3.connect('filmes.db')
    try:
        db.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                diretor TEXT NOT NULL,
                ano INTEGER NOT NULL,
                genero TEXT NOT NULL
            )
        ''')
        db.commit()
        return db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao banco de dados: {str(e)}")

@app.get("/filmes", response_model=List[FilmeResponse])
def listar_filmes():
    db = get_db()
    try:
        filmes = db.execute("SELECT * FROM filmes").fetchall()
        return [
            FilmeResponse(
                id=filme[0],
                titulo=filme[1],
                diretor=filme[2],
                ano=filme[3],
                genero=filme[4]
            )
            for filme in filmes
        ]
    finally:
        db.close()

@app.post("/filmes", response_model=FilmeResponse, status_code=201)
def criar_filme(filme: Filme):
    db = get_db()
    try:
        cursor = db.execute(
            "INSERT INTO filmes (titulo, diretor, ano, genero) VALUES (?, ?, ?, ?)",
            (filme.titulo, filme.diretor, filme.ano, filme.genero)
        )
        db.commit()
        
        novo_filme = db.execute(
            "SELECT * FROM filmes WHERE id = ?",
            (cursor.lastrowid,)
        ).fetchone()
        
        return FilmeResponse(
            id=novo_filme[0],
            titulo=novo_filme[1],
            diretor=novo_filme[2],
            ano=novo_filme[3],
            genero=novo_filme[4]
        )
    finally:
        db.close()

@app.get("/filmes/{filme_id}", response_model=FilmeResponse)
def obter_filme(filme_id: int):
    db = get_db()
    try:
        filme = db.execute(
            "SELECT * FROM filmes WHERE id = ?",
            (filme_id,)
        ).fetchone()
        
        if filme is None:
            raise HTTPException(status_code=404, detail="Filme não encontrado")
            
        return FilmeResponse(
            id=filme[0],
            titulo=filme[1],
            diretor=filme[2],
            ano=filme[3],
            genero=filme[4]
        )
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
