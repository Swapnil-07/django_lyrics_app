from django.forms import ModelForm
from home import models

class AlbumForm(ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'
    
class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'