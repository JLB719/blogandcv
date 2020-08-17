from django.db import models

# Create your models here.
class SkillItem(models.Model) :
    text = models.TextField(default='')

class AchItem(models.Model) :
    text = models.TextField(default='')

class NameItem(models.Model) :
    text = models.TextField(default='')

class NumberItem(models.Model) :
    text = models.TextField(default='')
class EmailItem(models.Model) :
    text = models.TextField(default='')
class PersonalProfileItem(models.Model) :
    text = models.TextField(default='')

class WorkExperience(models.Model) :
    company = models.TextField(default='')
    role = models.TextField(default = '')
    startdate = models.TextField(default = '')
    enddate = models.TextField(default='')
    description = models.TextField(default='')

class School(models.Model) :
    school = models.TextField(default='')
    startdate = models.TextField(default='')
    enddate = models.TextField(default='')
    qualifications = models.TextField(default = '')

class Qualifications(models.Model) :
    text = models.TextField(default='')

class Projects(models.Model):
    title = models.TextField(default='')
    description=models.TextField(default='')

class Notes(models.Model) :
    note=models.TextField(default='')
