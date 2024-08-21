from django import forms


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