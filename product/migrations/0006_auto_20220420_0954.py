# Generated by Django 3.0.1 on 2022-04-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_item_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BOOK', 'BOOK'), ('ELECTRONIC', 'ELECTRONIC'), ('CLOTHES', 'CLOTHES')], default='BOOK', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='state',
        ),
        migrations.AddField(
            model_name='item',
            name='state_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.CategoryItem'),
        ),
    ]
