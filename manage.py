#-------------------------------commit id---------------------------------------#

62e1eef54353e4a1500519930f2cee8ab2cd5101

#--------------------------------models.py---------------------------------------#
from django.db import models

class Restaurant(models.Model):
    '''
    Add has_delivery field into Restaurant model
    '''
    has_delivery  = models.BooleanField(default=False)

#-------------------------------------------------------------------------------#
