from django.contrib import admin
from webapp.models import contact,ResumeModel

class contactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject', 'message']
    
    
admin.site.register(contact, contactAdmin)


#=========================#
#This section is creating the CV table
#=========================#

admin.site.register(ResumeModel)