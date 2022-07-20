from django.shortcuts import render, redirect
from django.contrib import messages

def requirements(request):
    if request.method == "POST":
        request.session['conditions_accepted'] = True
        return redirect('home')
    return render(request, 'security/requirements.html')


def access_denied(request):
    return render(request, 'security/access_denied.html')
