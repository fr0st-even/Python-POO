from managers.user_manager import UserManager

class LoginController:
    def __init__(self, app):
        self.app = app
        self.current_user = None
    
    def login(self, email, password):
        user = UserManager.authenticate_user(email, password)
        if user:
            self.current_user = user
            self.app.show_home_window(user.email)
            return True
        return False
    
    def register(self, email, password):
        success, message = UserManager.register_user(email, password)
        return success, message  # Simplemente retornamos el estado y mensaje
    
    def logout(self):
        self.current_user = None
        self.app.logout()