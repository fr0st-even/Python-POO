class Contact:
    def __init__(self, name, phone, email, notes=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.notes = notes or ""
    
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'notes': self.notes
        }
    
    @classmethod
    def from_dict(cls, contact_dict):
        return cls(
            contact_dict['name'],
            contact_dict['phone'],
            contact_dict['email'],
            contact_dict.get('notes', '')
        )
    
    @staticmethod
    def validate_email(email):
        return '@' in email and '.' in email.split('@')[-1]
    
    @staticmethod
    def validate_phone(phone):
        return phone.isdigit()