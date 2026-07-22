## 第三章 逻辑电路

### 3.1 组合逻辑

#### 3.1.1 基本逻辑运算

泰拉瑞亚组合逻辑电路中存在四种基本逻辑运算：**非、异或、与、独热**。其中非和异或使用逻辑灯完成；与和独热使用逻辑门完成。


::: {.admonition .info}
现实组合逻辑电路中存在三种基本逻辑运算：**与、或、非**。

:::

::: {.admonition .tip}
线或应用于激活用电器，属于时序逻辑电路，此外组合逻辑电路中并不会使用或门，所以或并不属于组合逻辑电路的基本逻辑运算。

:::
##### 非

$$y = \lnot a$$

![](chapters/images/3/1/1/not.png)

##### 异或

$$y = a \oplus b$$

![](chapters/images/3/1/1/xor.png)

##### 与

$$y = a \land b$$

![](chapters/images/3/1/1/and.png)

##### 独热

$$y = \mathrm{OneHot}(a, b)$$

![](chapters/images/3/1/1/one-hot.png)

#### 3.1.2 更多逻辑运算

除了基本逻辑结算和前面介绍的常用逻辑运算外，组合逻辑中还有另外一些经常使用的逻辑运算。

##### 比较

比较运算是比较两个变量的大小或关系，当条件成立时输出 1，否则输出 0。

对于两个变量，可以定义六种基本的比较关系：**小于（LT）、大于（GT）、小于等于（LE）、大于等于（GE）、等于（EQ）、不等于（NE）**。它们在所有输入情况下的输出如下表所示：

| > | 输入 | > | > | > | > | > | 输出 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a | b | $a < b$ | $a > b$ | $a <= b$ | $a >= b$ | $a == b$ | $a\ != b$ |
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 |


::: {.admonition .info}
与运算只有在所有输入都为 1 时才输出 1，其余情况输出 0：

$$
a_1 \land a_2 \land \cdots \land a_n = 
\left\{
    \begin{array}{ll}
        1 & \textrm{当 } a_1 = a_2 = \cdots = a_n = 1 \textrm{ 时} \\
        0 & \textrm{其他情况}
    \end{array}
\right.
$$


:::: {.admonition .example}
![](chapters/images/3/1/2/and_all_one.png)

只有在输入 $a_1$ ~ $a_4$ 全为 1 时，输出才为 1；其余情况输出 0。

::::
如果将与运算的所有输入取反，则逻辑变为：所有输入都为 0 时输出 1，否则输出 0：

$$
\lnot a_1 \land \lnot a_2 \land \cdots \land \lnot a_n = 
\left\{
    \begin{array}{ll}
        1 & \textrm{当 } a_1 = a_2 = \cdots = a_n = 0 \textrm{ 时} \\
        0 & \textrm{其他情况}
    \end{array}
\right.
$$


:::: {.admonition .example}
![](chapters/images/3/1/2/and_all_zero.png)

只有在输入 $a_1$ ~ $a_4$ 全为 0 时，输出才为 1；其余情况输出 0。

::::
若只对部分输入取反，则该逻辑在“未取反的输入为 1，取反的输入为 0”时输出 1，其余情况输出 0：

$$
a_1 \land a_2 \land \cdots \land a_m \land \lnot b_1 \land \lnot b_2 \land \cdots \land \lnot b_n = 
\left\{
    \begin{array}{ll}
        1 & \textrm{当 } a_1 = a_2 = \cdots = a_n = 1 \textrm{ 且} \\ 
            & b_1 = b_2 = \cdots = b_n = 0 \textrm{ 时} \\
        0 & \textrm{其他情况}
    \end{array}
\right.
$$


:::: {.admonition .example}
![](chapters/images/3/1/2/and_half_one.png)

只有在输入 $a_1$ ~ $a_2$ 全为 1 且 $a_1$ ~ $a_2$ 全为 0 时，输出才为 1；其余情况输出 0。

::::
这种只在真值表中某一行输出为 1 的逻辑表达式称为 **最小项**。


:::: {.admonition .example}
对于三输入逻辑函数，若只希望在 $a = 0,\ b = 1,\ c = 1$ 时输出 1，可以使用最小项 $\lnot a \land b \land c$，该表达式仅在这一输入组合下输出 1。


::::: {.admonition .quote}
![](chapters/images/3/1/2/and_lut.png)

只有在输入 $a = 0,\ b = 1,\ c = 1$ 时，输出才为 1；其余情况输出 0。

:::::
::::
最小项中每个输入逻辑变量都会出现，且只会出现一次；每个变量在最小项中都有“取反”和“不取反”两种情况。因此对于 $n$ 个变量，一共有 $2^n$ 个最小项，恰好对应真值表的每一行。任意输入，都只会有一个最小项输出为 1。


:::: {.admonition .example}
三输入变量对应的最小项如下：

| > | > | 输入 | 输出为 1 最小项 |
| --- | --- | --- | --- |
| a | b | c | y |
| 0 | 0 | 0 | $\lnot a \land \lnot b \land \lnot c$ |
| 0 | 0 | 1 | $\lnot a \land \lnot b \land c$ |
| 0 | 1 | 0 | $\lnot a \land b \land \lnot c$ |
| 0 | 1 | 1 | $\lnot a \land b \land c$ |
| 1 | 0 | 0 | $a \land \lnot b \land \lnot c$ |
| 1 | 0 | 1 | $a \land \lnot b \land c$ |
| 1 | 1 | 0 | $a \land b \land \lnot c$ |
| 1 | 1 | 1 | $a \land b \land c$ |

可以看到真值表中某变量为 0，对应最小项中该变量取反；为 1，则不取反。


::::: {.admonition .quote}
![](chapters/images/3/1/2/and_lut_full.png)

三输入全部可能的最小项，一共有 $2^3 = 8$ 个最小项。

:::::
::::
当输出为 1 的情况不止一个时，可以将对应的最小项用异或连接。由于任意输入下最多只有一个最小项为 1，异或运算即可正确合并这些情况。这种由异或连接的最小项称为 **最小项之和**，它可以表示任意逻辑函数。


:::: {.admonition .example}
对于下表所示的三输入逻辑函数：

| > | > | 输入 | 输出 |
| --- | --- | --- | --- |
| a | b | c | y |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

其逻辑表达式可写为：

$$\lnot a \land b \land c \oplus a \land \lnot b \land c \oplus a \land b \land \lnot c \oplus a \land b \land c$$

对应四个输出为 1 的最小项之和。


::::: {.admonition .quote}
![](chapters/images/3/1/2/and_lut_all.png)

满足该真值表对应逻辑函数的电路。

:::::
::::
:::
利用最小项之和，可以得到六种比较运算对应的逻辑表达式：

| 运算 | 记号 | 逻辑表达式 |
| --- | --- | --- |
| 小于 | $a < b$ | $\lnot a \land b$ |
| 大于等于 | $a >= b$ | $\lnot (\lnot a \land b)$ |
| 大于 | $a > b$ | $a \land \lnot b$ |
| 小于等于 | $a <= b$ | $\lnot (a \land \lnot b)$ |
| 不等于 | $a\ != b$ | $a \oplus b$ |
| 等于 | $a == b$ | $\lnot (a \oplus b)$ |

![](chapters/images/3/1/2/compare.png)


::: {.admonition .tip}
可以看到，小于和大于等于、大于和小于等于、不等于和等于两两互为取反；小于和大于、小于等于和大于等于的区别是交换两个输入。在比较电路中，常利用这一性质减少所需的逻辑门数量。


:::: {.admonition .example}
![](chapters/images/3/1/2/compare_all.png)

* **NOT OUT** 控制是否对输出取反，以在小于（**LT**）和大于等于（**GE**）、大于（**GT**）和小于等于（**LE**）、等于（**EQ**）和不等于（**NE**）间切换；
* **SW IN** 交换两个输入，以在小于（**LT**）和大于（**GT**）、大于等于（**GE**）和小于等于（**LE**）间切换；

::::
:::
##### 乘（MUL）

两个变量乘运算的逻辑表达式为：

$$a \cdot b$$


::: {.admonition .info}
读作 a 乘 b。

:::
或者简写为：

$$ab$$

$n$ 个变量乘运算的逻辑表达式为：

$$a_1 \cdot a_2 \cdot \cdots \cdot a_n$$

或者简写为：

$$a_1 a_2 \cdots a_n$$

由乘法关系：

$0 \cdot 0 = 0$
$0 \cdot 1 = 0$
$1 \cdot 0 = 0$
$1 \cdot 1 = 1$

可列出真值表：

| > | 输入 | 输出 |
| --- | --- | --- |
| a | b | y |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |


::: {.admonition .tip}
可以发现与运算就是乘法运算。

$$a \cdot b = a \land b$$

![](chapters/images/3/1/2/mul.png)

:::

::: {.admonition .info}
任何数乘以 0 等于 0，任何数乘以 1 等于其本身。

$$0 \cdot a = 0$$

$$1 \cdot a = a$$

![](chapters/images/3/1/2/mul_0_1.png)

任何数乘以本身等于其本身。

$$a \cdot a = a$$

易得：

$$a \cdot a \cdot \cdots \cdot a = a$$


:::: {.admonition .tip}
证明可通过观察真值表完成。

::::
![](chapters/images/3/1/2/mul_self.png)

:::
##### 加（ADD）、减（SUB）

两个变量加运算的逻辑表达式为：

$$a + b$$


::: {.admonition .info}
读作 a 加 b。

:::
$n$ 个变量加运算的逻辑表达式为：

$$a_1 + a_2 + \cdots + a_n$$


::: {.admonition .question}
$$1 + 1 = \ ?$$

如果是在实数域，我们可以很容易的说出 $1 + 1 = 2$ ，但是在逻辑量中并没有 $2$。实际上，在逻辑运算中 $1 + 1 = 0$。

我们可以用两种方式理解这个结果：

* 如果是有进位加法 $(1 + 1 = 10)_2$，由于逻辑函数只有一位输出，所以抛弃高位的 $1$，只保留低位的 $0$；
* 加法可以理解为在数轴上从一个加数出发，前进另一个加数的距离，对于一个只有 $0$ 和 $1$ 首尾相连的循环数轴，如果从 $1$ 出发前进 $1$，就会到达 $0$。

$$\cdots \xrightarrow{+1} 1 \xrightarrow{+1} 0 \xrightarrow{+1} 1 \xrightarrow{+1} 0 \xrightarrow{+1} 1 \xrightarrow{+1} 0 \xrightarrow{+1} 1 \xrightarrow{+1} \cdots$$

:::
由加法关系：

$0 + 0 = 0$
$0 + 1 = 1$
$1 + 0 = 1$
$1 + 1 = 0$

可列出真值表：

| > | 输入 | 输出 |
| --- | --- | --- |
| a | b | y |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |


::: {.admonition .tip}
可以发现异或运算就是加法运算。

$$a + b = a \oplus b$$

![](chapters/images/3/1/2/add.png)


:::: {.admonition .tip}
双输入异或和独热等价，为便于理解，图中包括使用双灯异或门实现的异或逻辑。

$$a \oplus b = \mathrm{OneHot}(a, b)$$

::::
:::

::: {.admonition .info}
任何数加 0 等于其本身，任何数加 1 等于其本身的非。

$$a + 0 = a$$

$$a + 1 = \lnot a$$

![](chapters/images/3/1/2/add_0_1.png)


:::: {.admonition .tip}
线异或两项中的一项恒为 1 相当于线非。

::::
任何数加本身等于 0。

$$a + a = 0$$

易得：

$$\underbrace{a + a + \cdots + a}_{n} = \begin{cases} 0, & n = 2k, \\[4pt] a, & n = 2k+1, \end{cases} \qquad k \in \mathbb{n}.$$


:::: {.admonition .tip}
证明可通过观察真值表完成。

::::
![](chapters/images/3/1/2/add_self.png)


:::: {.admonition .tip}
奇数个相同项相加等于其本身，偶数个相同项相加等于 0。

::::
![](chapters/images/3/1/2/add_self_many.png)

:::

::: {.admonition .tip}
逻辑运算的结果也是逻辑量，这里的乘法和加法是逻辑量间的一位不进位乘和一位不进位加，并非我们在现实中常见的多位有进位乘和多位有进位加。

$$y = (a \cdot b) \bmod 2$$

$$y = (a + b) \bmod 2$$

由于逻辑量和逻辑运算都在 $GF(2)$ 上，所以可以省略 $\bmod \ 2$。

:::
观察上述数轴可以发现，从一个数出发，向左或向右前进相同距离的结果是一样的。

$$\cdots \xrightleftharpoons[\,-1\,]{\,+1\,} 1 \xrightleftharpoons[\,-1\,]{\,+1\,} 0 \xrightleftharpoons[\,-1\,]{\,+1\,} 1 \xrightleftharpoons[\,-1\,]{\,+1\,} 0 \xrightleftharpoons[\,-1\,]{\,+1\,} 1 \xrightleftharpoons[\,-1\,]{\,+1\,} 0 \xrightleftharpoons[\,-1\,]{\,+1\,} 1 \xrightleftharpoons[\,-1\,]{\,+1\,} \cdots$$

所以可以得出结论：

$$a + b = a - b$$

也就是说，在逻辑运算中，**加减等价**。


::: {.admonition .info}
令 $a = 0$，可得出以下推论：

$$b = -b$$


:::: {.admonition .tip}
取反指非运算，并不是取相反数。

::::
:::
#### 3.1.3 逻辑运算律

##### 交换律、结合律、分配律

加法和乘法满足交换律：

$$a + b = b + a$$

$$a \cdot b = b \cdot a$$


::: {.admonition .example}
![](chapters/images/3/1/3/commutativity.png)

:::
加法和乘法满足结合律：

$$a + (b + c) = (a + b) + c$$

$$a \cdot (b \cdot c) = (a \cdot b) \cdot c$$


::: {.admonition .example}
![](chapters/images/3/1/3/associativity.png)

:::
加法不满足分配律，乘法满足分配律：

$$a + b \cdot c \neq (a + b) \cdot (a + c)$$

$$a \cdot (b + c) = a \cdot b + a \cdot c$$


::: {.admonition .example}
![](chapters/images/3/1/3/distributivity.png)

:::
运算符 $+$、$-$、$\cdot$ 属于代数运算符，使用代数运算符连接的式子被称为 **代数运算式**，简称 **代数式**。相同运算符的运算次序是 **先左后右**，而不同运算符的运算次序是 **先乘法再加法**，若有括号，则 **先进行括号内运算**。


::: {.admonition .example}

:::: {.admonition .question}
证明：任何数乘以本身的非等于 0。

$$a \cdot \lnot a = 0$$

::::

:::: {.admonition .quote}
$$\begin{array}{lll} a \cdot \lnot a & = & a \cdot (a + 1) \\ & = & a \cdot a + a \\ & = & a + a \\ & = & 0 \end{array}$$

::::
![](chapters/images/3/1/3/mul_self_not.png)

:::

::: {.admonition .example}

:::: {.admonition .question}
证明：
$$a \land b = (\lnot a \oplus b) \land b$$

::::

:::: {.admonition .quote}
$$\begin{array}{lll} (\lnot a \oplus b) \land b & = & (a + 1 + b) \cdot b \\ & = & a \cdot b + b + b \cdot b \\ & = & a \cdot b + b + b \\ & = & a \cdot b\end{array}$$

::::

:::: {.admonition .tip}
有时会需要让与门上某些电线从特定逻辑灯引出，这时可以使用这个技巧重叠电线。

![](chapters/images/3/1/3/and_transformatio.png)

::::
:::
##### 普通灯

普通灯是异或逻辑（线异或），输入是其上所有电线连接的所有电源状态和普通灯初始状态，输出是普通灯状态。其上电线连接 $m$ 个电源的普通灯代数式中有 $m$ 项相加，每一项都对应一个其上电线连接的电源，然后再加上普通灯初始状态，灭灯为 0，亮灯为 1。


::: {.admonition .quote}
$$\mathrm{Lamp}(s_1,\cdots,s_m;l_0) = \sum_{i=1}^{m} s_i + l_0$$

$m$ 电源输入的普通灯代数式，$l_0$ 是普通灯本身状态，灭为 0，亮为 1。

:::

::: {.admonition .example}
有时会需要让某根电线穿过双灯异或门而不干扰异或门逻辑。

设异或的两个输入分别为 $m$ 和 $n$，输出为 $y$，则：

$$y = m + n$$

令 $m = a + b,\ n = b$ 则：

$$y = (a + b) + b = a$$

![](chapters/images/3/1/3/xor_anti-interference.png)

$y$ 始终等于 $a$，与 $b$ 的值无关。

:::
##### 与门

与门是与逻辑，输入是其上所有普通灯状态，输出是与门状态，输入输出间关系满足与逻辑。其上有 $n$ 个灯的与门代数式中有 $n$ 项相乘，每一项都对应一个其上普通灯。当与门状态与输出用电器相反时，完整表达式会在与门表达式的基础上加 1 取反。


::: {.admonition .quote}
$$\mathrm{AndGate}(l_1,\cdots,l_n) = \prod_{j=1}^{n} l_j$$

$n$ 灯输入与门代数式。

:::
将普通灯代数式带入与门代数式即可得到由普通灯和与门组成的全与门的代数式。


::: {.admonition .quote}
设与门上第 $j$ 个普通灯表达式如下：

$$l_{1j} = \mathrm{Lamp}(s_{j1},\cdots,s_{jk_j};l_{0j})$$

则全与门代数式如下：

$$
\mathrm{FullAndGate} 
\Big(
    \{s_{ji}\}_{
        \substack{
            1\le j\le n \\
            1\le i\le k_j
        }
    }; 
    \{l_{0j}\}_{j=1}^{n}
\Big) = 
\prod_{j=1}^{n} 
\left(
    \sum_{i=1}^{k_j} s_{ji} + l_{0j} 
\right)
$$

:::

::: {.admonition .example}

:::: {.admonition .question}
写出下列全与门的代数式：

![](chapters/images/3/1/3/and.png)

::::
* $Y_1 = (A + B + 1)(A + B + C)A$

* $Y_2 = (A + C)(A + B + C + 1)C + 1$

* $Y_3 = (B + 1)(A + B + C + 1)(C + 1) + 1$

* $Y_4 = B(A + B + C)(A + 1)$

:::
如果代数式或加一后的代数式可因式分解，每一个因式里只含加法不含乘法，则其对应的逻辑可以只用一个与门实现。


::: {.admonition .tip}
既代数式可以写成如下形式时，对应逻辑可以只用一个与门实现。

$$
f = \prod_{j=1}^{n} \left(\sum_{i} s_{ji} + l_{0j} \right) 
\quad 
\text{or} 
\quad 
f + 1 = \prod_{j=1}^{n} \left(\sum_{i} s_{ji} + l_{0j} \right)
$$

:::
能只使用一个逻辑门实现的逻辑被称为 **简单逻辑**。


::: {.admonition .example}
或运算逻辑式：

$$a \lor b = \lnot (\lnot a \land \lnot b)$$

或运算代数式：

$$ab + a + b$$


:::: {.admonition .quote}
$$
\begin{array}{lll} 
    a \lor b 
    & = & \lnot (\lnot a \land \lnot b) \\ 
    & = & (a + 1)(b + 1) + 1 \\ 
    & = & ab + a + b + 1 + 1 \\ 
    & = & ab + a + b 
\end{array}
$$

::::
或运算代数式可以使用因式分解将其写成因式里只含加法的形式：

$$\begin{array}{lll} ab + a + b & = & ab + a + b + 1 - 1 \\ & = & (a + 1)(b + 1) + 1 \end{array}$$

所以或逻辑可以只用一个与门实现。


:::: {.admonition .tip}
这里利用了推论 $1 = -1$。

::::
![](chapters/images/3/1/3/or.png)

:::

::: {.admonition .example}
逻辑式：

$$(a \lor b) \land (c \lor d)$$

代数式：

$$(ab + a + b)(cd + c + d)$$

代数式及代数式加一都不可将因式中的乘法消除，因此不可只用一个与门表示。

![](chapters/images/3/1/3/or_and.png)

:::
##### 异或门

异或门是独热逻辑，输入是其上所有普通灯状态，输出是异或门状态，输入输出间关系满足独热逻辑。其上有 $n$ 个灯的异或门代数式中有 $n$ 个逻辑变量，每一个逻辑变量都对应一个其上普通灯。当异或门状态与输出用电器相反时，完整表达式会在异或门表达式的基础上加 1 取反。


::: {.admonition .quote}
考虑三输入独热真值表：

| > | > | 输入 | 输出 |
| --- | --- | --- | --- |
| A | B | C | Y |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 |

使用最小项之和写出逻辑式：

$$\mathrm{OneHot}(a, b, c) = \lnot a \land \lnot b \land c \oplus \lnot a \land b \land \lnot c \oplus a \land \lnot b \land \lnot c$$

转换为代数式：

$$
\begin{array}{lll} 
    \mathrm{OneHot}(a, b, c) 
    & = & (a + 1)(b + 1)c + (a + 1)b(c + 1) + a(b + 1)(c + 1) \\ 
    & = & (ab + a + b + 1)c + \\ 
    & & (ac + a + c + 1)b + \\ 
    & & (bc + b + c + 1)a \\ 
    & = & abc + ac + bc + c + \\ 
    & & abc + ab + bc + b + \\ 
    & & abc + ab + ac + a \\ 
    & = & abc + a + b + c
\end{array}
$$


:::: {.admonition .tip}
这里利用了推论 $a + a = 0$，出现奇数次的项被保留，偶数次的项被消掉。

::::
同理四输入独热的表达式为：

$$\mathrm{OneHot}(a, b, c, d) = abc + abd + acd + bcd + a + b + c + d$$


:::: {.admonition .tip}
证明留给读者进行，同样是奇数次的项被保留，偶数次的项被消掉。

::::
:::

::: {.admonition .quote}
由上述结论推广可得：

$$
\mathrm{XorGate}(l_1,\cdots,l_n) = 
\sum_{
    \substack{
        i \subseteq \{1,\cdots,n\} \\ 
        |i| \equiv 1 \pmod{2}
    }
} \; 
\prod_{i \in i} l_i
$$

$n$ 灯输入异或门代数式。

:::
将普通灯代数式带入异或门代数式即可得到由普通灯和异或门组成的全异或门的代数式。


::: {.admonition .quote}
设异或门上第 $j$ 个普通灯表达式如下：

$$l_{1j} = \mathrm{Lamp}(s_{j1},\cdots,s_{jk_j};l_{0j})$$

则全异或门代数式如下：

$$
\mathrm{FullXorGate} 
\Big(
    \{s_{ji}\}_{\substack{
            1\le j\le n \\ 
            1\le i\le k_j
        }
    }; 
    \{l_{0j}\}_{j=1}^{n}
\Big) \\ = 
\sum_{
    \substack{
            I \subseteq \{1, \cdots, n\} \\ 
            |I| \equiv 1 \pmod{2}
        }
    } \; 
\prod_{j \in I} 
\left(
    \sum_{i=1}^{k_j} s_{ji} + l_{0j} 
\right)
$$

:::

::: {.admonition .tip}
同理，如果代数式可以写成如下形式时，对应逻辑可以只用一个异或门实现。

$$
f = \sum_{
    \substack{
        I \subseteq \{1,\cdots,n\} \\ 
        |I| \equiv 1 \pmod{2}
    }
} \; 
\prod_{i \in I} 
\left(
    \sum_{i=1}^{k_j} s_{ji} + l_{0j} 
\right) \\ 
\text{or} \\ 
f + 1 = \sum_{
    \substack{
        I \subseteq \{1,\cdots,n\} \\ 
        |I| \equiv 1 \pmod{2}
    }
} \; 
\prod_{i \in I} 
\left(
    \sum_{i=1}^{k_j} s_{ji} + l_{0j} 
\right)
$$

:::

::: {.admonition .example}

:::: {.admonition .question}
写出下列全异或门的代数式：

![](chapters/images/3/1/3/xor.png)

::::
三灯异或门的代数式为：

$$f = xyz + x + y + z$$

* $y_1 = (a + b + 1)(a + b + c)b + (a + b + 1) + (a + b + c) + b$
$x = a + b + 1,\ y = a + b + c,\ z = b$

* $y_2 = (b + 1)(a + b + c + 1)(c + 1) + (b + 1) + (a + b + c + 1) + (c + 1) + 1$
$x = b + 1,\ y = a + b + c + 1,\ z = c + 1$

* $y_3 = b(a + b + c + 1)a + b + (a + b + c + 1) + a + 1$
$x = b,\ y = a + b + c + 1,\ z = a$

* $y_4 = a(a + b + c)(a + c + 1) + a + (a + b + c) + (a + c + 1) + 1$
$x = a,\ y = a + b + c,\ z = a + c + 1$

:::

::: {.admonition .example}
观察下方电路：

![](chapters/images/3/1/3/xor_to_and.png)

写出代数式为：

$$(abc + a + b + c) + a + b + c = abc$$

满足与逻辑。

观察下方电路：

![](chapters/images/3/1/3/and_to_xor.png)

写出代数式为：

$$(abc) + a + b + c = abc + a + b + c$$ 

满足独热逻辑。

可见可以用与门实现异或门的独热逻辑，也可以用异或门实现与门的与逻辑。

:::

::: {.admonition .example}
三灯异或门的代数式为：

$$f = abc + a + b + c$$

令逻辑灯 $a = x + y,\ b = x + y,\ c = y$，则：

$$f = (x + y)(x + y)y + (x + y) + (x + y) + y = xy$$

满足二输入与逻辑。

![](chapters/images/3/1/3/3_xor_to_2_and.png)

:::

::: {.admonition .example}
三灯异或门的代数式为：

$$f = abc + a + b + c$$

令逻辑灯 $a = x + 1,\ b = y + 1,\ c = 1$，则：

$$f = (x + 1)(y + 1)1 + (x + 1) + (y + 1) + 1 = xy$$

满足二输入与逻辑。

![](chapters/images/3/1/3/3_xor_to_2_and_2.png)

:::

::: {.admonition .info}
易证：

$$\mathrm{OneHot}(0, a_1, a_2, \cdots, a_n) = \mathrm{OneHot}(a_1, a_2, \cdots, a_n)$$

$$\mathrm{OneHot}(1, a_1, a_2, \cdots, a_n) = \lnot a_1 \land \lnot a_2 \land \cdots \land \lnot a_n$$

:::

::: {.admonition .example}
三灯异或门的代数式为：

$$f = abc + a + b + c$$

令逻辑灯 $a = x,\ b = y,\ c = 1,\ z = f + 1$，则：

$$z = (xy1 + x + y + 1) + 1 = xy + x + y$$

满足二输入或逻辑。

![](chapters/images/3/1/3/3_xor_to_2_or.png)

:::
#### 3.1.4 逻辑函数

##### 最小项

任意逻辑函数可以被写成积之和的形式。如果乘积项中每个逻辑变量只出现一次，则该乘积项被称为 **最小项**。每一个最小项对应一个让逻辑函数输出为真的输入情况，而每个让逻辑函数输出为真的输入情况也可以对应写作一个最小项。

对于一个有 $j$ 种输入输出为真的逻辑函数，其逻辑表达式可以被写作 $j$ 个最小项求和的形式，被称为 **最小项之和**。和真值表中输出为 1 的数量一样，$j$ 最小为 $0$，最大为 $2^n$，其中 $n$ 为输入的逻辑变量数。


::: {.admonition .info}
最小项可以被简写为 $m_i$ 的形式，其中 $i$ 代表该最小项输出为真时对应输入转换为十进制的值。


:::: {.admonition .example}
三输入变量对应的最小项和简写如下：

| > | > | 输入 | 最小项 | 简写 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | $\lnot a \cdot \lnot b \cdot \lnot c$ | $m_0$ |
| 0 | 0 | 1 | $\lnot a \cdot \lnot b \cdot c$ | $m_1$ |
| 0 | 1 | 0 | $\lnot a \cdot b \cdot \lnot c$ | $m_2$ |
| 0 | 1 | 1 | $\lnot a \cdot b \cdot c$ | $m_3$ |
| 1 | 0 | 0 | $a \cdot \lnot b \cdot \lnot c$ | $m_4$ |
| 1 | 0 | 1 | $a \cdot \lnot b \cdot c$ | $m_5$ |
| 1 | 1 | 0 | $a \cdot b \cdot \lnot c$ | $m_6$ |
| 1 | 1 | 1 | $a \cdot b \cdot c$ | $m_7$ |

::::
最小项之和可以被写为形如 $m_i + m_j + \cdots + m_k = \sum_{}^{} m(i, j, \cdots, k)$ 的形式。


:::: {.admonition .example}
对于下表所示的三输入逻辑函数：

| > | > | 输入 | 输出 |
| --- | --- | --- | --- |
| a | b | c | y |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

其最小项之和的形式可以写为：

$$\lnot a \cdot b \cdot c + a \cdot \lnot b \cdot c + a \cdot b \cdot \lnot c + a \cdot b \cdot c$$

也可以简写为：

$$m_3 + m_5 + m_6 + m_7 = \sum_{}^{} m(3, 5, 6, 7)$$

::::
:::
通常我们已知逻辑函数，需要找到满足逻辑函数的电路表示。此时我们需要先将逻辑函数写成积之和，也就是最小项之和的形式，然后将积之和转换为和之积，以满足与门或异或门的格式。但利用运算律和因数分解进行转换都是比较困难的。

##### 字符串

在逻辑表达式中，逻辑量也被称为 **字母**，而若干字母使用加法连接而成的表达式被称为 **字符串**，简称 **串**。

由 0 个字符连接成的表达式记作 0，称为 **空串**；0 和 1 两个串称为 **平凡串**；除 0 和 1 外的串被称为 **非平凡串**。如果两个串恒等（等价），那么这两个串相同。


::: {.admonition .info}
字母顺序不同的串仍等价：

$$a + b = b + a$$

连接 1 相当于对字母取反：

$$a + 1 = \lnot a$$

连接 0 可以直接消掉：

$$a + 0 = a$$

一对重复字母可以抵消：

$$a + a = 0$$

:::
对于 $n$ 个字母，可以组成 $2^n$ 个不同的串，每个字母在串中都有存在和不存在两种可能。


::: {.admonition .example}
由字母 $1$、$a$、$b$ 组成的不同的串有 8 个：$0$、$1$、$a$、$b$、$a + b$、$a + 1$、$b + 1$、$a + b + 1$。


:::: {.admonition .tip}
一个串中可以包含重复的字母，但是由于性质 $a + a = 0$ 和 $a + 0 = a$，一对重复字母可以直接抵消。

::::
:::
给定一组串 $s_1$、$s_2$、$\cdot$、$s_r$，任选其中若干串（至少一个）求和，得到的串称为这组串的一个 **线性组合**。

如果一组非平凡串存在至少一个线性组合为平凡串（0 或 1），那么我们称这组非平凡串 **线性相关**；否则如果一组非平凡串的全部线性组合都是非平凡串，那么我们称这组非平凡串 **线性无关**。一组非平凡串的最大线性无关的子集的大小称为这组非平凡串的 **秩**。


::: {.admonition .example}
考虑三个串 $a + b$、$a + b + c$、$a + b + c + d$。

令

$x = a + b$
$y = a + b + c$
$z = a + b + c + d$

那么 $x$、$y$、$z$ 的所有不同线性组合为：

$x = a + b$
$y = a + b + c$
$z = a + b + c + d$
$x + y = c$
$x + z = c + d$
$y + z = d$
$x + y + z = a + b + d$

所有线性组合都是非平凡串，所以 $a + b$、$a + b + c$、$a + b + c + d$ 线性无关，$\{a + b, a + b + c, a + b + c + d\}$ 的最大线性无关子集就是它本身，其秩为 3。

:::

::: {.admonition .example}
考虑三个串 $a + b$、$b + c$、$a + c$。

令

$x = a + b$
$y = b + c$
$z = a + c$

那么 $x$、$y$、$z$ 的所有不同线性组合为：

$x = a + b$
$y = b + c$
$z = a + c$
$x + y = a + c$
$x + z = b + c$
$y + z = a + b$
$x + y + z = 0$


:::: {.admonition .tip}
注意到：

$x = y + z = a + b$
$y = x + z = b + c$
$z = x + y = a + c$

::::
其中 $x + y + z = 0$ 是平凡串，所以 $a + b$、$b + c$、$a + c$ 线性相关。

$\{a + b, b + c, a + c\}$ 的一个子集是 $\{a + b, b + c\}$

令

$x = a + b$
$y = b + c$

那么 $x$、$y$ 的所有不同线性组合为：

$x = a + b$
$y = b + c$
$x + y = a + c$

都是非平凡串，所以 $a + b$、$b + c$ 线性无关。$\{a + b, b + c\}$ 是 $\{a + b, b + c, a + c\}$ 的其中一个最大线性无关子集，大小为 2。

则 $a + b$、$b + c$、$a + c$ 的秩为 2。

:::
记一组串的秩为 $r$，那么这组串拥有的不同非平凡线性组合数量为 $2^r - 1$。反之，一组串拥有的不同非平凡线性组合数量一定有形式 $2^r - 1$，并且在该形式下这组串的秩为 $r$。


::: {.admonition .example}
考虑三个串：$a + b$、$a + b + c$、$a + b + c + d$，其秩为 3，则其有 $2^3 - 1 = 7$ 个不同的非线性组合：$a + b$、$a + b + c$、$a + b + c + d$、$c$、$c + d$、$d$、$a + b + d$；对于有 7 个不同的非线性组合的多个串，其秩为 $\log_2 (7+1) = 3$。

考虑三个串：$a + b$、$b + c$、$a + c$，其秩为 2，则其有 $2^2 - 1 = 3$ 个不同的非线性组合：$a + b$、$b + c$、$a + c$；对于有 3 个不同的非线性组合的多个串，其秩为 $\log_2(3+1) = 2$。

:::

::: {.admonition .info}
秩为 $r$ 的一组互不相同的非平凡串至多有 $2^r - 1$ 个。$n$ 个互不相同的非平凡串的秩至少为 $\lceil\log_2 (n+1)\rceil$。


:::: {.admonition .example}
对于秩为 3 的一组互不相同的非平凡串，如果用字母 $a$、$b$、$c$ 表示，最多可以写出：$a$、$b$、$c$、$a + b$、$a + c$、$b + c$、$a + b + c$ 七个，也就是三个字母所有可能组成的串去掉 $0$ 剩下的情况。其中任选两个串，其秩至少为 $\lceil\log_2 (2+1)\rceil = 2$，任选三个串，其秩至少为 $\lceil\log_2 (3+1)\rceil = 2$。

::::
:::
##### 单输入单普通灯方程


::: {.admonition .example}

:::: {.admonition .question}
对于逻辑函数 $f(a, b, c)$，当且仅当 $a, b, c = 1, 0, 0$ 或 $0, 1, 1$ 时取值为 1；其余情况取值为 0，求函数 $f$ 的单与门表示。

::::
对于三个字母 $a$、$b$、$c$ 组成的非平凡串，有 $a; b; c; a + b; a + c; b + c; a + b + c$ 七种情况。对于输入 $a, b, c = 1, 0, 0$ 或 $0, 1, 1$，总有线性无关串 $a + b$ 和 $b + c + 1$ 同时为 1。若 $f$ 可以分解为线性因式的乘积，那么这些线性因式在所有使 $f = 1$ 的最小项上，都必须取值为 1，因此，因式一定取自这些在最小项集合上恒等为 1 的非平凡串。不妨构造 $f = (a + b)(b + c + 1)$，经过验证，符合题意。

![](chapters/images/3/1/4/and_example_1.png)


:::: {.admonition .tip}
当变量数量较少且函数可以被分解为线性因式时，我们可以通过在给定最小项集合上，寻找一组线性无关且恒等为 1 的非平凡串来得到可能的因式。

不过这种方法依赖枚举与观察，接下来将介绍更通用的方法。

::::
:::
考虑前述 $m$ 输入，初始状态 $l_0$ 的普通灯通式：

$$\mathrm{Lamp}(s_1,\cdots,s_m;l_0) = \sum_{i=1}^{m} s_i + l_0$$

当输入的电源并没有全部连接到逻辑灯时，引入表示输入电源 $s_i$ 与逻辑灯的电线连接关系的项 $w_i$，当该电源通过电线连接到逻辑灯时，$w_i = 1$，当该电源没有通过电线连接到逻辑灯时，$w_i = 0$。

设有 $n$ 个输入电源，普通灯的初始状态 $l_0$，普通灯的最终状态 $l_1$。

则该普通灯终态表达式可以写为：

$$\sum_{i=1}^{n} w_i s_i + l_0 = l_1$$

对于这样的表达式，我们可以使用向量简化表示。

设电线连接向量为 $\mathbf{w}$

$$\mathbf{w} = (w_1, \cdots, w_n)$$

设电源状态向量为 $\mathbf{s}$

$$\mathbf{s} = (s_1, \cdots, s_n)$$


::: {.admonition .tip}
$\mathbf{s}$ 和 $\mathbf{w}$ 的维度相同，都是 $n$。标量、向量、矩阵进行乘法和加法运算时，要求对应维度相同。

:::
则该普通灯在输入一个向量后的终态表达式为：

$$\mathbf{w}\, \mathbf{s}^{\mathrm{T}} + l_0 = l_1$$

既：

$$
\begin{pmatrix} 
    w_1 & w_2 & \cdots & w_n 
\end{pmatrix} 
\begin{pmatrix} 
    s_1 \\ s_2 \\ \vdots \\ s_n 
\end{pmatrix} + l_0 = l_1
$$

$$w_1 s_1 + w_2 s_2 + \cdots + w_n s_n + l_0 = l_1$$


::: {.admonition .example}

:::: {.admonition .question}
考虑以下三输入普通灯：

![](chapters/images/3/1/4/and_example_2_1.png)

根据电线接法和输入状态，列出普通灯的表达式并求得普通灯终态：

![](chapters/images/3/1/4/and_example_2_2.png)

::::
$\mathbf{w}_1 = (1, 0, 1);\ \mathbf{s}_1 = (1, 1, 0);\ l_{01} = 0;$

$
l_{11} = 
\mathbf{w}_1\, \mathbf{s}_1^{\mathrm{T}} + l_{01} = 
\begin{pmatrix} 
    1 & 0 & 1 
\end{pmatrix} 
\begin{pmatrix} 
    1 \\ 1 \\ 0 
\end{pmatrix} + 0 = 
1 + 0 = 1
$

$\mathbf{w}_2 = (0, 1, 1);\ \mathbf{s}_1 = (1, 0, 1);\ l_{02} = 1;$

$
l_{12} = \mathbf{w}_2\, \mathbf{s}_2^{\mathrm{T}} + l_{02} = 
\begin{pmatrix} 
0 & 1 & 1 
\end{pmatrix} 
\begin{pmatrix} 
    1 \\ 0 \\ 1 
\end{pmatrix} + 1 = 
1 + 1 = 0
$

$\mathbf{w}_3 = (1, 0, 0);\ \mathbf{s}_1 = (0, 1, 1);\ l_{03} = 1;$

$
l_{13} = \mathbf{w}_3\, \mathbf{s}_3^{\mathrm{T}} + l_{03} = 
\begin{pmatrix} 
    1 & 0 & 0 
\end{pmatrix} 
\begin{pmatrix} 
    0 \\ 1 \\ 1 
\end{pmatrix} + 1 = 
0 + 1 = 1
$

:::
##### 单输入多普通灯方程

设全普通门上有 $m$ 个普通灯，有 $n$ 个输入电源。其中第 $j$ 个逻辑灯初始状态为 $l_{j0}$，电线连接为 $\mathbf{w}_j$，初态 $l_{0j}$，终态 $l_{1j}$，则其表达式为：

$$l_{1j} = \mathbf{w}_j\,\mathbf{s}^{\mathrm{T}} + l_{0j}$$

对于多个标量，我们可以将它们合并为向量表示；对于多个向量，我们可以将它们合并为矩阵表示。

设电线连接矩阵为 $\mathbf{W}$

$$
\mathbf{W} = 
\begin{pmatrix}
    \mathbf{w}_1 \\
    \mathbf{w}_2 \\
    \vdots \\ 
    \mathbf{w}_m
\end{pmatrix} = 
\begin{pmatrix} 
    w_{11} & w_{12} & \cdots & w_{1n} \\ 
    w_{21} & w_{22} & \cdots & w_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    w_{m1} & w_{m2} & \cdots & w_{mn} 
\end{pmatrix}$$

设电源状态向量为 $\mathbf{s}$

$$\mathbf{s} = (s_1, \cdots, s_n)$$

设逻辑灯初态向量为 $\mathbf{l}_0$

$$\mathbf{l}_0 = (l_{01}, \cdots, l_{0m})$$

设逻辑灯终态向量为 $\mathbf{l}_1$

$$\mathbf{l}_1 = (l_{11}, \cdots, l_{1m})$$

则多个普通灯在输入一个向量后的终态表达式为

$$\mathbf{W}\, \mathbf{s}^{\mathrm{T}} + \mathbf{l}_0^{\mathrm{T}} = \mathbf{l}_1^{\mathrm{T}}$$

既：

$$
\begin{pmatrix} 
    w_{11} & w_{12} & \cdots & w_{1n} \\ 
    w_{21} & w_{22} & \cdots & w_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    w_{m1} & w_{m2} & \cdots & w_{mn} 
\end{pmatrix} 
\begin{pmatrix} 
    s_1 \\ s_2 \\ \vdots \\ s_n
\end{pmatrix} + 
\begin{pmatrix} 
    l_{01} \\ l_{02} \\ \vdots \\ l_{0m} 
\end{pmatrix} = 
\begin{pmatrix} 
    l_{11} \\ l_{12} \\ \vdots \\ l_{1m} 
\end{pmatrix}
$$


::: {.admonition .example}

:::: {.admonition .question}
考虑以下三输入全普通门上的逻辑灯：

![](chapters/images/3/1/4/and_example_3_1.png)

根据电线接法和输入状态，列出全部普通灯的表达式并求得普通灯终态：

![](chapters/images/3/1/4/and_example_3_2.png)

::::
$
\mathbf{W}_1 = 
\begin{pmatrix} 
    1 & 1 & 0 \\ 
    0 & 1 & 1 
\end{pmatrix};\ 
\mathbf{s}_1 = (0, 1, 1);\ 
\mathbf{l}_{01} = (1, 1);
$

$
\mathbf{l}_{11} = 
\mathbf{W}_1\, \mathbf{s}_1^{\mathrm{T}} + \mathbf{l}_{01}^{\mathrm{T}} = 
\begin{pmatrix} 
    1 & 1 & 0 \\ 
    0 & 1 & 1 
\end{pmatrix}\, 
\begin{pmatrix} 
    0 \\ 1 \\ 1 
\end{pmatrix} + 
\begin{pmatrix} 
    1 \\ 1 
\end{pmatrix} = 
\begin{pmatrix} 
    1 \\ 0 
\end{pmatrix} + 
\begin{pmatrix} 
    1 \\ 1 
\end{pmatrix} = 
\begin{pmatrix} 
    0 \\ 1 
\end{pmatrix}
$

$
\mathbf{W}_2 = 
\begin{pmatrix} 
    1 & 1 & 0 \\ 
    0 & 0 & 1 
\end{pmatrix};\ 
\mathbf{s}_1 = (1, 0, 1);\ 
\mathbf{l}_{01} = (0, 1);
$

$
\mathbf{l}_{12} = 
\mathbf{W}_2\, \mathbf{s}_2^{\mathrm{T}} + \mathbf{l}_{02}^{\mathrm{T}} = 
\begin{pmatrix} 
    1 & 1 & 0 \\ 
    0 & 0 & 1 
\end{pmatrix}\, 
\begin{pmatrix} 
    1 \\ 0 \\ 1 
\end{pmatrix} + 
\begin{pmatrix} 
    0 \\ 1 
\end{pmatrix} = 
\begin{pmatrix} 
    1 \\ 1 
\end{pmatrix} + 
\begin{pmatrix} 
    0 \\ 1 
\end{pmatrix} = 
\begin{pmatrix} 
    1 \\ 0 
\end{pmatrix}
$

:::
与门在其上全部普通灯点亮时点亮；异或门在其上只有一个普通灯点亮时点亮。也就是说，与门在输入最小项时，其上逻辑灯终态向量全部元素为 1；异或门在输入最小项时，其上逻辑灯终态向量中有且仅有一个元素是 1。而对于非最小项的输入，逻辑灯终态是其余情况，不会满足逻辑门点亮条件，无需关注。


::: {.admonition .quote}
$$\mathbf{W}\, \mathbf{s}^{\mathrm{T}} + \mathbf{l}_0^{\mathrm{T}} = \mathbf{l}_1^{\mathrm{T}}$$

当逻辑门为与门，且输入最小项时，逻辑灯终态向量元素全部为 1。

$$\mathbf{l}_1 = (1, 1, \cdots, 1)$$

当逻辑门为异或门，且输入最小项时，逻辑灯终态向量元素中只有一个 1。

$$\mathbf{l}_1 = (0, 0, \cdots, 0, 1, 0, \cdots, 0)$$

:::

::: {.admonition .example}

:::: {.admonition .question}
将该电路使用最小项之和的形式表示：

![](chapters/images/3/1/4/and_example_4.png)

::::
由图可得逻辑灯初态向量为 $\mathbf{l}_0 = (0, 1)$，逻辑门为与门，输入为最小项时输出逻辑灯全亮，所以逻辑灯终态向量为 $\mathbf{l}_1 = (1, 1)$，接线矩阵为 $\mathbf{W} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$。

设输入最小项向量为 $\mathbf{s} = (a, b, c)$，则

$$\mathbf{W}\, \mathbf{s}^{\mathrm{T}} + \mathbf{l}_0^{\mathrm{T}} = \mathbf{l}_1^{\mathrm{T}}$$

带入可得

$$
\begin{pmatrix} 
    1 & 1 & 0 \\ 
    0 & 1 & 1 
\end{pmatrix}\, 
\begin{pmatrix} 
    a \\ b \\ c 
\end{pmatrix} + 
\begin{pmatrix} 
    0 \\ 1 
\end{pmatrix} = 
\begin{pmatrix} 
    1 \\ 1 
\end{pmatrix}
$$

化简得

$$
\left\{
    \begin{aligned}
        a + b = 1 \\ 
        b + c = 0
    \end{aligned}
\right.
$$

当 $a = 0$ 时，$b = 1$，$c = 1$；

当 $a = 1$ 时，$b = 0$，$c = 0$。

综上，该电路有两个最小项，分别是 $011$ 和 $100$。

:::
##### 多输入多普通灯方程

设全普通门上有 $m$ 个普通灯，有 $n$ 个输入电源，有 $p$ 个输入向量。其中第 $k$ 个输入向量为 $\mathbf{s}_{k}$，对应的逻辑灯初态向量为 $\mathbf{l}_{0k}$，逻辑灯终态向量为 $\mathbf{l}_{1k}$。

同理，当有多个输入向量时，我们也可以将它们合并为矩阵。

设电源状态矩阵为 $\mathbf{S}$

$$
\mathbf{S} = 
\begin{pmatrix} 
    \mathbf{s}_1 \\ 
    \mathbf{s}_2 \\ 
    \vdots \\ 
    \mathbf{s}_p 
\end{pmatrix} = 
\begin{pmatrix} 
    s_{11} & s_{12} & \cdots & s_{1n} \\ 
    s_{21} & s_{22} & \cdots & s_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    s_{p1} & s_{p2} & \cdots & s_{pn} 
\end{pmatrix}
$$

设电线连接矩阵为 $\mathbf{W}$

$$
\mathbf{W} = 
\begin{pmatrix}
    \mathbf{w}_1 \\
    \mathbf{w}_2 \\
    \vdots \\
    \mathbf{w}_m
\end{pmatrix} = 
\begin{pmatrix} 
    w_{11} & w_{12} & \cdots & w_{1n} \\
    w_{21} & w_{22} & \cdots & w_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    w_{m1} & w_{m2} & \cdots & w_{mn} 
\end{pmatrix}
$$

设逻辑灯初态矩阵为 $\mathbf{L}_0$

$$
\mathbf{L}_0 = 
\begin{pmatrix}
    \mathbf{l}_{01} \\
    \mathbf{l}_{02} \\
    \vdots \\
    \mathbf{l}_{0p}
\end{pmatrix} = 
\begin{pmatrix} 
    l_{011} & l_{012} & \cdots & l_{01m} \\ 
    l_{021} & l_{022} & \cdots & l_{02m} \\ 
    \vdots & \vdots & & \vdots \\ 
    l_{0p1} & l_{0p2} & \cdots & l_{0pm} 
\end{pmatrix}
$$

设逻辑灯终态矩阵为 $\mathbf{L}_1$

$$
\mathbf{L}_1 = 
\begin{pmatrix}
    \mathbf{l}_{11} \\
    \mathbf{l}_{12} \\
    \vdots \\ 
    \mathbf{l}_{1p}
\end{pmatrix} = 
\begin{pmatrix} 
    l_{111} & l_{112} & \cdots & l_{11m} \\ 
    l_{121} & l_{122} & \cdots & l_{12m} \\ 
    \vdots & \vdots & & \vdots \\ 
    l_{1p1} & l_{1p2} & \cdots & l_{1pm} 
\end{pmatrix}
$$

则多个普通灯在输入多个向量后的终态表达式为

$$\mathbf{W}\, \mathbf{S}^{\mathrm{T}} + \mathbf{L}_0^{\mathrm{T}} = \mathbf{L}_1^{\mathrm{T}}$$

既

$$
\begin{pmatrix} 
    w_{11} & w_{12} & \cdots & w_{1n} \\ 
    w_{21} & w_{22} & \cdots & w_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    w_{m1} & w_{m2} & \cdots & w_{mn} 
\end{pmatrix} 
\begin{pmatrix} 
    s_{11} & s_{12} & \cdots & s_{1n} \\ 
    s_{21} & s_{22} & \cdots & s_{2n} \\ 
    \vdots & \vdots & & \vdots \\ 
    s_{p1} & s_{p2} & \cdots & s_{pn} 
\end{pmatrix}^{\mathrm{T}} + \\ \ \\ 
\begin{pmatrix} 
    l_{011} & l_{012} & \cdots & l_{01m} \\ 
    l_{021} & l_{022} & \cdots & l_{02m} \\ 
    \vdots & \vdots & & \vdots \\ 
    l_{0p1} & l_{0p2} & \cdots & l_{0pm} 
\end{pmatrix}^{\mathrm{T}} = 
\begin{pmatrix} 
    l_{111} & l_{112} & \cdots & l_{11m} \\ 
    l_{121} & l_{122} & \cdots & l_{12m} \\ 
    \vdots & \vdots & & \vdots \\ 
    l_{1p1} & l_{1p2} & \cdots & l_{1pm} 
\end{pmatrix}^{\mathrm{T}}
$$

##### 全逻辑门方程

对于多个逻辑灯在输入多个向量后的终态表达式

$$\mathbf{W}\, \mathbf{S}^{\mathrm{T}} + \mathbf{L}_0^{\mathrm{T}} = \mathbf{L}_1^{\mathrm{T}}$$

将两边取转置得

$$\mathbf{S}\, \mathbf{W}^{\mathrm{T}} + \mathbf{L}_0 = \mathbf{L}_1$$

对于同一全逻辑门，初始逻辑灯相同，可令

$$
    \mathbf{S}_1 = 
    (\mathbf{S} | \mathbf{1}) = 
    \begin{pmatrix} 
        s_{11} & s_{12} & \cdots & s_{1n} & 1 \\ 
        s_{21} & s_{22} & \cdots & s_{2n} & 1 \\ 
        \vdots & \vdots & & \vdots & \vdots \\ 
        s_{p1} & s_{p2} & \cdots & s_{pn} & 1 
    \end{pmatrix}
$$

$$
    \mathbf{W}_1 = 
    (\mathbf{W} | \mathbf{l}_0^{\mathrm{T}}) = 
    \begin{pmatrix} 
        w_{11} & w_{12} & \cdots & w_{1n} & l_{01} \\ 
        w_{21} & w_{22} & \cdots & w_{2n} & l_{02} \\ 
        \vdots & \vdots & & \vdots & \vdots \\ 
        w_{m1} & w_{m2} & \cdots & w_{mn} & l_{0m} 
    \end{pmatrix}
$$

$$
    \mathbf{L}_1 = 
    \begin{pmatrix} 
        l_{111} & l_{112} & \cdots & l_{11m} \\ 
        l_{121} & l_{122} & \cdots & l_{12m} \\ 
        \vdots & \vdots & & \vdots \\ 
        l_{1p1} & l_{1p2} & \cdots & l_{1pm} 
    \end{pmatrix}
$$

则上式可写为

$$\mathbf{S}_1\, \mathbf{W}_1^{\mathrm{T}} = \mathbf{L}_1$$

既

$$
\begin{pmatrix} 
    s_{11} & s_{12} & \cdots & s_{1n} & 1 \\ 
    s_{21} & s_{22} & \cdots & s_{2n} & 1 \\ 
    \vdots & \vdots & & \vdots & \vdots \\ 
    s_{p1} & s_{p2} & \cdots & s_{pn} & 1 
\end{pmatrix} 
\begin{pmatrix} 
    w_{11} & w_{12} & \cdots & w_{1n} & l_{01} \\ 
    w_{21} & w_{22} & \cdots & w_{2n} & l_{02} \\ 
    \vdots & \vdots & & \vdots & \vdots \\ 
    w_{m1} & w_{m2} & \cdots & w_{mn} & l_{0m} 
\end{pmatrix}^{\mathrm{T}} = 
\begin{pmatrix} 
    l_{111} & l_{112} & \cdots & l_{11m} \\ 
    l_{121} & l_{122} & \cdots & l_{12m} \\ 
    \vdots & \vdots & & \vdots \\ 
    l_{1p1} & l_{1p2} & \cdots & l_{1pm} 
\end{pmatrix}
$$

在已知最小项求解电线连接和逻辑灯初态时，最小项矩阵 $\mathbf{S}_1$ 和逻辑灯终态矩阵 $\mathbf{L}_1$ 已知，接线与逻辑灯初态矩阵 $\mathbf{W}_1$ 未知，求解该矩阵方程即可得到电线连接和逻辑灯初态。

当已知接线 $\mathbf{W}_1$，求最小项 $\mathbf{S}_1$ 时，可以同时对两边求转置

$$\mathbf{W}_1\, \mathbf{S}_1^{\mathrm{T}} = \mathbf{L}_1^{\mathrm{T}}$$

##### 矩阵的初等变换

下面两种变换称为矩阵的 **初等行变换**：

* 将矩阵的两行交换；
* 将矩阵的某行加到另一行上。

记矩阵的第 $i$ 行为 $r_i$，则交换第 $i$ 行和第 $j$ 行被记为 $r_i \leftrightarrow r_j$，将第 $i$ 行加到第 $j$ 行被记为 $r_i + r_j$。

$$
\begin{pmatrix} 
    a_{11} & a_{12} & \cdots & a_{1n} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{i1} & a_{i2} & \cdots & a_{in} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{j1} & a_{j2} & \cdots & a_{jn} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{pmatrix} 
\xrightarrow{r_i \leftrightarrow r_j} 
\begin{pmatrix} 
    a_{11} & a_{12} & \cdots & a_{1n} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{j1} & a_{j2} & \cdots & a_{jn} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{i1} & a_{i2} & \cdots & a_{in} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{pmatrix}
$$

$$
\begin{pmatrix} 
    a_{11} & a_{12} & \cdots & a_{1n} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{i1} & a_{i2} & \cdots & a_{in} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{j1} & a_{j2} & \cdots & a_{jn} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{pmatrix} 
\xrightarrow{r_i + r_j} 
\begin{pmatrix} 
    a_{11} & a_{12} & \cdots & a_{1n} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{i1} & a_{i2} & \cdots & a_{in} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{j1} + a_{i1} & a_{j2} + a_{i2} & \cdots & a_{jn} + a_{in} \\ 
    \vdots & \vdots & & \vdots \\ 
    a_{m1} & a_{m2} & \cdots & a_{mn} 
\end{pmatrix}
$$

而我们将初等行变换定义中的“行”换成“列”，就得到了 **初等列变换** 的定义。记矩阵的第 $i$ 列为 $c_i$，则交换第 $i$ 行和第 $j$ 列被记为 $c_i \leftrightarrow c_j$，将第 $i$ 列加到第 $j$ 列被记为 $c_i + c_j$。矩阵的初等行变换和初等列变换统称为矩阵的 **初等变换**。

如果矩阵 $\mathbf{A}$ 可以经过有限次初等变换变成矩阵 $\mathbf{B}$，则称矩阵 $\mathbf{A}$ 与 $\mathbf{B}$ 等价。

当我们只使用初等行变换对矩阵进行变换时，可以得到一种特殊的矩阵，其特点是：

* 矩阵中全部元素为 0 的行都在矩阵的最下面；
* 每行左起第一个非 0 元素的下方元素都为 0。

这种特殊的矩阵被称为 **行阶梯形矩阵**，将普通矩阵变换为行阶梯形矩阵后，行阶梯形矩阵中的非零行的数量就是该矩阵的秩。


::: {.admonition .example}

:::: {.admonition .quote}
$$
\begin{pmatrix}
    1 & 1 & 0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 1 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$

行阶梯形矩阵

::::
我们可以在行阶梯形矩阵中画一条阶梯线让阶梯线下方全部元素为 0，阶梯线中的每个竖线都在每行的首个非零元素的左边，每个横线下方元素都是 0，每个阶梯只有一行，阶梯数就是非零行的行数。

:::
##### 解的存在性

在对逻辑门方程求解时，我们需要先判断方程是否有解，判断的方法如下：

先将两个已知矩阵：最小项矩阵 $\mathbf{S}_1$ 和逻辑门矩阵 $\mathbf{L}_1$ 合并为一个新的增广矩阵

$$
(\mathbf{S}_1 | \mathbf{L}_1) =
\left(
    \begin{array}{ccccc|ccccc} 
        s_{11} & s_{12} & \cdots & s_{1n} & 1 & l_{111} & l_{112} & \cdots & l_{11m} \\ 
        s_{21} & s_{22} & \cdots & s_{2n} & 1 & l_{121} & l_{122} & \cdots & l_{12m} \\ 
        \vdots & \vdots & & \vdots & \vdots & \vdots & \vdots & & \vdots \\ 
        s_{p1} & s_{p2} & \cdots & s_{pn} & 1 & l_{1p1} & l_{1p2} & \cdots & l_{1pm} 
    \end{array}
\right)
$$

然后将增广矩阵只使用初等行变换，转换为行阶梯矩阵。对于新的行阶梯矩阵，按照来自 $\mathbf{S}_1$ 和 $\mathbf{L}_1$ 的列重新划分为两个矩阵 $\boldsymbol{S}_1$ 和 $\boldsymbol{L}_1$。

当全部在新系数矩阵 $\boldsymbol{S}_1$ 中为全零的行在新常数矩阵 $\boldsymbol{L}_1$ 中对应的行也全零时，矩阵方程有解。

当存在在新系数矩阵 $\boldsymbol{S}_1$ 中为全零的行在新常数矩阵 $\boldsymbol{L}_1$ 中对应的行不为全零时，说明存在常数无法用未知数线性表示，存在矛盾方程，矩阵方程无解。

##### 解的数量




<div STYLE="page-break-after: always;"></div>
