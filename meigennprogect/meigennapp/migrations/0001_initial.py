# Generated by Django 3.0.3 on 2020-11-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeigennModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(choices=[('danger', '令和'), ('danger', '平成'), ('danger', '昭和'), ('danger', '大正'), ('danger', '明治')], max_length=50)),
                ('memo', models.TextField(max_length=200)),
                ('duedate', models.DateField()),
            ],
        ),
    ]
