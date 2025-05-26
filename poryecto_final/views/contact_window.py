import tkinter as tk
from tkinter import ttk, messagebox
from models.contact import Contact

class ContactWindow(tk.Toplevel):
    def __init__(self, controller, user_email):
        super().__init__()
        self.controller = controller
        self.user_email = user_email
        self.title(f"Contactos - {user_email}")
        self.geometry("800x600")
        
        self.selected_index = None
        self._create_widgets()
        self._load_contacts()
    
    def _create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Frame de búsqueda
        search_frame = tk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(search_frame, text="Buscar:").pack(side=tk.LEFT)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.search_entry.bind('<KeyRelease>', self._on_search)
        
        # Lista de contactos
        self.contacts_list = ttk.Treeview(main_frame, columns=('name', 'phone', 'email'), 
                                        show='headings', selectmode='browse')
        self.contacts_list.heading('name', text='Nombre')
        self.contacts_list.heading('phone', text='Teléfono')
        self.contacts_list.heading('email', text='Correo')
        self.contacts_list.column('name', width=200)
        self.contacts_list.column('phone', width=150)
        self.contacts_list.column('email', width=250)
        self.contacts_list.pack(expand=True, fill=tk.BOTH, pady=(0, 10))
        self.contacts_list.bind('<<TreeviewSelect>>', self._on_select)
        
        # Frame de botones
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Button(btn_frame, text="Nuevo", command=self._new_contact).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Editar", command=self._edit_contact).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self._delete_contact).pack(side=tk.LEFT, padx=5)
        
        # Frame del formulario
        form_frame = tk.LabelFrame(main_frame, text="Detalles del Contacto", padx=10, pady=10)
        form_frame.pack(fill=tk.BOTH)
        
        tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, sticky=tk.EW, pady=2, padx=(0, 10))
        
        tk.Label(form_frame, text="Teléfono:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=1, column=1, sticky=tk.EW, pady=2, padx=(0, 10))
        
        tk.Label(form_frame, text="Correo:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1, sticky=tk.EW, pady=2, padx=(0, 10))
        
        tk.Label(form_frame, text="Notas:").grid(row=3, column=0, sticky=tk.NW, pady=2)
        self.notes_text = tk.Text(form_frame, height=4, width=30)
        self.notes_text.grid(row=3, column=1, sticky=tk.EW, pady=2, padx=(0, 10))
        
        # Configurar expansión de columnas
        form_frame.columnconfigure(1, weight=1)
        
        # Botones del formulario
        form_btn_frame = tk.Frame(form_frame)
        form_btn_frame.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        
        self.save_btn = tk.Button(form_btn_frame, text="Guardar", command=self._save_contact)
        self.save_btn.pack(side=tk.LEFT, padx=5)
        tk.Button(form_btn_frame, text="Limpiar", command=self._clear_form).pack(side=tk.LEFT, padx=5)
    
    def _load_contacts(self):
        self.contacts_list.delete(*self.contacts_list.get_children())
        contacts = self.controller.get_contacts(self.user_email)
        for contact in contacts:
            self.contacts_list.insert('', tk.END, values=(
                contact.name, contact.phone, contact.email
            ))
    
    def _on_search(self, event=None):
        search_term = self.search_entry.get()
        filtered = self.controller.search_contacts(self.user_email, search_term)
        self.contacts_list.delete(*self.contacts_list.get_children())
        for contact in filtered:
            self.contacts_list.insert('', tk.END, values=(
                contact.name, contact.phone, contact.email
            ))
    
    def _on_select(self, event):
        selected = self.contacts_list.selection()
        if not selected:
            return
        
        self.selected_index = self.contacts_list.index(selected[0])
        contact = self.controller.get_contact(self.user_email, self.selected_index)
        
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact.name)
        
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact.phone)
        
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact.email)
        
        self.notes_text.delete(1.0, tk.END)
        self.notes_text.insert(1.0, contact.notes)
    
    def _new_contact(self):
        self.selected_index = None
        self._clear_form()
        self.name_entry.focus_set()
    
    def _edit_contact(self):
        if self.selected_index is None:
            messagebox.showwarning("Advertencia", "Seleccione un contacto para editar")
            return
        
        contact = self.controller.get_contact(self.user_email, self.selected_index)
        self._clear_form()
        
        self.name_entry.insert(0, contact.name)
        self.phone_entry.insert(0, contact.phone)
        self.email_entry.insert(0, contact.email)
        self.notes_text.insert(1.0, contact.notes)
    
    def _delete_contact(self):
        if self.selected_index is None:
            messagebox.showwarning("Advertencia", "Seleccione un contacto para eliminar")
            return
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este contacto?"):
            success = self.controller.delete_contact(self.user_email, self.selected_index)
            if success:
                self._load_contacts()
                self._clear_form()
                self.selected_index = None
    
    def _save_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        notes = self.notes_text.get(1.0, tk.END).strip()
        
        if not name or not phone or not email:
            messagebox.showwarning("Advertencia", "Nombre, teléfono y correo son obligatorios")
            return
        
        if not Contact.validate_email(email):
            messagebox.showwarning("Advertencia", "Ingrese un correo electrónico válido")
            return
        
        if not Contact.validate_phone(phone):
            messagebox.showwarning("Advertencia", "El teléfono debe contener solo números")
            return
        
        contact = Contact(name, phone, email, notes)
        
        if self.selected_index is None:
            # Nuevo contacto
            self.controller.add_contact(self.user_email, contact)
        else:
            # Editar contacto existente
            self.controller.update_contact(self.user_email, self.selected_index, contact)
        
        self._load_contacts()
        self._clear_form()
        self.selected_index = None
    
    def _clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.notes_text.delete(1.0, tk.END)