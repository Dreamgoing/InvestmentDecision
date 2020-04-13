# 一个关于买房还是投资的数学题

## 问题

现阶段是买房好，还是投资理财好？

## 前提假设

我们首先假设如下几个前提：

+ 假设以等额本息支付房贷。
+ 假设房子每年以固定的增长率增长。
+ 假设投资收益每年保持固定的增长率。
+ 假设以等额本息方式支付房贷，相应的，投资理财则每月定投等额本息每月支付的金额

我们设定有如下几个变量：

+ 房屋总值: houseValue
+ 当前手上现金: cash
+ 贷款期限, 这里我们假定都是30年期限: yearTerm
+ 贷款利率: interestRate
+ 房价每年平均增长率: housePriceRate
+ 等额本息每月支付金额: monthlyPayment
+ 等额本息30年期限总支付利息: totalInterest (利息计算方式使用等额本息进行计算，这里不再赘述)
+ 投资理财平均收益率: earningRate
+ 房屋30年后总价值: houseTotalReward
+ 理财30年后总价值: investmentTotalReward

## 计算公式

#### 房产投资：

$$
houseTotalReward = houseValue*(1.0 + housePriceRate)^{yearTerm}
$$

#### 股票理财投资：

$$
\begin{align*}investmentTotalReward = cash*(1.0+earningRate)^{yearTerm}+\\monthlyPayment*(1.0+earningRate)^{yearTerm-1} + \\ monthlyPayment*(1.0+earningRate)^{yearTerm-2}+\\monthlyPayment*(1.0+earningRate)^{yearTerm-3}+...+ monthlyPayment\\\end{align*}
$$



## 直观结果

我们开始假设了很多个变量，因此我们要固定其中一些变量，选取单一变量进行研究（控制变量法）。

#### 1. 以房价增速为变量

首先固定：

+ 当前持有现金100w
+ 房屋总价值400w
+ 贷款利率5.59%
+ 贷款期限30年
+ 投资固定收益7%

我们得到结论：

当房价每年以5%的速度增加时，计算得：

+ 投资房产总收益: 17287769
+ 投资理财总收益:  9675465

当房价每年以4%的速度增加时，计算得：

+ 投资房产总收益：12973590
+ 投资理财总收益：9675465

## 个人理解

只有房价增速在4%一下时，可以说理财和房价的收益是相当的。

## 如何本地运行

`python investDecision.py`

## 局限性说明

本模型是比较简陋的数学模型，计算所用到的数学知识也是非常的基础。对于政策因素，通货膨胀，房产寿命，投资理财风险，突发情况等， 没有考虑在内。且得出结论仅供参考，不构成任何投资决策。

