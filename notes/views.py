
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Note
import os
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

#Fix 2:
key = os.environ.get("NOTES_ENCRYPTION_KEY")
cipher = Fernet(key.encode()) if key else None

@login_required
def home(request):
    search = request.GET.get("search")
    #Vulnerable 1: 
    #notes = Note.objects.all()
    #Fix 1:
    notes = Note.objects.filter(user=request.user)
    #Vulnerable 3:
    #if search:
    #notes = Note.objects.raw(
        #f"SELECT * FROM notes_note WHERE user_id = {request.user.id} AND title LIKE '%{search}%'"
    #)
    #Fix 3:
    if search:
        notes=notes.filter(title__icontains=search)

    #Fix 2:
    for note in notes:
        try:
            note.content = cipher.decrypt(note.content.encode()).decode()
        except InvalidToken:
            pass

    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")

        #Fix 2:
        encrypted_content = cipher.encrypt(content.encode()).decode()
        Note.objects.create(user=request.user, title=title, content=encrypted_content)
        return redirect("home")

    return render(request, "notes/home.html", {"notes": notes})
    