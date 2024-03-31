from django import forms
from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['id', 'fullname', 'tel', 'zoone', 'shaqada', 'due_date', 'completion', 'memo']
        widgets = {
            'due_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm,self).__init__(*args, **kwargs)
        self.fields['shaqada'].empty_label="Select"
        self.fields['tel'].required=False