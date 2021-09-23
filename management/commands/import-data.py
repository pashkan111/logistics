from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data'
    
    def handle(self, *args, **options):
        self.stdout.write("Importing products")
    