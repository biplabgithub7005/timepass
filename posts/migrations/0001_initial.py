# Generated by Django 2.2.1 on 2019-07-11 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='post.png', upload_to='posts')),
                ('file', models.FileField(default='video', upload_to='files')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Signup')),
            ],
        ),
    ]
