from django.contrib import admin
from core.models import Brands, Clients
from worker.models import Worker



admin.site.register(Brands)
admin.site.register(Worker)
admin.site.register(Clients)
