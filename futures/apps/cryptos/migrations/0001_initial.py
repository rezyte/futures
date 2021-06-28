# Generated by Django 3.2.4 on 2021-06-28 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('acro', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair_name', models.CharField(blank=True, max_length=20, null=True)),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_pair', related_query_name='fist_pair', to='cryptos.coin')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fsecond_pair', related_query_name='second_pair', to='cryptos.coin')),
            ],
        ),
    ]