# Generated by Django 2.2.4 on 2019-12-02 20:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20191126_2120'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='shoppcart',
            unique_together={('prodcartid', 'buyerid')},
        ),
    ]