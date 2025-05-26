import tkinter as tk
from tkinter import messagebox, ttk

class LoginWindow(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Agenda de Contactos - Login")
        self.geometry("400x300")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        
        self._create_widgets()
    
    def _create_widgets(self):
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(main_frame, text="Agenda de Contactos", font=("Arial", 16)).pack(pady=10)
        
        notebook = ttk.Notebook(main_frame)
        notebook.pack(expand=True, fill=tk.BOTH)
        
        # Login Tab
        login_tab = ttk.Frame(notebook)
        notebook.add(login_tab, text="Iniciar Sesión")
        
        tk.Label(login_tab, text="Correo electrónico:").pack(pady=(10, 0))
        self.login_email = tk.Entry(login_tab)
        self.login_email.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(login_tab, text="Contraseña:").pack()
        self.login_password = tk.Entry(login_tab, show="*")
        self.login_password.pack(fill=tk.X, pady=(0, 10))
        
        login_btn = tk.Button(login_tab, text="Iniciar Sesión", command=self._on_login)
        login_btn.pack(pady=10)
        
        # Register Tab
        register_tab = ttk.Frame(notebook)
        notebook.add(register_tab, text="Registrarse")
        
        tk.Label(register_tab, text="Correo electrónico:").pack(pady=(10, 0))
        self.register_email = tk.Entry(register_tab)
        self.register_email.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(register_tab, text="Contraseña:").pack()
        self.register_password = tk.Entry(register_tab, show="*")
        self.register_password.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(register_tab, text="Confirmar contraseña:").pack()
        self.register_confirm = tk.Entry(register_tab, show="*")
        self.register_confirm.pack(fill=tk.X, pady=(0, 10))
        
        register_btn = tk.Button(register_tab, text="Registrarse", command=self._on_register)
        register_btn.pack(pady=0)
    
    def _on_login(self):
        email = self.login_email.get()
        password = self.login_password.get()
        
        if self.controller.login(email, password):
            # Login exitoso, la ventana se cerrará automáticamente
            pass
        else:
            self.show_error("Credenciales incorrectas")
    
    def _on_register(self):
        email = self.register_email.get()
        password = self.register_password.get()
        confirm = self.register_confirm.get()
        
        if not email or not password or not confirm:
            self.show_error("Todos los campos son obligatorios")
            return
        
        if password != confirm:
            self.show_error("Las contraseñas no coinciden")
            return
        
        if len(password) < 6:
            self.show_error("La contraseña debe tener al menos 6 caracteres")
            return
        
        success, message = self.controller.register(email, password)
        if success:
            self.show_success(message)
            self.clear_fields()
        else:
            self.show_error(message)
    
    def show_error(self, message):
        messagebox.showerror("Error", message)
    
    def show_success(self, message):
        messagebox.showinfo("Éxito", message)
    
    def clear_fields(self):
        self.login_email.delete(0, tk.END)
        self.login_password.delete(0, tk.END)
        self.register_email.delete(0, tk.END)
        self.register_password.delete(0, tk.END)
        self.register_confirm.delete(0, tk.END)
    
    def _on_close(self):
        self.destroy()
        self.controller.app.on_close()