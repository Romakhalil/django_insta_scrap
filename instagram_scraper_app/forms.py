from django import forms

class InstagramScrapeForm(forms.Form):
    username = forms.CharField(max_length=50, label='Instagram Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Instagram Password')
    hashtag = forms.CharField(max_length=100, label='Hashtag')
