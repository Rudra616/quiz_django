from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)

class AnswerAdmin(admin.StackedInline):
    model = Ans
    extra = 1

class questionadmin(admin.ModelAdmin):
    inlines = [AnswerAdmin] 

admin.site.register(Question ,questionadmin)
admin.site.register(Ans)