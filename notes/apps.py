from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = "notes"

    def ready(self):
        #Fix 5: 
        import notes.signals    
