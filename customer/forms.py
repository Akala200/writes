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
        exclude =  ('order_id', 'order_uuid', 'deadline', 'publication_date')
        widgets = {
            'order_type': forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'option': 'type',
            
            }),
                'pages': forms.Select(attrs={
                    'class': 'form-control-sm form-control',
                    'placeholder': '1 page / 275 words',
                
                }),
                'service': forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 
                    
                }),
                'sources': forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 
                    
                }),
                'deadline' : forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 
                    
                }),
                'subject':  forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 

                 }),

                'style':  forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 

                 }),
                'level':  forms.Select(attrs={
                'class' : 'form-control-sm form-control',
                'height': '45px',
                'border-radius': '7px',
                'value': 'type' 

                 }),

                 'topic': forms.TextInput(attrs={
                     'width': '335px',
                     'height': '55px',
                     'border-radius': '10px',
                     'class': 'form-control',
                     'placeholder': 'Topic'

                 }),
                 
                 'description': forms.Textarea(attrs={
                     'width': '335px',
                     'border-radius': '10px',
                     'class': 'form-control',
                     'placeholder': 'Description',
                     'margin-top': '0px',
                     'margin-bottom': '0px',
                     'height': '400px',
                     'border-radius': '10px'

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
 
    






