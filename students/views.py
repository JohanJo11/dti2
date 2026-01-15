from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *




# Create your views here.

def student(request):
    #student = Student.objects.values_list('first_name','last_name').values()
    #student = Student.objects.filter(first_name = 'Johan', id = 3).values()            #  , eshte AND
    #student = Student.objects.filter(first_name = 'Johan').values() | Student.objects.filter(last_name = 'Halili').values()   # | eshte OR       
    #student = Student.objects.filter(phone_number__startswith = 68).values()      
    #student = Student.objects.filter(age__gt = 19).values()      
    #student = Student.objects.filter(age__lt = 30).values()    
    #student = Student.objects.order_by('id').values()   
    #student = Student.objects.order_by('age').values()   
    #student = Student.objects.order_by('-age').values()                  # me - i kapim nga me e madhja te me e vogla
    #student = Student.objects.order_by('first_name','-age').values()   
    
    #student = Student.objects.exclude(phone_number__endswith = 3).values()          # .exclude = perfshin cdo gje pervec kushtit
    #student = Student.objects.filter(first_name__contains = 'a' , ~Q phone_number__endswith=3)
     
    #student = Student.objects.filter(
    #Q(first_name__contains='a') & ~Q(phone_number__endswith='5')).values()      # Q lets us combine conditions in flexible ways, like OR or NOT

    #student = Student.objects.filter(age__gt = 16 , phone_number__startswith=68).values()

    student = Student.objects.all().values()
    """ 
    __contains = "687" --- kontrollon qe 687 te jete brenda variablit
    __date  --- kontrollon daten
    __in --- kontrollon a eshte variabli ne nje liste vlerash
    __range --- kontrollon ne nje range
    __regex --- kontrollon sipas nje regular exp  

    """  
    template = loader.get_template('student.html')
    context = {'students': student}
    return HttpResponse(template.render(context, request))

def checkout(request):
    return render(request, 'checkout-bootstrap.html')

def carousel(request):
    return render(request, 'carousel.html')

def carousel2(request):
    footballers = Footballer.objects.all()
    template = loader.get_template('carousel2.html')
    context = {
        'footballers':footballers
    }
    return HttpResponse(template.render(context,request))


def footballer(request):
     footballers = Footballer.objects.all().values()
     nationalities = Nationality.objects.all().values()
     template = loader.get_template('football_table.html')
     context = {'footballers': footballers,
                'nationalities': nationalities
                }
     return HttpResponse(template.render(context, request))



def check_footballers(request):
    teams = Team.objects.all()
    #teams_info = {}  # dictionary qe do mbaje info per cdo ekip ===> nuk funksionon me kete menyre duhet liste sepse brenda nje variabli {{}} nuk njihen []
    teams_info = []

    for team in teams:
        footballers = Footballer.objects.filter(team=team)

        #listat per lojtaret e huaj dhe lojtaret vendas
        foreign_footballers = []
        same_nationality_players = []
        
        for f in footballers:                         #loopi qe kontrollon nese lojtaret jane vendas apo te huaj
            if f.nationality != team.nationality:
                foreign_footballers.append(f)
            else:
                same_nationality_players.append(f)

        if len(foreign_footballers) > 4:
            status = 'e kuqe'   
        else:
            status = 'jeshile'  

        teams_info.append({
            'team': team,
            'same_nationality': same_nationality_players,
            'length_foreign_players': len(foreign_footballers),
            'status': status
        })

    context = {'teams_info': teams_info}
    return render(request, 'check_footballer.html', context)

