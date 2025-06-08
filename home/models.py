# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    bio = models.CharField(max_length=255, null=True, blank=True)
    admin = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Patients(models.Model):

    #__Patients_FIELDS__
    prenom = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    date de naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    numero de telephone = models.CharField(max_length=255, null=True, blank=True)

    #__Patients_FIELDS__END

    class Meta:
        verbose_name        = _("Patients")
        verbose_name_plural = _("Patients")


class Samples(models.Model):

    #__Samples_FIELDS__
    sample type = models.CharField(max_length=255, null=True, blank=True)

    #__Samples_FIELDS__END

    class Meta:
        verbose_name        = _("Samples")
        verbose_name_plural = _("Samples")



#__MODELS__END
