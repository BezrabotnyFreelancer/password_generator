from django.shortcuts import render
from django.shortcuts import redirect
from .error import EmptyString
# Create your views here.
from .generator import generate_password
from storage.secure import encode_password, key
from storage.models import PasswordStorage

def return_password(request):
    final_password = ''
    if request.method == 'POST':
        length = request.POST.get('length')
        
        try:
            final_password += generate_password(int(length))
            context = {'password': final_password, 'length': length}
            
            if 'site' in request.POST:
                try:
                    url = request.POST.get('site')
                    if url == '':
                        raise EmptyString
                
                except EmptyString:
                    return render(request, 'main/index.html', context)
                
                encoded_password = encode_password(final_password)
                generated_object = PasswordStorage
                generated_object.create_passwd_from_generator(
                    user=request.user,
                    site=url,
                    password=encoded_password,
                    key=key                        
                )
                
                return redirect('storage_list')
            
            return render(request, 'main/index.html', context)
        
        except:
            return render(request, 'main/index.html')
    
    else:
        return render(request, 'main/index.html')
    
