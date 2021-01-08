# Generated by Django 3.1.5 on 2021-01-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100)),
                ('PRDDesc', models.TextField()),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PRDCreated', models.DateTimeField()),
            ],
        ),
    ]
