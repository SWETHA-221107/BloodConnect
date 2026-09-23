from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BloodRequest(models.Model):
    requester_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    hospital = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.requester_name
    