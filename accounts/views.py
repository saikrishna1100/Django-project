from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def register_view(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return redirect("/login")
    context={"form":form}
    return render(request,"accounts/register.html",context=context)
        
    
def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            request.session['user_id'] = user.id
            
            
            return redirect("/")
    else:
        form=AuthenticationForm(request)
    context={"form":form}    

        # username=request.POST.get("username")
        # password =request.POST.get("password")
        # user=authenticate(request,username=username,password=password)
        # if user is None:
        #     context={"error":"Invalid user data"}
        #     return render(request,"accounts/login.html",context=context)
        # login(request,user)
        # return redirect("/admin")
    return render(request,"accounts/login.html",context=context)    


def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect("/login/")
    return render(request,"accounts/logout.html",{})


