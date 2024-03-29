from django.shortcuts import render
from .forms import CustomAuthenticationForm

def welcome(request):
	return render(request, 'welcome.html')
	

def index(request):
	return render(request, 'index.html')
	
def graphs(request):
	return render(request, 'graphs.html')
    
def regression(request):
	return render(request, 'regression.html')
	
def regression1(request):
	return render(request, 'regression1.html')
