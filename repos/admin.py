from django.contrib import admin
from repos.models import Repo

class RepoAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'last_update')

admin.site.register(Repo, RepoAdmin)
