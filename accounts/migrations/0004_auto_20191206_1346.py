# Generated by Django 3.0 on 2019-12-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('WITH', 'Withdrawal'), ('DEPS', 'Deposit')], max_length=10),
        ),
    ]
