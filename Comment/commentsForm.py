from django import forms


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    username = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'class':'form-control', 'aria-label':'Comment', 'ria-describedby':'basic-addon2'}))
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'aria-label':'Comment', 'ria-describedby':'basic-addon2'}))
