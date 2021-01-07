from django.shortcuts import render

# Create your views here.

def individu_list(request):
    return render(request, 'home/individu_list.html', {})
