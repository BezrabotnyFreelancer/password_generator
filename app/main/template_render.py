from django.shortcuts import render


def index_html(request, context=None):
    if context == None:
        return render(request, 'main/index.html')
    else:
        return render(request, 'main/index.html', context)