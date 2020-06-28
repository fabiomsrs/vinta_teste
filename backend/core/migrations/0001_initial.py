# Generated by Django 2.2.13 on 2020-06-08 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('owner', models.CharField(max_length=150, verbose_name='Proprietário')),
                ('date', models.DateTimeField(verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Repo',
                'verbose_name_plural': 'Repos',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150, verbose_name='Autor')),
                ('url', models.URLField(verbose_name='url')),
                ('date', models.DateTimeField(verbose_name='Data')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='core.Repo', verbose_name='Repositório')),
            ],
            options={
                'verbose_name': 'Commit',
                'verbose_name_plural': 'Commits',
                'ordering': ('date',),
            },
        ),
    ]