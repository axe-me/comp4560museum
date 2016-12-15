# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-15 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.AutoField(max_length=255, primary_key=True, serialize=False)),
                ('eventDate', models.DateTimeField(null=True)),
                ('verbatimEventDate', models.CharField(max_length=255, null=True)),
                ('habitat', models.CharField(max_length=255, null=True)),
                ('samplingProtocol', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('identificationID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('identifiedBy', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.AutoField(max_length=255, primary_key=True, serialize=False)),
                ('stateProvince', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('municipality', models.CharField(max_length=255, null=True)),
                ('locality', models.CharField(max_length=255, null=True)),
                ('verbatimElevation', models.CharField(max_length=30, null=True)),
                ('minimumElevationInMeters', models.CharField(max_length=30, null=True)),
                ('verbatimCoordinates', models.CharField(max_length=255, null=True)),
                ('verbatimLatitude', models.CharField(max_length=100, null=True)),
                ('verbatimLongitude', models.CharField(max_length=100, null=True)),
                ('verbatimCoordinateSystem', models.CharField(max_length=100, null=True)),
                ('verbatimSRS', models.CharField(max_length=100, null=True)),
                ('decimalLatitude', models.FloatField(null=True)),
                ('decimalLongitude', models.FloatField(null=True)),
                ('geodeticDatum', models.CharField(max_length=100, null=True)),
                ('coordinateUncertaintyInMeters', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('occurrenceID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('bibliographicCitation', models.CharField(max_length=100, null=True)),
                ('datasetName', models.CharField(max_length=100, null=True)),
                ('collectionCode', models.CharField(max_length=100, null=True)),
                ('catalogNumber', models.CharField(max_length=100, null=True)),
                ('occurenceRemarks', models.CharField(max_length=100, null=True)),
                ('recordNumber', models.CharField(max_length=100, null=True)),
                ('recordedBy', models.CharField(max_length=100, null=True)),
                ('associatedMedia', models.CharField(max_length=100)),
                ('preparations', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=100)),
                ('lifeStage', models.CharField(max_length=100)),
                ('reproductiveCondition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=40, null=True)),
                ('collectionName', models.CharField(max_length=40)),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mzm_api.Event')),
                ('identificationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mzm_api.Identification')),
                ('locationID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mzm_api.Location')),
                ('occurrenceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mzm_api.Occurrence')),
            ],
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('taxonID', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('scientificNameID', models.CharField(max_length=255, null=True)),
                ('acceptedNameUsage', models.CharField(max_length=255, null=True)),
                ('kingdom', models.CharField(max_length=100, null=True)),
                ('phylum', models.CharField(max_length=100, null=True)),
                ('taxon_class', models.CharField(db_column='class', max_length=100, null=True)),
                ('order', models.CharField(max_length=100, null=True)),
                ('family', models.CharField(max_length=100, null=True)),
                ('genus', models.CharField(max_length=100, null=True)),
                ('subgenus', models.CharField(max_length=100, null=True)),
                ('specificEpithet', models.CharField(max_length=100, null=True)),
                ('taxonRank', models.CharField(max_length=100, null=True)),
                ('verbatimTaxonRank', models.CharField(max_length=100, null=True)),
                ('scientificNameAuthorship', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='root',
            name='taxonID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mzm_api.Taxon'),
        ),
    ]
