from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField(label='code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'code': 'Coupon Code',
        }
        self.fields['code'].label = False
        self.fields['code'].widget.attrs['placeholder'] = placeholders['code']
