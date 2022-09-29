# Wagtail CMS's boilerplate by Codi Cooperatiu

This boilerplate is the standard Django boilerplate used in Codi Cooperatiu's
projects with a Wagtail on top of that, for that reason the installation steps
taken are these:
https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html

A major difference from this guide is that we're not setting up MEDIA_ROOT or
MEDIA_URL because we're using python itself to serve the static files, through
the package Whitenoise.

## Prerequisites

Knowledge of Python, virtual environments and Django are assumed for
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

### First setup in Wagtail's admin panel

The behavior of the root page deserves some special attention to understand and
avoid confusion.

Using the Pages menu, go to the root level (at the topmost breadcrumb you'll
only see an earth globe) and read the information card. That means that at this
root level you will only need to have multiple pages if you are using different
sites in the same project. Right now, without any other pages added, when you
access your site's URL (http://localhost:8001) you'll just see a page with that
root page title.

To make it less confusing, edit the page "Home Page" to
a meaningful name, like "blog", your customer's brand name, etc.

While editing that page, go to the Promote tab and note that the `Slug` field
contains **home**. This is another source of confusion given that this slug does
not actually exist, as you can see if you try to access `http://localhost:8001/home/`.

With a "normal" or standalone installation of Wagtail, this home page is
already an instance of a class that you can find in the sample source code
they provide, so you can just modify or extend it right away.
In this case, though, we're adding wagtail to an existing Django installation,
for that reason we need a bit more work before we can start modifying the
home page.
Check `cms_site/migrations/0002_replace_home.py` to see how we solved this.
Thanks to that migration, you can just get to `cms_site.models.home.HomePage`
and work with this class without having to worry about manually creating the
page and linking it to the site every time you reset the database.

### Internationalization

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

TO DO

### Updating

TO DO
