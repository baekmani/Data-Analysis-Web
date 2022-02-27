# Generated by Django 4.0.1 on 2022-02-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, verbose_name='닉네임')),
                ('email', models.CharField(max_length=64, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
            ],
            options={
                'db_table': 'account',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]
