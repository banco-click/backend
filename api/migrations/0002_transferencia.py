# Generated by Django 3.2.6 on 2021-09-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('destino', models.CharField(max_length=255)),
                ('data', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]