from django.contrib import admin
from myapp.models import staffs

# Register your models here.

class staffsAdmin (admin.ModelAdmin):#員工資料排列順序
    list_display=('id','cName','cPhone','cLine','cpassword')  
admin.site.register(staffs,staffsAdmin)