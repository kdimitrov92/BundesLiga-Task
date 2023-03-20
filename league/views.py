from datetime import datetime

from django.shortcuts import render
from django.views.generic import View

from league.utils import API, Team


class Home(View):
    def get(self, request, *args, **kwargs):
        today = datetime.now().date()
        team_search = request.GET.get('team_search', '').strip()

        all_matches = API().getMatchdataByLeagueSaison("bl1", "2022").Matchdata

        finished_matches = [item for item in all_matches if item.matchIsFinished]
        following_gameday_data = [item for item in all_matches if item.matchDateTime.date() >= today]
        team_ratios = self.get_ratios(finished_matches)

        if team_search:
            finished_matches = self.filter_matches_by_team(finished_matches, team_search)
            following_gameday_data = self.filter_matches_by_team(following_gameday_data, team_search)
            team_ratios = self.filter_ratios_by_team(team_ratios, team_search)

        return render(request, 'league.html', context={
            'all_matches_info': finished_matches,
            'upcoming_gameday_matches': following_gameday_data,
            'team_ratios': team_ratios,
            'team_search': team_search,
        })

    @staticmethod
    def get_ratios(matches):
        teams = {}
        for match in matches:
            if match.idTeam1 not in teams:
                teams[match.idTeam1] = Team(match.nameTeam1, match.iconUrlTeam1)

            if match.idTeam2 not in teams:
                teams[match.idTeam2] = Team(match.nameTeam2, match.iconUrlTeam2)

            if match.pointsTeam1 > match.pointsTeam2:
                teams[match.idTeam1].wins += 1
                teams[match.idTeam2].losses += 1
            elif match.pointsTeam1 < match.pointsTeam2:
                teams[match.idTeam1].losses += 1
                teams[match.idTeam2].wins += 1
            else:
                teams[match.idTeam1].draws += 1
                teams[match.idTeam2].draws += 1

        return teams

    @staticmethod
    def filter_matches_by_team(matches, team_search):
        return filter(lambda match: team_search in match.nameTeam1 or team_search in match.nameTeam2, matches)

    @staticmethod
    def filter_ratios_by_team(teams, team_search):
        return dict(filter(lambda team: team_search in team[1].name, teams.items()))
