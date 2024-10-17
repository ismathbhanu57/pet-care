from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude=['status']

class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        exclude = ["status"]




class Add_notificationsForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ["sell_for"]
# forms.py

class AppoitmentsForm(forms.ModelForm):
    class Meta:
        model = Appoitments
        exclude=['status']


class PrecautionsForm(forms.ModelForm):
    class Meta:
        model = Precautions
        fields = "__all__"

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"

class PrescriptionsForm(forms.ModelForm):
    class Meta:
        model = Prescriptions
        fields = "__all__"

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"

class Friends_RequestsForms(forms.ModelForm):
    class Meta:
        model = Friends_Requests
        exclude = ["status"]


class Add_PostsForms(forms.ModelForm):
    class Meta:
        model = Add_Posts
        exclude = ["status"]


class Add_CommentsForm(forms.ModelForm):
    class Meta:
        model = Add_Comments
        fields = "__all__"

