from django.db import models

# Create your models here.
import os
from django.conf import settings

UPLOAD_DIR = os.path.join(settings.BASE_DIR, 'media/uploads')

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)
