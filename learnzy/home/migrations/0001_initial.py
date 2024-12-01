# Generated by Django 4.2.16 on 2024-12-01 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('instructor_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('video_url', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='photos/%y%m%d')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
    ]