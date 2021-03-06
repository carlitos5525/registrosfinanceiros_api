# Generated by Django 3.2.3 on 2021-06-02 00:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('cost_center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('due_date', models.DateField()),
                ('pay_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('LT', 'Late'), ('PD', 'Paid'), ('PR', 'Predicted')], max_length=2)),
                ('payment_method', models.CharField(choices=[('B', 'Boleto'), ('CD', 'Cartão de débito'), ('CC', 'Cartão de crédito'), ('TED', 'TED'), ('DOC', 'DOC'), ('PIX', 'PIX'), ('CHQ', 'Cheque'), ('DDA', 'DDA')], max_length=3)),
                ('bank_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.bankaccount')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
        migrations.CreateModel(
            name='Ammount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('type', models.CharField(blank=True, choices=[('F', 'Fixo'), ('V', 'Variavel')], max_length=2, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('cost_center_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cost_center.costcenter')),
                ('finance_register', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_register.register')),
            ],
            options={
                'verbose_name': 'Lançamento',
                'verbose_name_plural': 'Lançamentos',
            },
        ),
    ]
