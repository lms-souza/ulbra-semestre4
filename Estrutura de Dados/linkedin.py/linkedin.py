import sqlite3

# Função para criar o banco de dados
def criar_banco():
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            perfil_linkedin TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conexoes (
            id INTEGER PRIMARY KEY,
            contato1_id INTEGER,
            contato2_id INTEGER,
            FOREIGN KEY (contato1_id) REFERENCES contatos(id),
            FOREIGN KEY (contato2_id) REFERENCES contatos(id)
        )
    ''')

    conn.commit()
    conn.close()

# Função para adicionar um contato
def adicionar_contato(nome, perfil_linkedin):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (?, ?)', (nome, perfil_linkedin))
    conn.commit()
    conn.close()

# Função para listar contatos
def listar_contatos():
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()

    conn.close()
    return contatos

# Função para adicionar uma conexão
def adicionar_conexao(contato1_id, contato2_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = ? AND contato2_id = ?) OR (contato1_id = ? AND contato2_id = ?)',
                      (contato1_id, contato2_id, contato2_id, contato1_id))

        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (?, ?)', (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos já existe.")
        
        conn.commit()
        
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Ocorreu um erro de concorrência. Tente novamente.")
        
    conn.close()

# Função para listar conexões de um contato
def listar_conexoes(contato_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = ? THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = ? OR conexoes.contato2_id = ?
    ''', (contato_id, contato_id, contato_id))

    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

# Função para excluir um contato
def excluir_contato(contato_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('BEGIN')

    try:
        cursor.execute('DELETE FROM conexoes WHERE contato1_id = ? OR contato2_id = ?', (contato_id, contato_id))
        cursor.execute('DELETE FROM contatos WHERE id = ?', (contato_id,))
        conn.commit()
        print("Contato excluído com sucesso.")
    except (sqlite3.IntegrityError, sqlite3.OperationalError):
        conn.rollback()
        print("Ocorreu um erro ao excluir o contato. Tente novamente.")

    conn.close()

# Função para validar o id de um contato
def validar_contato(contato_id):
    conn = sqlite3.connect('linkedin_network.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos WHERE id = ?', (contato_id,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        return False
    else:
        return True

# Função principal do menu
def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Adicionar Conexão")
        print("4. Listar Conexões de um Contato")
        print("5. Excluir Contato")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            perfil_linkedin = input("Perfil do LinkedIn: ")
            adicionar_contato(nome, perfil_linkedin)
        elif escolha == "2":
            contatos = listar_contatos()
            print("Lista de Contatos:")
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn: {contato[2]}")
        elif escolha == "3":
            contato1_id = int(input("ID do primeiro contato: "))
            if not validar_contato(contato1_id):
                print("ID inválido ou inexistente.")
                continue
            contato2_id = int(input("ID do segundo contato: "))
            if not validar_contato(contato2_id):
                print("ID inválido ou inexistente.")
                continue
            adicionar_conexao(contato1_id, contato2_id)
        elif escolha == "4":
            contato_id = int(input("ID do contato: "))
            if not validar_contato(contato_id):
                print("ID inválido ou inexistente.")
                continue
            conexoes = listar_conexoes(contato_id)
            print("Conexões do Contato:")
            for conexao in conexoes:
                print(conexao[0])
        elif escolha == "5":
            contato_id = int(input("ID do contato a ser excluído: "))
            if not validar_contato(contato_id):
                print("ID inválido ou inexistente.")
                continue
            excluir_contato(contato_id)
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    criar_banco()  # Certifique-se de que as tabelas estão criadas
    menu()
