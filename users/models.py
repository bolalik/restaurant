
from django.contrib.auth.models import AbstractUser
from django.db import models


# class Role(models.Model):
#     STUDENT = 1
#     TEACHER = 2
#     ADMIN = 3
#     ROLE_CHOICES = (
#         (STUDENT, 'student'),
#         (TEACHER, 'teacher'),
#         (ADMIN, 'admin'),
#     )


class User(AbstractUser):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (ADMIN, 'admin'),
    )

    roles = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=1)

    def is_admin(self):
        return self.roles == self.ADMIN

    def is_teacher(self):
        return self.roles == self.TEACHER
