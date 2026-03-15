from django.db import models

class MediaItem(models.Model):
    CATEGORY_CHOICES = [
        ('leadership', 'Leadership'),
        ('academics', 'Academic Achievements'),
        ('outreach', 'Community & Advocacy'),
        ('workshops', 'Events & Workshops'),
        ('news', 'Press & Media'),
    ]
        
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='academics'
    )
    image = models.ImageField(upload_to='media_gallery/')
    caption = models.TextField()
    view_more_link = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.title}"
    
    
class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # Blank if "Present"

    class Meta:
        ordering = ['-start_date']
        
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name}"