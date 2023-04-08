from django.shortcuts import render
from .forms import HostelForm
from .models import  Hostel
# Create your views here.
def show_hostel(request):
    form=HostelForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        room_id=form.cleaned_data["room_id"]
        count=form.cleaned_data["count"]
        hstlinstance=Hostel.objects.create(room_id=room_id,count=count)
        context["form"]=HostelForm()
        context["object"]=hstlinstance
    return render(request,"hstl/hstl_list.html",context=context)

def show_rooms(request):
       data=Hostel.objects.all() 
       context={
           "data" :data
       }
       return render(request,"hstl/show_rooms.html",context=context)
   
def show_ind(request,room_id=None):
    article_obj=None
    if room_id is not None:
        article_obj=Hostel.objects.get(room_id=room_id)
    context={
        "object":article_obj,
    }
    
    return render(request,"hstl/detail.html",context=context)
       
       
        