from django.shortcuts import render


def index_view(request):
    return render(request, 'users/index.html', {})
