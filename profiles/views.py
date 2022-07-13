from django.shortcuts import render



def view_profile(request):
	template = "profiles/profiles.html"
	return render(request, template)