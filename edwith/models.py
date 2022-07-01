from django.db import models

# Create your models here.
class EdwithAllList(models.Model):
    num = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=1000, blank=True, null=True)
    lecturer = models.CharField(max_length=100, blank=True, null=True)
    org = models.CharField(max_length=100, blank=True, null=True)
    like_num = models.IntegerField(blank=True, null=True)
    student_num = models.IntegerField(blank=True, null=True)
    href = models.CharField(max_length=1000, blank=True, null=True)
    level_text = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edwith_all_list'