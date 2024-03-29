# Generated by Django 3.2.18 on 2023-04-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reference_No', models.CharField(max_length=8)),
                ('Serial_No', models.CharField(max_length=20)),
                ('CMDB_item_type', models.CharField(max_length=20)),
                ('User_name', models.CharField(max_length=50)),
                ('Email_address', models.EmailField(max_length=254, verbose_name=50)),
                ('Organisation', models.CharField(max_length=60)),
            ],
        ),
    ]
