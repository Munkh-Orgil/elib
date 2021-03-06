# Generated by Django 2.2.6 on 2019-11-27 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20191127_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10, null=True, verbose_name='Ангилал')),
            ],
            options={
                'verbose_name_plural': 'Ангилалууд',
            },
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Category', verbose_name='Ангилал'),
        ),
    ]
