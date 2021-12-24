from django import forms
from tinymce.widgets import TinyMCE
from apps.blog.models import Comment, Post

# Create your forms here.
class PostForm(forms.ModelForm):
    content = forms.CharField(label="Contenido",
        widget=TinyMCE(attrs={"cols": 80, "rows": 15, "class": "form-control"})
    )

    class Meta:
        model = Post
        fields = ("title", "overview", "content", "featured", "category", "thumbnail",)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("content",)