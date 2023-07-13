from django.core.management.base import BaseCommand
from apps.blogs.models import Category


class Command(BaseCommand):
    help = 'Creates default categories'

    def handle(self, *args, **options):
        self.create_categories()

    def create_categories(self):
        categories = [
            {
                'name': 'Category 1',
                'desc': 'Category 1 description'
            },
            {
                'name': 'Category 2',
                'desc': 'Category 2 description'
            },
            {
                'name': 'Category 3',
                'desc': 'Category 3 description'
            }
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'desc': category_data['desc']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Category '{category.name}' created."))
