from django.db import models
from django.utils import timezone
 
# Create your models here.

month_choices = (
        ("January", 'JANUARY'),
        ("February", 'FEBRUARY'),
        ("March",'MARCH' ),
        ( "April",'APRIL'),
        ("May",'MAY' ),
        ("June",'JUNE' ),
        ("July",'JULY' ),
        ("August",'AUGUST' ),
        ("September",'SEPTEMBER' ),
        ( "October",'OCTOBER'),
        ("November",'NOVEMBER'),
        ( "December", 'DECEMBER')
    )
class HRBP(models.Model):
    excel_reference =  models.FileField(upload_to='HRBP/', 
    help_text='Upload Excel Reference (Note: always clean data and do not change formatting)')

    month = models.CharField(max_length=20, 
    choices=month_choices,
    default='JANUARY',
    help_text='Enter the Month to generate the report')
    """ I deleted the actual fields but description is below:

    I created Image fields for each required report graph generated through matplotlib and added default values, 
    These default values are overwritten everytime a report is generated ( to save memory, but can only handle 1 process since deletion may use the database at the same time)
    This would raise errors as I did not place checks for race conditions
    Specific use only for couple of people using the specific app at one time ( It may work but I haven't done the tests)
    """

    def __str__(self):
        return self.excel_reference.url

 