import re

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password  # Ahora almacena la contraseña en texto plano
    
    def to_dict(self):
        return {
            'email': self.email,
            'password': self.password  # Sin codificación
        }
    
    @classmethod
    def from_dict(cls, user_dict):
        return cls(user_dict['email'], user_dict['password'])
    
    def verify_password(self, password):
        return self.password == password  # Comparación directa
    
    @staticmethod
    def validate_email_domain(email):
        """Valida que el dominio del correo sea uno permitido"""
        valid_domains = [
            'gmail.com', 'outlook.com', 'hotmail.com', 'yahoo.com',
            'protonmail.com', 'icloud.com', 'aol.com', 'mail.com',
            'zoho.com', 'yandex.com'
        ]
        
        # Extraer el dominio del correo
        match = re.match(r'^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', email)
        if not match:
            return False
        
        domain = match.group(1).lower()
        return domain in valid_domains