# Generated by Django 4.2.1 on 2023-06-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.CharField(default='fa-solid fa-computer-speaker', max_length=50, verbose_name='Класс иконки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
