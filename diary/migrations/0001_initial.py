# Generated by Django 3.2.9 on 2021-11-30 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, unique=True)),
                ('password', models.SlugField()),
                ('diaries', models.PositiveIntegerField(default=0)),
                ('completed_diaries', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('japanese_translation', models.TextField()),
                ('english_text', models.TextField()),
                ('image', models.ImageField(blank=True, default='defo', upload_to='documents/')),
                ('completed', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.user')),
            ],
        ),
    ]
