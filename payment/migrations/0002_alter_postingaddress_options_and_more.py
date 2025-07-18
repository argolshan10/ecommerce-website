# Generated by Django 5.2 on 2025-07-02 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postingaddress',
            options={'verbose_name_plural': 'Posting Address'},
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='address1',
            new_name='posting_address1',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='address2',
            new_name='posting_address2',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='city',
            new_name='posting_city',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='country',
            new_name='posting_country',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='email',
            new_name='posting_email',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='full_name',
            new_name='posting_full_name',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='state',
            new_name='posting_state',
        ),
        migrations.RenameField(
            model_name='postingaddress',
            old_name='zipcode',
            new_name='posting_zipcode',
        ),
    ]
