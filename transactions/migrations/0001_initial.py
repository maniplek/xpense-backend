# Generated by Django 4.0 on 2021-12-24 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('expenses', '0001_initial'),
        ('income', '0001_initial'),
        ('accounts', '0001_initial'),
        ('users', '0006_user_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amout_limit', models.IntegerField(blank=True, default=200000)),
                ('default_currency', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='expenses.expense')),
                ('income', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='income.income')),
            ],
        ),
    ]
