from django.db import models

# Create your models here.
class KocwAllList(models.Model):
    num = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length=100, blank=True, null=True)
    course_url = models.CharField(max_length=1000, blank=True, null=True)
    lecturer = models.CharField(max_length=100, blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    taxon = models.CharField(max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=100, blank=True, null=True)
    term = models.CharField(max_length=100, blank=True, null=True)
    popular_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kocw_all_list'
