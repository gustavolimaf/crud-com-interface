import tkinter as tk
from tkinter import ttk, messagebox
from database import Database

class Application:
    def __init__(self, root):
        self.db = Database()
        root.title("Sistema de Clientes & Pedidos")
        root.geometry('800x600')
        root.resizable(False, False)
        self.style = ttk.Style(root)
        self.style.theme_use('clam')
        self.style.configure('Treeview', rowheight=25)
        self.style.configure('TButton', padding=6, relief='flat')
        self.build_ui(root)
        self.load_data()

    def build_ui(self, root):
        self.notebook = ttk.Notebook(root)
        self.frame_c = ttk.Frame(self.notebook, padding=10)
        self.frame_p = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.frame_c, text='👥 Clientes')
        self.notebook.add(self.frame_p, text='🚲 Pedidos')
        self.notebook.pack(fill='both', expand=True)
        self._build_clientes_tab()
        self._build_pedidos_tab()

    def _build_clientes_tab(self):
        frm = ttk.LabelFrame(self.frame_c, text='Dados do Cliente', padding=10)
        frm.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        ttk.Label(frm, text='Nome:').grid(row=0, column=0, sticky='w')
        self.entry_nome = ttk.Entry(frm, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(frm, text='Email:').grid(row=1, column=0, sticky='w')
        self.entry_email = ttk.Entry(frm, width=30)
        self.entry_email.grid(row=1, column=1, padx=5, pady=2)
        btns = ttk.Frame(frm)
        btns.grid(row=2, column=0, columnspan=2, pady=10)
        for txt, cmd in [('Inserir', self.add_cliente), ('Editar', self.edit_cliente), ('Excluir', self.del_cliente)]:
            ttk.Button(btns, text=txt, command=cmd).pack(side='left', padx=5)

        cols = ('ID', 'Nome', 'Email')
        tbl_frm = ttk.Frame(self.frame_c)
        tbl_frm.grid(row=1, column=0, sticky='nsew')
        scroll = ttk.Scrollbar(tbl_frm, orient='vertical')
        scroll.pack(side='right', fill='y')
        self.tree_c = ttk.Treeview(tbl_frm, columns=cols, show='headings', yscrollcommand=scroll.set)
        for c in cols:
            self.tree_c.heading(c, text=c)
            self.tree_c.column(c, width=200, anchor='center')
        self.tree_c.pack(fill='both', expand=True)
        scroll.config(command=self.tree_c.yview)

    def _build_pedidos_tab(self):
        frm = ttk.LabelFrame(self.frame_p, text='Dados do Pedido', padding=10)
        frm.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        ttk.Label(frm, text='Cliente:').grid(row=0, column=0, sticky='w')
        self.combo_c = ttk.Combobox(frm, width=28)
        self.combo_c.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(frm, text='Descrição:').grid(row=1, column=0, sticky='w')
        self.entry_desc = ttk.Entry(frm, width=30)
        self.entry_desc.grid(row=1, column=1, padx=5, pady=2)
        ttk.Label(frm, text='Quantidade:').grid(row=2, column=0, sticky='w')
        self.entry_qt = ttk.Entry(frm, width=30)
        self.entry_qt.grid(row=2, column=1, padx=5, pady=2)
        btns = ttk.Frame(frm)
        btns.grid(row=3, column=0, columnspan=2, pady=10)
        for txt, cmd in [('Inserir', self.add_pedido), ('Editar', self.edit_pedido), ('Excluir', self.del_pedido)]:
            ttk.Button(btns, text=txt, command=cmd).pack(side='left', padx=5)

        cols = ('ID', 'Cliente', 'Descrição', 'Qtd')
        tbl_frm = ttk.Frame(self.frame_p)
        tbl_frm.grid(row=1, column=0, sticky='nsew')
        scroll = ttk.Scrollbar(tbl_frm, orient='vertical')
        scroll.pack(side='right', fill='y')
        self.tree_p = ttk.Treeview(tbl_frm, columns=cols, show='headings', yscrollcommand=scroll.set)
        for c in cols:
            self.tree_p.heading(c, text=c)
            self.tree_p.column(c, width=180, anchor='center')
        self.tree_p.pack(fill='both', expand=True)
        scroll.config(command=self.tree_p.yview)

    def add_cliente(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        if not nome:
            messagebox.showwarning('Validação', 'Nome obrigatório')
            return
        self.db.insert_cliente(nome, email)
        self.load_clientes()
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def edit_cliente(self):
        try:
            sel = self.tree_c.selection()[0]
        except:
            messagebox.showinfo('Seleção', 'Selecione um cliente')
            return
        cid, _, _ = self.tree_c.item(sel, 'values')
        novo_nome = self.entry_nome.get().strip()
        novo_email = self.entry_email.get().strip()
        if not novo_nome:
            messagebox.showwarning('Validação', 'Nome obrigatório')
            return
        self.db.update_cliente(cid, novo_nome, novo_email)
        self.load_clientes()

    def del_cliente(self):
        try:
            sel = self.tree_c.selection()[0]
        except:
            messagebox.showinfo('Seleção', 'Selecione um cliente')
            return
        cid = self.tree_c.item(sel, 'values')[0]
        if messagebox.askyesno('Confirmar', 'Excluir este cliente?'):
            self.db.delete_cliente(cid)
            self.load_clientes()

    def add_pedido(self):
        try:
            cid = int(self.combo_c.get().split(' - ')[0])
            desc = self.entry_desc.get().strip()
            qt = int(self.entry_qt.get())
            if not desc:
                raise ValueError
        except:
            messagebox.showwarning('Validação', 'Verifique campos do pedido')
            return
        self.db.insert_pedido(cid, desc, qt)
        self.load_pedidos()
        self.entry_desc.delete(0, tk.END)
        self.entry_qt.delete(0, tk.END)

    def edit_pedido(self):
        try:
            sel = self.tree_p.selection()[0]
        except:
            messagebox.showinfo('Seleção', 'Selecione um pedido')
            return
        pid = self.tree_p.item(sel, 'values')[0]
        cid = int(self.combo_c.get().split(' - ')[0])
        desc = self.entry_desc.get().strip()
        qt = int(self.entry_qt.get())
        self.db.update_pedido(pid, cid, desc, qt)
        self.load_pedidos()

    def del_pedido(self):
        try:
            sel = self.tree_p.selection()[0]
        except:
            messagebox.showinfo('Seleção', 'Selecione um pedido')
            return
        pid = self.tree_p.item(sel, 'values')[0]
        if messagebox.askyesno('Confirmar', 'Excluir este pedido?'):
            self.db.delete_pedido(pid)
            self.load_pedidos()

    def load_clientes(self):
        for i in self.tree_c.get_children():
            self.tree_c.delete(i)
        for row in self.db.fetch_clientes():
            self.tree_c.insert('', tk.END, values=row)
        self.combo_c['values'] = [f"{r[0]} - {r[1]}" for r in self.db.fetch_clientes()]

    def load_pedidos(self):
        for i in self.tree_p.get_children():
            self.tree_p.delete(i)
        for row in self.db.fetch_pedidos():
            self.tree_p.insert('', tk.END, values=row)

    def load_data(self):
        self.load_clientes()
        self.load_pedidos()