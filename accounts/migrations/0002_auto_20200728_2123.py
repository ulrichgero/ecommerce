# Generated by Django 3.0.4 on 2020-07-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Seller', 'verbose_name_plural': 'Sellers'},
        ),
        migrations.AddField(
            model_name='seller',
            name='store_description',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='seller',
            name='store_name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
