import django.forms as forms
from .models import Texts, Classes

        
class TextForm(forms.ModelForm):
    class Meta:
        model = Texts
        fields = ['text', 'classes']
    text = forms.Textarea()
    classes = forms.ModelMultipleChoiceField(
        queryset = Classes.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )
    #fields = ('text', 'classes')