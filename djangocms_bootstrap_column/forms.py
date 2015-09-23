from django import forms
from djangocms_bootstrap_column.models import MultiResponsiveColumns, WIDTH_CHOICES
from django.utils.translation import ugettext_lazy as _


class MultiResponsiveColumnForm(forms.ModelForm):
    NUM_COLUMNS = ((i, str(i)) for i in range(1, 13))

    create = forms.ChoiceField(choices=NUM_COLUMNS, label=_("Create Columns"),
                               help_text=_("Create this number of columns"))
    create_width = forms.ChoiceField(choices=WIDTH_CHOICES, label=_("Column width"),
                                     help_text=("Width of created columns in 12ths. You can still change the width of the column afterwards."))

    class Meta:
        model = MultiResponsiveColumns
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
