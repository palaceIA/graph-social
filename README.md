# 📘 Grafo Social Interativo

## 📝 Descrição do Projeto
Este projeto implementa um **Grafo Social** utilizando **Python 3.8+**, seguindo uma abordagem totalmente **orientada a objetos (OOP)**.  
Cada vértice representa um usuário e cada aresta representa uma relação de amizade.

A solução também inclui um **sistema interativo no terminal**, permitindo que o usuário:

- Cadastre novos usuários;
- Crie amizades;
- Liste todo o grafo;
- Receba sugestões de amizade baseadas em vizinhos em comum;
- Calcule a distância social (menor caminho) entre dois usuários;
- Liste as componentes conexas do grafo.

O projeto foi desenvolvido com base no enunciado do trabalho da disciplina de Estruturas de Dados, utilizando grafos como modelo de representação e explorando tanto requisitos mínimos quanto funcionalidades avançadas.

---

## 🖥 Linguagem e Versão Utilizada
- **Python 3.8+**  
  (Compatível com Python 3.8, 3.9, 3.10, 3.11 e 3.12)

---

## ▶️ Instruções de Execução

### 1. Crie o ambiente virtual (opcional, mas recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
````

### 2. Execute o arquivo principal interativo

Dentro da pasta raiz do projeto, execute:

```bash
python main_interativo.py
```

### 3. O menu do sistema aparecerá assim:

```
===== MENU - GRAFO SOCIAL =====
1 - Adicionar usuário
2 - Criar amizade
3 - Mostrar grafo
4 - Sugerir amigos
5 - Distância social
6 - Componentes conexas
0 - Sair
================================
Escolha uma opção:
```

---

## 📥 Exemplos de Entrada/Saída

### ➤ **Exemplo 1 — Adicionar usuários e mostrar o grafo**

Entrada:

```
1
alice
1
bruno
3
```

Saída:

```
===== GRAFO SOCIAL =====
alice: []
bruno: []
```

---

### ➤ **Exemplo 2 — Criar amizade**

Entrada:

```
2
alice
bruno
3
```

Saída:

```
alice: [bruno]
bruno: [alice]
```

---

### ➤ **Exemplo 3 — Sugestão de amigos**

Entrada:

```
4
alice
5
```

Saída:

```
===== Sugestões de amigos para 'alice' =====
 → carla (vizinhos em comum: 1)
 → diego (vizinhos em comum: 1)
```

---

### ➤ **Exemplo 4 — Distância social**

Entrada:

```
5
alice
erica
```

Saída:

```
Distância: 3
Caminho: alice → bruno → diego → erica
```

---

### ➤ **Exemplo 5 — Componentes conexas**

Entrada:

```
6
```

Saída:

```
Componente 1: ['alice', 'bruno', 'carla', 'diego', 'erica']
Componente 2: ['felipe', 'giovana', 'helena']
```

### 🚀 **Funcionalidades Avançadas Implementadas**

* **Sugestão de amigos** baseada em vizinhos em comum
* **Distância social (BFS)** mostrando caminho mínimo
* **Componentes conexas**
* **Sistema interativo de console**

---
