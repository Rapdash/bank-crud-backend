# Generated by Django 3.0 on 2019-12-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191206_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit')], max_length=10),
        ),
    ]
