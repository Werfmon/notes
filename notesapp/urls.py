from os import name
from django.urls import path

from .views import (
    loggeduser,
    loginUser,
    logutuser,
    registerUser,
    index,
    registerpage,
    addnote,
    deletenote
)

app_name = 'notesapp'

urlpatterns = [
    path("loginuser/", loginUser, name="login"),
    path("registeruser/", registerUser, name="register"),
    path("", index, name="loginview"),
    path("register/", registerpage),
    path("logged/", loggeduser, name='logged'),
    path("logoutuser/", logutuser),
    path("addnote/", addnote, name="addnote"),
    path("deletenote/<int:id>", deletenote, name="deletenote"),
]
