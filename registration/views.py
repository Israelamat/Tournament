from django.shortcuts import render, redirect
from registration.forms import SignUpForm

def signup(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/reg/accountcreated")
    else:
        form = SignUpForm()
    return render(response, "registration/signup.html", {"form":form})

def account_created(response):
    return render(response, 'registration/account_created.html', {})
