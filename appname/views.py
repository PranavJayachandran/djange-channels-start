from django.shortcuts import render


def index(request):
    return render(request, "char/index.html")

def room(request,room_name):
    return render(request,"char/room.html",{'room_name':room_name})