# Generated by Django 4.2.2 on 2023-06-07 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='book',
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='book.book'),
            preserve_default=False,
        ),
    ]
