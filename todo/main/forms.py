from django.forms import ModelForm
from main.models import Todo 

class Todo_form(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

