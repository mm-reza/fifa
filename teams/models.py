#pylint: disable = E1101
#pylint: disable = W0614


from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class Teams(models.Model):
    RANKS = (
        (0,0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    group = models.CharField(max_length=5)
    ranking = models.CharField(max_length=5, blank=True, null=True)
    round = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    index = models.IntegerField()
    # prediction = models.IntegerField(choices=RANKS, default=1)
    # result = models.IntegerField(choices=RANKS, default=0)
    point = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        # return self.user.username
        # return str(self.id)
        return self.team
    
    class Meta:
        unique_together = ('ranking', 'round', 'team')



# class Predictions(models.Model):
#     RANKS = (
#         (0,0),
#         (1, 1),
#         (2, 2),
#         (3, 3),
#         (4, 4),
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     round = models.CharField(max_length=50)
#     team = models.ForeignKey(Teams, on_delete=models.CASCADE)
#     index = models.IntegerField()
#     group = models.CharField(max_length=5)
#     prediction = models.IntegerField(choices=RANKS, default=1)
#     result = models.IntegerField(choices=RANKS, default=0)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     point = models.IntegerField(default=0)
#     def __str__(self):
#         # return str(self.id)
#         return self.user.username
            
#     class Meta:
#         unique_together = ('user', 'round', 'team')


class Predictions(models.Model):
    RANKS = (
('A1', 'A1'),
('A2', 'A2'),
('A3', 'A3'),
('A4', 'A4'),
('B1', 'B1'),
('B2', 'B2'),
('B3', 'B3'),
('B4', 'B4'),
('C1', 'C1'),
('C2', 'C2'),
('C3', 'C3'),
('C4', 'C4'),
('D1', 'D1'),
('D2', 'D2'),
('D3', 'D3'),
('D4', 'D4'),
('E1', 'E1'),
('E2', 'E2'),
('E3', 'E3'),
('E4', 'E4'),
('F1', 'F1'),
('F2', 'F2'),
('F3', 'F3'),
('F4', 'F4'),
('G1', 'G1'),
('G2', 'G2'),
('G3', 'G3'),
('G4', 'G4'),
('H1', 'H1'),
('H2', 'H2'),
('H3', 'H3'),
('H4', 'H4'),
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.CharField(max_length=50)
    rank = models.CharField(choices=RANKS, default="1", max_length=5)
    index = models.CharField(max_length=50)
    group = models.CharField(max_length=5)
    prediction = models.ForeignKey(Teams, related_name="pre", on_delete=models.CASCADE)
    result = models.ForeignKey(Teams, related_name="res", on_delete=models.CASCADE, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    point = models.IntegerField(default=0)
    def __str__(self):
        # return str(self.id)
        return self.user.username
            
    class Meta:
        # unique_together = ('user', 'round', 'rank')
        unique_together = ('user', 'round', 'prediction')


class PredictForm(ModelForm):
    class Meta:
        model = Predictions
        fields = ['rank', 'prediction']
        


# class Quizzes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     prediction = models.IntegerChoices(max_length=2, choices=RANKS, default=1)
#     result = models.IntegerChoices(max_length=2, choices=RANKS, default=1)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#     point = models.IntegerField()
#     def __str__(self):
#         # return str(self.id)
#         return self.user.username

