from django.db import models


# Create your models here.

class BaseTable(models.Model):
    tableName = models.CharField(max_length=500, db_column='tableName', primary_key='tableName')
    db = models.IntegerField(default=1, db_column='db')
    size = models.IntegerField(default=1, db_column='size')

    class Meta:
        db_table = 'base_table'
