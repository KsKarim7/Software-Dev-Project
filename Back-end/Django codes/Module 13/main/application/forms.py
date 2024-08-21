from django import forms
from django.core import validators


# widgets = field to html input

class contactForm(forms.Form):
    name = forms.CharField(label="Your name: ",initial='Omuk',help_text="Max length 50 characters",required=False,disabled=False,widget=forms.Textarea(attrs = {'id':'text_area','class':'class1 class 2','placeholder':'Enter your name'}))
    file = forms.FileField()
    email = forms.EmailField(label = "User email")
    
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # alternative:
    age = forms.CharField(widget=forms.NumberInput)

    check = forms.BooleanField()
    bornday = forms.CharField(widget=forms.DateInput(attrs= {'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs= {'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices = CHOICES,widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices = MEAL,widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if(len(valName) < 10):
#     #         raise forms.ValidationError("Name should be at least 10 characters long.")
#     #     return valName
#     # def clean_email(self):
#     #     valEmail = self.cleaned_data['email']
#     #     if not "@" in valEmail:
#     #         raise forms.ValidationError("Invalid email format.")
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError("Email should have '.com' domain.")
#     #     return valEmail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
        
#         if(len(name) < 10):
#             raise forms.ValidationError("Name should be at least 10 characters long.")
#         if not "@" in email:
#             raise forms.ValidationError("Invalid email format.")
#         if '.com' not in email:
#             raise forms.ValidationError("Email should have '.com' domain.")
        
#         return cleaned_data


def len_check(value):
    if(len(value) < 10):
        raise forms.ValidationError("Enter a value consists at least 10 character")

class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,message='Name should be at least 10 characters long')])
    text = forms.CharField(widget=forms.TextInput,validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Please enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message="Age must be Maximum 34"),validators.MinValueValidator(18,message="Age must be atleast 18")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message ='Your file must be in pdf format ')])
    # Regex,url,parseBlock are more features



class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)



    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        name = self.cleaned_data['name']

        if(password != confirm_password):
            raise forms.ValidationError("Passwords do not match.")
        if(len(name)<15):
            raise forms.ValidationError("Name should be at least 15 characters long.")
        