import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('clientes_pedidos.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER,
                descricao TEXT NOT NULL,
                quantidade INTEGER,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        ''')
        self.conn.commit()

    def insert_cliente(self, nome, email):
        self.conn.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
        self.conn.commit()

    def update_cliente(self, cid, nome, email):
        self.conn.execute('UPDATE clientes SET nome=?, email=? WHERE id=?', (nome, email, cid))
        self.conn.commit()

    def delete_cliente(self, cid):
        self.conn.execute('DELETE FROM clientes WHERE id=?', (cid,))
        self.conn.commit()

    def fetch_clientes(self):
        cursor = self.conn.execute('SELECT id, nome, email FROM clientes')
        return cursor.fetchall()

    def insert_pedido(self, cliente_id, descricao, quantidade):
        self.conn.execute('INSERT INTO pedidos (cliente_id, descricao, quantidade) VALUES (?, ?, ?)',
                          (cliente_id, descricao, quantidade))
        self.conn.commit()

    def update_pedido(self, pid, cliente_id, descricao, quantidade):
        self.conn.execute('''
            UPDATE pedidos SET cliente_id=?, descricao=?, quantidade=? WHERE id=?
        ''', (cliente_id, descricao, quantidade, pid))
        self.conn.commit()

    def delete_pedido(self, pid):
        self.conn.execute('DELETE FROM pedidos WHERE id=?', (pid,))
        self.conn.commit()

    def fetch_pedidos(self):
        query = '''
            SELECT pedidos.id, clientes.nome, pedidos.descricao, pedidos.quantidade
            FROM pedidos
            JOIN clientes ON pedidos.cliente_id = clientes.id
        '''
        cursor = self.conn.execute(query)
        return cursor.fetchall()
