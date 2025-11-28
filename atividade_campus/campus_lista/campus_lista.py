"""
arquivo: campus_lista.py
------------------------
Define a classe CampusLista, responsável por gerenciar um campus da UFC.

Cada campus possui vários cursos, armazenados em uma lista interna.
Este arquivo implementa operações CRUD para cursos:

- cadastrar curso (CREATE)
- listar cursos (READ)
- atualizar curso (UPDATE)
- remover curso (DELETE)

Também possui busca por código e contagem automática de cursos.
"""

from .curso import Curso

class CampusLista:
    _id_curso = 1  # contador global de cursos

    def __init__(self, nome: str):
        self.nome = nome
        self.cursos = []

    # CREATE
    def cadastrar_curso(self, nome: str, carga_horaria: int):
        curso = Curso(CampusLista._id_curso, nome, carga_horaria)
        self.cursos.append(curso)
        CampusLista._id_curso += 1
        print(f"Curso cadastrado com sucesso:\n{curso}")

    # READ
    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado neste campus.")
        else:
            for curso in self.cursos:
                print(curso)

    def procurar_curso(self, codigo: int):
        return next((c for c in self.cursos if c.codigo == codigo), None)

    # UPDATE
    def atualizar_curso(self, codigo: int, novo_nome: str = None, nova_ch: int = None):
        curso = self.procurar_curso(codigo)
        if not curso:
            print("Curso não encontrado.")
            return

        if novo_nome:
            curso.atualizar_nome(novo_nome)
        if nova_ch:
            curso.atualizar_ch(nova_ch)

        print(f"Curso atualizado:\n{curso}")

    # DELETE
    def remover_curso(self, codigo: int):
        curso = self.procurar_curso(codigo)
        if curso:
            self.cursos.remove(curso)
            print(f"Curso {codigo} removido com sucesso.")
        else:
            print("Curso não encontrado.")

    def __str__(self):
        return f"Campus: {self.nome} | Total de Cursos: {len(self.cursos)}"
