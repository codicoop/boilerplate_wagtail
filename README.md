# Wagtail CMS's boilerplate by Codi Cooperatiu

This boilerplate is the standard Django boilerplate used in Codi Cooperatiu's
projects with a Wagtail on top of that, for that reason the installation steps
taken are these:
https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html

A major difference from this guide is that we're not setting up MEDIA_ROOT or
MEDIA_URL because we're using python itself to serve the static files, through
the package Whitenoise.

## Prerequisites

Knowledge of Python, virtual environments, Django and Wagtail are assumed for
this tutorial.

We use Pyenv to have multiple Python versions and Poetry for managing packages
and the virtual environment, but you can use anything else.

## About Docker

A Dockerfile is included given that we use Docker for both the local development
and deploys to production, but you can just delete the docker folder if you are
not going to use it.

## Steps to start a new project

1. Open https://github.com/codicoop/boilerplate_wagtail and create a new repository
using the "Use this template" button, or download all the files as .zip and
manually create a new repository.
2. Using [https://python-poetry.org/](Poetry), create the virtual environment
and install its dependencies: `poetry install`. If you want to use any other
package manager, check the dependencies listed in the `pyproject.toml` file and
then you can remove this file and `poetry.lock`.
3. `cp docker/settings/settings.env.example docker/settings/development.env` and
check and adjust settings. I you want to use a different name, also update
docker/docker-compose.yml's `env_file` property.
4. In the `docker` folder you can now do: `docker-compose up`.
5. Run migrations and create a super user using the app's container shell:
`docker exec -it develop_wagtail_boilerplate_app /bin/bash`.
6. Wagtail's admin will be accessible at http://localhost:8001/cms/
7. To create your new app, you need to run `django-admin startapp` **from
the `/src/apps` folder** and then add it to `INSTALLED_APPS` setting like this:
`"apps.application_name"`
8. In you new app's folder modify `apps.py` prefixing the `name` property with
the apps folder, like this: `name = "apps.application_name"`

From this point, if it's your first time using Wagtail it's highly recommendable
to read [this tutorial](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)
as well as [the documentation](https://docs.wagtail.org/en/stable/topics/index.html)

## Development guidelines

### Code formatting, validation and tests

#### Tox for black and tests
A Tox setup is provided and the tox software itself is included as a dependency
in `pyproject.toml`.

To let tox reformat your code using Black, you need to get inside the virtual
environment shell (`poetry shell`) and run:
`tox -e format`

Some format changes cannot be done automatically. You'll get a list of them when
you run:

`tox`

Which will validate the format and run the tests.

#### Github actions

Tox will automatically be run when you push a PR to Github. The configuration
is in the `.github` folder.

### Initial migration

This boilerplate include a migration that sets up the initial home page for you.

We're detailing here what would normally be the manual setup you'll have to do
when you initialize Wagtail over an existing Django project.

This migration will:

- Setup the initial Home page with the correct information. We highly recommend
to read *apps.cms_site.migrations.0002_data_replace_home*'s documentation to
understand what's going on with the home page.
- Create an initial superuser, using the settings `DJANGO_SUPERUSER_EMAIL` and
`DJANGO_SUPERUSER_PASSWORD`. You need to have these settings defined
before running the initial migration for this to happen. Note that the first
time you generate fixtures for the site (as explained later on), those will get
"bound" to the user name you are using. For example, if I start the project
and create content with the user hola@codi.coop, every other developer needs to
have this same user created to be able to import the fixtures.

### Internationalization

You have 2 separated blocks of content to be translated
1. The source code literals, which include all the strings from the front end
templates as well as the strings in your python files for the CMS panel.
2. The content of the website itself.

Recommendations for your development process:

- Leave the translations for the very
last of the steps, after all the final information is in place and the customer
gave the OK for the base language.
- For your content, use the most comfortable language for your customer to work
with.
- In your source code, always use english for your literals, even if the website
is not going to be available in this language at all. More details about that
in the following sections.

#### Source code

Translation tags are used across the templates and this part is handled by Django,
not by Wagtail, so you'll need to generate the localization .po files, translate,
and compile them.

The same goes for all the strings in the backend that are localized with
`_("Hello")`.

#### Wagtail content

It's recommended to read this [Wagtail documentation's section](https://docs.wagtail.org/en/stable/advanced_topics/i18n.html#multi-language-content)
and the [Wagtail Localize documentation](https://www.wagtail-localize.org/tutorial/1-project-set-up/).

##### Configure available languages

> In our experience we found that not including the english language or not
> making it the default one in the Django settings some problems might appear.
> We believe that this could be because all the localized strings in Django and
> any package are written in english in the source code, and mixing it with
> source code in another language is something that gets in the way of the .po
> files management.

1. Firstly edit `WAGTAIL_CONTENT_LANGUAGES` in settings to specify the available
languages.
2. Access `Settings -> Locales` in the admin panel and add the locales that you
want. Usually you'll want to enable de tree synchronization.
3. If you are using the tree synchronization, all the existing page are now
duplicated in the added locale. Select one of them and click on the Translate
button to enable the synchronized translation for this page, which will only ask
you for the new strings. New pages will also be created for all other languages.
4. If you want a different structure (i.e., the translated page will have
different blocks), stop the synchronized translation for this page.

If you want to prevent the editor from creating or removing locales you can
remove the `Locales` menu by removing `wagtail_localize.locales` from
`INSTALLED_APPS`. You will still be able to manage them through console
(use `python manage.py shell_plus`).

You can modify the field's status *translatable* vs *synchronized*, although
the default behavior is usually the desired one. [Link to documentation](https://www.wagtail-localize.org/how-to/field-configuration/).
We still have to test it better, but the idea is that when you modify the main
page, its translations might have some fields override in order to keep the
synchronization.

For now, it's recommended to avoid ListBlocks for content susceptible to
translation:

> The recommended work around at the moment is to change all ListBlocks into
> nested StreamBlocks instead. We should be able to solve this one when Wagtail
> RFC 65 is implemented, which adds UUIDs into ListBlock.

This RFC was included in a PR in 2021, so we should check if this is something
already implemented but not updated in the documentation, or is still pending.

##### Translatable snippets

Snippets can be translatable: https://docs.wagtail.org/en/stable/advanced_topics/i18n.html#translatable-snippets

##### Generating the .po files

To translate the source code, you need to use the django's manage.py to
generate the .po files and then compile them.

In a previous project, it workes using the parameter `--all`, but this time I
only managed to make it work by specifying the languages:

    python manage.py makemessages -l ca -v 3
    python manage.py makemessages -l es -v 3

Also, when using it from the poetry's virtual environment, if I tried it with
`django-admin` instead of `python manage.py`, it didn't work.

You will need `gettext` installed to be able to generate these files. There's
the idea of installing it in the Docker image so everyone will be able to
generate the files from the docker container itself, but it's not done yet. So
for Windows users, better ask someone with linux to generate the files for you.

### Development tools and advice for localized content

Beware that when you create a translation for a page (for instance, if you
choose to synchronize the tree when creating the new locale, it will generate
a new page for each existing one), when you query all the child pages of a page
you will get ALL of them, not filtered by the desired language.

An easy example to understand is with a blog. Let's say that in the index page
you are filling the context with all the blog articles, which are child pages
of that index page.
To avoid displaying every article in all the languages, you should use this:

```python
def get_context(self, request, *args, **kwargs):
    context = super().get_context(request, *args, **kwargs)
    collection_page_model = apps.get_model("cms_site", "CustomProject")
    article_pages = blog_index_page_model.objects.requested_locale(
        request,
    ).live().specific()
    context.update(
        {
            "article_pages": article_pages,
        }
    )
    return context
```

*(the `.live().specific()` is a suggestion)*

To understand how it works, check `RequestedLocalePageManager`.

### Wagtail's styleguide

Including `"wagtail.contrib.styleguide"` in your `INSTALLED_APPS` will add a
menu option in settings to help you with colors, icons, etc. while developing.
Make sure to disable it in production if you don't want your customer to see
the option.

### Assets

The configuration expects a `/src/assets/` folder containing all static images, css
and js. This folder should be created if it doesn't exist already or Django
will complaint with warnings.

The static assets are going to be served through the library Whitenoise when
debug is deactivated. Beware that whitenoise makes an index of the static files
when starting up, therefore if you change a static file you need to first
`collectstatic` and then restart the container.
Given that locally you'll be having debug activated and when deploying in
pre-production or production you'll use the docker image (which already runs
`collectstatic` when building it) you'll only need to run it manually when
testing `debug = False` locally.

### Fixtures

#### To create or update the fixtures with the current data, do the following:

1. Create the desired data through the admin site.
2. Use the `python manage.py exportfixtures` command.

#### Loading the fixtures

Fixtures are not loaded during the initial migration because the `contenttype`
table is not filled yet, wich causes `loaddata` to fail.
Also, is better to have the flexibility to decide if you want or not to load
them.

Run this command:

    python manage.py importfixtures

> To be able to load the fixtures, the `DJANGO_SUPERUSER_EMAIL` setting must be
> set to `hola@codi.coop`.

### CMS's admin modifications to page actions, and how to manage them

We use hooks to modify the available page actions to control what the editors
can and cannot do beyond what can be controlled by the permissions system.

As you'll see in the official documentation, most hooks let you just add more
buttons, but not edit or remove the existing ones.

But the hooks that are prefixed *construct_* give us access to the entire
renderization, for example:
https://docs.wagtail.org/en/stable/reference/hooks.html#construct-page-action-menu

Following this technique, this boilerplate comes with the following properties
in the `BasePage` model:

    is_submitable = False
    is_unpublishable = False

Which control that the corresponding buttons are rendered or not.

    show_more_dropdown_in_list_actions = False

Which hides the "More" dropdown in the actions for each page in the list view.

You can customize all these tweaks in `apps.base.wagtail_hooks`.


# TO DO: Different phases of developing

## Initial phase

- Need to recreate migrations and database constantly
- Need to bring the frontend developer some structure to place the template. If
the project is headless they can build up all the html without the endpoints yet.

## Content-related phase

In this phase we have most of the development finished and we are filling up the
cms with the final content.
Our goal is to deliver the site with the initial content preloaded and ready to
open in production, not just the CMS for the editor to fill everything itself.

At the same time, the backend developers will still need to reset the database
quite a lot of times, which could lead to the frontend developer to have to fill
the content manually multiple times, consuming time and generating frustration.

To address that we need to set "checkpoints" in which there's a commitment from
the backend developers to keep the database structure intact unless something
extremely important requires to break it.
Then, the frontend developer can work with this branch until the content is
ready, and ask the backend devs. to create a data migration that will load
all the database to that point.

# Releasing new versions to pre-production and production.

The docker image is stored at Digital Ocean's (from now on: DO) Container Registry.

The latest version of the general instructions for deployments in DO will be
[here](http://docus.codi.coop:3000/en/knowledge-base/deploy-do):

There's a VPS for pre-production releases, and at this time the project is not
yet released to production but it's
expected to deploy it at DO. For this reason, this documentation only covers
pre-production.

**Steps overview**

When we finish a sprint, it will go through thorough testing until the new
release it's ready to be presented to the
consumer (that is: TandemMarianao) in order to have them test and verify the
changes before going to production.

The current version at `develop` will be deployed at the pre-production server
and the consumer will be informed along
with a changelog.

For this deployment we'll generate the docker image and upload it to DO, then
connect to the server and make necessary
adjustments if any, start the containers using docker-compose and run `migrate`
and any other necessary commands.

Once we have the feedback and we fix the potential bugs they find, we'll be
ready to move it to `main` and make a new
release to pre-production that this time will only be tested by us, and if
everything is OK, will be released to
production.

## Deploying to develop (pre-production)

### Building the docker image

Before deploying to pre-production, you'll need to update the image at DO.

From the root folder run:

    docker build -t ciurans:preproduction -f docker/Dockerfile .

For the next steps, you should check the instructions directly at the DO's
control panel, by going to Container Registry
and using the *Push images using Docker CLI* link at the footer. Nonetheless,
we're copying below those instructions:

After having set up the `doctl` command in your system according to the
aforementioned documentation, copy the generated
image to another tag that will include the DO prefix:

    docker tag ciurans:preproduction registry.digitalocean.com/codihub/ciurans:preproduction

Then push it:

    docker push registry.digitalocean.com/codihub/ciurans:preproduction

Now check the DO's Container Registry page and that new release should appear.

### First time deployment

To allow for faster releases in pre-production, we'll be using the same
dockerization than for your local development
environment, with the difference of using the `docker/preproduction.yml`
docker-compose file instead of the default one.

The main differences between the default `docker-compose.yml` and
`preproduction.yml` are:
- Nginx opens a different port.
- The app image points to the remote image uploaded to DO, instead of a `build`
command.
- The app points to a different settings file (`docker/settings/preproduction.env`).

> Keep in mind that most of the changes in the dockerization will usually need
> to be replicated in `preproduction.yml`,
> as well as adding or changing the settings variables in `preproduction.env`
> when necessary.

Steps for setting up the pre-production in a server for the first time:

1. Build and upload the new docker image as described above.
2. Update the `preproduction.yml`, for instance, changing the docker image tag
3. name for the latest one, and push changes.
3. Clone the [repository](git@github.com:codicoop/ciurans.git) in a folder.
In our case, inside `/srv/develop/`.
4. In `docker/settings/`, copy `settings.env.example` to `preproduction.env`
and edit the variables.
5. Your server will need to be authenticated with DO to be able to pull the
image. To find out, try to pull it manually,
i.e. `docker pull registry.digitalocean.com/codihub/ciurans:preproduction`.
6. To set up the DO's client and authorize, follow
[this instructions](https://docs.digitalocean.com/reference/doctl/how-to/install/)
until you have the `doctl` installed and logged in, and then do
`doctl registry login` to specifically authenticate to
be able to interact with the Container Registry.
7. Go to `docker/` and run `docker-compose -f preproduction.yml up -d`.

Migrations should've run automatically already and, with them, you should have
the superuser account created with the
credentials specified in the settings file.

### Updating

Deploying a new pre-production release is as easy as updating the docker image
to DO, and in the server pull the repo's
changes and start the dockerization.

Detailed steps:

1. Build and upload the new docker image as described above.
2. Update `preproduction.yml` so the docker image name is the new one. You can create a branch or just use `develop`.
Beware that the image name may appear in different containers (startup-commands, celery...).
3. In the server, make sure you're in the right branch and `git pull` the changes.
4. If the dockerization was modified, you might need to stop any running containers before proceeding.
5. Update the settings at `/docker/settings/preproduction.env` if necessary.
6. At `/docker/`, start the dockerization with `docker-compose -f preproduction.yml up -d`. Remember that the compose
already runs `migrate` in the process.

## Deploying to production

### Building the docker image

Before deploying to production, you'll need to update the image at DO.

Follow the same steps as described in *Building the docker image* for preproduction,
but instead of using the tag `ciurans:preproduction`, use:

    ciurans:release-YY.MM.001

### First time deployment

At some point of the process we need to give access to the client for them to
start filling the information at the CMS, collect photos for the sections,
write missing texts, etc.

We already leave the fixtures in the best state that we can with the information
that we have before giving access to the client.

An option is to give access in the preproduction server, but given that's the
first time, we can do the production deployment at DO. That way when we reach
the point in which is ready to be opened to the public, only a change of DNSs
will be necessary.

#### The first deployment itself

Follow the steps detailed in the wiki, until you have the project_name.do.codi.coop
host working correctly.

Then:

1. Run migrations.
2. Import the fixtures.
3. Log-in using the default superuser account according the the environment variable
settings.
4. This password should only be used for a first time login to change it for another
one, given that is stored in the environment variables and in local files of
the developers, and given that is a highly sensitive information, we don't want
to risk forgetting to change it in case we leave it for later.
So, right away, change the password for this user, and write down the new login
details in the password manager.

#### Updating a version that includes new fixtures

If you upload a new image version containing updated fixtures, make sure that
you are doing this in a stage of the process in which the client did not update
any information yet.

From the moment they start including real information, the fixtures should never
be updated again in production. They should be kept updated as they're a great
tool for developing, though.

If you are in this situation in which you can completely override the CMS's
database and you want to do that with new fixtures, the steps are:

1. Make sure the fixtures are clean from undesired information. I.e., is you've
been testing the contact form, the `AjaxContactSubmission` (if you kept the name)
will be full of garbage entries. Before generating the fixtures empty the model,
you can use the `shell_plus` command and then something like
`AjaxContactSubmission.objects.all().delete()`.
2. Obviously update the docker image and app settings as with any update.
2. Go to the Databases section, and directly delete the project's database.
**Double check as much as possible at this point to make sure you are deleting
the right database.**
3. Recreate the database with the same exact name.
4. At the app, run the command to import the fixtures.

Now you won't be able to login with the superuser account because the password
is again the one specified in the environment variables.
Read and follow the instructions of the 4th point in the section above,
*The first deployment itself*. With the difference that this time you should
set the same password that we already have in the password manager, don't create
a new entry.


### Updating

TO DO

## React Setup

Consultar [els docus](http://docus.codi.coop:3000/e/en/knowledge-base/front/react_setup)

## Configuring the webpage's Menu

### For editors: How to use it

In the CMS panel, go to Settings - Main menu.

Click Add menu item, then select the page you want to link to it, leave every
other field empty and Save.

Now reload the page and the menu item should appear.
If not, find and edit the linked Page and at the Promote tab, check the
"Show in menus" field, and Publish.

The label for the menu items is the `Menu title` field of the page. If that
field does not exist, it's going to use the `Page title`.
When a Page is available in multiple languages, the menu item is going to show
the localized string according to the language that the user is using.

### For developers: How to create new pages to be included in menus

Just use the `base.models.MenuLabelMixin` mixin, as you'll see, this will add the
field for the menu item's label, as well as setting the "Show in menus" field
enabled by default.

### Implementation technical notes

2 packages are involved in the process:
https://github.com/jazzband/wagtailmenus
https://github.com/wagtail/wagtail-localize

The problem is that wagtailmenus don't support localization yet.

There's a workaround to make wagtailmenus return the localized version of the
page, of which you can find information:
- In this issue: https://github.com/jazzband/wagtailmenus/issues/242#issuecomment-795138779
- At the documentation included in the class base.models.LocalizedMainMenu
- At the documentation included in the class base.models.LocalizedMainMenuItem

Note that this all can work only if you use this setting:

    WAGTAILMENUS_MAIN_MENU_MODEL = "base.LocalizedMainMenu"

