# Generated by Django 3.0.5 on 2020-10-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member_inno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(max_length=50)),
                ('address_line1', models.CharField(max_length=100, null=True)),
                ('address_line2', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=45, null=True)),
                ('pin', models.IntegerField()),
                ('country', models.CharField(max_length=45, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapp.Member_inno')),
            ],
        ),
    ]