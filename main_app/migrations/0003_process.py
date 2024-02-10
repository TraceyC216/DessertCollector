# Generated by Django 4.2.9 on 2024-02-04 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_dessert_allergens_dessert_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('step', models.CharField(choices=[('R', 'Check Recipe'), ('I', 'Buy Ingredients')], default='R', max_length=1)),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dessert')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
