from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import RegisterUserForm, PasswordChangingForm
from django.contrib.auth import authenticate,login, logout , update_session_auth_hash
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.decorators.http import require_safe, require_http_methods

# Create your views here.

@require_http_methods(["POST", "GET"])
def logar_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(request,username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'Usuário logado com sucesso.')
            return redirect('/')
        else:
            messages.error(request, "Username ou senha incorretos! Tente novamente!")
            return redirect('/auth/login/')
    else:
        form_login = AuthenticationForm()
    return render(request, "login.html", {'form_login': form_login})


@require_http_methods(["POST", "GET"])
def cadastrar_user(request):
    if request.method == "POST":
       form_usuario = RegisterUserForm(request.POST)
       if form_usuario.is_valid():
           form_usuario.save()
           username = form_usuario.cleaned_data['username']
           password = form_usuario.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           messages.success(request,("Cadastrado com sucesso!"))
           return redirect('/')
    else:
       form_usuario = RegisterUserForm()
    return render(request,'cadastro.html', {'form_usuario': form_usuario})


@require_http_methods(["POST", "GET"])
@login_required(login_url='logar_user')
def deslogar_usuario(request):
    logout(request)
    messages.success(request, 'Usuário deslogado com sucesso.')
    return redirect('/')

@require_http_methods(["POST", "GET"])
@login_required(login_url='logar_user')
def mudar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangingForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('/auth/mudar_senha_sucesso/')
    else:
        form_senha = PasswordChangingForm(request.user)
    return render(request, 'mudar_senha.html', {'form_senha': form_senha})

@require_http_methods(["POST", "GET"])
@login_required(login_url='logar_user')
def mudar_senha_sucesso(request):
    return render(request, 'mudar_senha_sucesso.html')



@require_http_methods(["POST", "GET"])
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "senha/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8001',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/auth/reset_password_sent/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="senha/password_reset.html", context={"password_reset_form":password_reset_form})
