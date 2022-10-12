from django import forms
from .models import PostModel

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = PostModel
        fields = ('title','content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')
