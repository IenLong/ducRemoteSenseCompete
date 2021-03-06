# Generated by Django 2.1.2 on 2019-04-05 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField()),
                ('dataset', models.CharField(max_length=128)),
                ('rule', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.IntegerField()),
                ('score', models.FloatField()),
                ('is_review', models.BooleanField()),
                ('competition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=32, unique=True)),
                ('captain_name', models.CharField(max_length=32)),
                ('competition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('work_id', models.IntegerField(choices=[(1, '院所'), (2, '公司'), (3, '学校'), (4, '个人')])),
                ('work_place', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('ID_card', models.CharField(max_length=18, unique=True)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('is_captain', models.BooleanField(verbose_name='是否为队长')),
                ('competition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.Competition')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.Team')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.Team'),
        ),
        migrations.AddField(
            model_name='result',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RSCompeteAPI.User'),
        ),
    ]
