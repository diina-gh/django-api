from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == "apps.blogs":
        # Define the default categories
        default_categories = [
            {
                'name': 'Category 0',
                'desc': 'Category 0 description'
            }
        ]

        # Create default categories
        for category_data in default_categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'desc': category_data['desc']}
            )
            if created:
                print(f"Category '{category.name}' created.")




