from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.utils.compat.dj import python_2_unicode_compatible

if hasattr(settings, "COLUMN_WIDTH_CHOICES"):
    WIDTH_CHOICES = settings.COLUMN_WIDTH_CHOICES
else:
    WIDTH_CHOICES = (
        ('1', _("1")),
        ('2', _("2")),
        ('3', _('3')),
        ('4', _("4")),
        ('5', _('5')),
        ('6', _("6")),
        ('7', _('7')),
        ('8', _('8')),
        ('9', _('9')),
        ('10', _('10')),
        ('11', _('11')),
        ('12', _('12')),
    )


@python_2_unicode_compatible
class MultiResponsiveColumns(CMSPlugin):
    """
    A plugin that has sub Column classes
    """
    def __str__(self):
        return _(u"%s columns") % self.cmsplugin_set.all().count()


@python_2_unicode_compatible
class ResponsiveColumn(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """

    width = models.CharField(_("width"), choices=WIDTH_CHOICES, default=WIDTH_CHOICES[0][0], max_length=50)

    def __str__(self):
        return u"%s" % self.get_width_display()
