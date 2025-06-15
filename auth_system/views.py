from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('novations')
        else:
            messages.error(request, "Неправильне ім'я користувача або пароль")

    return render(request, 'auth_system/login.html')