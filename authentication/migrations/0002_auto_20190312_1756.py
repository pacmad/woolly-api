# Generated by Django 2.1.7 on 2019-03-12 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'ordering': ('id',), 'verbose_name': 'User Type'},
        ),
    ]
