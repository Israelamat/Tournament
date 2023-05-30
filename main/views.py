from django.shortcuts import render
from django.http import HttpResponse
from .models import League, Team, Match, Scores
from .forms import CreateLeagueForm, EditMatchForm, CreateTeamForm, CreatePlayerForm, EditLeagueForm, EditScoreForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def league(response, id):
    l = League.objects.get(league_id=id)
    teams = list(l.team_set.all())
    m = [Match.objects.filter(home_team_id__in=[t.team_id for t in l.team_set.all()], match_day=i) for i in range(1,len(teams))]
    if response.method == "POST":
        if response.POST.get("addTeam"):
            team_name = response.POST.get("team name")
            if len(team_name) <= 30:
                l.team_set.create(name=team_name, shorthand=team_name[:3])
        elif response.POST.get("deleteL"):
            League.objects.filter(league_id=id).delete()
            return redirect('/')
        elif response.POST.get("generateSchedule"):
            for match_list in m:
                match_list.delete()
            mid = int(len(teams)/2)
            list1 = teams[:mid]
            list2 = teams[mid:]
            list2.reverse()
            st_team = teams[0]
            dn_teams = teams[1:]
            for i in range(len(list1)):
                Match.objects.create(home_team_id=list1[i], away_team_id=list2[i], match_day=1)
            for j in range(len(teams)-2):
                dn_teams.insert(0, dn_teams.pop())
                teams = [st_team] + dn_teams
                list1 = teams[:mid]
                list2 = teams[mid:]
                list2.reverse()
                for i in range(len(list1)):
                    Match.objects.create(home_team_id=list1[i], away_team_id=list2[i], match_day=j+2)
            count_points(id)

    return render(response, 'main/league.html', {"l" : l, "m": m})

@login_required
def team(response, lid, tid):
    t = Team.objects.get(team_id=tid)
    if response.method == "POST":
        if response.POST.get("addPlayer"):
            first_name = response.POST.get("first name")
            second_name = response.POST.get("second name")
            position = response.POST.get("position")
            if len(first_name) <= 30 and len(second_name) <= 30 and len(position) <= 20:
                t.player_set.create(first_name=first_name, second_name=second_name, position=position)
        elif response.POST.get("deleteT"):
            Team.objects.filter(team_id=tid).delete()
            return redirect('/{}'.format(lid))
    return render(response, 'main/team.html', {"t":t})

def home(response):
    return render(response, "main/home.html", {})

@login_required
def create_league(request):
    if request.method == "POST":
        form = CreateLeagueForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/')
    else:
        form = CreateLeagueForm()
    return render(request, 'main/add_league.html', {'form':form})

@login_required
def create_team(request, lid):
    if request.method == "POST":
        form = CreateTeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.league_id = League.objects.get(league_id=lid)
            team.save()
            return redirect("/{}".format(lid))
    else:
        form = CreateTeamForm()
    return render(request, 'main/add_team.html', {"form":form})

@login_required
def create_player(request, lid, tid):
    if request.method == "POST":
        form = CreatePlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.team_id = Team.objects.get(team_id=tid)
            player.save()
            return redirect("/{}/{}".format(lid, tid))
    else:
        form = CreatePlayerForm()
    return render(request, 'main/add_player.html', {"form":form})
@login_required
def edit_match(request, lid, mid):
    l = League.objects.get(league_id=lid)
    m = Match.objects.get(match_id=mid)
    if request.method == "POST":
        form_match = EditMatchForm(request.POST, instance=Match.objects.get(match_id=mid))
        if form_match.is_valid():
            form_match.save()
            count_points(lid)
            return redirect('/{}'.format(lid))
    else:
        form_match = EditMatchForm()
    return render(request, 'main/edit_match.html', {"form_match" : form_match, "l" : l, "m" : m})

@login_required
def add_score(request, mid, lid):
    if request.method == "POST":
        form_score = EditScoreForm(request.POST)
        if form_score.is_valid():
            score = form_score.save(commit=False)
            score.match_id = Match.objects.get(match_id=mid)
            score.save()
            return redirect('/{}/editmatch/{}'.format(lid, mid))
    else:
        form_score = EditScoreForm()
    return render(request, 'main/add_score.html', {"form_score" : form_score})

def count_points(lid):
    for team in League.objects.get(league_id=lid).team_set.all():
        team.points = 0
        team.goals_scored = 0
        team.goals_lost = 0
        team.wins = 0
        team.draws = 0
        team.lost = 0
        team.save()
    matches = Match.objects.filter(home_team_id__in=[t.team_id for t in League.objects.get(league_id=lid).team_set.all()])
    for match in matches:
        if match.home_team_result == None or match.away_team_result == None:
            continue
        if match.home_team_result > match.away_team_result:
            match.home_team_id.points += 3
            match.home_team_id.wins += 1
            match.away_team_id.lost += 1
            match.away_team_id.goals_lost += match.home_team_result
            match.away_team_id.goals_scored += match.away_team_result
            match.home_team_id.goals_lost += match.away_team_result
            match.home_team_id.goals_scored += match.home_team_result
            match.away_team_id.save()
            match.home_team_id.save()
        elif match.home_team_result == match.away_team_result:
            match.home_team_id.points += 1
            match.away_team_id.points += 1
            match.away_team_id.goals_lost += match.home_team_result
            match.away_team_id.goals_scored += match.away_team_result
            match.home_team_id.goals_lost += match.away_team_result
            match.home_team_id.goals_scored += match.home_team_result
            match.home_team_id.draws += 1
            match.away_team_id.draws += 1
            match.away_team_id.save()
            match.home_team_id.save()
        elif match.home_team_result < match.away_team_result:
            match.away_team_id.points += 3
            match.away_team_id.goals_lost += match.home_team_result
            match.away_team_id.goals_scored += match.away_team_result
            match.home_team_id.goals_lost += match.away_team_result
            match.home_team_id.goals_scored += match.home_team_result
            match.home_team_id.lost += 1
            match.away_team_id.wins += 1
            match.away_team_id.save()
            match.home_team_id.save()

@login_required
def edit_league(request, lid):
    if request.method == "POST":
        form = EditLeagueForm(request.POST, instance=League.objects.get(league_id=lid))
        if form.is_valid():
            form.save()
            return redirect('/{}'.format(lid))
    else:
        form = EditLeagueForm()
    return render(request, 'main/edit_league.html', {"form" : form})

