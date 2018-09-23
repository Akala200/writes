from django import forms

from .models import Wallet, Order, AdditionalFiles


class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '$'
    }))


class PlaceAnOrderForm(forms.ModelForm):

       
    def __init__(self, *args, **kwargs):
         super(PlaceAnOrderForm, self).__init__(*args, **kwargs)
         self.fields['order_type'].widget
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
                'deadline' : forms.DateTimeInput(attrs={
                'class' : 'datetimepicker form-control',
                'placeholder': 'Please Choose deadline'
               
                    
                }),
                'subject':  forms.Select(attrs={
                'class' : 'form-control show-tick',

               

                 }),

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
        fields = ['files']
        widgets = {
            'files' : forms.FileInput(attrs={
                'class': 'custom-file-input',

            })
            
            
           
        }
 
    






