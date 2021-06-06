# Generated by Django 3.2.3 on 2021-06-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_bankaccount_company_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='company_id',
        ),
        migrations.AddField(
            model_name='company',
            name='bank_accounts',
            field=models.ManyToManyField(to='company.BankAccount'),
        ),
    ]
