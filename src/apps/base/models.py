from wagtail.core.models import Page


class BasePage(Page):
    subpage_types = []

    class Meta:
        abstract = True
