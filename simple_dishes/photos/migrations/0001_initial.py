# Generated by Django 4.1 on 2023-06-22 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='хавчик', max_length=50)),
                ('photo', models.ImageField(upload_to='for_gallery')),
            ],
        ),
    ]
