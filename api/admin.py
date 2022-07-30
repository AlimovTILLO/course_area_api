from django.contrib import admin

from .models import Category, SubCategory, School, Course, City


class CourseInline(admin.StackedInline):
    model = Course
    extra = 0


class SchoolAdmin(admin.ModelAdmin):
    inlines = [CourseInline]



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(City)
admin.site.register(School, SchoolAdmin)

