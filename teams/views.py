from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Teams, Predictions, PredictForm

from .forms import *
from users.models import Profile

# Create your views here.

def home(request):

    t = Teams.objects.all()
    context = {
		'teams' : t
	}
    print(t)
    return render(request, 'teams/home.html', context)

def PostListView(request):

    current_user = request.user

    print(current_user)



    p_form = PredictForm()

    a = Teams.objects.filter(group="A")  #.values_list("team", flat=True)
    b = Teams.objects.filter(group="B")
    c = Teams.objects.filter(group="C")
    d = Teams.objects.filter(group="D")
    e = Teams.objects.filter(group="E")
    f = Teams.objects.filter(group="F")
    g = Teams.objects.filter(group="G")
    h = Teams.objects.filter(group="H")

    teams = [a, b, c, d, e, f, g, h]

    # print(type(teams), teams[0])

    # import pandas as pd
    # data = pd.read_csv('C:/Users/Reza/Desktop/teams.csv', header = None) 

    # for i in data.index:
    #     t = Teams(user = current_user, round='Group Stage', team=data[0][i], group = data[1][i], index= data[2][i])
    #     t.save()
        # tem = Teams.objects.get(team=data[0][i])
        # t = Predictions(user = current_user, round='Group Stage', team = tem, group = data[1][i], index= data[2][i])
        # t.save()
    form = GroupStage(request.POST)
    context = {
    'teams' : teams,
    'A': a,
    'B': b,
    'C': c,
    'D': d,
    'E': e,
    'F': f, 
    'G': g, 
    'H': h,
    'form':form
    }
    if request.method == 'POST':  # if there is a post
        if form.is_valid():
            data = Predictions()
            A1 = form.cleaned_data['A1']
            A2 = form.cleaned_data['A2']
            A3 = form.cleaned_data['A3']
            A4 = form.cleaned_data['A4']
            B1 = form.cleaned_data['B1']
            B2 = form.cleaned_data['B2']
            B3 = form.cleaned_data['B3']
            B4 = form.cleaned_data['B4']
            C1 = form.cleaned_data['C1']
            C2 = form.cleaned_data['C2']
            C3 = form.cleaned_data['C3']
            C4 = form.cleaned_data['C4']
            D1 = form.cleaned_data['D1']
            D2 = form.cleaned_data['D2']
            D3 = form.cleaned_data['D3']
            D4 = form.cleaned_data['D4']
            E1 = form.cleaned_data['E1']
            E2 = form.cleaned_data['E2']
            E3 = form.cleaned_data['E3']
            E4 = form.cleaned_data['E4']
            F1 = form.cleaned_data['F1']
            F2 = form.cleaned_data['F2']
            F3 = form.cleaned_data['F3']
            F4 = form.cleaned_data['F4']
            G1 = form.cleaned_data['G1']
            G2 = form.cleaned_data['G2']
            G3 = form.cleaned_data['G3']
            G4 = form.cleaned_data['G4']
            H1 = form.cleaned_data['H1']
            H2 = form.cleaned_data['H2']
            H3 = form.cleaned_data['H3']
            H4 = form.cleaned_data['H4']
            group_stage = {
                'A1':A1, 'A2':A2, 'A3':A3, 'A4':A4,
                'B1':B1, 'B2':B2, 'B3':B3, 'B4':B4,
                'C1':C1, 'C2':C2, 'C3':C3, 'C4':C4, 
                'D1':D1, 'D2':D2, 'D3':D3, 'D4':D4, 
                'E1':E1, 'E2':E2, 'E3':E3, 'E4':E4, 
                'F1':F1, 'F2':F2, 'F3':F3, 'F4':F4, 
                'G1':G1, 'G2':G2, 'G3':G3, 'G4':G4,
                'H1':H1, 'H2':H2, 'H3':H3, 'H4':H4,
                }
            print(group_stage)
            if current_user.is_authenticated:
                user_predictions = Predictions.objects.filter(user=current_user, round = 'Group Stage')
                if len(user_predictions)>0:
                    print(user_predictions)
                    messages.warning(request, "You have already predicted !")
                else:    
                    for r, value in group_stage.items():
                        t = Teams.objects.get(team=value, round='Group Stage')
                        p = Predictions(user = current_user, round='Group Stage', rank = r, index=t.group, group = t.group, prediction=t)
                        p.save()

        else:
            print('form not valid')

    return render(request, "teams/home.html", context)


def Super16(request):

    current_user = request.user

    print(current_user)

    a = Teams.objects.filter(group="16A")  #.values_list("team", flat=True)
    b = Teams.objects.filter(group="16B")
    c = Teams.objects.filter(group="16C")
    d = Teams.objects.filter(group="16D")
    e = Teams.objects.filter(group="16E")
    f = Teams.objects.filter(group="16F")
    g = Teams.objects.filter(group="16G")
    h = Teams.objects.filter(group="16H")

    teams = [a, b, c, d, e, f, g, h]

    # print(type(teams), teams[0])

    # import pandas as pd
    # data = pd.read_csv('C:/Users/Reza/Desktop/teams.csv', header = None) 

    # for i in data.index:
    #     t = Teams(user = current_user, round='Group Stage', team=data[0][i], group = data[1][i], index= data[2][i])
    #     t.save()
        # tem = Teams.objects.get(team=data[0][i])
        # t = Predictions(user = current_user, round='Group Stage', team = tem, group = data[1][i], index= data[2][i])
        # t.save()
    form = super16(request.POST)
    context = {
    'teams' : teams,
    'A': a,
    'B': b,
    'C': c,
    'D': d,
    'E': e,
    'F': f, 
    'G': g, 
    'H': h,
    'form':form
    }
    if request.method == 'POST':  # if there is a post
        if form.is_valid():
            data = Predictions()
            S1 = form.cleaned_data['S1']
            S2 = form.cleaned_data['S2']
            S3 = form.cleaned_data['S3']
            S4 = form.cleaned_data['S4']
            S5 = form.cleaned_data['S5']
            S6 = form.cleaned_data['S6']
            S7 = form.cleaned_data['S7']
            S8 = form.cleaned_data['S8']

            group_stage = {
                'S1':S1, 
                'S2':S2, 
                'S3':S3, 
                'S4':S4, 
                'S5':S5, 
                'S6':S6, 
                'S7':S7, 
                'S8':S8, 

                }
            print(group_stage)
            if current_user.is_authenticated:
                user_predictions = Predictions.objects.filter(user=current_user, round = '16')
                if len(user_predictions)>0:
                    print(user_predictions)
                    messages.warning(request, "You have already predicted !")
                else:    
                    for r, value in group_stage.items():
                        t = Teams.objects.get(team=value, round='16')
                        p = Predictions(user = current_user, round='16', rank = r, index=t.group, group = t.group, prediction=t)
                        p.save()

        else:
            print('form not valid')

    return render(request, "teams/super16.html", context)

# class PostListView(ListView):
#     model = Teams
#     template_name = 'teams/home.html'  # <app>/<model>_<viewtype>.html
#     a = Teams.objects.filter(group='A')
#     context_object_name = 'teams'
#     ordering = ['-create_at']
#     # paginate_by = 2


def QuarterFinal(request):

    current_user = request.user

    print(current_user)

    a = Teams.objects.filter(round = '8')  #.values_list("team", flat=True)
    teams = Teams.objects.filter(round='Group Stage')

    user_predictions = Predictions.objects.filter(user=current_user)
    u=[]
    for ur in user_predictions:
        u.append(ur.prediction)

    

    a_new = []

    for q in a:
        a_new.append(q)
    new = []
    for x in a_new:
        if x in u:
            pass
        else:
            new.append(x)
    print('---------', new, teams)
    
            
    
   

    # print(type(teams), teams[0])

    # import pandas as pd
    # data = pd.read_csv('C:/Users/Reza/Desktop/teams.csv', header = None) 

    # for i in data.index:
    #     t = Teams(user = current_user, round='Group Stage', team=data[0][i], group = data[1][i], index= data[2][i])
    #     t.save()
        # tem = Teams.objects.get(team=data[0][i])
        # t = Predictions(user = current_user, round='Group Stage', team = tem, group = data[1][i], index= data[2][i])
        # t.save()
    form = super8(request.POST)
    context = {
    'teams' : teams,
    'A': new[0],
    'form':form
    }
    if request.method == 'POST':  # if there is a post
        if form.is_valid():
            data = Predictions()
            S = form.cleaned_data['S']
            
            group_stage = {
                'S':S, 
                }
            print(group_stage)
            if current_user.is_authenticated:
   
                if x in u :
                    print(user_predictions)
                    messages.warning(request, "You have already predicted !")
                else:    
                    for r, value in group_stage.items():
                        t = Teams.objects.get(team=value, round='8')
                        p = Predictions(user = current_user, round='8', rank = r, index=t.group, group = t.group, prediction=t)
                        p.save()

        else:
            print('form not valid')

    return render(request, "teams/super8.html", context)

def SemiFinal(request):


    return render(request, "teams/home.html")

def Final(request):


    return render(request, "teams/home.html")
 

def Scores(request):

    scores = Profile.objects.all()



    for s in scores:

        pre = Predictions.objects.filter(user=s.user)
        points = 0
        print(pre)
        for a in pre:
            try:
                print("----------------",a.rank, type(a))
                res = Teams.objects.get(ranking=a.rank, round=a.round)
                a.result= res
                if a.rank==a.prediction.ranking:
                    a.point=a.prediction.point
                else:
                    a.point=0         
                a.save()

                points+=a.point
            except:
                pass

            s.points=points
            s.save()

    context ={

        "scores" : scores

    }


    return render(request, "teams/scores.html", context)


class PostDetailView(DetailView):
    model = Teams


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Teams
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teams
    fields = ['point']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Teams
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False	


def about(request):
	return render(request, 'teams/about.html', {'title': 'about'})

# AJAX
def load_teams(request):
    context = []
    print(len(context))

    x = len(context)

    while(x <= 0):
        print(x)
        context = []
        x = len(context)
    
    return render(request, 'teams/teams.html', context)
	# return JsonResponse(list(schadules.values('title')), safe=False)
