from views.login_window import LoginWindow
from views.home_window import HomeWindow
from views.contact_window import ContactWindow
from controllers.login_controller import LoginController
from controllers.contact_controller import ContactController

class App:
    def __init__(self):
        self.login_controller = LoginController(self)
        self.contact_controller = ContactController()
        self.current_window = None
        self.show_login_window()
    
    def show_login_window(self):
        if self.current_window:
            self.current_window.destroy()
        
        self.current_window = LoginWindow(self.login_controller)
        self.current_window.mainloop()
    
    def show_home_window(self, user_email):
        if self.current_window:
            self.current_window.destroy()
        
        self.current_window = HomeWindow(self, user_email)
        self.current_window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def open_contact_window(self, user_email):
        if self.current_window:
            self.current_window.destroy()
        
        self.current_window = ContactWindow(self.contact_controller, user_email)
        self.current_window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def logout(self):
        if self.current_window:
            self.current_window.destroy()
        self.show_login_window()
    
    def on_close(self):
        if self.current_window:
            self.current_window.destroy()
        exit(0)

if __name__ == "__main__":
    app = App()