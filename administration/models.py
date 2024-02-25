from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
# from administration.views import encrypt_aadhar_number


def encrypt_aadhar_number(aadhar_number):
    key = settings.ENCRYPTION_KEY
    cipher_suite = Fernet(key)
    encrypted_aadhar_number = cipher_suite.encrypt(str(aadhar_number).encode())
    return encrypted_aadhar_number.decode()

def decrypt_aadhar_number(encrypted_aadhar_number):
    key = settings.ENCRYPTION_KEY
    cipher_suite = Fernet(key)
    decrypted_aadhar_number = cipher_suite.decrypt(encrypted_aadhar_number.encode())
    return decrypted_aadhar_number.decode()


# Create your models here.
class doctor_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_id = models.CharField(max_length=50, null=True)
    linkedin = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.user.username
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_img", default="profile_pic.png")
    verified = models.BooleanField(default=False)
    aadhar_img = models.ImageField(upload_to="aadhar_img", blank=True)
    aadhar_number = models.BinaryField(blank=True)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.aadhar_number:
            self.aadhar_number = encrypt_aadhar_number(self.aadhar_number)
        super().save(*args, **kwargs)

class experience(models.Model):
    experience_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.experience_name

class education(models.Model):
    education_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.education_name

class camp_info(models.Model):
    camp_name = models.CharField(max_length=200, null=True)
    camp_location = models.TextField(max_length = 1000, null=True)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    hospital = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.camp_name