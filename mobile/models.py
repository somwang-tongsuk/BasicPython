from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=120)
	product_desc = models.TextField(null=True)

	def __str__(self):
		return self.product_name #ดึงตัวแปลข้างนอกมาใช้งานได้

class EMS(models.Model):
	ems_number = models.CharField(max_length=120)
	ems_name = models.CharField(max_length=120)

	def __str__(self):
		return 'Name: {} EMS: {}'.format(self.ems_name,self.ems_number)