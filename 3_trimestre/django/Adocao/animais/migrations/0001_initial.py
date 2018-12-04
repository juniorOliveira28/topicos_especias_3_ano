# Generated by Django 2.0.6 on 2018-12-04 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('raca', models.CharField(max_length=52)),
                ('idade', models.CharField(max_length=52)),
                ('porte', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(help_text='Informe apenas a sigla', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome Completo', max_length=50)),
                ('emails', models.CharField(max_length=50)),
                ('nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animais.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animais.Tipo'),
        ),
    ]
