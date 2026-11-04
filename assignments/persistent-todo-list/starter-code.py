# Código Inicial para a Atividade de Lista de Tarefas Persistente
# Use apenas a biblioteca padrão do Python (nenhuma instalação necessária).

import json

NOTES_FILE = "notes.txt"
TASKS_FILE = "tasks.json"


# Tarefa 1: Escrever e ler um arquivo de texto

def save_note(filename, text):
    """Acrescenta `text` como uma nova linha ao final do arquivo."""
    # Dica: abra o arquivo no modo "a" (append) dentro de um bloco `with`
    pass


def read_notes(filename):
    """Retorna uma lista com as linhas do arquivo, sem o '\\n' final.

    Se o arquivo não existir, retorna uma lista vazia.
    """
    # Dica: use try/except FileNotFoundError
    pass


# Tarefa 2: Salvar e carregar tarefas em JSON

def save_tasks(filename, tasks):
    """Grava a lista de tarefas no arquivo em formato JSON."""
    # Dica: json.dump(tasks, arquivo)
    pass


def load_tasks(filename):
    """Lê a lista de tarefas do arquivo JSON.

    Se o arquivo não existir, retorna uma lista vazia.
    """
    # Dica: json.load(arquivo)
    pass


# Tarefa 3: Criar o menu da lista de tarefas

def show_menu():
    print("\n=== Minha Lista de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")


def main():
    tasks = load_tasks(TASKS_FILE)

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == "1":
            # Peça o título, adicione {"title": ..., "done": False} e salve
            pass
        elif option == "2":
            # Mostre cada tarefa com [x] ou [ ] e seu número
            pass
        elif option == "3":
            # Peça o número da tarefa, marque como concluída e salve
            pass
        elif option == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Exemplo de uso das Tarefas 1 e 2 (descomente para testar):
# save_note(NOTES_FILE, "Estudar para a prova de história")
# save_note(NOTES_FILE, "Levar o livro para a biblioteca")
# print(read_notes(NOTES_FILE))
#
# save_tasks(TASKS_FILE, [{"title": "Comprar leite", "done": False}])
# print(load_tasks(TASKS_FILE))

if __name__ == "__main__":
    main()
