from django.forms import ModelForm
from .models import Project, Review, Tag

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image' , 'description', 'demo_link', 'source_link']
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'input'}

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        
        labels = {
        'value': "Place your vote",
        'body': "Leave a comment",
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'input'}