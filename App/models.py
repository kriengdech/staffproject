from django.db import models



 

class Staff(models.Model):
    GENDER = (
        ('ชาย','ชาย'),
        ('หญิง','หญิง'),        
    )
    title_list=(('ดช.','ดช.'),
                ('ดญ.','ดญ.'),
                ('นาย','นาย'),
                ('นส.','นส.'))
    bloodchoices=(('A','A'),
                ('B','B'),
                ('O','O'),
                ('AB','AB'))    
    title = models.CharField(max_length=6,null=True,choices=title_list)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)  
    mobile = models.CharField(max_length=20)
    card_id_no = models.CharField(max_length=20)
    birthdate = models.DateField(null=False,blank=False)   
    age = models.CharField(max_length=3)
    bloodgrp = models.CharField(max_length=5,choices=bloodchoices)
    gender = models.CharField(max_length=5,null=True,choices=GENDER)
    email = models.CharField(max_length=30)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name  
