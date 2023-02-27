# Generated by Django 4.0.5 on 2023-02-25 14:21

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='uploads/category/')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True)),
                ('paid_amount', models.IntegerField(blank=True, null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=255)),
                ('payement_intent', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_product', models.IntegerField()),
                ('income', models.IntegerField()),
                ('joined_in', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('digital_product', models.FileField(upload_to='uploads/digital_product/')),
                ('image', models.ImageField(null=True, upload_to='uploads/product_images/')),
                ('video', models.FileField(null=True, upload_to='uploads/videos/')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('sold', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'waitingapproval'), ('active', 'active'), ('deleted', 'deleted')], default='active', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='store.product')),
            ],
        ),
    ]
