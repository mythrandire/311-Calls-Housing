# Generated by Django 3.0 on 2019-12-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maphousing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criteria',
            name='criteria',
            field=models.CharField(choices=[('Noise', 'Noise Complaints'), ('Water System', 'Water Issues'), ('Electrical', 'Electrical Problems'), ('Rodent', 'Rodent Infestation'), ('Hazardous Materials', 'Hazards'), ('Asbestos', 'Asbestos on Site')], max_length=255),
        ),
    ]
