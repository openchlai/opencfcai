# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .utils import forward_raw_data_to_main_system
# from.models import RawData

# # Signal to trigger forwarding
# @receiver(post_save, sender=RawData)
# def trigger_forwarding_on_save(sender, instance, created, **kwargs):
#     if created:
#         forward_raw_data_to_main_system(instance)
