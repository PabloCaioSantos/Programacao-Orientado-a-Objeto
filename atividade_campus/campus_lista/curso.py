"""
arquivo: curso.py
-----------------
Define a classe Curso, que representa um curso pertencente a um campus.
Possui atributos básicos: código, nome e carga horária.

Também inclui métodos para atualizar dados e exibir informações do curso.
"""

class Curso:
    def __init__(self, codigo: int, nome: str, carga_horaria: int):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def atualizar_nome(self, novo_nome: str):
        self.nome = novo_nome

    def atualizar_ch(self, nova_ch: int):
        self.carga_horaria = nova_ch

    def __str__(self):
        return f"Curso {self.codigo} | Nome: {self.nome} | CH: {self.carga_horaria}h"
