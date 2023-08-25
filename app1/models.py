from django.db import models

class Customer_details(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)

class product_details(models.Model):
    img=models.ImageField(max_length=30)
    alt=models.CharField(max_length=20,unique=True)
    small_des=models.TextField()
    big_des=models.TextField()
    price=models.CharField(max_length=50)
    s_icon=models.CharField(max_length=50)
    c_icon=models.CharField(max_length=50)
    category=models.CharField(max_length=50)

class store_details(models.Model):
    username=models.CharField(max_length=50)
    img=models.ImageField(max_length=30)
    alt=models.CharField(max_length=20)
    small_des=models.TextField()
    big_des=models.TextField()
    price=models.CharField(max_length=50)
    s_icon=models.CharField(max_length=50)
    c_icon=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    score=models.IntegerField()

    class Meta:
        unique_together=('username','alt')

class course_page(models.Model):
    alt=models.CharField(max_length=20)
    f_1=models.CharField(max_length=100)
    s_2=models.CharField(max_length=100)
    t_3=models.CharField(max_length=100)
    f_4=models.CharField(max_length=100)
    f_5=models.CharField(max_length=100)
    s_6=models.CharField(max_length=100)
    s_7=models.CharField(max_length=100)
    l_1=models.CharField(max_length=1500)
    l_2=models.CharField(max_length=100)
    l_3=models.CharField(max_length=1500)
    l_4=models.CharField(max_length=1500)
    l_5=models.CharField(max_length=1500)
    l_6=models.CharField(max_length=1500)
    l_7=models.CharField(max_length=1500)


class test(models.Model):
    alt=models.CharField(max_length=20)
    q_n=models.CharField(max_length=50)

class score(models.Model):
    username=models.CharField(max_length=50)
    alt=models.CharField(max_length=20)
    score=models.IntegerField()

# Create your models here.
