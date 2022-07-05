from django.db import models

# Create your models here.
class MoocAllList(models.Model):
    num = models.AutoField(db_column='NUM', primary_key=True)  # Field name made lowercase.
    enrollment_start = models.DateTimeField(blank=True, null=True)
    enrollment_end = models.DateTimeField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    start_display = models.CharField(max_length=20, blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    invitation_only = models.IntegerField(blank=True, null=True)
    audit_yn = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    org_name = models.CharField(max_length=50, blank=True, null=True)
    teachers = models.CharField(max_length=300, blank=True, null=True)
    language_name = models.CharField(max_length=20, blank=True, null=True)
    middle_classfy = models.CharField(max_length=20, blank=True, null=True)
    middle_classfy_name = models.CharField(max_length=20, blank=True, null=True)
    fourth_industry_yn = models.CharField(max_length=3, blank=True, null=True)
    ai_sec_yn = models.CharField(max_length=3, blank=True, null=True)
    effort_time = models.CharField(max_length=50, blank=True, null=True)
    video_time = models.CharField(max_length=50, blank=True, null=True)
    learning_time = models.CharField(max_length=50, blank=True, null=True)
    id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    course_id = models.CharField(max_length=100, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mooc_all_list'
