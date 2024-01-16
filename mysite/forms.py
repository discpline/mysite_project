from django import forms
from .models import SendMessage,Comment


class SendMessageForm(forms.ModelForm):

    first_name = forms.CharField(label='first_name',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Your First Name',
                                       'data-rule': 'minlen:4',
                                       'data-msg': 'Please enter at least 4 chars'}))

    last_name = forms.CharField(label='last_name',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Your Last Name',
                               'data-rule': 'minlen:4',
                               'data-msg': 'Please enter at least 4 chars'}))
    subject = forms.CharField(label='subject', widget=forms.Textarea(attrs={'placeholder': 'Subject',
                                                                            'class': 'form-control',
                                                                            'rows': '5'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                           'class': 'form-control',
                                                                           'id': 'email',
                                                                           'data-rule': 'email',
                                                                           'data-msg': 'Please enter a valid email'}))
    message = forms.CharField(label='message', widget=forms.Textarea(attrs={'placeholder': 'Message',
                                                                            'class': 'form-control',
                                                                            'rows': '5'}))

    class Meta:
        model = SendMessage
        fields = ('first_name', 'last_name', 'subject', 'email', 'message')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


