from portfolio.portfolio_projects.models import Project
from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('title', )


admin.site.register(Project, ProjectAdmin)