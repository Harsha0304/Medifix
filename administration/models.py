from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import hashlib
# Create your moworkplace = (
workplace = (
    ("Remote","Remote"),
    ("On-Site","On-Site"),
    ("Hybird","Hybird"),
)

type_of_camp = (
    ("Paid","Paid"),
    ("Free","Free"),
)

employment_type = (
    ("Full-Time","Full-Time"),
    ("Part-TIme","Part-TIme"),
    ("Internship","Internship"),
    ("Self-Employed","Self-Employed"),
    ("Trainee","Trainee"),
    ("Freelance","Freelance"),
)

def no_future_date_validator(value):
    if value > timezone.now().date():
        raise ValidationError('Future dates are not allowed')
    
class profile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    aadhar_card_hashed = models.CharField(max_length=128, null=True)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user_name.username
    
    def set_aadhar_card(self, aadhar_card):
        hashed_aadhar = hashlib.sha256(str(aadhar_card).encode()).hexdigest()
        self.aadhar_card_hashed = hashed_aadhar

    def verify_aadhar_card(self, aadhar_card):
        hashed_aadhar_input = hashlib.sha256(str(aadhar_card).encode()).hexdigest()
        return hashed_aadhar_input == self.aadhar_card_hashed
    
class doctor(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor_id = models.IntegerField()
    profile = models.URLField(max_length = 200, null=True)

    def __str__(self):
        return self.user_name.username
    
class education(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    institue_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    feild_of_study = models.CharField(max_length=80, null=True, blank=True)
    start_date = models.DateField(blank=True, validators=[no_future_date_validator], null=True)
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    activities_societies = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.user_name.username
    
    def clean(self):
        super().clean()
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date cannot be before issue date.'})

class license_certification(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    issuing_organization = models.CharField(max_length=60, null=True)
    issue_date = models.DateField(null=True)
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=40, null=True, blank=True)
    credential_url = models.URLField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.user_name.username
    
    def clean(self):
        super().clean()
        if self.expiry_date and self.expiry_date < self.issue_date:
            raise ValidationError({'expiry_date': 'Expiry date cannot be before issue date.'})

class Skill(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class skills_selection(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill,
        related_name='user_skills',
    )
    
    def __str__(self):
        return self.user_name.username

class experience(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    experience_title = models.CharField(max_length=30, null=True)
    employment_type = models.CharField(max_length=30, null=True, choices=employment_type)
    company_name = models.CharField(max_length=40, null=True)
    location = models.CharField(max_length=90, null=True, blank=True)
    location_type = models.CharField(max_length=30, null=True, choices=workplace)
    currently_working_on_this_role = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.experience_title
    
    def clean(self):
        super().clean()
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date cannot be before issue date.'})
        
        if self.currently_working_on_this_role and self.end_date:
            raise ValidationError("End date should be empty when working on the experience.")
        elif not self.currently_working_on_this_role and not self.end_date:
            raise ValidationError("End date is mandatory when not working on the experience.")
    
class Project(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50, null=True)
    working_on_the_project = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=2000, null=True)
    project_url = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.user_name.username
    
    def clean(self):
        super().clean()
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError({'end_date': 'End date cannot be before issue date.'})
        
        if self.working_on_the_project and self.end_date:
            raise ValidationError("End date should be empty when working on the project.")
        elif not self.working_on_the_project and not self.end_date:
            raise ValidationError("End date is mandatory when not working on the project.")

class camp_details(models.Model):
    camp_name = models.CharField(max_length=200,null=True)
    location = models.CharField(max_length=200, null=True)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    contact_website = models.URLField(max_length=200, null=True, blank=True)
    hospital_name = models.CharField(max_length=150,null=True, blank=True)
    club_name = models.CharField(max_length=150,null=True, blank=True)
    other = models.CharField(max_length = 150, null=True, blank=True)
    description = models.TextField(max_length = 1000, null=True)
    type_of_camp = models.CharField(max_length=30, null=True, choices=type_of_camp)
    cost = models.IntegerField()
    other_services = models.TextField(max_length=6000, null=True)
    total_camp_registrations = models.IntegerField()

    def __str__(self):
        return self.camp_name
    
    def clean(self):
        super().clean()
        if not (self.hospital_name or self.club_name or self.other):
            raise ValidationError("At least one of the fields Hospital Name or Club Name or Other must be filled.")
        
        if self.type_of_camp == "Paid" and not self.cost:
            raise ValidationError("Cost field is mandatory for paid camps.")
        elif self.type_of_camp == "Free" and self.cost is not None:
            raise ValidationError("Cost field should not be filled for free camps.")