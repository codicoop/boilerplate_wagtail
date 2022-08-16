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
        self.dump_locales()
        self.dump_content()

    def dump_locales(self):
        path = "apps/base/fixtures/locales.json"
        parameters = (
            "--indent=2",
            "wagtailcore.locale",
            f"-o={path}",
        )
        call_command("dumpdata", *parameters, verbosity=2)
        self.stdout.write(f"Fixtures updated at {path}.")

    def dump_content(self):
        path = "apps/base/fixtures/content.json"
        parameters = (
            "--natural-foreign",
            "--indent=2",
            "-e=contenttypes",
            "-e=auth.permission",
            "-e=auth.group",
            "-e=sessions",
            "-e=users",
            "-e=wagtailcore.groupcollectionpermission",
            "-e=wagtailcore.grouppagepermission",
            "-e=wagtailimages.rendition",
            # "-e=wagtailcore.pagerevision",
            "-e=wagtailcore.pagesubscription",
            "-e=wagtailcore.workflow",
            "-e=wagtailcore.task",
            "-e=wagtailcore.workflowtask",
            "-e=wagtailcore.workflowpage",
            "-e=wagtailcore.collection",  # ????????????
            "-e=wagtailcore.site",
            "-e=wagtailcore.locale",
            "-e=wagtailsearch.indexentry",
            "-e=wagtail_localize.translationlog",
            f"-o={path}",
        )
        call_command("dumpdata", *parameters, verbosity=2)
        self.stdout.write(f"Fixtures updated at {path}.")
