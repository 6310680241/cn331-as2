from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_teacher = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    is_authenticated = True
    is_anonymous = False

    def __str__(self) -> str:
        teacherMark = u'\u2713' if self.is_teacher else ""
        return f"{self.username} ({self.first_name} {self.last_name}) {teacherMark}"

class Subject(models.Model):
    code = models.CharField(max_length=7)
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    semester = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(3), MinValueValidator(1)])
    max_seat = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(1)])
    active = models.BooleanField(default=True)
    enroll = models.ManyToManyField(User, blank=True, related_name="enroll")

    def save(self, *args, **kwargs):
        teacher = get_object_or_404(User, id=self.teacher.id)
        if teacher.is_teacher is not True:
            raise ValueError('Selected user must be teacher')
        # if "enroll" in self and self.enroll.count() >= self.max_seat:
        #     raise ValueError('Full')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.name} ({self.teacher.first_name} {self.teacher.last_name})"