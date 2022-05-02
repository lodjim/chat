from django.shortcuts import render


def index(request):
    return render(request, 'salon/index.html')


def room(request, room_name):
    return render(request, 'salon/room.html', {
        'room_name': room_name
    })
