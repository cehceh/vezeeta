from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
gender_choices=[
    ('M','Male'),
    ('F','Female')
]
specialist=[
    ('جلدية','جلدية'),
    ('اسنان','اسنان'),
    ('نفسي','نفسي'),
    ('اطفال حديثي الولادة','اطفال حديثي الولادة'),
    ('مخ واعصاب','مخ واعصاب'),
    ('عظام','عظام'),
    ('نساء وتوليد','نساء وتوليد'),
    ('انف واذن وحنجرة','انف واذن وحنجرة'),
    ('قلب واوعية دموية','قلب واوعية دموية'),
    ('امراض دم','امراض دم'),
    ('اورام','اورام'),
    ('باطنه','باطنه'),
    ('تخسيس وتغذية','تخسيس وتغذية'),
    ('جراحة اطفال','جراحة اطفال'),
    ('جراحة اورام','جراحة اورام'),
    ('جراحة اوعية دموية','جراحة اوعية دموية'),
    ('جراحة تجميل','جراحة تجميل'),
    ('جراحه سمنة ومناظير','جراحه سمنة ومناظير')
]
class doctor_profile_1(models.Model):
    #user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=1000,null=True,blank=True)
    gender= models.CharField(max_length=5,choices=gender_choices)
    specialist_doctor= models.ForeignKey('category', related_name='doctor_category', on_delete=models.CASCADE,blank=True,null=True)
    desription=models.TextField(max_length=5000,null=True,blank=True)
    address1 = models.ForeignKey('place', related_name='doctor_place', on_delete=models.CASCADE)
    price=models.IntegerField(null=True,blank=True)
    waiting_time=models.FloatField(max_length=5,null=True,blank=True)
    opening_hours=models.IntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=30,blank=True, null=True)
    doctor_image=models.ImageField(upload_to='doctor_photo/')
    slug=models.SlugField(blank=True,null=True,max_length=50)
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)   
        super(doctor_profile_1, self).save(*args, **kwargs) # Call the real save() method
#def  user_created(sender,**kwargs):
#    if kwargs['created']:
 #       doctor_profile.objects.create(user=kwargs['instance'])
#post_save.connect(doctor_profile,sender=User)
class category(models.Model):
    speialists=models.CharField( max_length=50,choices=specialist)
    def __str__(self):
        return self.speialists
class place(models.Model):
    location=models.CharField( max_length=50,blank=True, null=True)
    

    class Meta:
        verbose_name = ("place")
        verbose_name_plural = ("places")

    def __str__(self):
        return self.location
