from django.db import models
from django.conf import settings
from .course import Course
from django.core.validators import MaxValueValidator

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )
    raiting = models.SmallIntegerField(
        validators=[MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'course')
    
    def __str__(self):
        return f'{self.user.username} - {self.course.title} - {self.raiting}\nComentario: {self.comment}'