from django.contrib import admin

from .models import*

class PositionAdmin(admin.ModelAdmin):
    list_display=['title_name']
admin.site.register(Position, PositionAdmin)

class ElectionAdmin(admin.ModelAdmin):
    list_display=('Election_name', 'Election_date', 'status')
admin.site.register(Election, ElectionAdmin)

class VoterAdmin(admin.ModelAdmin):
    list_display=('reg_no', 'voter_name','gender','address', 'contact', 'course', 'election')
admin.site.register(Voter, VoterAdmin)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'elect', 'post', 'gender', 'address', 'contact' )
admin.site.register(Candidate, CandidateAdmin)

class BallotAdmin(admin.ModelAdmin):
    list_display = ('elect_tion', 'voter', 'position', 'Candidate')
admin.site.register(Ballot)

