from django import forms
from .models import *


class AddMaalForm(forms.ModelForm):
    class Meta:
        model = MaalModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddMaalForm, self).__init__(*args, **kwargs)
        self.fields['fir'].label = "FIR का नंबर "
        self.fields['fir'].widget = forms.TextInput(attrs={'placeholder': 'FIR का नंबर'})
        self.fields['thana'].label = "थाना "
        self.fields['maal_type'].label = "माल का टाइप "
        self.fields['if_other'].label = "If अन्य Please specify"
        self.fields['if_other'].widget = forms.TextInput(attrs={'id': 'id_other'})
        self.fields['photo'].label = "फोटो "
        self.fields['seizure_date'].label = "माल जब्त होने की  दिनांक "
        self.fields['seizure_date'].widget = forms.TextInput(attrs={'id': 'seizuredate'})
        self.fields['vivechak'].label = "विवेचक "
        self.fields['under_section'].label = "अंडर सेक्शन "
        self.fields['description'].label = "माल का विवरण "
        self.fields['place'].label = "माल रखने का स्थान "
        self.fields['status'].label = "माल का स्टेटस "
        self.fields['court'].label = "कोर्ट "
        self.fields['date_of_disposal'].label = "date of disposal"
        self.fields['date_of_disposal'].widget = forms.TextInput(attrs={'id': 'disposaldate'})
