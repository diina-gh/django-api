from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.blogs.models import Category, Post


class Command(BaseCommand):
    help = 'Creates default posts'

    def handle(self, *args, **options):
        self.create_posts()


    def create_posts(self):
        posts = [
            {
                'title': 'Post 1',
                'desc': 'Post 1 description',
                'category': 'Category 1'
            },
            {
                'title': 'Post 2',
                'desc': 'Post 2 description',
                'category': 'Category 2'
            },
            {
                'title': 'Post 3',
                'desc': 'Post 3 description',
                'category': 'Category 3'
            },
            {
                'title': 'Post 4',
                'desc': 'Post 4 description',
                'category': 'Category 1'
            },
            {
                'title': 'Post 5',
                'desc': 'Post 5 description',
                'category': 'Category 2'
            }
        ]

        for post_data in posts:
            category = Category.objects.get(name=post_data['category'])
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'desc': post_data['desc'],
                    'category': category,
                    'user': User.objects.first() 
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Post '{post.title}' created."))
