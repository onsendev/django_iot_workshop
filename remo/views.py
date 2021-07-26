from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET

from remo.modules.api import NatureRemoApi
from remo.modules.wbgt import Wbgt

from .models import SensorValue

# /remo/dashboard
@require_GET
def dashboard(request):
    pass

# /remo/invoke/<str:action_name>
@require_POST
def invoke(request, action_name):
    pass
