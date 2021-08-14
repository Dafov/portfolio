from portfolio.portfolio_projects.models import Project
from django.contrib import admin

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    # list_display = ('title', 'likes_count')
    list_display = ('title', )
    list_filter = ('title', )

    # def likes_count(self, obj):
    #     return obj.like_set.count()


admin.site.register(Project, ProjectAdmin)