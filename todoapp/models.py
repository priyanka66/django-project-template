from django.db import models

TASK_STATUS = ((0, "Pending"),
               (1, "Completed"))
TASK_PRIORITY = ((0, "High"),
               (1, "Low")) 

TASK_VISIBILITY = ((1, "Private"),
                 (0, "Public"))

class user(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_password = models.CharField(max_length=20)
    def __unicode__(self):
        return (self.user_name,self.user_email)
    
    
class task(models.Model):
    task_name = models.CharField(max_length=200) 
    task_description = models.CharField(max_length=200)
    task_status = models.IntegerField(choices=TASK_STATUS, default=0)
    task_priority = models.IntegerField(choices=TASK_PRIORITY, default=1) 
    task_visibility = models.IntegerField(choices=TASK_VISIBILITY, default=0)
    user_name = models.ForeignKey(user)
    
    def __unicode__(self):
        return (self.task_name,self.task_description,self.task_priority,self.task_status,self.task_visibility)
    
    

