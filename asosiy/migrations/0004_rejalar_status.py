# Generated by Django 4.1.1 on 2022-09-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0003_rejalar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejalar',
            name='status',
            field=models.CharField(default='Yangi', max_length=12),
        ),
    ]
