# -*- coding: utf-8 -*-


class TennisGameDefactored1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        scoreTypes = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        if (self.p1points == self.p2points):
            result = scoreTypes.get(self.p1points, "Deuce")
            if result != "Deuce":
                result += "-All"

        elif max(self.p1points, self.p2points) >= 4:
            if abs(self.p1points - self.p2points) == 1:
                result = "Advantage "
            else:
                result = "Win for "

            if self.p1points > self.p2points:
                result += self.player1Name
            else:
                result += self.player2Name
        else:
            p1Score = scoreTypes[self.p1points]
            p2Score = scoreTypes[self.p2points]
            result = p1Score + "-" + p2Score
        return result


class TennisGameDefactored2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        if playerName == self.player2Name:
            self.p2points += 1

    def score(self):
        result = ""
        scoreTypes = ["Love", "Fifteen", "Thirty", "Forty"]

        if self.p1points == self.p2points:
            if self.p1points < 4:
                result = scoreTypes[self.p1points] + "-All"
            else:
                result = "Deuce"
        elif max(self.p1points, self.p2points) <= 3:
            P1res = scoreTypes[self.p1points]
            P2res = scoreTypes[self.p2points]
            result = P1res + "-" + P2res
        else:
            if abs(self.p1points - self.p2points) == 1:
                result = "Advantage "
            else:
                result = "Win for "

            if self.p1points > self.p2points:
                result += self.player1Name
            else:
                result += self.player2Name

        return result


class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1Name = player1Name
        self.p2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0

    def won_point(self, n):
        if n == self.p1Name:
            self.p1Points += 1
        else:
            self.p2Points += 1

    def score(self):
        result = ""
        score = ""
        if max(self.p1Points, self.p2Points) <= 3:
            scoreTypes = ["Love", "Fifteen", "Thirty", "Forty"]
            p1Score = scoreTypes[self.p1Points]
            p2Score = scoreTypes[self.p2Points]

            if self.p1Points == self.p2Points:
                result = p1Score + "-All"
            else:

                result = p1Score + "-" + p2Score

        else:
            if (self.p1Points == self.p2Points):
                result = "Deuce"
            else:
                winner = ""
                if self.p1Points > self.p2Points:
                    winner = self.p1Name
                else:
                    winner = self.p2Name

                if abs(self.p1Points-self.p2Points) == 1:
                    result = "Advantage " + winner
                else:
                    result = "Win for " + winner
        return result


# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1
