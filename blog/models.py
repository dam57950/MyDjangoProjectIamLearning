from django.db import models
from django.dispatch import receiver

from versatileimagefield.fields import VersatileImageField, \
    PPOIField


# Create your models here.
# from django.shortcuts import get_object_or_404, redirect

class PhotoElement(models.Model):
    name = models.CharField(
        'Name',
        max_length=80
    )
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI'
    )


@receiver(models.signals.post_delete, sender=PhotoElement)
def delete_ExampleImageModel_images(sender, instance, **kwargs):
    """
    Deletes ExampleImageModel image renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.image.delete_all_created_images()
    # Deletes Original Image
    instance.image.delete(save=False)


#    name = models.CharField(max_length=20)
#    place = models.CharField(max_length=20)
#    description = models.TextField(default="Standard pics")
#    image = VersatileImageField(upload_to='static/images/')
#    image = VersatileImageField(
#        'Votre photo',
#        upload_to='testimagemodel/', )


# def PhotoElement_delete(request, photo_id):
#    photo_element = get_object_or_404(PhotoElement, id=photo_id)
#    if photo_element.photo:
#        photo_element.photo.delete()
#   photo_element.delete()
#    return redirect("/dashboard/doors")

