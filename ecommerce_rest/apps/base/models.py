from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id =  models.AutoField(primary_key=True)
    state = models.BooleanField('Status', default=True)
    created_date = models.DateField('created_date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('updated_date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('delete_date', auto_now=True, auto_now_add=False)
    class Meta:
        abstract = True
        verbose_name = 'Base model'
        verbose_name_plural = 'Base models'