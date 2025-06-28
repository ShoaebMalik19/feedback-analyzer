from django.db import models

# This model represents one feedback entry
class Feedback(models.Model):
    text = models.TextField()  # The user's original feedback
    sentiment = models.CharField(max_length=20)  # POSITIVE or NEGATIVE
    confidence = models.FloatField()  # Confidence score (like 99.85)

    def __str__(self):
        return f"{self.text[:30]} - {self.sentiment} ({self.confidence}%)"
