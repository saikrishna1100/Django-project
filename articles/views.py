from django.shortcuts import render
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.
@login_required
def article_search_view(request):
   
    query_dict=request.GET
    try:
        query=int(query_dict.get("query"))
    except:
        query=None
    article_obj=None  
    if(query is not None):
          article_obj=Article.objects.get(id=query)
    context={"object":article_obj}
    return render(request,"articles/search.html",context=context)
  
@login_required 
def article_create_view(request):
    form=ArticleForm(request.POST or None)
    context={
        "form":form
        
    }
    if form.is_valid():
        # title=form.cleaned_data.get("title")
        # content=form.cleaned_data.get("content")
        # article_object=Article.objects.create(title=title,content=content)
        article_object=form.save()
        context["form"]=ArticleForm()
        context["object"]=article_object
        context["created"]=True
    return render(request,"articles/create.html",context=context)

@login_required
def article_detail_view(request,id=None):
    article_obj=None
    if id is not None:
        article_obj=Article.objects.get(id=id)
    context={
        "object":article_obj,
    }
    
    return render(request,"articles/detail.html",context=context)
