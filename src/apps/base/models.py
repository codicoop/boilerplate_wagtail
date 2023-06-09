from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page, PageManager
from wagtailmenus.conf import settings as wagtail_settings
from wagtailmenus.models import AbstractMainMenu, AbstractMainMenuItem


class RequestedLocalePageManager(PageManager):
    def requested_locale(self, request):
        # current_locale is included in the request using a middleware
        return self.get_queryset().filter(locale=request.current_locale)


class BasePage(Page):
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        verbose_name=_("Header image"),
        on_delete=models.SET_NULL,
        related_name="+",
        # Needs to be true for initial migrations to work, given that we're
        # programatically creating a HomePage instance.
        null=True,
        blank=False,
        help_text=_(
            "Aquesta imatge està pensada per ser decorativa i crear "
            "acompanyar el contingut. Segons la resolució i el dispositiu de "
            "l'usuari, la mida i proporció variarà, i per tant es retallaran "
            "parts de la imatge. La proporció recomanada és de 2x1, amb una "
            "mida mínima de 2.000x1.000px."
        ),
    )

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
    ]
    max_count = 1
    show_in_menus_default = False
    parent_page_types = ["cms_site.HomePage"]
    is_submitable = False
    is_unpublishable = False
    # Removing this dropdown is also removing the "Delete" page option that it
    # contains. If you enable it, make sure that you actually pretend to give
    # the editor access to every action it provides!
    show_more_dropdown_in_list_actions = False
    objects = RequestedLocalePageManager()

    class Meta:
        abstract = True

    def get_context(self, request, *args, **kwargs):
        ctxt = super().get_context(request, *args, **kwargs)
        legal_page = apps.get_model("cms_site", "LegalPage").objects.first()
        if legal_page:
            ctxt.update(
                {
                    "legal_page": legal_page,
                },
            )
        return ctxt


class MenuLabelMixin(models.Model):
    """
    Mixin for BasePage.
    """

    menu_label = models.CharField(
        _("Menu title"),
        max_length=15,
        null=True,
        blank=True,
        help_text=_("If not set, the menu title will be the page title."),
    )

    promote_panels = BasePage.promote_panels + [
        FieldPanel("menu_label"),
    ]
    show_in_menus_default = True

    class Meta:
        abstract = True


class LocalizedMainMenu(AbstractMainMenu):
    def get_pages_for_display(self):
        """Returns a queryset of all pages needed to render the menu."""
        if hasattr(self, "_raw_menu_items"):
            # get_top_level_items() may have set this
            menu_items = self._raw_menu_items
        else:
            menu_items = self.get_base_menuitem_queryset()

        # Start with an empty queryset, and expand as needed
        queryset = Page.objects.none()

        for item in (item for item in menu_items if item.link_page):
            """Workaround:
            The trick of extending AbstactMainMenuItem to change
            its self.link_page to self.link_page.localized introduces a bug
            that prevents menu items with subpages to be displayed.

            Say you save a menu while using the admin in english language,
            now in the Menu model you have the english versions of the Page
            objects.
            Let's say the page is "Projects" with ID 30 in english.

            Then you visit the site in catalan, now the page that was ID 30 in
            english is ID 8 in catalan.

            get_top_level_items() will be called and will do this:
            menu_items = self.get_base_menuitem_queryset()
            Now you have all the menu items in the Menu model as they were
            stored, that is, in english, so "Projects" in menu_items has
            id 30.
            Then it will compare menu_item items with get_pages_for_display()
            items. The latest will contain the pages already localized, except
            if the menu item allows submenus, in that case IT WILL NOT.
            Therefore the Projects page in get_pages_for_display will be the
            english one, and its ID will be 30.

            That's when it checks this:
            try:
            item.link_page = self.pages_for_display[item.link_page_id]

            Which, in the case described, fails and the menu item is not
            displayed.

            Forcing get_pages_for_display to use the localized link_page
            solves it:
            """
            if item.link_page.localized:
                item.link_page = item.link_page.localized

            if (
                item.allow_subnav
                and item.link_page.depth >= wagtail_settings.SECTION_ROOT_DEPTH
            ):
                # Add this branch to the overall `queryset`
                queryset = queryset | Page.objects.filter(
                    path__startswith=item.link_page.path,
                    depth__lt=item.link_page.depth + self.max_levels,
                )
            else:
                # Add this page only to the overall `queryset`
                queryset = queryset | Page.objects.filter(id=item.link_page_id)

        # Filter out pages unsutable display
        queryset = self.get_base_page_queryset() & queryset

        # Always return 'specific' page instances
        return queryset.specific()


class LocalizedMainMenuItem(AbstractMainMenuItem):
    menu = ParentalKey(
        LocalizedMainMenu,
        on_delete=models.CASCADE,
        related_name=wagtail_settings.MAIN_MENU_ITEMS_RELATED_NAME,
    )

    def __init__(self, *args, **kwargs):
        """
        This makes the menu work seamlessly with multi-language entirely:
        - In the admin you only add the pages once per language, but the
          menu also appears even if you are visiting the page that is in
          another language.
        - The menu item's text is in the current language.
        - The menu item's link point to the right language.
        """
        super().__init__(*args, **kwargs)
        if self.link_page and self.link_page.localized:
            self.link_page = self.link_page.localized

    @property
    def menu_text(self):
        if (
            self.link_page
            and hasattr(self.link_page, "menu_label")
            and self.link_page.menu_label is not None
        ):
            return self.link_page.menu_label
        return super().menu_text
