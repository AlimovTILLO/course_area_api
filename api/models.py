from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class  SubCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, on_update=models.SET_NULL)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.title

class City(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, verbose_name="Slug")

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name="Course")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    description = models.CharField(max_length=255, verbose_name="Description")
    category = models.ForeignKey(Category, blank=True, null=True , on_delete=models.SET_NULL, on_update=models.SET_NULL)
    sub_category = models.ForeignKey(SubCategory, blank=True, null=True , on_delete=models.SET_NULL, on_update=models.SET_NULL)
    city = models.ForeignKey(City, blank=True, null=True , on_delete=models.SET_NULL, on_update=models.SET_NULL)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title
