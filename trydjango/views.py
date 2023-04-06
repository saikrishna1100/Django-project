''' to render the web pages it is just like a controllers'''
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

@login_required
def home(request,*args,**kwargs):
    '''take in a request and return the pages'''
    
    
    article_querylist=Article.objects.all()
    
    context={
             "list":article_querylist
             }
     
    HTML_STRING= render_to_string("home-view.html",context=context)
    return HttpResponse(HTML_STRING)