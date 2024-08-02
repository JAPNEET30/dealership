from tkinter import Frame
from unittest.util import _MAX_LENGTH
from django.db import models
from django.template import Engine
from usercore.models import businessid

#Constants
choices={'Sold_to_Customer':'sold_customer','Sold_to_dealership':'sold_dealer',
'In_Warehouse':'in_stock'}
factory_status = models.CharField(choices={'unknown':'unknown','waiting for delivery':'waiting for delivery',
'received':'received'}, max_length=30)

#classes
class categories(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=50)
    other = models.JSONField()
    is_accessories_included = models.BooleanField()
    accessories = models.JSONField(blank=True, null=True)

class locations(models.Model):
    businessid=models.ForeignKey(to=businessid, on_delete=models.PROTECT, default=0)
    name = models.CharField(max_length=20)
    tag = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=20, choices={'Storage':'storage','Point Of Sale':'point_of_sale', 'Both':'both'})

class vehicle_entry(models.Model):
    invoice_no = models.CharField(max_length=50)
    invoice_date = models.DateField()
    businessid = models.ForeignKey(to=businessid, on_delete=models.PROTECT, default=0)
    model_name = models.CharField(max_length=50)
    varient = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    frame_no = models.CharField(max_length=40, blank=True, unique=True)
    engine_no = models.CharField(blank=True, default=0, max_length=40, unique=True)
    is_damaged = models.BooleanField(max_length=40, default=True)
    status = models.CharField(max_length=20)
    date_of_delivery = models.DateTimeField(blank=True)
    date_of_sale = models.DateTimeField()
    storage_location = models.CharField(max_length=50)
    timestamp_of_entry = models.DateTimeField()

class stock(models.Model):
    businessid = models.ForeignKey(to=businessid, default = 0, on_delete=models.PROTECT)
    frame_no = models.CharField(max_length=40)
    location = models.CharField(max_length=50)

class accessories(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    frame_no = models.CharField(max_length=40)
    accessories = models.JSONField()

class damaged(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    frame_no = models.OneToOneField(to=vehicle_entry, default=0, on_delete=models.PROTECT)
    image = models.JSONField()

class incoming_vehicles(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    frame_no = models.CharField(max_length=50)
    seller = models.CharField(max_length=50, default='Factory')
    delivery_data = models.DateField(verbose_name='Delivery Date')
    invoice_no = models.CharField(max_length=50)
    invoice_date = models.DateField()

class outgoing_vehicles(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    frame_no=models.CharField(max_length=50)
    engine_no=models.CharField(max_length=50)
    is_delivered = models.BooleanField(default=False)
    receiving_party = models.CharField(max_length=100)
    damage_report = models.CharField(max_length=100)

class vehicle_log(models.Model):
    businessid = models.ForeignKey(to=businessid, default=0, on_delete=models.PROTECT)
    frame_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    operation = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    