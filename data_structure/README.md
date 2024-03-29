# 数据结构
- [数据结构](#数据结构)
  - [低吸高抛问题:](#低吸高抛问题)
    - [问题描述:](#问题描述)
    - [按照获利计算:](#按照获利计算)
    - [差价盈利方式的出结果:](#差价盈利方式的出结果)
    - [最简单的知道哪个人赚的最多的方式:](#最简单的知道哪个人赚的最多的方式)
  - [朋友资产:](#朋友资产)


## 低吸高抛问题:

### 问题描述:

现在有一堆果子，价格为6块一颗，你需要100颗果子自己用。<br>

你打听到果灾将要爆发，这果子肯定涨价。<br>

你想捞一笔，于是，你花了大量资金6块买了350颗果子，第二天果子真的开始涨价。<br>

果子10块一颗的时候，你卖出了350颗果子，然后8块的时候你买入了自己需要的100颗果子。<br>

另外有人说，要是他就买了350颗果子后，直接留下100颗，剩下的250颗果子在10块一颗的时候全部卖出。<br>

提问，究竟谁更精明？是第一个人还是第二个人？<br>


### 按照获利计算:

第一种策略：<br>

1. 花费 \(6 x 350 = 2100\) 块买入350颗果子。
2. 以 \(10 x 350 = 3500\) 块卖出350颗果子，获利 \(3500 - 2100 = 1400\) 块。
3. 然后以 \(8 x 100 = 800\) 块买入100颗果子。

总获利为 \(1400 - 800 = 600\) 块。<br>

第二种策略：<br>

1. 花费 \(6 x 350 = 2100\) 块买入350颗果子。
2. 保留100颗自用，剩下 \(350 - 100 = 250\) 颗果子以 \(10 x 250 = 2500\) 块卖出，获利 \(2500 - 2100 = 400\) 块。

比较两种策略：<br>

- 第一种策略的总获利是 \(600\) 块。
- 第二种策略的总获利是 \(400\) 块。


### 差价盈利方式的出结果:

> 6块 --> 10块赚4块，10块 --> 8块亏2块。

第一个人： 4x(250+100)-2x100

第二个人： 4x250

这种计算方法强调的是每颗果子价格变动带来的直接盈利，而不是整体的净收益或净利润。<br>

注意，这种方法并不考虑最终的净利润，它只考虑了每次交易产生的差价盈利。<br>


### 最简单的知道哪个人赚的最多的方式:

这题，起决定性作用的是那100颗果子。<br>

100个果子，本金都是6块。如果你窝在手里，没有波动收益，如果10块卖，8块再买入，就净赚了 (10-8)x100 的波动收益❤️。<br>


## 朋友资产:

朋友2年时间资产缩水80%，市值减少700亿，请问朋友原来身价多少？<br>

朋友的资产在2年内缩水了80%，市值减少了700亿。要计算原来的身价，我们可以用以下公式：<br>

设原来的身价为 \( x \) 亿，那么现在的市值是 \( x \) 的20%。根据题目，这个20%的值比原来少了700亿，所以我们有方程式：<br>

\[ 0.20x = x - 700 \]

我们可以解这个方程来找到原始的市值 \( x \)。现在我将计算它。<br>

朋友原来的身价约为875亿。<br>