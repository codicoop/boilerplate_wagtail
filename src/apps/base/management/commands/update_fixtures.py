from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Exports the current data to the fixture that is going to be loaded "
        "when migrations are run. This is meant to make it easier for the "
        "developers to have an initial set of data, and can also be used to "
        "prepare all the final data locally in the first release to "
        "production. Beware that this fixture needs to be compatible with the "
        "latest state of the models, given that the migration that will import"
        " it will be run after all other app's migrations."
    )

    def handle(self, *args, **options):
        path = "apps/base/fixtures/full_site.json"
        parameters = (
            "--natural-foreign",
            "--indent=2",
            "-e=contenttypes",
            "-e=auth.permission",
            "-e=wagtailcore.groupcollectionpermission",
            "-e=wagtailcore.grouppagepermission",
            "-e=wagtailimages.rendition",
            "-e=wagtailcore.pagerevision",
            "-e=sessions",
            f"-o={path}",
        )
        call_command("dumpdata", *parameters, verbosity=2)

        self.stdout.write(
            f"Fixtures updated at {path}."
        )
