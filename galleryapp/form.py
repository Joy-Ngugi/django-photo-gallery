from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tag, Photo

class RegistrationForm(UserCreationForm):
   email = forms.EmailField()
   class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']

   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['username'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })

class FilterForm(forms.Form):
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), required=False)
    
   
class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image', 'tags', 'description', 'details']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['title'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-2 border-blue-300 shadow-sm focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'mt-1 block  rounded-md  border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-blue-500'
        })
        self.fields['tags'].widget.attrs.update({
            'class': 'mt-1  space-y-2 block w-full text-gray-700 ',
            'label_class': 'text-3xl font-semibold text-gray-800'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md  border-2 border-blue-300 shadow-sm focus:ring-blue-500 focus:border-blue-500'
        })
        self.fields['details'].widget.attrs.update({
            'class': 'mt-1 block w-full rounded-md border-2 border-blue-300 shadow-sm focus:ring-indigo-500 focus:border-blue-500'
        })