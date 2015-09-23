from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from djangocms_bootstrap_column.models import MultiResponsiveColumns, ResponsiveColumn
from django.utils.translation import ugettext_lazy as _
from djangocms_bootstrap_column.forms import MultiResponsiveColumnForm
from cms.models import CMSPlugin


class MultiResponsiveColumnPlugin(CMSPluginBase):
    model = MultiResponsiveColumns
    module = _("Responsive Columns")
    name = _("Responsive Columns")
    render_template = "cms/plugins/multi_column.html"
    allow_children = True
    child_classes = ["ResponsiveColumnPlugin"]
    form = MultiResponsiveColumnForm

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

    def save_model(self, request, obj, form, change):
        response = super(MultiResponsiveColumnPlugin, self).save_model(request, obj, form, change)
        for x in range(int(form.cleaned_data['create'])):
            col = ResponsiveColumn(parent=obj, placeholder=obj.placeholder, language=obj.language,
                         width=form.cleaned_data['create_width'], position=CMSPlugin.objects.filter(parent=obj).count(),
                         plugin_type=ResponsiveColumnPlugin.__name__)
            col.save()
        return response


class ResponsiveColumnPlugin(CMSPluginBase):
    model = ResponsiveColumn
    module = _("Responsive Columns")
    name = _("Responsive Column")
    render_template = "cms/plugins/responsive_column.html"
    parent_classes = ["MultiResponsiveColumnPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            })
        return context

plugin_pool.register_plugin(MultiResponsiveColumnPlugin)
plugin_pool.register_plugin(ResponsiveColumnPlugin)
