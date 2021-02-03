# Generated by Django 2.2.17 on 2021-02-02 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('individu', '0005_remove_individu_statut'),
    ]

    operations = [
        migrations.AddField(
            model_name='individu',
            name='STATUT',
            field=models.ForeignKey(db_column='RefID_Statut', default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='individu.Statut'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statut',
            name='ID',
            field=models.AutoField(db_column='ID_Statut', primary_key=True, serialize=False),
        ),
    ]