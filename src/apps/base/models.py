from wagtail.models import Page


class BasePage(Page):
    subpage_types = []
    show_in_menus_default = True

    class Meta:
        abstract = True
