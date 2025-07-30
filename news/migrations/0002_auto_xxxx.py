# news/migrations/0002_auto_xxxx.py
from django.db import migrations
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from news.models import Post


def add_permissions(apps, schema_editor):
    content_type = ContentType.objects.get_for_model(Post)
    add_post = Permission.objects.get_or_create(
        codename='add_post',
        name='Can add post',
        content_type=content_type,
    )
    change_post = Permission.objects.get_or_create(
        codename='change_post',
        name='Can change post',
        content_type=content_type,
    )

    authors_group = Group.objects.get(name='authors')
    authors_group.permissions.add(add_post[0], change_post[0])


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_permissions),
    ]