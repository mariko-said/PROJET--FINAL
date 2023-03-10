# Generated by Django 4.1.5 on 2023-01-18 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_add'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prix', models.FloatField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=5000)),
                ('date_add', models.DateTimeField(auto_now=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='menu.categorie')),
            ],
            options={
                'ordering': ['-date_add'],
            },
        ),
    ]
