# Generated by Django 4.1.3 on 2022-11-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_customer_payment_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Banke', 'Banke'), ('Bagmati', 'Bagmati'), ('Bheri', 'Bheri'), ('Dhawalagiri', 'Dhawalagiri'), ('Gandaki ', 'Gandaki'), ('Janakpur ', 'Janakpur '), ('Karnali', 'Karnali'), ('koshi', 'koshi'), ('Lumbini', 'Lumbini'), ('Mahakali', 'Mahakali'), ('Mechi', 'Mechi'), ('Narayani', 'Narayani'), ('Rapti', 'Rapti'), ('Sagarmatha', 'Sagarmatha'), ('seti', 'seti')], max_length=50),
        ),
    ]