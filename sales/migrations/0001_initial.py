# Generated by Django 2.1 on 2020-03-22 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('shortname', models.CharField(max_length=200)),
                ('fun_id', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('default', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('max_per_user', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('nemopay_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ItemField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editable', models.BooleanField(default=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemfields', to='sales.Field')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemfields', to='sales.Item')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('max_per_user', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'ONGOING'), (1, 'AWAITING_VALIDATION'), (2, 'VALIDATED'), (3, 'AWAITING_PAYMENT'), (4, 'PAID'), (5, 'EXPIRED'), (6, 'CANCELLED')], default=0)),
                ('tra_id', models.IntegerField(blank=True, default=None, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines', to='sales.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlines', to='sales.Order')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='OrderLineField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, editable='isEditable', max_length=1000, null=True)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlinefields', to='sales.Field')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('orderline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlineitems', to='sales.OrderLine')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('is_active', models.BooleanField(default=True)),
                ('is_public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('begin_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('max_item_quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('association', models.ForeignKey(on_delete=None, related_name='sales', to='sales.Association')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='orderlinefield',
            name='orderlineitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderlinefields', to='sales.OrderLineItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='sales.Sale'),
        ),
        migrations.AddField(
            model_name='item',
            name='fields',
            field=models.ManyToManyField(through='sales.ItemField', to='sales.Field'),
        ),
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='sales.ItemGroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.Sale'),
        ),
        migrations.AddField(
            model_name='item',
            name='usertype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authentication.UserType'),
        ),
        migrations.AddField(
            model_name='field',
            name='items',
            field=models.ManyToManyField(through='sales.ItemField', to='sales.Item'),
        ),
    ]
