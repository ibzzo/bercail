# Generated by Django 4.1 on 2023-06-01 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prevention', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Poultry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('productivity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('poultry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviculture.poultry')),
            ],
        ),
        migrations.CreateModel(
            name='PoultryDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviculture.disease')),
                ('poultry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviculture.poultry')),
            ],
        ),
        migrations.AddField(
            model_name='poultry',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviculture.species'),
        ),
        migrations.CreateModel(
            name='Egg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('poultry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviculture.poultry')),
            ],
        ),
    ]
