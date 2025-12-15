from django.shortcuts import render

# Create your views here.
def index(request):
	index_context = {}
	return render(request, "index.html", index_context)

def about(request):
	about_context = {}
	return render(request, "about.html", about_context)

def contact(request):
	contact_context = {}
	return render(request, "contact.html", contact_context)