from django import forms
from .models import*
 
class GroupStage(forms.Form):
    A1=forms.ModelChoiceField(label='A1', queryset=Teams.objects.filter(group='A'))
    A2=forms.ModelChoiceField(label='A2', queryset=Teams.objects.filter(group='A'))
    A3=forms.ModelChoiceField(label='A3', queryset=Teams.objects.filter(group='A'))
    A4=forms.ModelChoiceField(label='A4', queryset=Teams.objects.filter(group='A'))
    B1=forms.ModelChoiceField(label='B1', queryset=Teams.objects.filter(group='B'))
    B2=forms.ModelChoiceField(label='B2', queryset=Teams.objects.filter(group='B'))
    B3=forms.ModelChoiceField(label='B3', queryset=Teams.objects.filter(group='B'))
    B4=forms.ModelChoiceField(label='B4', queryset=Teams.objects.filter(group='B'))
    C1=forms.ModelChoiceField(label='C1', queryset=Teams.objects.filter(group='C'))
    C2=forms.ModelChoiceField(label='C2', queryset=Teams.objects.filter(group='C'))
    C3=forms.ModelChoiceField(label='C3', queryset=Teams.objects.filter(group='C'))
    C4=forms.ModelChoiceField(label='C4', queryset=Teams.objects.filter(group='C'))
    D1=forms.ModelChoiceField(label='D1', queryset=Teams.objects.filter(group='D'))
    D2=forms.ModelChoiceField(label='D2', queryset=Teams.objects.filter(group='D'))
    D3=forms.ModelChoiceField(label='D3', queryset=Teams.objects.filter(group='D'))
    D4=forms.ModelChoiceField(label='D4', queryset=Teams.objects.filter(group='D'))
    E1=forms.ModelChoiceField(label='E1', queryset=Teams.objects.filter(group='E'))
    E2=forms.ModelChoiceField(label='E2', queryset=Teams.objects.filter(group='E'))
    E3=forms.ModelChoiceField(label='E3', queryset=Teams.objects.filter(group='E'))
    E4=forms.ModelChoiceField(label='E4', queryset=Teams.objects.filter(group='E'))
    F1=forms.ModelChoiceField(label='F1', queryset=Teams.objects.filter(group='F'))
    F2=forms.ModelChoiceField(label='F2', queryset=Teams.objects.filter(group='F'))
    F3=forms.ModelChoiceField(label='F3', queryset=Teams.objects.filter(group='F'))
    F4=forms.ModelChoiceField(label='F4', queryset=Teams.objects.filter(group='F'))
    G1=forms.ModelChoiceField(label='G1', queryset=Teams.objects.filter(group='G'))
    G2=forms.ModelChoiceField(label='G2', queryset=Teams.objects.filter(group='G'))
    G3=forms.ModelChoiceField(label='G3', queryset=Teams.objects.filter(group='G'))
    G4=forms.ModelChoiceField(label='G4', queryset=Teams.objects.filter(group='G'))
    H1=forms.ModelChoiceField(label='H1', queryset=Teams.objects.filter(group='H'))
    H2=forms.ModelChoiceField(label='H2', queryset=Teams.objects.filter(group='H'))
    H3=forms.ModelChoiceField(label='H3', queryset=Teams.objects.filter(group='H'))
    H4=forms.ModelChoiceField(label='H4', queryset=Teams.objects.filter(group='H'))

class super16(forms.Form):
    S1=forms.ModelChoiceField(label='S1', queryset=Teams.objects.filter(group='16A'))
    S2=forms.ModelChoiceField(label='S2', queryset=Teams.objects.filter(group='16A'))
    S3=forms.ModelChoiceField(label='S3', queryset=Teams.objects.filter(group='16B'))
    S4=forms.ModelChoiceField(label='S4', queryset=Teams.objects.filter(group='16B'))
    S5=forms.ModelChoiceField(label='S5', queryset=Teams.objects.filter(group='16C'))
    S6=forms.ModelChoiceField(label='S6', queryset=Teams.objects.filter(group='16C'))
    S7=forms.ModelChoiceField(label='S7', queryset=Teams.objects.filter(group='16D'))
    S8=forms.ModelChoiceField(label='S8', queryset=Teams.objects.filter(group='16D'))
    # S9=forms.ModelChoiceField(label='S9', queryset=Teams.objects.filter(group='16E'))
    # S10=forms.ModelChoiceField(label='S10', queryset=Teams.objects.filter(group='16E'))
    # S11=forms.ModelChoiceField(label='S11', queryset=Teams.objects.filter(group='16F'))
    # S12=forms.ModelChoiceField(label='S12', queryset=Teams.objects.filter(group='16F'))
    # S13=forms.ModelChoiceField(label='S13', queryset=Teams.objects.filter(group='16G'))
    # S14=forms.ModelChoiceField(label='S14', queryset=Teams.objects.filter(group='16G'))
    # S15=forms.ModelChoiceField(label='S15', queryset=Teams.objects.filter(group='16H'))
    # S16=forms.ModelChoiceField(label='S16', queryset=Teams.objects.filter(group='16H'))
    
class super8(forms.Form):
    S = forms.ModelChoiceField(label='S', queryset=Teams.objects.filter(group='8'))
