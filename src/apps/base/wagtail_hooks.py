from wagtail import hooks


"""
TO DO:
Review this, there might be some new way to achieve this?
To understand the motivation and goals, read this:
https://stackoverflow.com/questions/75676645/in-wagtail-how-to-prevent-page-deletion-by-editors-or-set-a-minimum-number-of

This fields were removed from BasePage until some solid solution is found:

    is_submitable = False
    is_unpublishable = False
    # Removing this dropdown is also removing the "Delete" page option that it
    # contains. If you enable it, make sure that you actually pretend to give
    # the editor access to every action it provides!
    show_more_dropdown_in_list_actions = False

"""
# @hooks.register("construct_page_listing_buttons")
# def remove_page_listing_button_item(buttons, page, page_perms, context=None):
#     specific_page = page.specific
#     if not specific_page.show_more_dropdown_in_list_actions:
#         buttons.pop()  # removes the last button, which is the 'more' dropdown.
