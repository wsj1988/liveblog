# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.core import serializers
from django.http import HttpResponse
from models import Update

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/update_list.html'
    model = Update

def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = 'text/javascript'
    response.write(serializers.serializer('json', Update.objects.filter(pk__gt=id)))
    return response
