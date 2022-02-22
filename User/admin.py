from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(accountsCheck)

class userAddressAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'user','address', 'city','state','zip','tag','is_dataRetrived')

class addressDetailsAdmin(admin.ModelAdmin):
    list_display = ('number', 'address')

class detailsTagsAdmin(admin.ModelAdmin):
    list_display = ('user', 'addressDetails')

admin.site.register(userAddress,userAddressAdmin)
admin.site.register(addressDetails,addressDetailsAdmin)
admin.site.register(addressDetailsTags)
admin.site.register(detailsTags,detailsTagsAdmin)