from wagtail import hooks


# @hooks.register("construct_page_listing_buttons")
# def remove_page_listing_button_item(buttons, page, page_perms, context=None):
#     specific_page = page.specific
#     if not specific_page.show_more_dropdown_in_list_actions:
#         buttons.pop()  # removes the last button, which is the 'more' dropdown.
