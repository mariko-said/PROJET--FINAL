# Generated by Django 4.1.5 on 2023-01-21 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_produit_options_produit_date_update_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='produit',
        ),
        migrations.DeleteModel(
            name='Avis',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]