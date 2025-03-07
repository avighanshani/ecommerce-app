from django.db import models

# Create your views here.
# models.py will be minimal since we're using Python data structures
class Booking:
    def __init__(self, name, email, date, service_type, status="pending"):
        self.name = name
        self.email = email
        self.date = date
        self.service_type = service_type
        self.status = status
