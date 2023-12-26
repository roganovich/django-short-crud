from django.core.management.base import BaseCommand, CommandError
from shop.models import Post
import json


class Command(BaseCommand):
    help = "Import posts from json file"

    def handle(self, *args, **options):
        with open('media/posts.json', encoding="utf8") as f:
            posts_json = json.load(f)

        for post in posts_json:
            post = Post(title=post["title"], content=post["content"], author_id=post["user_id"])
            post.save()
        exit()
