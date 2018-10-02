from django import forms

from datetimewidget.widgets import DateTimeWidget



from .models import Wallet, Order, AdditionalFiles

from writers.models import Rating


class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))


class PlaceAnOrderForm(forms.ModelForm):

       
    def __init__(self, *args, **kwargs):
         super(PlaceAnOrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        exclude =  ('order_id', 'order_uuid',  'publication_date')
        widgets = {
            'order_type': forms.Select(attrs={
                'class' : 'form-control show-tick',
                'required': 'please select choice'
         
            
            }),
                'pages': forms.Select(attrs={
                    'class': 'form-control show-tick',
                    'placeholder': '1 page / 275 words',
                
                }),
                'service': forms.Select(attrs={
                'class' : 'form-control show-tick',
               
                    
                }),
                'sources': forms.Select(attrs={
                'class' : 'form-control show-tick',
               
                    
                }),
 
               
                'subject':  forms.Select(attrs={
                'class' : 'form-control show-tick',

               

                 }),

                 'deadline':  DateTimeWidget(attrs={'class':'datepicker form-control',
                 'placeholder': 'Specify deadline'}, usel10n = True, bootstrap_version=3),
                    

                'style':  forms.Select(attrs={
                'class' : 'form-control show-tick',
               

                 }),
                'level':  forms.Select(attrs={
                'class' : 'form-control show-tick',
               

                 }),

                 'topic': forms.TextInput(attrs={
                     'class': 'form-control',
                     'placeholder': 'Topic'

                 }),
                 
                 'description': forms.Textarea(attrs={
                     'class':  'form-control no-resize',
                     'placeholder': 'Description should be more than 20 words'

                     

                 })
            
        }




class CancelOrderForm(forms.Form):
    REASON = (
        ('Select reason', 'Select reason'),
        ('Expensive Price', 'Expensive Price'),
        ('Duplicate Order','Duplicate Order',),
        ('Do not Need', 'Do not Need')
    )

    reason = forms.ChoiceField(choices=REASON, widget=forms.Select(attrs={
        'class': 'custom-select',
        'value': 'select reason'
    }))
    
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Please help us improve, kindly comment your reason'
    }))


class  AdditionalFileForm(forms.ModelForm):
    class Meta:
        model = AdditionalFiles
        exclude = ['user']
        widgets = {
            '' : forms.FileInput(attrs={
                'class': 'custom-file-input',

            })
            
            
           
        }
 
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('rating_id',)


    






