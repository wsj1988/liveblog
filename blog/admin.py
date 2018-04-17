# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib import admin
from models import Update

# Register your models here.
class UpdateAdmin(admin.ModelAdmin):
    def Meta(self):
        model = Update

admin.site.register(Update, UpdateAdmin)
