from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin


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

    def autocomplete_label(self):
        return self.name

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

    def autocomplete_label(self):
        return self.name


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
