from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, SignupForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/pages/login.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            authenticated_user = authenticate(
                username=form.cleaned_data.get('username', ''),
                password=form.cleaned_data.get('password', ''),
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("home:index")

            messages.error(request, 'Credenciais Inválidas')
            return redirect("users:login")

        messages.error(request, 'Credenciais Inválidas')
        return redirect("users:login")


@login_required(login_url='users:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect('users:login')

    if request.POST.get('username') != request.user.username:
        return redirect('users:login')

    logout(request)
    return redirect('home:index')


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'users/pages/signup.html', {
            'form': form
        })

    def post(self, request):
        POST = request.POST
        request.session['register_form_data'] = POST
        form = SignupForm(POST or None)

        if form.is_valid():
            data = form.save(commit=False)
            data.set_password(data.password)
            data.save()

            del(request.session['register_form_data'])
            messages.success(request, 'User Created Successfuly')  # noqa
            return redirect('users:login')

        messages.error(request, 'Fix the erros')
        return render(request, 'users/pages/signup.html', {
            "form": form
        })


class ProfileView(View):
    def get(self, request):
        return render(request, 'users/pages/profile.html')
