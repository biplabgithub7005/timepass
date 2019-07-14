# Generated by Django 2.2.1 on 2019-07-11 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(default='file title', max_length=100)),
                ('file_path', models.FileField(default='sample.pdf', upload_to='files')),
                ('file_date', models.DateField(auto_now_add=True)),
                ('file_desc', models.CharField(default='This is your file for download click download button', max_length=100)),
            ],
        ),
    ]