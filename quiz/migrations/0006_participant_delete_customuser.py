# Generated by Django 4.2.4 on 2023-08-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_customuser_delete_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='이름')),
                ('student_id', models.CharField(max_length=10, verbose_name='학번')),
                ('phone_num', models.CharField(max_length=13, verbose_name='전화번호')),
                ('score', models.IntegerField(default=0, verbose_name='점수')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
