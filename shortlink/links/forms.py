from django import forms


class CutLink(forms.Form):
    fullLink = forms.URLField(max_length=255, label="Полная ссылка")

