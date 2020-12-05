from django.db import models


# Create your models here.

class BaseTable(models.Model):
    # 数据库字段映射的实体字段=models.类型（max_length=最大长度，db_column=数据库类名 ，primary_key=主键）
    tableName = models.CharField(max_length=500, db_column='tableName', primary_key='tableName')
    db = models.IntegerField(default=1, db_column='db')
    size = models.IntegerField(default=1, db_column='size')

    class Meta:
        # 数据库的表明
        db_table = 'base_table'
