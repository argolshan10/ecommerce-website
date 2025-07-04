from django import forms
from .models import PostingAddress

class PostingForm(forms.ModelForm):
    posting_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name:'}),required=True)
    posting_email = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                               required=True)
    posting_address1 = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address1'}),
                               required=True)
    posting_address2 = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}),
                               required=True)
    posting_city = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
                               required=True)
    posting_state = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
                               required=True)
    posting_zipcode = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
                               required=True)
    posting_country = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
                               required=True)

    class Meta:
        model = PostingAddress
        fields = ['posting_full_name' , 'posting_email' , 'posting_address1' , 'posting_address2' , 'posting_city' , 'posting_state' , 'posting_zipcode' , 'posting_country' ]
        exclude = ['user' , ]



