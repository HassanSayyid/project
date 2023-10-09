from django.db import models

STATUS=[
    ('o', 'Open'),
    ('d', 'Done')
]

GENDER={
   ('f', 'female'),
   ('m', 'male')
   }

class Position(models.Model):
    title_name = models.CharField(max_length = 50)
    
    def __str__(self):
        return f'''{self.title_name}'''


class Election(models.Model):
    Election_name = models.CharField(max_length = 25)
    Election_date= models.DateField(auto_now = False)
    status = models.CharField(max_length = 50, choices=STATUS)
    def __str__(self):
        return f'''{self.Election_name}
    -{self.Election_date}-{self.status}'''



class Voter(models.Model):
    reg_no= models.CharField(max_length = 50)
    voter_name = models.CharField(max_length = 25)
    gender = models.CharField(max_length = 2, choices=GENDER)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length = 20)
    course= models.CharField(max_length= 20)
    election = models.ForeignKey(Election, on_delete = models.CASCADE)
    def __str__(self):
        return f'''{self.reg_no}
    -{self.voter_name}-{self.gender}-{self.address}-
    {self.contact}-{self.course}-{self.election}'''



class Candidate(models.Model):
    candidate_name = models.CharField(max_length = 50)
    elect= models.ForeignKey(Election, on_delete = models.CASCADE)
    post= models.ForeignKey(Position, on_delete = models.CASCADE)
    gender = models.CharField(max_length = 2, choices=GENDER) 
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length = 20)
    def __str__(self):
        return f'''{self.candidate_name}
        -{self.post}-{self.gender}-{self.address}-
        {self.contact}-{self.elect}'''



class Ballot(models.Model):
    
     elec_tion = models.ForeignKey(Election, on_delete = models.CASCADE)
     voter  = models.ForeignKey(Voter, on_delete = models.CASCADE)
     position = models.ForeignKey(Position, on_delete = models.CASCADE)
     Candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
     def __str__(self):
        return f'''{self.elec_tion}
    -{self.voter}-{self.position}-{self.Candidate}-
    '''