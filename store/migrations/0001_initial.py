# Generated by Django 4.1.3 on 2022-11-02 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('payement_method', models.CharField(choices=[('Cash on delivery', 'Cash on deleivery'), ('khalti', 'khalti'), ('esewa', 'esewa')], default='Cash on Delivery', max_length=20)),
                ('payment_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Achham ', 'Achham'), ('Banke', 'Banke'), ('Bhaktapur', 'Bhaktapur'), ('Bhojpur', 'Bhojpur'), ('Dhawalagiri', 'Dhawalagiri'), ('Gorkha ', 'Gorkha'), ('Janakpur ', 'Janakpur '), ('Karnali', 'Karnali'), ('Lumbini', 'Lumbini'), ('Mahakali', 'Mahakali'), ('Mechi', 'Mechi'), ('Narayani', 'Narayani'), ('Rapti', 'Rapti'), ('Sagarmatha', 'Sagarmatha')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('Shoes', 'Shoes'), ('mobile', 'mobile'), ('Laptop', 'Laptop')], max_length=10)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Delivered', 'Delivered')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
