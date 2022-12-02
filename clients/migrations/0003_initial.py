# Generated by Django 4.1.3 on 2022-12-02 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_delete_client_delete_mocksales'),
    ]

    operations = [
        migrations.CreateModel(
            name='MockSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('information', models.TextField()),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='clients.mocksales')),
            ],
        ),
    ]
