# Generated by Django 2.1.2 on 2019-04-08 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSCompeteAPI', '0002_auto_20190408_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.User'),
        ),
    ]
