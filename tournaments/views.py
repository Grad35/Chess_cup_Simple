from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm
from .models import Tournament,Application
def home(request):
    return render(request,"tournaments/home.html",{"tournaments":Tournament.objects.all()})
def signup(request):
    if request.user.is_authenticated: return redirect("dashboard")
    form=SignUpForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        user=form.save(); login(request,user)
        messages.success(request,"Аккаунт создан. Добро пожаловать!")
        return redirect("dashboard")
    return render(request,"tournaments/form_page.html",{"form":form,"title":"Создать аккаунт","button":"Зарегистрироваться"})
@login_required
def apply_tournament(request,tournament_id):
    tournament=get_object_or_404(Tournament,id=tournament_id)
    if not tournament.is_open: messages.error(request,"Регистрация на этот турнир закрыта.")
    else:
        _,created=Application.objects.get_or_create(user=request.user,tournament=tournament)
        messages.success(request,"Заявка отправлена!" if created else "Вы уже подали заявку.")
    return redirect("dashboard")
@login_required
def dashboard(request):
    apps=Application.objects.filter(user=request.user).select_related("tournament")
    return render(request,"tournaments/dashboard.html",{"applications":apps})
