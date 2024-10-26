from django.contrib import admin
from .models import MyVarity,MyReview,store,MyCertificate

# Register your models here.
class MyReviewInline(admin.TabularInline):
    model=MyReview
    extra=2

class MyVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines=[MyReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('my_varities',)

class MyCertificateAdmin(admin.ModelAdmin):
    list_display=('my','certificate_number')

admin.site.register(MyVarity,MyVarietyAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(MyCertificate,MyCertificateAdmin)
