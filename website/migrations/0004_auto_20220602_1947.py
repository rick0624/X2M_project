# Generated by Django 3.2.13 on 2022-06-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_news_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='new',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
