from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=128,unique=True)
	story=models.TextField()
	slug = models.SlugField(unique=True)

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	blog_title=models.ForeignKey(Blog)
	comment=models.CharField(max_length=128)
	def __unicode__(self):
		return self.comment


from django.contrib.auth.models import User
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
    
	def __unicode__(self):
		return self.user.username