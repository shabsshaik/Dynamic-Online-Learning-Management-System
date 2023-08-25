from django.contrib import admin

from app1.models import Customer_details,product_details,store_details,course_page,test,score

class customer_admin(admin.ModelAdmin):
    list_display=('username','email','password')

admin.site.register(Customer_details,customer_admin)

class product_admin(admin.ModelAdmin):
    list_display=('img','alt','small_des','big_des','price','s_icon','c_icon','category')

admin.site.register(product_details,product_admin)


class purchase_admin(admin.ModelAdmin):
    list_display=('username','img','alt','small_des','big_des','price','s_icon','c_icon','category','score')

admin.site.register(store_details,purchase_admin)

class course_admin(admin.ModelAdmin):
    list_display=('alt','f_1','s_2','t_3','f_4','f_5','s_6','s_7','l_1','l_2','l_3','l_4','l_5','l_6','l_7')

admin.site.register(course_page,course_admin)

class test_admin(admin.ModelAdmin):
    list_display=('alt','q_n')

admin.site.register(test,test_admin)

class score_admin(admin.ModelAdmin):
    list_display=('username','alt','score')

admin.site.register(score,score_admin)

# Register your models here.
