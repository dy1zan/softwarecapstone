import pickle

from django import forms
from django.forms import ModelForm

from entity.models import Member
from entity.models.company import Company
from entity.models.group import Group


class AddressWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(),
            forms.TextInput()
        ]
        super(AddressWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return pickle.loads(value)
        else:
            return ['', '']


class AddressField(forms.fields.MultiValueField):
    widget = AddressWidget

    def __init__(self, *args, **kwargs):
        list_fields = [
            forms.fields.CharField(max_length=40),
            forms.fields.CharField(max_length=40)
        ]
        super(AddressField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        return pickle.dumps(values)


class CompanyApplicationForm(ModelForm):
    address = AddressField()
    address.label = "Address"

    class Meta:
        model = Company

        fields = [
            'name',
            'contact_phone',
            'contact_email',
            'website',
            'summer_students',
            'industry',
            'type_of_business',
            'size',
            'specialist_area'
        ]


class EditCompanyForm(ModelForm):
    """
    Form for updating company information
    """

    class Meta:
        model = Company
        fields = (
            'name',
            'size',
            'industry',
            'specialist_area',
            'contact_phone',
            'contact_email',
            'website',
            'type_of_business',
            'address',
            'summer_students'
        )


class EditGroupForm(ModelForm):
    """
    Form for updating group information
    """

    class Meta:
        model = Group
        fields = (
            'name',
            'website',
            'description'
        )


class AddMembeerForm(forms.Form):
    """
    Allows some entity to add members to their entity
    """

    username = forms.CharField(label='Username', max_length=50)
    role = forms.ChoiceField(label='User\'s role', choices=Member.Roles.choices)
    