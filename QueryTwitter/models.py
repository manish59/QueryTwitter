from django.db import models

class QueryHashTag(models.Model):
    HashTag=models.CharField(max_length=1000,primary_key=True,db_column='HashTag')
    TimeStamp=models.DateTimeField(auto_now=True,db_column='TimeStamp')
    class Meta:
        verbose_name_plural='QueryHashTag'
        