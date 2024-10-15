from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        u_name = request.POST['username']
        e_mail = request.POST['email']
        p_word = request.POST['password']
        c_word = request.POST['confirm_password']

        if p_word == c_word:
            if User.objects.filter(username=u_name).exists():
                messages.info(request, "Username already taken")
                return render(request, "signup.html")
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request, "Email already taken")
                return render(request, "signup.html")
            else:
                user = User.objects.create_user(username=u_name, email=e_mail, password=p_word)
                user.save()
                return redirect("signup_success")  # Assuming you have a URL pattern named 'signup_success'
        else:
            messages.info(request, "Passwords aren't matching")
            return render(request, "signup.html")
    else:
        return render(request, "signup.html")
