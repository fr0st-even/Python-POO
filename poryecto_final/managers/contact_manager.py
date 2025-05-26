import json
import os
from models.agenda import Agenda

AGENDAS_DIR = 'data/agendas/'

class ContactManager:
    @staticmethod
    def get_agenda_filename(user_email):
        return f"{AGENDAS_DIR}agenda_{user_email}.json"
    
    @staticmethod
    def load_agenda(user_email):
        filename = ContactManager.get_agenda_filename(user_email)
        if not os.path.exists(filename):
            return Agenda(user_email)
        
        try:
            with open(filename, 'r') as file:
                agenda_data = json.load(file)
                return Agenda.from_dict(agenda_data)
        except (json.JSONDecodeError, FileNotFoundError):
            return Agenda(user_email)
    
    @staticmethod
    def save_agenda(agenda):
        os.makedirs(AGENDAS_DIR, exist_ok=True)
        filename = ContactManager.get_agenda_filename(agenda.user_email)
        with open(filename, 'w') as file:
            json.dump(agenda.to_dict(), file, indent=4)