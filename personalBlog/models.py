from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# import signal method post_save and receiver decorator


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    username=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    #####Not using a one to one field, but Foreign Key can trigger "'RelatedManager' object has no attribute 'save'" Exception -> 1 user 1 Profile
    profileName=models.CharField(max_length=20, blank=True, null=True, default="John Doe")
    bio=models.TextField(null=True, blank=True, default="Your bio here...")
    created=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username.__str__()


@receiver(post_save, sender=User) #Connecting signal and receiver ---> does not have to be a decorator!
def create_Profile(sender, instance, created, **kwargs):

    if created: # is this the first instance?
        UserProfile.objects.create(username=instance)
#auto create a profile, when a user is created


#@receiver(post_save, sender=User)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
# if not newly created, just save the instance


class Article(models.Model):
    author=models.ForeignKey(User, on_delete=models.PROTECT)
    headline=models.CharField(max_length=100, default="Your Title....")
    content=models.TextField()
    timestampCreated=models.DateTimeField(auto_now_add=True)
    timestampUpdated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.headline