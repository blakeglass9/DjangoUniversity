from django.db import models

class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    # Model manager
    objects = models.Manager()

    def __str__(self):
        return f"{self.campus_name} ({self.state}) - ID: {self.campus_id}"

    class Meta:
        verbose_name = "University Campus"

