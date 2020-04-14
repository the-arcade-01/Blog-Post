from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(resquest):
    articles = Article.objects.all().order_by('date')
    return render(resquest,'articles/article_list.html',{'articles':articles})
