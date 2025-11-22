from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # For SEO friendly URLS
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    # For the money field below, we use DecimalField to avoid floating point precision issues
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    # I used image urls since stroging urls is easier for this scope compared to file upload
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        # PERFORMANCE REQUIREMENT: Database Indexing on frequently queried fields

        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['category']),
            models.Index(fields=['name']),
        ]

        def __str__(self):
            return self.name