# Generated by Django 4.1.5 on 2023-02-02 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_remove_avis_produit_remove_avis_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Categorie', to='menu.categorie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='produit',
            name='titre',
            field=models.CharField(max_length=200),
        ),
    ]
