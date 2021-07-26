from django.core.management.base import BaseCommand
from remo.models import SensorValue
from remo.api import NatureRemoApi

class Command(BaseCommand):
    def handle(self, *args, **options):
        # センサーの値をAPIで取得し、SensorValueモデルを1件新たに保存
        pass
