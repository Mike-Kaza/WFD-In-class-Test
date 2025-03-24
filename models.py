from django.db import models

#Salesperson

class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

#Car

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    car_for_sale = models.BooleanField(default=True)

#Customer

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

#Invoice

class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)  
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    salesperson_id = models.ForeignKey(Salesperson, on_delete=models.CASCADE)  

#Service_Ticket

class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)  
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)  
    date_received = models.DateField()

#Mechanic

class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

#Service Mechanic

class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)
    service_ticket_id = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)  
    mechanic_id = models.ForeignKey(Mechanic, on_delete=models.CASCADE) 
    hours = models.IntegerField()

#Parts

class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=100)
    description = models.TextField()

#Parts_used

class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    part_id = models.ForeignKey(Parts, on_delete=models.CASCADE)  
    service_ticket_id = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE) 
    number_used = models.IntegerField()
