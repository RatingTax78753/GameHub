# Generated by Django 5.0.6 on 2024-09-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suporte', '0002_delete_termodeusoeprivacidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='simbolo',
            field=models.ImageField(blank=True, null=True, upload_to='Suporte/Topico/'),
        ),
    ]
