import json
import os
from models.user import User

USERS_FILE = 'data/users.json'

class UserManager:
    @staticmethod
    def load_users():
        if not os.path.exists(USERS_FILE):
            return []
        
        try:
            with open(USERS_FILE, 'r') as file:
                users_data = json.load(file)
                return [User.from_dict(user_data) for user_data in users_data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    @staticmethod
    def save_users(users):
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, 'w') as file:
            json.dump([user.to_dict() for user in users], file, indent=4)
    
    @staticmethod
    def register_user(email, password):
        users = UserManager.load_users()
        
        # Validar dominio de correo
        if not User.validate_email_domain(email):
            return False, "Dominio de correo no permitido"
        
        # Verificar si el usuario ya existe
        if any(user.email == email for user in users):
            return False, "El correo ya está registrado"
        
        new_user = User(email, password)
        users.append(new_user)
        UserManager.save_users(users)
        return True, "Registro exitoso"
    
    @staticmethod
    def authenticate_user(email, password):
        users = UserManager.load_users()
        for user in users:
            if user.email == email and user.verify_password(password):
                return user
        return None