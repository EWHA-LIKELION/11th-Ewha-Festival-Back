# Generated by Django 3.0.8 on 2023-04-28 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('college', models.CharField(choices=[('교육관', '교육관'), ('대강당', '대강당'), ('신세계관', '신세계관'), ('생활관', '생활관'), ('정문', '정문'), ('포스코관', '포스코관'), ('학문관', '학문관'), ('후윳길', '후윳길')], max_length=20)),
                ('name', models.TextField()),
                ('number', models.CharField(blank=True, max_length=10)),
                ('thumnail', models.TextField(blank=True, null=True)),
                ('opened', models.BooleanField(default=False)),
                ('time', models.TextField(default='10:00 ~ 17:00')),
                ('hashtag', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('음식', '음식'), ('굿즈', '굿즈'), ('체험', '체험'), ('기타', '기타')], max_length=5)),
                ('date', models.IntegerField(choices=[(10, 10), (11, 11), (12, 12)], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일')], max_length=5)),
                ('date', models.IntegerField(choices=[(10, 10), (11, 11), (12, 12)])),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notices', to='booth.Booth')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('is_soldout', models.BooleanField(default=False)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='booth.Booth')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.TextField()),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='booth.Booth')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='booth.Booth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booth',
            name='category',
            field=models.ManyToManyField(related_name='booths', to='booth.Category'),
        ),
        migrations.AddField(
            model_name='booth',
            name='day',
            field=models.ManyToManyField(related_name='booths', to='booth.Day'),
        ),
        migrations.AddField(
            model_name='booth',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='booths', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booth',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
