from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user, login, logout
from .models import Note
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'notesapp/login.html')

def registerpage(request):
    return render(request, 'notesapp/register.html')


def loginUser(request):

    if not request.method == "POST":
        return HttpResponse(status=405)

    data = request.POST
    user = authenticate(request, username=data['username'], password=data['password'])
    if user is not None:
        login(request, user)
        return redirect('../logged')
    else:
        print('Invalid login')
        return HttpResponse(status=404)


def registerUser(request):

    if not request.method == "POST":
        return HttpResponse(status=405)

    try:
        data = request.POST
        user = User.objects.create_user(data['username'], None, data['password'])
        user.first_name = data['firstname']
        user.last_name = data['lastname']
        user.save()
        return HttpResponse(status=200)
    except:
        print('user exist')
        return HttpResponse(status=406)

@login_required
def loggeduser(request):
    username = get_user(request).get_username()
    symbol = username[0]
    notes = Note.objects.filter(user=get_user(request))
    print(notes)
    return render(request, 'notesapp/home.html', {'user': username, 'symbol': symbol, 'notes': notes})

@login_required
def logutuser(request):
    logout(request)
    return redirect('../')

@login_required
def addnote(request):
    data = request.POST
    Note.objects.create(name=data['name'], content=data['content'], user=get_user(request))
    return redirect('notesapp:logged')

@login_required
def deletenote(request, id):
    note = Note.objects.filter(user=get_user(request)).get(id=id)
    note.delete()
    return redirect('notesapp:logged')