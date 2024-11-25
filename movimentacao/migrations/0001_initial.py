# Generated by Django 5.1.2 on 2024-11-18 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projeto', '0002_remove_produto_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], max_length=1)),
                ('valor_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projeto.produto')),
            ],
        ),
    ]
