# Generated by Django 4.2.7 on 2023-11-22 11:39

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product', models.ManyToManyField(to='ecom.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
