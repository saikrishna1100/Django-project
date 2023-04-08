from django import forms 
from .models import Article



class ArticleForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = "required-field"

    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',"placeholder":"enter title"}),
            'content': forms.Textarea(attrs={'class': 'form-control',"placeholder":"enter content"}),
        }
    def clean(self):
        data=self.cleaned_data
        title=data.get("title")
        aa=Article.objects.all().filter(title__icontains=title)
        if aa.exists():
            self.add_error("title", f"{title} is already taken")
        return data    
                
            
    

class ArticleFormold(forms.Form):
    title=forms.CharField()
    content=forms.CharField()
    
    
    # def clean_title(self):
    #     cleaned_data=self.cleaned_data
    #     print("cleaned title",cleaned_data)
    #     title=cleaned_data.get("title")
    #     if Article.objects.filter(title=title).exists():
    #         self.add_error("title","the title is already taken")
    #         #raise forms.ValidationError("this title is taken")
    #     print("title",title)
    #     return title
    
        
    
    