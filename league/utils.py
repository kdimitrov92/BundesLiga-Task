from suds.client import Client


class Team:
    def __init__(self, name, icon_url):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.icon_url = icon_url

    @property
    def ratio(self):
        return f'{self.wins} / {self.losses} / {self.draws}'


class API(object):
    """
    NOTE: This is an exact copy of the GitHub repo implementation provided in the task. No PEP8 followed here.
    """
    API_PATH = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"

    def info(self):
        return self._getClient()

    def getAvailGroups(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetAvailGroups(leagueShortcut, leagueSaison)
        return response

    def getAvailLeagues(self):
        response = self._getClient().service.GetAvailLeagues()
        return response

    def getAvailLeaguesBySports(self, sportID):
        response = self._getClient().service.GetAvailLeaguesBySports(sportID)
        return response

    def getAvailSports(self):
        response = self._getClient().service.GetAvailSports()
        return response

    def getCurrentGroup(self, leagueShortcut):
        response = self._getClient().service.GetCurrentGroup(leagueShortcut)
        return response

    def getCurrentGroupOrderID(self, leagueShortcut):
        response = self._getClient().service.GetCurrentGroupOrderID(leagueShortcut)
        return response

    def getFussballdaten(self, spieltag, liga, saison, userkennung):
        pass

    def getGoalGettersByLeagueSaison(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetGoalGettersByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getGoalsByLeagueSaison(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetGoalsByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getGoalsByMatch(self, matchID):
        response = self._getClient().service.GetGoalsByMatch(matchID)
        return response

    def getLastChangeDateByGroupLeagueSaison(self, groupOrderID, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetLastChangeDateByGroupLeagueSaison(groupOrderID, leagueShortcut,
                                                                                  leagueSaison)
        return response

    def getLastChangeDateByLeagueSaison(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetLastChangeDateByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getLastMatch(self, leagueShortcut):
        response = self._getClient().service.GetLastMatch(leagueShortcut)
        return response

    def getLastMatchByLeagueTeam(self, leagueId, teamId):
        response = self._getClient().service.GetLastMatchByLeagueTeam(leagueId, teamId)
        return response

    def getMatchByMatchID(self, matchID):
        response = self._getClient().service.GetMatchByMatchID(matchID)
        return response

    def getMatchdataByGroupLeagueSaison(self, groupOrderID, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetMatchdataByGroupLeagueSaison(groupOrderID, leagueShortcut, leagueSaison)
        return response

    def getMatchdataByGroupLeagueSaisonJSON(self, groupOrderID, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetMatchdataByGroupLeagueSaisonJSON(groupOrderID, leagueShortcut,
                                                                                 leagueSaison)
        return response

    def getMatchdataByLeagueDateTime(self, fromDateTime, toDateTime, leagueShortcut):
        response = self._getClient().service.GetMatchdataByLeagueDateTime(fromDateTime, toDateTime, leagueShortcut)
        return response

    def getMatchdataByLeagueSaison(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetMatchdataByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getMatchdataByTeams(self, teamID1, teamID2):
        response = self._getClient().service.GetMatchdataByTeams(teamID1, teamID2)
        return response

    def getNextMatch(self, leagueShortcut):
        response = self._getClient().service.GetNextMatch(leagueShortcut)
        return response

    def getNextMatchByLeagueTeam(self, leagueId, teamId):
        response = self._getClient().service.GetNextMatchByLeagueTeam(leagueId, teamId)
        return response

    def getTeamsByLeagueSaison(self, leagueShortcut, leagueSaison):
        response = self._getClient().service.GetTeamsByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def _getClient(self):
        return Client(self.API_PATH)
