from models.contact import Contact

class Agenda:
    def __init__(self, user_email):
        self.user_email = user_email
        self.contacts = []
    
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def edit_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            return True
        return False
    
    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            return True
        return False
    
    def search_contact(self, name):
        return [contact for contact in self.contacts if name.lower() in contact.name.lower()]
    
    def to_dict(self):
        return {
            'user_email': self.user_email,
            'contacts': [contact.to_dict() for contact in self.contacts]
        }
    
    @classmethod
    def from_dict(cls, agenda_dict):
        agenda = cls(agenda_dict['user_email'])
        agenda.contacts = [Contact.from_dict(contact) for contact in agenda_dict['contacts']]
        return agenda