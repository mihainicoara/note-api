import uuid
from django.db import models

# Create your models here.
class NoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notes"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title