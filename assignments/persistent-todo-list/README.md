# 📘 Atividade: Lista de Tarefas Persistente

## 🎯 Objetivo

Aprenda a salvar e recuperar dados em arquivos usando apenas a biblioteca padrão do Python. Você vai construir uma lista de tarefas que continua existindo mesmo depois que o programa é encerrado, praticando `open()`, o bloco `with` e o módulo `json`.

## 📝 Tarefas

### 🛠️ Escrever e ler um arquivo de texto

#### Descrição

Antes de guardar tarefas, pratique o básico: crie funções que gravem linhas em um arquivo de texto e depois leiam esse conteúdo de volta.

#### Requisitos

O programa concluído deve:

- Implementar `save_note(filename, text)` que acrescente `text` como uma nova linha ao final do arquivo, usando `with open(..., "a")`.
- Implementar `read_notes(filename)` que retorne uma lista com todas as linhas do arquivo, sem o `\n` no final de cada uma.
- Retornar uma lista vazia em `read_notes` se o arquivo ainda não existir (dica: use `try`/`except FileNotFoundError`).
- Demonstrar o uso salvando duas anotações em `notes.txt` e imprimindo o resultado de `read_notes("notes.txt")`.

Exemplo de saída:

```text
['Estudar para a prova de história', 'Levar o livro para a biblioteca']
```


### 🛠️ Salvar e carregar tarefas em JSON

#### Descrição

Linhas de texto simples não guardam informações extras, como se a tarefa já foi concluída. Use o módulo `json` para salvar uma lista de dicionários e recarregá-la quando o programa iniciar.

#### Requisitos

O programa concluído deve:

- Representar cada tarefa como um dicionário no formato `{"title": "Comprar leite", "done": False}`.
- Implementar `save_tasks(filename, tasks)` que grave a lista no arquivo usando `json.dump()`.
- Implementar `load_tasks(filename)` que leia o arquivo com `json.load()` e retorne a lista; se o arquivo não existir, retorne uma lista vazia.
- Demonstrar que os dados persistem: salve uma lista com duas tarefas em `tasks.json`, carregue-a de volta e imprima o resultado.

Exemplo do conteúdo de `tasks.json`:

```json
[
  {"title": "Comprar leite", "done": false},
  {"title": "Terminar o dever de matemática", "done": true}
]
```


### 🛠️ Criar o menu da lista de tarefas

#### Descrição

Junte tudo em um pequeno programa interativo. Ao iniciar, ele carrega as tarefas salvas; a cada alteração, grava o arquivo novamente, para que nada se perca ao fechar o programa.

#### Requisitos

O programa concluído deve:

- Carregar as tarefas de `tasks.json` assim que o programa começar.
- Exibir um menu com as opções: `1` adicionar tarefa, `2` listar tarefas, `3` concluir tarefa e `4` sair, repetindo até o usuário escolher sair.
- Ao listar, mostrar o número de cada tarefa e marcar as concluídas com `[x]` e as pendentes com `[ ]`.
- Ao adicionar ou concluir uma tarefa, chamar `save_tasks` imediatamente após a alteração.
- Exibir uma mensagem amigável se o usuário informar um número de tarefa inválido ao concluir.

Exemplo de interação:

```text
=== Minha Lista de Tarefas ===
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Sair
Escolha uma opção: 2

[ ] 1. Comprar leite
[x] 2. Terminar o dever de matemática
```
