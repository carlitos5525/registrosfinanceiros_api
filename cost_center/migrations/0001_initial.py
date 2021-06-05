# Generated by Django 3.2.3 on 2021-06-02 00:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'Centro de Custo',
                'verbose_name_plural': 'Centros de Custo',
            },
        ),
    ]