# Wagtail CMS's boilerplate by Codi Cooperatiu

This boilerplate is the standard Django boilerplate used in Codi Cooperatiu's
projects with a Wagtail on top of that, for that reason the installation steps
taken are these:
https://docs.wagtail.org/en/stable/getting_started/integrating_into_django.html

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
