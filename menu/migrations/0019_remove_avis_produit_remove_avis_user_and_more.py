# Generated by Django 4.1.5 on 2023-02-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_tag_alter_produit_categorie_alter_produit_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='avis',
            name='user',
        ),
        migrations.RemoveField(
            model_name='commentaire',
            name='produit',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Produit', to='menu.categorie'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='Produit'),
        ),
        migrations.DeleteModel(
            name='Avis',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]
