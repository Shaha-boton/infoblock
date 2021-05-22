from blockapp.models import Article
from django.shortcuts import render

# Create your views here.

def home(request):
    posts = Article.objects.all()
    return render(request, 'blockapp/home.html',{'posts':posts})