# Generated by Django 4.2.3 on 2023-08-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Cancelled', 'cancelled'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]