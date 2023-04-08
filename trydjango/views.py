''' to render the web pages it is just like a controllers'''
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
@login_required
def home(request,*args,**kwargs):
    '''take in a request and return the pages'''
    
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        article_querylist=Article.objects.all()
        context={
            "user":user,
             "list":article_querylist
             }
        return render(request, 'home-view.html',context=context)
    else:
        return redirect('/login/')
        