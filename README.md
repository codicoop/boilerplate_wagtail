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
`docker exec -it develop_project_name_app /bin/bash`.
6. Wagtail's admin will be accessible at http://localhost:8001/cms/
7. To create your new app, you need to run `django-admin startapp` **from
the `/src/apps` folder** and then add it to `INSTALLED_APPS` setting like this:
`"apps.application_name"`
8. In you new app's folder check that in `apps.py` the `BaseConfig` sets the
property name also prefixed with the apps folder, like this: `name = "apps.application_name"`

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
`collectstatic` when building it) you usually don't need to run it manually.

