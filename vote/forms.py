from django.forms import ModelForm, inlineformset_factory

from .models import Address, Choice


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ('votes', )


ChoiceFormSet = inlineformset_factory(Address, Choice, form=ChoiceForm, extra=2)




