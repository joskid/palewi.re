from django.contrib import admin

from models import Link

class LinkAdmin(admin.ModelAdmin):
    model = Link
    extra = 3

admin.site.register(Link, LinkAdmin)
