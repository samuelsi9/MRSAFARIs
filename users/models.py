from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
          return f'{self.user.username} Profile'
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
     return self.sender.username 
    