from django.contrib import admin
from authentication.models import Userinfo

# Register your models here.


@admin.register(Userinfo)


class UserInfo(admin.ModelAdmin):
    list_display =Userinfo.DisplayFields
    search_fields=Userinfo.SearchablFields



