from django import forms

from soal.models import Soal
from .extra.my_validation import file_allowed_types
from .extra.my_validation import file_allowed_size
#from .extra.my_validation import password_allowed_size

class FormSoal(forms.ModelForm):

    #password = forms.CharField(max_length=8, widget=forms.PasswordInput)
    
    validation = [file_allowed_types, file_allowed_size]

    def __init__(self, *args, **kwargs):
        super(FormSoal, self).__init__(*args, **kwargs)
        self.fields['file_soal'].validators.extend(self.validation)
        #self.fields['password'].validators.append(password_allowed_size)
    
    class Meta:
        model = Soal
        exclude = ('tanggal','guru', 'status')


class FormPencarianSoal(forms.Form):

    nama_soal = forms.CharField(max_length=30, 
        widget=forms.TextInput(
            attrs={
                    'class':'uk-search-field', 
                    'type':'search',
                }
            )
        )