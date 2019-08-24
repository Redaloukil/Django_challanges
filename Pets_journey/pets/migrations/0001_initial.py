# Generated by Django 2.1.1 on 2019-08-24 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.Pet')),
            ],
            bases=('pets.pet',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pets.Pet')),
            ],
            bases=('pets.pet',),
        ),
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owners.Owner'),
        ),
    ]
