from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Imports the fixtures ensuring it uses the right order."
    )

    def handle(self, *args, **options):
        fixtures = [
            "apps/base/fixtures/locales.json",
            "apps/base/fixtures/content.json",
        ]
        for fixture in fixtures:
            call_command("loaddata", fixture, verbosity=2)

        fixtures_str = ", ".join(fixtures)
        self.stdout.write(
            f"Fixtures {fixtures_str} loaded."
        )
