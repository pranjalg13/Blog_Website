# Generated by Django 2.2.2 on 2020-05-03 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200503_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_blog',
            name='author',
        ),
    ]