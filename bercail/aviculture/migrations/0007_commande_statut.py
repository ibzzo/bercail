# Generated by Django 4.1 on 2023-06-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviculture', '0006_remove_commande_prenom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='statut',
            field=models.CharField(default='En attente', max_length=100),
        ),
    ]
