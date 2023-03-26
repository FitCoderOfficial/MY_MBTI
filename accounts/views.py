from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser
import uuid

def home(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/home.html', {'users': users})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mbti_check')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def mbti_check(request):
    if request.method == 'POST':
        mbti = request.POST.get('mbti')
        request.user.mbti = mbti
        request.user.shared_link = f"https://mywebsite.com/mbti/{str(uuid.uuid4())}/"
        request.user.save()
        return redirect('mbti_share', request.user.id)
    return render(request, 'accounts/mbti_check.html')

def mbti_share(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'accounts/mbti_share.html', {'user': user})
