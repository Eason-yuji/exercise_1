# Generated by Django 2.2.5 on 2020-12-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.BookInfo'),
            preserve_default=False,
        ),
    ]
