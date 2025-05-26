import tkinter as tk
from tkinter import ttk

class HomeWindow(tk.Toplevel):
    def __init__(self, controller, user_email):
        super().__init__()
        self.controller = controller
        self.user_email = user_email
        self.title(f"Agenda de Contactos - {user_email}")
        self.geometry("600x400")
        
        self._create_widgets()
    
    def _create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Bienvenida
        tk.Label(main_frame, text=f"Bienvenido, {self.user_email}", 
                font=("Arial", 14)).pack(pady=10)
        
        # Botones
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="Gestionar Contactos", 
                 command=self._open_contacts).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Cerrar Sesión", 
                 command=self._logout).pack(side=tk.LEFT, padx=10)
    
    def _open_contacts(self):
        self.controller.open_contact_window(self.user_email)
    
    def _logout(self):
        self.controller.logout()
        self.destroy()