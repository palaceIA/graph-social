from typing import Dict, List, Set

class Grafo:
    def __init__(self, direcionado: bool = False) -> None:
        self.direcionado = direcionado
        self.lista_adjacencia: Dict[str, Set[str]] = {}

    def adicionar_vertice(self, vertice: str) -> None:
        """Adiciona um vértice ao grafo, caso não exista."""
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = set()

    def adicionar_aresta(self, origem: str, destino: str) -> None:
        """
        Adiciona uma aresta entre dois vértices.
        Em grafos não-direcionados, adiciona o caminho de volta.
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)

        self.lista_adjacencia[origem].add(destino)

        if not self.direcionado:
            self.lista_adjacencia[destino].add(origem)

    def remover_aresta(self, origem: str, destino: str) -> None:
        """Remove a aresta entre origem → destino."""
        if origem in self.lista_adjacencia:
            self.lista_adjacencia[origem].discard(destino)
        if not self.direcionado and destino in self.lista_adjacencia:
            self.lista_adjacencia[destino].discard(origem)

    def remover_vertice(self, vertice: str) -> None:
        """Remove um vértice e todas as arestas associadas a ele."""
        if vertice not in self.lista_adjacencia:
            return

        for outro_vertice in list(self.lista_adjacencia.keys()):
            self.lista_adjacencia[outro_vertice].discard(vertice)

        del self.lista_adjacencia[vertice]

    def obter_vertices(self) -> List[str]:
        return list(self.lista_adjacencia.keys())

    def obter_vizinhos(self, vertice: str) -> Set[str]:
        return set(self.lista_adjacencia.get(vertice, set()))

    def possui_vertice(self, vertice: str) -> bool:
        return vertice in self.lista_adjacencia

    def possui_aresta(self, origem: str, destino: str) -> bool:
        return (
            origem in self.lista_adjacencia
            and destino in self.lista_adjacencia[origem]
        )

    def __str__(self) -> str:
        linhas = []
        for vertice in sorted(self.lista_adjacencia.keys()):
            vizinhos_formatados = ", ".join(sorted(self.lista_adjacencia[vertice]))
            linhas.append(f"{vertice}: [{vizinhos_formatados}]")
        return "\n".join(linhas)
