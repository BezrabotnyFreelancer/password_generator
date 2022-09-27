from django.shortcuts import redirect
from .generator import generate_password
from storage.secure import encode_password, key
from storage.models import PasswordStorage
from .models import TempGenPassword
from .template_render import index_html
# Create your views here.


def return_password(request):
    if request.method == 'POST' and (request.POST.get('site') == None or request.POST.get('site') == ''):
               
        length = request.POST.get('length')
        
        try:
            final_password = generate_password(int(length))
            context = {'password': final_password, 'length': length}          
        except:
            return index_html(request)
        
        if request.user.is_authenticated:
            instance = TempGenPassword
            instance.delete_record(request.user)
            instance.add_record(request.user, final_password)
        return index_html(request, context)
    
    elif request.method == 'POST' and request.POST.get('site') != '':
        url = request.POST.get('site')
        not_encrypted_password = TempGenPassword.objects.get(user=request.user)
        encrypted_password = encode_password(not_encrypted_password.password)
        instance = PasswordStorage
        instance.create_passwd_from_generator(
            user=request.user,
            site=url,
            password=encrypted_password,
            key=key
        )
        return redirect('storage_list')
    
    else:
        return index_html(request)
    
