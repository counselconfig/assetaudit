from django.db import models

class Post(models.Model):
    Reference_No = models.CharField(max_length=8)
    Serial_No = models.CharField(max_length=20)    
    CMDB_item_type = models.CharField(max_length=20) 
    User_name= models.CharField(max_length=50)   
    Email_address = models.EmailField(50)  
    Organisation = models.CharField(max_length=60)