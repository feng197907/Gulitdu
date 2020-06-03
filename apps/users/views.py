from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm
from .models import UserProfile
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.changed_data['email']
            password = user_register_form.changed_data['password']

            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request, 'users/register.html', {'msg': '用户已存在'})
            else:
                user = UserProfile
                user.username = email
                user.set_password(password)
                user.email = email
                user.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'users/register.html', {'user_register_form': user_register_form})
