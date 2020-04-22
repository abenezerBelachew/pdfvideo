# Generated by Django 3.0.5 on 2020-04-22 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('youtube_link', models.URLField(blank=True, null=True)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
    ]
