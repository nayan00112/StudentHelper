from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def registration(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        password1 = request.POST['create_password']
        password2 = request.POST['conform_password']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "username is used.")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is Used.")
            else:
                user = User.objects.create_user(
                    username=uname, first_name=fname, last_name=lname, email=email, password=password1)
                user.save()
                user = auth.authenticate(username=uname, password=password1)
                auth.login(request, user)
                return redirect("/")
        else:
            messages.info(request, "Password is not matching...")

    return render(request, "account/registration.html")


def login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password1 = request.POST['password']
        user = auth.authenticate(username=uname, password=password1)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")

    return render(request, "account/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def myprofile(request):
    if User.is_authenticated:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            email = request.POST["email"]
            cpass = request.POST["old_password"]
            pass1 = request.POST["create_password"]
            pass2 = request.POST["conform_password"]
            if (pass1 == pass2):
                user = auth.authenticate(username=request.user, password=cpass)
                if user is not None:
                    if User.objects.filter(username=username).exists() and str(User.objects.filter(username=username).first().id) != str(request.user.id):
                        messages.info(request, "username is used.")
                    elif User.objects.filter(email=email).exists() and str(User.objects.filter(email = email).first().id) != str(request.user.id):
                        messages.info(request, "Email is Used.")
                    else:
                        user.username = username
                        user.first_name = first_name
                        user.last_name = last_name
                        user.email = email
                        user.set_password(pass1)
                        user.save()
                        auth.logout(request)
                        messages.success(request, "Updated Successfully and logout.")
                        return redirect("/")
            else:
                messages.info(request, "Password is not matching...")
        return render(request, "account/myprofile.html")
    else:
        messages.info("Signin required!")
        return redirect(request, "/")