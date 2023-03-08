from django.db import migrations


def replace_home(apps, schema_editor):
    """
    TLDR: After this migration, you can just use the model
    *apps.cms_site.models.HomePage* to modify your home page. Still we
    recommend you to read this documentation.

    If we were using a standalone Wagtail installation, we would already have
    a 'home' app with a 'HomePage' page model and we could just extend it,
    and no extra steps would be needed in the CMS admin.
    But having Wagtail installed on top of an existing Django installation
    leaves us without this initial 'home' app, but Wagtail needs to create
    a page instance initially anyway (I guess that if there's only the Root
    level something might crash?).
    That means that with the normal initialization over a Django project, you
    end up with a database containing a Page (inside the Root level) that is
    using the model: wagtail.project_template.home.models.HomePage.

    That means that when you access the root level of your site, aka:
    https://localhost:8001/
    You will always see the Welcome page and you cannot modify its model
    anywhere.

    You will normally want to have your own model for the Home page that you
    can add fields and modify at your will.

    From that point you normally need to:
    1. Create an app with some model that you will use as the home page.
    2. After migrating, access the admin panel and create a page at root leave
      using your new model (with a slug different than 'home').
    3. Go to Sites and modify the default site to make the new page the default
      one.
    4. Delete the Welcome page.
    5. Edit your new page and (now that the slug is available) replace its slug
      with 'home'. You'll see that this slug is somehow hardcoded to make it
      answer to https://localhost:8001/, not to https://localhost:8001/home/.

    Our experience is that while developing a new project, each time you reset
    the database you then need to repeat these steps in the admin panel which
    is very annoying.

    The purpose of this migration is to replace the "Welcome to Wagtail" page
    by our own HomePage model automatically so none of these steps are necessary
    anymore.

    - The Root page in Wagtail 2.16.2:
    root_page_fields = {
        'id': 1,
        'path': '0001',
        'depth': 1,
        'numchild': 1,
        'translation_key': UUID('f3a676c1-a472-4d02-8d8d-25ba7aa263e4'),
        'locale_id': 1,
        'title': 'Root',
        'draft_title': 'Root',
        'slug': 'root',
        'content_type_id': 1,
        'live': True,
        'has_unpublished_changes': False,
        'url_path': '/',
        'owner_id': None,
        'seo_title': '',
        'show_in_menus': False,
        'search_description': '',
        'go_live_at': None,
        'expire_at': None,
        'expired': False,
        'locked': False,
        'locked_at': None,
        'locked_by_id': None,
        'first_published_at': None,
        'last_published_at': None,
        'latest_revision_created_at': None,
        'live_revision_id': None,
        'alias_of_id': None,
    }

    - The "Welcome to Wagtail" default Home Page in Wagtail 2.16.2:
    welcome_to_wagtail_page_fields = {
        'id': 2,
        'path': '00010001',
        'depth': 2,
        'numchild': 0,
        'translation_key': UUID('f31ea051-eeac-43b1-bc51-d132e70b74bb'),
        'locale_id': 1,
        'title': 'Welcome to your new Wagtail site!',
        'draft_title': 'Welcome to your new Wagtail site!',
        'slug': 'home',
        'content_type_id': 1,
        'live': True,
        'has_unpublished_changes': False,
        'url_path': '/home/',
        'owner_id': None,
        'seo_title': '',
        'show_in_menus': False,
        'search_description': '',
        'go_live_at': None,
        'expire_at': None,
        'expired': False,
        'locked': False,
        'locked_at': None,
        'locked_by_id': None,
        'first_published_at': None,
        'last_published_at': None,
        'latest_revision_created_at': None,
        'live_revision_id': None,
        'alias_of_id': None
    }
    """

    home_page_model = apps.get_model("cms_site", "HomePage")
    site_model = apps.get_model("wagtailcore", "Site")
    page_model = apps.get_model("wagtailcore", "Page")
    cont_type_model = apps.get_model("contenttypes", "ContentType")
    initial_site = site_model.objects.all()[0]
    welcome_to_wagtail_page = page_model.objects.get(
        id=initial_site.root_page_id,
    )
    home_cont_type = cont_type_model.objects.get_for_model(home_page_model)
    fields = {
        'id': welcome_to_wagtail_page.id,
        'path': welcome_to_wagtail_page.path,
        'depth': welcome_to_wagtail_page.depth,
        'numchild': welcome_to_wagtail_page.numchild,
        'translation_key': welcome_to_wagtail_page.translation_key,
        'locale_id': welcome_to_wagtail_page.locale_id,
        'title': 'Home Page',
        'draft_title': 'Home Page',
        'slug': welcome_to_wagtail_page.slug,
        'content_type': home_cont_type,
        'live': welcome_to_wagtail_page.live,
        'url_path': welcome_to_wagtail_page.url_path,
    }
    welcome_to_wagtail_page.delete()
    new_home = home_page_model(**fields)
    new_home.save()

    initial_site.root_page = new_home
    initial_site.save()
    print("Home page replaced.")


class Migration(migrations.Migration):

    dependencies = [
        ('cms_site', '0001_initial'),
        ('wagtailcore', '__latest__'),
    ]

    operations = [
        migrations.RunPython(replace_home),
    ]
