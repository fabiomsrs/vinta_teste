# Generated by Django 2.2.13 on 2020-07-03 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import social_django.fields
import social_django.storage


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(db_index=True, max_length=255)),
                ('extra_data', social_django.fields.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Social User',
                'verbose_name_plural': 'Social Users',
            },
            bases=(models.Model, social_django.storage.DjangoUserMixin),
        ),
    ]