from django.contrib import admin
from .models import User,Category,Product,Regiter

"""
CREDENTIALS{
    Username: admin
    password: admin2023
}
"""

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Regiter)
