from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=10)

    def __str__(self):
        return f" {self.name}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()

    def __str__(self):
        return f" {self.id} {self.title}"

class Comment(models.Model):
    user = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.id} comentario del libro {self.book}"

