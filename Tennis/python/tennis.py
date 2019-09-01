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
            result = scoreTypes.get(self.p1points, "")
            if not result:
                result = "Deuce"
            else:
                result += "-All"

        # elif (self.p1points >= 4 or self.p2points >= 4):
        elif max(self.p1points, self.p2points) >= 4:
            minusResult = self.p1points - self.p2points

            if (minusResult == 1):
                result = "Advantage " + self.player1Name
            elif (minusResult == -1):
                result = "Advantage " + self.player2Name
            elif (minusResult >= 2):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
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
        scoreTypes = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        scoreDifference = abs(self.p1points - self.p2points)
        maxScore = max(self.p1points, self.p2points)
        play1Leads = True if self.p1points > self.p2points else False

        if self.p1points == self.p2points:
            if self.p1points < 4:
                result = scoreTypes[self.p1points] + "-All"
            else:
                result = "Deuce"
        elif maxScore <= 3:
            P1res = scoreTypes[self.p1points]
            P2res = scoreTypes[self.p2points]
            result = P1res + "-" + P2res
        else:
            if scoreDifference == 1:
                result = "Advantage "
            else:
                result = "Win for "
            result += self.player1Name if play1Leads else self.player2Name

        return result


class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s


# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored1
