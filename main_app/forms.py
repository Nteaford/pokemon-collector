from django.forms import ModelForm
from .models import GymBadge

class GymBadgeForm(ModelForm):
  class Meta:
    model = GymBadge
    fields = ['badge']