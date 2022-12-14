from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreationPasswordInStorageForm
from .models import PasswordStorage
from .secure import encode_password, decode_password, key
# Create your views here.

  
class PasswordList(LoginRequiredMixin, ListView):
    model = PasswordStorage
    login_url = reverse_lazy('account_login')
    template_name = 'storage/storage_list.html'
    context_object_name = 'password_storage_list'
                
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
        

@login_required(login_url=reverse_lazy('account_login'))
def password_detail(request, pk):
    storage = PasswordStorage.objects.get(pk=pk)

    if request.user == storage.user:
        decoded_passwd = decode_password(storage.password[1:], storage.key)
        context = {
                'storage': storage,
                'decoded_password': decoded_passwd,
                }
        return render(request, 'storage/storage_detail.html', context=context)
    
    else:
        return HttpResponse("<h1>You don't have an access on this page!</h1>")

 
class PasswordDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PasswordStorage
    login_url = reverse_lazy('account_login')
    template_name = 'storage/storage_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('storage_list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    

class PasswordUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PasswordStorage
    login_url = reverse_lazy('account_login')
    template_name = 'storage/storage_update.html'
    fields = ['site', 'password']
    
    def get_initial(self):
        initial = super(PasswordUpdate, self).get_initial()
        initial['password'] = 'New password'
        return initial
    
    def form_valid(self, form):
        edited_password = form.save(commit=False)
        encoded_passwd = encode_password(edited_password.password)
        edited_password.password = encoded_passwd
        edited_password.key = key
        edited_password.save()
        return super().form_valid(form) 
        
    def get_success_url(self):
        record = self.get_object()       
        return record.get_absolute_url()

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class CreatePassword(LoginRequiredMixin, CreateView):
    model = PasswordStorage
    form_class = CreationPasswordInStorageForm
    login_url = reverse_lazy('account_login')
    template_name = 'storage/storage_create.html'
    
    def form_valid(self, form):
        new_password = form.save(commit=False)
        new_password.user = self.request.user
        new_password.password = encode_password(new_password.password)
        new_password.key = key
        new_password.save()
        return super().form_valid(form)