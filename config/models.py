from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class ConfigBase(SingletonModel):
    title = models.CharField(max_length=125)
    description = RichTextField()

    def __str__(self):
        return self.title


class Rules(ConfigBase):
    pass


class AboutUs(ConfigBase):
    pass


class Contact(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
