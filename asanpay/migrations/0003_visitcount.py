# Generated by Django 4.2.1 on 2023-05-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asanpay', '0002_alter_contactmodel_page_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]