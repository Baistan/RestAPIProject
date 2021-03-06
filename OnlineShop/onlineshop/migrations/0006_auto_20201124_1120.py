# Generated by Django 3.1.3 on 2020-11-24 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0005_producttoorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttoorder',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_order', to='onlineshop.order'),
        ),
        migrations.RemoveField(
            model_name='producttoorder',
            name='products',
        ),
        migrations.AddField(
            model_name='producttoorder',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='onlineshop.product'),
        ),
    ]
