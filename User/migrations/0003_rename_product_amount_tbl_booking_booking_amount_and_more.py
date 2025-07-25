# Generated by Django 5.1.5 on 2025-02-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_tbl_customise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_booking',
            old_name='product_amount',
            new_name='booking_amount',
        ),
        migrations.RemoveField(
            model_name='tbl_booking',
            name='product_status',
        ),
        migrations.AddField(
            model_name='tbl_booking',
            name='booking_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_cart',
            name='cart_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tbl_booking',
            name='booking_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tbl_cart',
            name='cart_qty',
            field=models.IntegerField(default=1),
        ),
    ]
