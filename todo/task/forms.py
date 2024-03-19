from django import forms
from .models import Task



class TodoForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'details', 'due_date', 'priority','created_at']
class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'details', 'due_date', 'priority']
