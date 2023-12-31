# Generated by Django 4.2.5 on 2023-12-09 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название брэнда')),
                ('description', models.TextField(default='Нет описания')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('contacts', models.CharField(max_length=100, verbose_name='Контакты')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brands')),
                ('workers', models.ManyToManyField(blank=True, related_name='client', to='worker.worker')),
            ],
        ),
    ]
