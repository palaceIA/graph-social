"""
social_graph.py
Implementação de um Grafo Social com funcionalidades avançadas.
"""

from typing import List, Dict, Optional, Tuple
from collections import deque
from graphs.graph_base import Grafo


class GrafoSocial(Grafo):
    """
    Grafo Social onde cada vértice representa uma pessoa (usuário).
    """

    def __init__(self):
        super().__init__(direcionado=False)


    def adicionar_usuario(self, usuario: str) -> None:
        self.adicionar_vertice(usuario)

    def adicionar_amizade(self, usuario_a: str, usuario_b: str) -> None:
        if usuario_a != usuario_b:
            self.adicionar_aresta(usuario_a, usuario_b)

    def remover_usuario(self, usuario: str) -> None:
        self.remover_vertice(usuario)

    def remover_amizade(self, usuario_a: str, usuario_b: str) -> None:
        self.remover_aresta(usuario_a, usuario_b)

    def sugerir_amigos(self, usuario: str, quantidade: int = 5) -> List[Tuple[str, int]]:
        """
        Sugere amigos com base na quantidade de vizinhos em comum.
        Retorna uma lista ordenada de (possivel_amigo, pontuação).
        """
        if usuario not in self.lista_adjacencia:
            return []

        amigos_atuais = self.lista_adjacencia[usuario]
        pontuacoes: Dict[str, int] = {}

        for amigo in amigos_atuais:
            for possivel_amigo in self.lista_adjacencia.get(amigo, set()):
                if possivel_amigo == usuario:
                    continue
                if possivel_amigo in amigos_atuais:
                    continue

                pontuacoes[possivel_amigo] = pontuacoes.get(possivel_amigo, 0) + 1

        return sorted(
            pontuacoes.items(),
            key=lambda x: (-x[1], x[0])
        )[:quantidade]

    def distancia_social(self, origem: str, destino: str) -> Optional[Tuple[int, List[str]]]:
        """
        Calcula a distância social mínima entre dois usuários (via BFS).
        Retorna (distância, caminho) ou None se não houver conexão.
        """
        if origem not in self.lista_adjacencia or destino not in self.lista_adjacencia:
            return None

        if origem == destino:
            return 0, [origem]

        fila = deque([origem])
        visitados = {origem}
        predecessores: Dict[str, Optional[str]] = {origem: None}

        while fila:
            usuario_atual = fila.popleft()

            for vizinho in self.lista_adjacencia[usuario_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    predecessores[vizinho] = usuario_atual

                    if vizinho == destino:
                        caminho = [destino]
                        atual = destino

                        while predecessores[atual] is not None:
                            atual = predecessores[atual]
                            caminho.append(atual)

                        caminho.reverse()
                        return len(caminho) - 1, caminho

                    fila.append(vizinho)

        return None

    def componentes_conexas(self) -> List[set]:
        """
        Retorna todas as componentes conexas do grafo.
        """
        visitados = set()
        componentes = []

        for usuario in self.lista_adjacencia.keys():
            if usuario in visitados:
                continue

            componente_atual = set()
            fila = [usuario]
            visitados.add(usuario)

            while fila:
                atual = fila.pop()
                componente_atual.add(atual)

                for vizinho in self.lista_adjacencia[atual]:
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)

            componentes.append(componente_atual)

        return componentes
