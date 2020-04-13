# coding: utf-8
import math
from abc import abstractmethod


class LoanCalculator:
    def __init__(self, loanAmount, loanMonthlyTerm, interestRate):
        self.loanAmount = loanAmount
        self.loanTerm = loanMonthlyTerm
        self.monthlyInterestRate = interestRate * 1.0 / 12

    @property
    @abstractmethod
    def monthlyRepayment(self):
        pass

    @property
    @abstractmethod
    def totalInterest(self):
        pass

    @property
    @abstractmethod
    def totalRepayment(self):
        pass

    @property
    @abstractmethod
    def monthlyInterest(self):
        pass

    @property
    @abstractmethod
    def monthlyPrincipal(self):
        pass

    @abstractmethod
    def showDetail(self):
        pass

    @staticmethod
    def printListPerYear(data):
        for it in range(0, int(len(data) / 12)):
            print('Year {}: {}'.format(it + 1, data[it * 12: it * 12 + 12]))


class MatchingTheRepaymentOfPrincipalAndInterest(LoanCalculator):
    # Fixed monthlyRepayment
    @property
    def monthlyRepayment(self):
        return self.loanAmount * self.monthlyInterestRate * \
               math.pow(1.0 + self.monthlyInterestRate, self.loanTerm) / \
               (math.pow(1.0 + self.monthlyInterestRate, self.loanTerm) - 1)

    @property
    def totalInterest(self):
        return self.monthlyRepayment * self.loanTerm - self.loanAmount

    @property
    def totalRepayment(self):
        return self.monthlyRepayment * self.loanTerm

    @property
    def monthlyInterest(self):
        return [self.loanAmount * self.monthlyInterestRate *
                (math.pow(1.0 + self.monthlyInterestRate, self.loanTerm) - math.pow(1.0 + self.monthlyInterestRate, it))
                / (math.pow(1.0 + self.monthlyInterestRate, self.loanTerm) - 1)
                for it in
                range(0, self.loanTerm)]

    @property
    def monthlyPrincipal(self):
        return [self.loanAmount * self.monthlyInterestRate * math.pow(1 + self.monthlyInterestRate, it) /
                (math.pow(1.0 + self.monthlyInterestRate, self.loanTerm) - 1) for it in range(0, self.loanTerm)]

    def showDetail(self):
        print('Monthly Repayment: {}'.format(self.monthlyRepayment))
        print('Total Interest: {}'.format(self.totalInterest))
        print('Total Repayment: {}'.format(self.totalRepayment))


class MatchingThePrincipalRepayment(LoanCalculator):
    @property
    def monthlyPrincipal(self):
        return self.loanAmount * 1.0 / self.loanTerm

    @property
    def monthlyRepayment(self):
        return [self.monthlyPrincipal + (self.loanAmount - it * self.monthlyPrincipal) * self.monthlyInterestRate
                for it in range(0, self.loanTerm)]

    @property
    def monthlyInterest(self):
        return [(self.loanAmount - it * self.monthlyPrincipal) * self.monthlyInterestRate for it in
                range(0, self.loanTerm)]

    @property
    def totalInterest(self):
        return (self.loanTerm * 1. + 1) * self.loanAmount * self.monthlyInterestRate / 2

    @property
    def totalRepayment(self):
        return self.loanAmount + self.totalInterest

    def showDetail(self):
        print('Monthly Repayment:')
        self.printListPerYear(self.monthlyRepayment)
        print('Total Interest: {}'.format(self.totalInterest))
        print('Total Repayment: {}'.format(self.totalRepayment))


if __name__ == '__main__':
    loan = 780000
    term = 360
    rate = 0.05635

    calA = MatchingTheRepaymentOfPrincipalAndInterest(loan, term, rate)
    calA.showDetail()
    # print(calA.monthlyInterest)
    # print(calA.monthlyPrincipal)

    print('-----')

    calB = MatchingThePrincipalRepayment(loan, term, rate)
    calB.showDetail()
    # print(calB.monthlyInterest)
    # print(calB.monthlyPrincipal)
