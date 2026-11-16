from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = "notes"

    def ready(self):
        #Vulnerable 5:
        #pass
        
        #Fix 5: 
        import notes.signals    
