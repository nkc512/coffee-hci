from django.contrib import admin
from .models import Blend,Profile_Review,Profile,Batch,Gen_Review,TasteProfile

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blend,AuthorAdmin)
admin.site.register(Profile_Review,AuthorAdmin)
admin.site.register(Profile,AuthorAdmin)
admin.site.register(Batch,AuthorAdmin)
admin.site.register(Gen_Review,AuthorAdmin)
admin.site.register(TasteProfile,AuthorAdmin)
