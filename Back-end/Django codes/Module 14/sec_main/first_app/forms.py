from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['roll']
        labels = {
            'name': 'Student Name',
            'roll': 'Roll Number',
        }
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'btn-primary btn'}),
            'roll' : forms.TextInput()
        }
        help_texts = {
            'name' : 'Input your name',
        }
        error_messages = {
            'name' : {
                'required' : 'Name is required',
                'max_length' : 'Name should not exceed 50 characters',
            },
        }