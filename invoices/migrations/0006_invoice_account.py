# Generated by Django 2.2.3 on 2019-07-29 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_assigned_to'),
        ('invoices', '0005_invoicehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='accounts',
            field=models.ManyToManyField(related_name='accounts_invoices', to='accounts.Account'),
        ),
    ]