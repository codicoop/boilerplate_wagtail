from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class CollectionItemType(TranslatableMixin):
    name = models.CharField(_("name"), max_length=255)

    panels = [
        FieldPanel("name"),
    ]

    class Meta(TranslatableMixin.Meta):
        verbose_name = _("Collection item type")
        verbose_name_plural = _("Collection item types")

    def __str__(self):
        return self.name


@register_snippet
class CollectionItemFinishing(TranslatableMixin):
    name = models.CharField(_("name"), max_length=255)

    panels = [
        FieldPanel("name"),
    ]

    class Meta(TranslatableMixin.Meta):
        verbose_name = _("Collection item finishing")
        verbose_name_plural = _("Collection item finishings")

    def __str__(self):
        return self.name


@register_snippet
class CollectionItemModel(TranslatableMixin):
    name = models.CharField(_("name"), max_length=255)

    panels = [
        FieldPanel("name"),
    ]

    class Meta(TranslatableMixin.Meta):
        verbose_name = _("Collection item model")
        verbose_name_plural = _("Collection item models")

    def __str__(self):
        return self.name
