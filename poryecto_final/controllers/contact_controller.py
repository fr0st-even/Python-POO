from managers.contact_manager import ContactManager
from models.contact import Contact

class ContactController:
    def get_contacts(self, user_email):
        agenda = ContactManager.load_agenda(user_email)
        return agenda.contacts
    
    def get_contact(self, user_email, index):
        agenda = ContactManager.load_agenda(user_email)
        if 0 <= index < len(agenda.contacts):
            return agenda.contacts[index]
        return None
    
    def search_contacts(self, user_email, search_term):
        agenda = ContactManager.load_agenda(user_email)
        return agenda.search_contact(search_term)
    
    def add_contact(self, user_email, contact):
        agenda = ContactManager.load_agenda(user_email)
        agenda.add_contact(contact)
        ContactManager.save_agenda(agenda)
    
    def update_contact(self, user_email, index, contact):
        agenda = ContactManager.load_agenda(user_email)
        if agenda.edit_contact(index, contact):
            ContactManager.save_agenda(agenda)
            return True
        return False
    
    def delete_contact(self, user_email, index):
        agenda = ContactManager.load_agenda(user_email)
        if agenda.delete_contact(index):
            ContactManager.save_agenda(agenda)
            return True
        return False