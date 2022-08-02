from django.db import models

# Create your models here.
class approvals(models.Model):
    GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
    MARRIED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
    GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
    SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
    PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    dependants=models.IntegerField(default=0)
	

    def __str__(self):
	    return '{}, {}'.format(self.lastname, self.firstname)