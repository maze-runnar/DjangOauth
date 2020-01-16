from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    premium_member = models.BooleanField()
    password = models.CharField(max_length  = 20 , null = False)
    email = models.EmailField(("email"), max_length=254)
    # gender = models.BooleanField(_("gender"))
    # userfile = models.FileField(_("userfile"), upload_to=None, max_length=100)
    # profile = models.ImageField(_("profile"), upload_to=None, height_field=None, width_field=None, max_length=None)
    # joinat = models.DateTimeField(_(""), auto_now=True, auto_now_add=True)
    # bio = models.TextField(_bio("bio"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'