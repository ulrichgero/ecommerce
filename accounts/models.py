from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from django.utils import timezone





# Create your models here.


#user model --> using AbstractBaseUser
class MyUser(AbstractUser):
	USER_TYPE_CHOICES = (
		('Admin', 'ADMIN'),
		('Editor', 'EDITOR'),
		('Seller', 'SELLER'),
		('Manager', 'MANAGER'), 
	)
	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, blank=True, default=True)
	name = models.CharField(_("Name of User"), blank=True, max_length=225)

	def get_absolute_url(self):
		return reverse("accounts:detail", kwargs={"username": self.username})
 