# Generated by Django 3.1.2 on 2020-10-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=1000)),
                ('deskripsi', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/%y')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
