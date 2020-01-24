from django.shortcuts import render


def index(request):
    output = {}
    return render(request, 'hockey/index.html', output)