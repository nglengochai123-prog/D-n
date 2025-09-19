from django.contrib import admin
class BookrAdminSite(admin.AdminSite):
 title_header = 'Bookr'
 site_header = 'Bookr administration'
 index_title = 'Bookr site admin'