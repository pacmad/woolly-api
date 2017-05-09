# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bank_account', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AssociationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('rights', models.CharField(max_length=50)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Association')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('remaining_quantity', models.IntegerField()),
                ('initial_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSpecifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('api_url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('max_payment_date', models.DateField()),
                ('max_article_quantity', models.IntegerField()),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Association')),
                ('payment_methods', models.ManyToManyField(to='core.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='WoollyUserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='core.OrderLine', to='core.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemspecifications',
            name='woolly_user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WoollyUserType'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ItemGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='specifications',
            field=models.ManyToManyField(through='core.ItemSpecifications', to='core.WoollyUserType'),
        ),
    ]
