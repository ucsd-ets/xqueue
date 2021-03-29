from django.contrib import admin

from submission_queue.models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'requester_id',
        'queue_name',
        'arrival_time',
        'grader_id',
        'num_failures'
    )
