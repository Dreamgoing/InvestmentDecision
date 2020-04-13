# coding: utf-8
import math

from loanCalculator import MatchingTheRepaymentOfPrincipalAndInterest


class InvestmentDecision:
    def __init__(self, cash, houseValue, interestRate, yearTerm, housePriceRate, stockRate, cashInvestRate):
        self.cash = cash
        self.houseValue = houseValue
        self.interestRate = interestRate
        self.yearTerm = yearTerm
        self.houseRiseRate = housePriceRate
        self.stockRate = stockRate
        self.cashInvestRate = cashInvestRate
        self.houseLoanCalculator = MatchingTheRepaymentOfPrincipalAndInterest(self.houseValue - self.cash,
                                                                              self.yearTerm * 12,
                                                                              self.interestRate
                                                                              )

    def stockInvestTotalReward(self):
        return self.exponentReward(self.cash, self.stockRate, self.yearTerm) + (
                self.houseLoanCalculator.monthlyRepayment * math.pow(1.0 + self.cashInvestRate / 12,
                                                                     self.yearTerm * 12) - 1) / self.cashInvestRate

    @staticmethod
    def exponentReward(value, rate, yearTerm):
        return value * math.pow(1.0 + rate, yearTerm)

    def houseInvestTotalReward(self):
        houseRiseValue = self.exponentReward(self.houseValue, self.houseRiseRate, self.yearTerm)
        print('Total repayment:{}'.format(self.houseLoanCalculator.totalRepayment))
        print('Total house value: {}'.format(houseRiseValue))
        print('Monthly repayment: {}'.format(self.houseLoanCalculator.monthlyRepayment))
        print('Total loan interest value: {}'.format(self.houseLoanCalculator.totalInterest))
        return houseRiseValue

    @staticmethod
    def calCompoundAnnualGrowthRates(startValue, endValue, yearTeam):
        return (endValue * 1.0 / startValue) ** (1.0 / yearTeam) - 1


if __name__ == '__main__':
    mycash = 1000000
    myhouseValue = 4000000
    myinterestRate = 0.059
    myhouseRiseRate = 0.04
    myyearTeam = 30
    mycashInvestRate = 0.07
    mystockRate = 0.07

    decision = InvestmentDecision(mycash, myhouseValue, myinterestRate, myyearTeam, myhouseRiseRate, mystockRate,
                                  mycashInvestRate)

    print(
        'Real house total investment reward: {}'.format(decision.houseInvestTotalReward()))
    print(
        'Real stock investment reward: {}'.format(decision.stockInvestTotalReward()))

    print(InvestmentDecision.calCompoundAnnualGrowthRates(1000, 6000, 25))
