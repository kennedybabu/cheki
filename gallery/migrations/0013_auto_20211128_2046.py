# Generated by Django 3.2.9 on 2021-11-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20211128_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='gallery.Category'),
        ),
    ]