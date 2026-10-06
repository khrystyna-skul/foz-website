from django.contrib import admin
from .models import FacultyInfo, Department, Specialty, Teacher

@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_name')
    search_fields = ('name', 'head_name')

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'coordinator_name')
    list_filter = ('department',)
    search_fields = ('name', 'code', 'coordinator_name')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'position', 'degree')