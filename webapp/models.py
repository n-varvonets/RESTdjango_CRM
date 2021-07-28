from django.db import models

# Create your models here.


class Employees(models.Model):
    json_data=models.JSONField(default='{}')
    # firstname=models.CharField(max_length=10)
    # lastname=models.CharField(max_length=10)
    # emp_id=models.IntegerField()
    #
    # def __str__(self):
    #     return self.json_data