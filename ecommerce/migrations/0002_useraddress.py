# Generated by Django 2.2.4 on 2019-12-11 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseno', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=50)),
                ('uaddid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.UserProfile')),
            ],
        ),
    ]
