from django.shortcuts import render
from .models import College
from .forms import CollegeForm
# Create your views here.
def show_college_data(request):
    context={
        "data":College.objects.all()
    }
    return render(request,"college/show.html",context=context)
def add_college(request):
    form =CollegeForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        form_object=form.save()
        context["object"]=form_object
        context["created"]=True
    return render(request,"college/addcollege.html",context=context)    
        
        
        