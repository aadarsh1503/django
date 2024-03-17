from django.contrib import admin

from .models import *

admin.site.register(Receipe)
admin.site.register(Student)
admin.site.register(Studentid)
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Rating)

class SubjectMarkAdmin(admin.ModelAdmin):
 list_display=['student' , 'subject', 'marks']

admin.site.register(SubjectMarks , SubjectMarkAdmin)

class ReportRankAdmin(admin.ModelAdmin):
 
  list_display=['student' , 'date_of_report_card_generation']
admin.site.register(ReportRank , ReportRankAdmin) 