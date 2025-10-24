from django.shortcuts import render


def curriculo_brenno(request):
    return render(request, 'curriculo/curriculo.html')


def curriculo_spiff(request):
    return render(request, 'curriculo/index.html')