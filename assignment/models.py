from django.db import models
from django.shortcuts import get_object_or_404
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Subject(models.Model):
    code = models.CharField(max_length=7)
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    semester = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(3), MinValueValidator(1)])
    max_seat = models.PositiveIntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(1)])
    credit = models.PositiveSmallIntegerField(default=3, validators=[MaxValueValidator(3), MinValueValidator(0)])
    active = models.BooleanField(default=True)
    enroll = models.ManyToManyField(User, blank=True, related_name="enroll")

    def save(self, *args, **kwargs):
        teacher = get_object_or_404(User, id=self.teacher.id)
        if teacher.is_staff is not True:
            raise ValueError('Selected user must be staff')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.code} - {self.name} ({self.teacher.first_name} {self.teacher.last_name})"