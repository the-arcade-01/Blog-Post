from django.shortcuts import render

# Create your views here.
def article_list(resquest):
    return render(resquest,'articles/article_list.html')
