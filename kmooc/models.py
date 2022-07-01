from django.db import models

# Create your models here.
class MoocAllList(models.Model):
    num = models.AutoField(db_column='NUM', primary_key=True)  # Field name made lowercase.
    enrollment_start = models.CharField(max_length=300, blank=True, null=True)
    enrollment_end = models.CharField(max_length=300, blank=True, null=True)
    start = models.CharField(max_length=300, blank=True, null=True)
    start_display = models.CharField(max_length=300, blank=True, null=True)
    end = models.CharField(max_length=300, blank=True, null=True)
    week = models.CharField(max_length=300, blank=True, null=True)
    hidden = models.CharField(max_length=300, blank=True, null=True)
    invitation_only = models.CharField(max_length=300, blank=True, null=True)
    audit_yn = models.CharField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    org_name = models.CharField(max_length=300, blank=True, null=True)
    teachers = models.CharField(max_length=300, blank=True, null=True)
    language_name = models.CharField(max_length=300, blank=True, null=True)
    middle_classfy = models.CharField(max_length=300, blank=True, null=True)
    middle_classfy_name = models.CharField(max_length=300, blank=True, null=True
)
    fourth_industry_yn = models.CharField(max_length=300, blank=True, null=True)
    ai_sec_yn = models.CharField(max_length=300, blank=True, null=True)
    effort_time = models.CharField(max_length=300, blank=True, null=True)
    video_time = models.CharField(max_length=300, blank=True, null=True)
    learning_time = models.CharField(max_length=300, blank=True, null=True)
    id = models.CharField(max_length=300, blank=True, null=True)
    course_id = models.CharField(max_length=300, blank=True, null=True)
    star = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mooc_all_list'