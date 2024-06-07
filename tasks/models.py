from django.db import models

# User models.
class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  SUPER_ADMIN = 'superadmin'
  END_USER = 'enduser'
  ADMIN = 'admin'
  user_type = ((ADMIN, 'admin'), (SUPER_ADMIN, 'superadmin'), (END_USER, 'enduser'))

  def __str__(self) :
     return self.username  
  
#End of User models.

# Project models.
class Project(models.Model):
  project_id = models.AutoField(primary_key=True)
  project_name = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  def __str__(self) :
     return self.project_name
#End of User models.

# Task models.
class Task(models.Model):
  task_id = models.AutoField(primary_key=True)
  task_name = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
  # Assuming foreign key for user who created the task
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  due_time = models.DateTimeField(blank=True, null=True)
  # Assuming a choices field for repeated or one-time task
  REPEATED = 'repeated'
  ONE_TIME = 'onetime'
  task_type_choices = ((REPEATED, 'Repeated'), (ONE_TIME, 'One-time'))
  task_type = models.CharField(max_length=10, choices=task_type_choices, default=ONE_TIME)

  def __str__(self) :
     return self.task_name
#End of Task models.

# TimeRecord models.
class TimeRecord(models.Model):
  time_record_id = models.AutoField(primary_key=True)
  task = models.ForeignKey(Task, on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  def __str__(self) :
     return  f"Time Record #{self.time_record_id}"
#End of TimeRecord models.