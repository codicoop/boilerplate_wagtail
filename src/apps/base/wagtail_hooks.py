from wagtail import hooks


@hooks.register('construct_page_action_menu')
def remove_disabled_actions(menu_items, request, context):
    specific_page = context["page"].specific
    if not specific_page.is_submitable:
        menu_items[:] = [item for item in menu_items if item.name != 'action-submit']
    if not specific_page.is_unpublishable:
        menu_items[:] = [item for item in menu_items if item.name != 'action-unpublish']


@hooks.register('construct_page_listing_buttons')
def remove_page_listing_button_item(buttons, page, page_perms, context=None):
    specific_page = page.specific
    if not specific_page.show_more_dropdown_in_list_actions:
        buttons.pop() # removes the last button, which is the 'more' dropdown.
