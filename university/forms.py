from django import forms
from .models import College
class CollegeForm(forms.ModelForm):
    
    class Meta:
        model=College
        fields=["name","clgid","address"]
        
    def clean(self):
        cleaned_data=self.cleaned_data
        name=cleaned_data.get("name")
        if College.objects.filter(name=name).exists():
            self.add_error("name","the name is already taken")
        print("all data",cleaned_data)
        return cleaned_data    
        
        
        
        