# Generated by Django 2.2.6 on 2019-11-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20191025_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='Хаяг'),
        ),
    ]
