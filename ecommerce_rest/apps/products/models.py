from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class MeasureUnit(BaseModel):
    description = models.CharField('Description', max_length = 50, blank = False, null = False, unique = True)
    historial = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value
    
    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'
    def __str__(self):
        return self.description

class CategoryProduct(BaseModel):
    description = models.CharField('Description', max_length = 50, blank = False, null = False, unique = True)        
    histoical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value
    
    class Meta:
         verbose_name = "Product's category"
         verbose_name_plural = "Products' categories"
    def __str__(self):
        return self.description

class Indicator(BaseModel):
    decount_value = models.PositiveSmallIntegerField(default = 0)
    category_product = models.ForeignKey(CategoryProduct, on_delete = models.CASCADE, verbose_name = 'offertIndicator')
    histoical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value    
    class Meta:
         verbose_name = "Offer's indicator"
         verbose_name_plural = "Offer's indicators"
    def __str__(self):
        return f"Category's offer {self.category_product} : {self.decount_value}%"

class Product(BaseModel):
    name = models.CharField("Product's name", max_length = 150, unique = True, blank = False, null = False)
    description = models.TextField("Product's description", blank=False, null = False)
    image = models.ImageField('path image', upload_to = 'products/', blank = True, null = True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete = models.CASCADE, verbose_name = 'Mesuare Unit', null = True)
    category = models.ForeignKey(CategoryProduct, on_delete = models.CASCADE, verbose_name = 'Category', null = True)
    histoical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.change_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.change_by = value    
    class Meta:
         verbose_name = "Product"
         verbose_name_plural = "Products"
    def __str__(self):
        return self.name