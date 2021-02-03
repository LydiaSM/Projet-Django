# Generated by Django 2.2.17 on 2021-02-02 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('individu', '0006_auto_20210202_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupe',
            name='ID',
            field=models.AutoField(db_column='ID_Groupe', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='individu',
            name='GROUPE',
            field=models.ForeignKey(db_column='RefID_Groupe', on_delete=django.db.models.deletion.DO_NOTHING, to='individu.Groupe'),
        ),
    ]
