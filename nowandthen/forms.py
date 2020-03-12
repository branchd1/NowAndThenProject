from django import forms
from nowandthen.models import Page, Category, Pictures
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import User
from nowandthen.models import UserProfile


ERA_CHOICES= [
    ('Present_day', 'Present Day'),
    ('2010-2020', '2010-2020'),
    ('2000-2010', '2000-2010'),
    ('1990s', '1990s'),
    ('1980s', '1980s')
    ]

class PicturesForm(forms.ModelForm):
    title = forms.CharField(help_text="What is your picture's title?")
    description = forms.CharField(help_text="Please tell us about a bit about your picture.")
    tag_one = forms.CharField(help_text="Please provide a word to describe your image. This will help people to find it")
    tag_two = forms.CharField(help_text="Please give us an additional word to describe the picture.")
    era = forms.CharField(help_text="What era does this picture relate to?",widget=forms.Select(choices=ERA_CHOICES))
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Pictures
        fields = ('image', 'title', 'description', 'tag_one', 'tag_two','era',)
 

class CategoryForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

# An inline class to provide additional information on the form.
    class Meta:
# Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Page
    # What fields do we want to include in our form?
    # This way we don't need every field in the model present.
    # Some fields may allow NULL values; we may not want to include them.
    # Here, we are hiding the foreign key.
    # we can either exclude the category field from the form,
        exclude = ('category',)
    # or specify the fields to include (don't include the category field).
    #fields = ('title', 'url', 'views')
        def clean(self):
            cleaned_data = self.cleaned_data
            url = cleaned_data.get('url')
            # If url is not empty and doesn't start with 'http://',
            # then prepend 'http://'.
            if url and not url.startswith('http://'):
                url = f'http://{url}'
                cleaned_data['url'] = url
            return cleaned_data
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
