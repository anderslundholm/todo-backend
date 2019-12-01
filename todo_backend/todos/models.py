from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def get_description(self):
        return self.description

    def __str__(self):
        """A string representation of the model."""
        return self.title


class Entry(models.Model):
    text_entry = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, related_name='entries',
                             on_delete=models.CASCADE)

    def get_text_entry(self):
        return self.text_entry

    def __str__(self):
        """A string representation of the model."""
        return self.text_entry

    # class Meta:
    #     ordering = ['text_entry']
