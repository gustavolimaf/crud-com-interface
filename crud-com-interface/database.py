class Database:
    def __init__(self):
        self.clientes = []
        self.pedidos = []
        self.cliente_id = 1
        self.pedido_id = 1

    def insert_cliente(self, nome, email):
        self.clientes.append((self.cliente_id, nome, email))
        self.cliente_id += 1

    def update_cliente(self, cid, nome, email):
        cid = int(cid)
        self.clientes = [(c[0], nome, email) if c[0] == cid else c for c in self.clientes]

    def delete_cliente(self, cid):
        cid = int(cid)
        self.clientes = [c for c in self.clientes if c[0] != cid]
        self.pedidos = [p for p in self.pedidos if p[1] != cid]

    def fetch_clientes(self):
        return self.clientes

    def insert_pedido(self, cid, desc, qt):
        self.pedidos.append((self.pedido_id, cid, desc, qt))
        self.pedido_id += 1

    def update_pedido(self, pid, cid, desc, qt):
        pid = int(pid)
        self.pedidos = [(p[0], cid, desc, qt) if p[0] == pid else p for p in self.pedidos]

    def delete_pedido(self, pid):
        pid = int(pid)
        self.pedidos = [p for p in self.pedidos if p[0] != pid]

    def fetch_pedidos(self):
        display = []
        clientes_dict = {c[0]: c[1] for c in self.clientes}
        for p in self.pedidos:
            display.append((p[0], clientes_dict.get(p[1], 'Desconhecido'), p[2], p[3]))
        return display
