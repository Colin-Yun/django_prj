from django.contrib import admin
from .models import Question

# Register your models here.

#admin.site.register(Candidate)

class QustionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QustionAdmin)

