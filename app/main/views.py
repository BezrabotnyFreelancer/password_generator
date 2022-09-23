from django.shortcuts import render
# Create your views here.
from .generator import generate_password

def return_password(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        final_password = generate_password(int(length))
        context = {'password': final_password, 'length': length}
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html')
