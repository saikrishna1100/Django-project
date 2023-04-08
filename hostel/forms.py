from django import forms

class HostelForm(forms.Form):
     room_id=forms.IntegerField()
     count=forms.IntegerField()
     
     def clean(self):
          data=self.cleaned_data
          room_id=data.get("room_id")
          if(room_id<0):
               self.add_error("room_id","the room should not negative")
          
       
     
     

     
     
     