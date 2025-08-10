from django.contrib import admin
from .models import *

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ['region', 'district', 'city', 'street', 'house_number']
    list_display_links = ['region', 'district', 'city', 'street', 'house_number']
    list_filter = ['region', 'city']
    search_fields = ['region', 'city']
    list_per_page = 10


@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ['name_organization', 'inn_organization', 'type_organization']
    list_display_links = ['name_organization', 'inn_organization', 'type_organization']
    list_filter = ['type_organization']
    search_fields = ['name_organization']
    list_per_page = 10

@admin.register(Structures)
class StructuresAdmin(admin.ModelAdmin):
    list_display = ['name_structure', 'adress_structure']
    list_display_links = ['name_structure', 'adress_structure']
    list_filter = ['name_structure', 'adress_structure']
    search_fields = ['name_structure', 'adress_structure']
    list_per_page = 10

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ['parallel_class', 'name_class', 'name_structure']
    list_display_links = ['parallel_class', 'name_class', 'name_structure']
    list_filter = ['parallel_class', 'name_structure']
    list_per_page = 10

@admin.register(Publishings)
class PublishingsAdmin(admin.ModelAdmin):
    list_display = ['name_publishing']
    list_display_links = ['name_publishing']
    list_filter = ['name_publishing']
    search_fields = ['name_publishing']
    list_per_page = 10

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['name_author', 'name_coauthor']
    list_display_links = ['name_author', 'name_coauthor']
    list_filter = ['name_author']
    search_fields = ['name_author']
    list_per_page = 10

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id_book','name_book', 'author_book', 'category_book', 'publishing_book', 'publishing_yearv', 'name_structure']
    list_display_links = ['id_book','name_book', 'author_book', 'category_book', 'publishing_book', 'publishing_yearv', 'name_structure']
    list_filter = ['author_book', 'publishing_book', 'category_book', 'publishing_yearv']
    search_fields = ['name_book', 'author_book']
    list_per_page = 10

@admin.register(UsersLibrary)
class UsersLibraryAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'last_name_user', 'first_name_user', 'patronymic_user', 'phone_user', 'mail_user', 'name_class', 'status_user', 'classroom_teacher', 'name_structure']
    list_display_links = ['id_user', 'last_name_user', 'first_name_user', 'patronymic_user', 'phone_user', 'mail_user', 'name_class', 'status_user', 'classroom_teacher', 'name_structure']
    list_filter = ['status_user']
    search_fields = ['last_name_user']
    list_per_page = 10

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = []
#     list_display_links = []
#     list_filter = []
#     search_fields = []
#     list_per_page = 20
