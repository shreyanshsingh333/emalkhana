from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


maal_type_choices = (
    ('वस्तू', 'वस्तू'),
    ('शराब', 'शराब'),
    ('नशीला पदार्थ', 'नशीला पदार्थ'),
    ('अन्य', 'अन्य'),
)

status_choices = (
    ('in trial', 'in trial'),
    ('completed', 'completed'),
    ('option3', 'option3'),
)

act_choices = (
    ('IPC', 'ipc'),
    ('option2', 'option2'),
    ('option3', 'option3'),
)


class Vivechak(models.Model):
    pradesh = models.CharField(max_length=100, blank=False)
    jila = models.CharField(max_length=100, blank=False)
    vibhag = models.CharField(max_length=100, blank=False)
    unit = models.CharField(max_length=100, blank=False)
    subunit = models.CharField(max_length=100, blank=False)
    pno = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100, blank=False)
    post = models.CharField(max_length=100, blank=False)
    mobile = models.CharField(max_length=100, blank=False)
    adharcard = models.CharField(max_length=20, blank=True, validators=[RegexValidator(regex='^(\d{12})$',
                                                                           message='Enter 12 digits number only.')])
    pancard = models.CharField(max_length=20, blank=True, validators=[RegexValidator(regex='^(.{10})$',
                                                                         message='Length should be 10.')])

    def __str__(self):
        return self.name+'('+self.mobile+')'


class MaalModel(models.Model):
    fir = models.CharField(max_length=100, blank=False)
    thana = models.CharField(max_length=50, blank=False)
    maal_type = models.CharField(max_length=50, blank=False, choices=maal_type_choices)
    if_other = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='maal_images', blank=False)
    seizure_date = models.DateField(blank=False, null=True)
    vivechak = models.ForeignKey(Vivechak, models.SET_NULL, blank=False, null=True)
    under_section = models.CharField(max_length=100, blank=False)
    act = models.CharField(max_length=50, blank=False, choices=act_choices)
    description = models.CharField(max_length=500, blank=False)
    place = models.CharField(max_length=100, blank=False)
    status = models.CharField(max_length=50, blank=False, choices=status_choices)
    court = models.CharField(max_length=100, blank=False)
    date_of_disposal = models.DateField(blank=False, null=True)
