## 第二章 电路基础

### 2.1 电源、电线、用电器

#### 2.1.1 电路激活过程

在泰拉瑞亚中，电路由电源、电线、用电器组成，电源在满足条件时会产生一个脉冲，经电线传导到用电器，用电器响应该信号。电源和用电器统称 **电路物品**，也就是参与电路的物块。


::: {.admonition .example}
![](chapters/images/2/1/1/wiring.png)

电路由电源（开关）、电线（红色电线）、用电器（火把）组成。

:::
电路物品处于物块图层，而电线在单独的电线图层，与电路物品处于不同的图层，它们可以重叠。如果某电线与某电路物品重叠，我们说该电路物品在该电线下，该电线在该电路物品上。


::: {.admonition .example}
![](chapters/images/2/1/1/wiring_layer.png)

电源（开关）和用电器（火把）位于物块图层，电线（红色电线）位于电线图层。

:::
接下来的讨论中，将会用激活来表示电路的活跃状态：**电源激活 $\rightarrow$ 电源上的电线激活 $\rightarrow$ 电线下的用电器激活**。电源的激活指电源通过其上电线发出信号，电线的激活指其传递其下电源发出的信号到其下用电器，用电器的激活指其上电线被激活。


::: {.admonition .example}
![](chapters/images/2/1/1/wiring_active.png)

$\textcircled{1}$ 电源（开关）激活 $\rightarrow$ $\textcircled{2}$ 电源上的电线（红色电线）激活 $\rightarrow$ $\textcircled{3}$ 电线下的用电器（火把）激活

:::
#### 2.1.2 电路物品

电源指可以激活其上电线的物块，每个电源有特定的激活条件。逻辑门被称为 **逻辑电源**，除了逻辑门以外的电源被称为 **物理电源**。物理电源可以将非电信号转换为电信号，是逻辑电路的输入端口。只有物理电源可以新建逻辑结算，逻辑电源不能新建逻辑结算。


::: {.admonition .example}
![](chapters/images/2/1/2/source.png)

电源包括开关、拉杆、压力板、逻辑感应器等。

:::
用电器指可被其上电线激活的物块，每个用电器有特定的响应方式。逻辑门灯被称为 **逻辑用电器**，除了逻辑门灯以外的用电器被称为 **物理用电器**。物理用电器可以将电信号转换为非电信号，是逻辑电路的输出端口。


::: {.admonition .example}
![](chapters/images/2/1/2/drain.png)

用电器火把、传送机、传送枪站、机关等。

:::
逻辑电源和逻辑用电器统称逻辑 **电路物品**，物理电源和物理用电器统称 **物理电路物品**。

而只由电线和逻辑电路物品（逻辑门和逻辑门灯）组成的电路被称为 **逻辑电路**。电路是由 **输入端口、逻辑电路、输出端口** 组成的。


::: {.admonition .example}
![](chapters/images/2/1/2/logic.png)

输入端口（开关）、逻辑电路（逻辑门、逻辑门灯、电线）、输出端口（火把）。

:::

::: {.admonition .info}
存在即是电源又是用电器的图格，如计时器。

:::

::: {.admonition .tip}
物理电源和物理用电器的激活条件和响应方式可查阅附录。

:::
##### 多图格电路物品

对于由多个图格组成的电源，并不会因为一根电线连接该电源的多个图格而增加电源激活时该电线的激活次数，电线只连接多图格电源的一个图格和多个图格是一样的。在电源激活时，其上的每根电线都只会被激活一次。


::: {.admonition .example}
![](chapters/images/2/1/2/multitile_source.png)

左右两种连接方式完全一样，尽管第二种连接了更多图格。

:::

::: {.admonition .tip}
不同颜色的电线或同颜色但中间没有连接的电线不是一根电线，在电源激活时，其上的每根电线都会被激活一次。

:::

::: {.admonition .example}
![](chapters/images/2/1/2/multitile_source_wires.png)

激活拉杆时，左边的火把会被红线激活一次，点亮；中间的火把会被蓝线激活一次，点亮；右边的火把会被蓝线激活一次，红线激活一次，先点亮后熄灭（过程不可见）。

:::
对于由多个图格组成的用电器，并不会因为一根电线连接该用电器的多个图格而增加该电线激活时该用电器的响应次数，电线只连接多图格用电器的一个图格和多个图格是一样的。在一根电线激活时，其下的用电器只会响应一次。


::: {.admonition .example}
![](chapters/images/2/1/2/multitile_drain.png)

左右两种连接方式完全一样，尽管第二种连接了更多图格。

:::

::: {.admonition .tip}
但不同颜色的电线或同颜色但中间没有连接的电线不是一根电线，在激活用电器时，用电器会分别响应每一根电线上的每一次信号。

:::

::: {.admonition .example}
![](chapters/images/2/1/2/multitile_drain_wires.png)

激活开关时，左边的开关只连接了一种颜色的电线，炮台只旋转一次；右边的开关连接了四种颜色的电线，炮台会旋转四次（过程不可见）。

:::
有些用电器的响应效果会根据激活图格的位置不同而改变。


::: {.admonition .example}
![](chapters/images/2/1/2/multitile_drain_regions.png)

传送枪站、大炮、兔兔炮等多图格用电器会因为激活的图格位置不同而响应不同。

:::
##### 有冷却时间的电路物品

有些用电器的响应会受到冷却时间限制，在冷却时间结束前被激活不会响应。


::: {.admonition .example}
![](chapters/images/2/1/2/cooldown_drain.png)

有冷却时间的用电器包括炮台发射、机关、雕像、马桶等。

:::
有冷却时间的用电器被激活并响应后，用电器所在的所有图格坐标与冷却时间（帧）会被加入到所有有冷却时间的电路物品共用的冷却机关列表（多图格用电器的每个格子都会被加入）。

每帧冷却机关列表内的所有图格的冷却时间会减一，在图格冷却时间为零后，冷却时间结束，该坐标会从列表中移除。


::: {.admonition .tip}
有冷却时间的用电器的名字和冷却时间可以在附录查询。

:::
当列表已满或用电器的所有图格都在冷却列表中时（多图格用电器需要所有图格都在列表里），用电器被激活后不会响应。


::: {.admonition .info}
计时器也使用冷却时间列表记录下一次激活的时间，但开启和关闭并不受冷却时间影响。列表满后开启的计时器不会激活。

:::
将正在冷却的用电器挖掉并不会从列表中移除该用电器的图格，但挖掉计时器会将计时器从列表中移除，计时器不会再激活。


::: {.admonition .info}
对于冷却时间相同的项，冷却机关列表是后进先出的，计时器电路中会使用这个性质。

:::
没有冷却时间的用电器可以在一帧内被激活任意次数。


::: {.admonition .example}
![](chapters/images/2/1/2/nocooldown_drain.png)

无冷却时间的用电器包括逻辑门灯、炮台转向、像素盒、晶莹宝石块、促动器等。

:::
##### 状态表示

有些电源看起来有两个或多个状态，并且每次状态切换会激活其上电线，这种电源被称为 **状态表示电源**，简称 **状态电源**。状态电源在不满足条件到满足条件和满足条件到不满足条件两种情况时都会激活。


::: {.admonition .example}
![](chapters/images/2/1/2/source_state.png)

加重压力板有抬起和按下两种状态，在按下到抬起和抬起到按下时都会激活；普通逻辑门有亮和灭两种状态，在灭切换到亮和亮切换到灭都会激活。

:::

::: {.admonition .example}
![](chapters/images/2/1/2/source_state_wiring.png)

加重压力板按下时会激活一次火把，加重压力板抬起时也会激活一次火把。

:::
有些用电器看起来有两个或多个状态，其上电线激活时会在几个状态间切换，这种用电器被称为 **状态表示用电器**，简称 **状态用电器**。状态用电器是有记忆的，它会记住之前的状态，下一次状态变化会在当前状态的基础上变化。

状态电源和状态用电器统称 **状态电路物品**。


::: {.admonition .example}
![](chapters/images/2/1/2/drain_state.png)

火把和普通逻辑灯会在激活时由亮切换到灭，或由灭切换到亮，具体是哪种取决于激活前的状态。

:::

::: {.admonition .example}
![](chapters/images/2/1/2/drain_state_wiring.png)

火把被激活第一次由灭变亮，激活第二次由亮变灭。

:::
对于有两个状态的状态电路物品，我们可以人为设定一个状态为 0（一般指灭或初始态），另一个状态为 1（一般指亮或另一态）。在不激活时，状态电路物品会维持之前的状态不变。


::: {.admonition .info}
也有一些状态电路物品不止两个状态。

:::

::: {.admonition .example}
烟囱有三个状态、彩线灯泡有十六个状态、传送枪台有十八个状态。

![](chapters/images/2/1/2/drain_multistate.png)

:::
我们称只使用状态电路物品和电线的电路为 **状态表示电路**，简称 **状态电路**。状态表示电路的状态可以从电路中直接读出，所有电路物品的状态是同步变化的。


::: {.admonition .example}
![](chapters/images/2/1/2/drain_state_wiring.png)

如果认为开关向上/火把灭为 0 ，开关向下/火把亮为 1，则开关和火把的状态同步变化，同时为 0 或同时为 1。

:::
##### 激活表示

有些电源看起来只有一个状态，或者看起来有多个状态但是只在一个状态切换到另一个状态时会激活，反过来不会，这种电源被称为 **激活表示电源**，简称 **激活电源**。激活电源只在不满足条件到满足条件时激活，不会在满足条件到不满足条件时激活。


::: {.admonition .example}
![](chapters/images/2/1/2/source_active.png)

如普通压力板尽管看起来有抬起和按下两种状态，但是只会在抬起到按下时会激活，按下到抬起不会激活，所以是激活电源；而故障逻辑门看起来只有一种状态，是激活电源。


:::

::: {.admonition .example}
![](chapters/images/2/1/2/source_active_wiring.png)

压力板按下一次时会激活一次火把，压力板按下两次时会激活两次火把。

:::
有些用电器看起来只有一个状态，这种用电器被称为 **激活表示用电器** ，简称 **激活用电器**。激活用电器是没有记忆的，激活时会直接响应而不考虑之前的状态。

激活电源和激活用电器统称 **激活电路物品**。


::: {.admonition .example}
![](chapters/images/2/1/2/drain_active.png)

广播盒会在被激活时发出内部文本，传送器会在被激活时传送上方人物与 NPC。

:::

::: {.admonition .example}
![](chapters/images/2/1/2/drain_active_wiring.png)

广播盒被激活发送文本。

:::
对于激活电路物品的每个周期，每个激活电路物品都有激活和不激活两种状态，我们可以令激活态/暂态为 1，非激活态/稳态为 0。在不激活时，激活电路物品会恢复并维持不激活态/稳态。


::: {.admonition .tip}
这里的周期指的是电路结算的最小单位，对于逻辑电路来说是逻辑帧。

:::
我们称只使用激活电路物品和电线的电路为 **激活表示电路**，简称 **激活电路**。激活与否并不会改变激活电路物品的状态，所以电路的状态不能从电路中直接读出。


::: {.admonition .example}
![](chapters/images/2/1/2/source_active_wiring_2.png)

我们看不到激活电路物品的状态，只能通过其它方式间接判断。

:::
如果我们忽略状态电路的状态，那么也可以将状态电路看做激活电路。


::: {.admonition .example}
![](chapters/images/2/1/2/drain_active_wiring.png)

我们可以忽略开关的状态，把状态电源开关当做激活电源使用。

:::
#### 2.1.3 电线

现实中的数字电路电线会有低电平、高电平、高阻态、未知态等状态，但是泰拉瑞亚中的电线只能传递脉冲信号（激活）一种信号，本身并没有状态或电平。电线下任一电源激活时，电线会激活，并激活其下所有用电器。

电线只是标记电路物品的连接关系（拓扑关系），与颜色、长度和形状无关，没有延迟。电线没有长度和连接电源或用电器数量的限制，连接或不连接电线不会改变电路物品的状态。

电线会将其下电源的状态或变化（激活）无损的传递到其下用电器，在传递过程中不会改变传递的信号，电线没有运算和记忆能力。


::: {.admonition .tip}
电路物品有状态与激活两种，但是电线上传递的信号只有激活信号一种。

:::

::: {.admonition .example}
![](chapters/images/2/1/3/topology_wire.png)

电线只标记电路物品的连接关系，与颜色、长度和形状无关。

:::
共有四种颜色的电线，相同颜色的电线在相邻格子会被连接到一起，组成一根电线；激活电线时，整根电线上的所有格子的电线会一起激活。而不同颜色的电线是在不同的图层上，不会被连接到一起。


::: {.admonition .example}
![](chapters/images/2/1/3/color_wire.png)

四色电线

:::

::: {.admonition .example}
![](chapters/images/2/1/3/color_wire_2.png)

不同颜色电线在不同图层，当同一格有多色电线时，它们的显示颜色会混合，但彼此间互不影响。

:::
使用分线盒或像素盒可以把一个图格内的相同颜色的电线分开。分线盒同时作用于一个图格中所有颜色的电线。一共有三种分线盒，分别把来自上下和左右、上左和下右、上右和下左的同色电线分开。像素盒只能将来自上下和左右的同色电线分开。


::: {.admonition .example}
![](chapters/images/2/1/3/junction_box.png)

开关分别能控制：全部火把、下方火把、左侧火把、右侧火把、下方火把。

:::
##### 最简电路

本章第一节提到电路是由物理输入端口、逻辑电路、物理输出端口组成的，而逻辑电路是由逻辑电源（逻辑输入端口）、逻辑用电器（逻辑输出端口）、电线组成的。所以我们可以得到电路的最简形式：一根电线与其下所有的电路物品。这样的电路被称为 **最简形式电路**，简称 **最简电路**，任何电路都是由这样的一个或多个最简电路组成。


::: {.admonition .example}
![](chapters/images/2/1/3/simplest_wiring.png)

最简电路，由一根红色电线（电线）、三个开关（电源）、三个火把（用电器）组成。

:::
由于大部分电路同时包括状态表示和激活表示，所以对于电路状态表示和激活表示的讨论通常对最简电路进行。当最简电路中只有状态电路物品和电线时，被称为 **最简状态电路**；当最简电路中只有激活电路物品和电线时，被称为 **最简激活电路**。

最简状态电路中的电线会在其下任一状态电源状态发生变化时令其下全部状态用电器状态发生变化；最简激活电路中的电线会在其下任一激活电源激活（进入激活态）时令其下全部激活用电器激活（进入激活态）。


::: {.admonition .example}
![](chapters/images/2/1/3/simplest_state_active_wiring.png)

最简状态电路和最简激活电路。

:::
当最简电路的电源中存在激活电源，用电器中存在状态用电器，则该最简电路存在激活转状态；当最简电路的电源中存在状态电源，用电器中存在激活用电器，则该最简电路存在状态转激活。


::: {.admonition .example}
![](chapters/images/2/1/3/simplest_convert_wiring.png)

激活转状态和状态转激活。

:::

::: {.admonition .example}
![](chapters/images/2/1/3/simplest_wiring_example.png)

我们可以将复杂的电路拆分成最简形式，然后逐条电线的分析。

:::
##### 参考状态

尽管电线是没有状态的，但是有时为了便于讨论，我们会假设电线有状态，这种状态被称为 **参考状态**。最简状态电路中的电线被称为 **状态传递电线**，简称 **状态电线**；最简激活电路中的电线被称为 **激活传递电线**，简称 **激活电线**。当最简电路中同时存在激活和状态表示时，我们根据更加关注的是状态还是激活来选择电线的类型，通常由用电器的类型决定，忽略电源的类型。后文会用将状态电线的参考状态简称为 **电线的状态**。一般设定电线的初态/稳态为 0；另一态/暂态为 1。

##### 线非

对于最简状态电路，电源和用电器的状态是同步变化的。但是由于电源和用电器的状态是可以人为设定的，如果我们设定一对电源和用电器的状态相反，将电源状态看做输入，将用电器看做输出，我们就会得到一个输入与输出始终相反的电路，也就是非逻辑。


::: {.admonition .example}
![](chapters/images/2/1/3/wire_not.png)

设定左侧火把与开关状态相同，则可以用火把代替开关状态。使用电线连接输入（状态电源开关）与输出（状态用电器火把），输入和输出状态始终相反，存在非逻辑。

$$y = \lnot a$$

:::
像这样不使用逻辑门，只使用一个任意状态电源、一个任意状态用电器和一根电线实现的非逻辑被称为 **线非**。由于线非的存在，我们可以在任意状态用电器处实现对输入的取反，而不需要使用逻辑门。

##### 线异或

异或逻辑又被叫做可控非逻辑，因为当一个输入为 0 时，输出与另一个输入相等；当一个输入为 1 时，输出为另一个输入的反相。考虑最简状态电路中的两个电源和一个用电器，将电源状态看做输入，将用电器看做输出，当一个输入为 0 时，输出与另一个输入相等；当一个输入为 1 时，输出为另一个输入的反相；满足异或逻辑。


::: {.admonition .example}
![](chapters/images/2/1/3/wire_xor.png)

使用电线连接输入（两个状态电源开关）与输出（状态用电器火把）满足异或逻辑。

$$y = a \oplus b$$

:::
由于异或具有交换率，交换两个输入对输出没有影响，所以输出与两个输入的顺序无关，具有普适性。同理，异或具有结合律，所以即便有多个输入，输出仍然满足所有输入间异或，可以任意扩展。


::: {.admonition .example}
![](chapters/images/2/1/3/wire_xor_multi.png)

$$y = a \oplus b \oplus c \oplus d \oplus e \oplus f$$

:::
像这样不使用逻辑门，只使用多个状态电源和一个状态用电器实现异或逻辑的方式被称为 **线异或**。由于线异或的存在，我们可以在任意状态用电器处实现异或，而不需要使用逻辑门。


::: {.admonition .tip}
线非是线异或只有一个输入的特殊情况。

:::
线异或的输入是状态用电器上所有电线连接的所有电源状态和状态用电器自身状态，输出是状态用电器状态，输入和输出间满足异或关系。


::: {.admonition .info}
电线在线异或中只标记连接关系，并不参与运算，线异或的输入是电源和用电器自身状态，输入电源在一个或多个电线上不会影响结果，输出与输入连接到输入的方式无关。


:::: {.admonition .tip}
一个电源通过不同电线连接到用电器算多次连接；一个多图格电源的多个图格通过一条电线连接到用电器算一次连接。

::::

:::: {.admonition .example}
![](chapters/images/2/1/3/wire_xor_color.png)

$$y = a \oplus b \oplus c \oplus d \oplus e \oplus f$$

::::
:::

::: {.admonition .tip}
注意区分线异或的异或和异或门的独热逻辑在输入数量大于等于 3 时是不同的。

![](chapters/images/2/1/3/wire_xor_and_xor_gate.png)

:::

::: {.admonition .tip}
线异或是泰拉瑞亚电路中最常用的运算。

:::
##### 线或

或逻辑中，当任意输入为 1 时，输出为 1；只有全部输入都为 0 时，输出为 0。考虑最简激活电路中的多个电源和一个用电器，任意电源激活时，用电器会被激活；没有电源激活时，用电器不会被激活；满足或逻辑。


::: {.admonition .example}
![](chapters/images/2/1/3/wire_or.png)

使用电线连接输入（两个激活电源开关）与输出（激活用电器广播盒）满足或逻辑。

$$y = a \lor b$$

:::
像这样不使用逻辑门，只使用多个激活电源和一个激活用电器实现或逻辑的方式被称为 **线或**。由于线或的存在，我们可以在任意激活用电器处实现或，而不需要使用逻辑门。

线或的输入是激活用电器上所有电线连接的所有电源状态，输出是激活用电器状态，输入和输出间满足或关系。


::: {.admonition .info}
电线在线或中只标记连接关系，并不参与运算，线或的输入是电源状态，输入电源在一个或多个电线上不会影响结果，输出与输入连接到输入的方式无关。


:::: {.admonition .example}
![](chapters/images/2/1/3/wire_or_color.png)

$$y = a \lor b \lor c \lor d \lor e \lor f$$

::::
:::

::: {.admonition .tip}
多输入或与两两或等价，所以线或与多输入或门等价。

:::

::: {.admonition .example}
![](chapters/images/2/1/3/wire_or_multi.png)

$$y = a \lor b \lor c \lor d \lor e \lor f$$

:::

::: {.admonition .tip}
然而对于没有冷却时间的物理激活用电器（如广播盒），被激活一次就会响应一次，即便是同时激活多次，每一次都会单独响应，并不是严格的线或逻辑。

严格的线或逻辑只存在于逻辑电路（故障灯），通常用于检测多位信号中是否存在或全为 0 / 1，用来代替较大的多输入或门，较线异或应用较少。

:::

::: {.admonition .tip}
线非、线异或、线或揭示了一个用电器通过一条或多条电线连接到多个电源时，用电器本身状态和多个连接电源状态间的关系。

:::
### 2.2 逻辑门

#### 2.2.1 逻辑门灯和逻辑门

泰拉瑞亚中的逻辑门由逻辑门和逻辑门灯组成，逻辑门灯可以被堆叠于逻辑门上。逻辑门上的逻辑门灯指其上方中间不相隔任何非逻辑灯图格的全部逻辑门灯。


::: {.admonition .example}
![](chapters/images/2/2/1/full_logic_gate.png)

逻辑灯堆叠于逻辑门上。

:::
##### 逻辑门灯

逻辑门灯有三种，分别是 **逻辑门灯（亮）、逻辑门灯（灭）、逻辑门灯（故障）** 。其中逻辑门灯（亮）和逻辑门灯（灭）被称为 **普通逻辑门灯**，简称 **普通灯**；逻辑门灯（故障）被称为 **故障逻辑门灯**，简称 **故障灯**。


::: {.admonition .quote}
![](chapters/images/2/2/1/logic_lamp.png)

逻辑门灯（亮）、逻辑门灯（灭）、逻辑门灯（故障）。

:::
逻辑灯是用电器，输入是其上所有电线连接的所有电源状态和自身状态，输出是自身状态。

普通灯是状态用电器，有记忆，输入包括自身状态，输入满足线非和线异或逻辑；故障灯是激活用电器，无记忆，输入不包括自身状态，输入满足线或逻辑。


::: {.admonition .tip}
记忆指的是能记住之前状态的能力，故障灯只有在被激活的逻辑帧是激活态，下一个逻辑帧如果没有被激活就会恢复不激活态；普通灯不被激活时始终维持之前的状态不变。

:::
逻辑灯必须堆叠在逻辑门上，我们说这些逻辑灯在该逻辑门上，该逻辑门在这些逻辑灯下。


::: {.admonition .quote}
设一个逻辑灯有 $m$ 个电源输入，电源的状态分别是 $s_1, s_2, \cdots, s_m$，则： 

普通灯（灭）的逻辑式：

$$\mathrm{OffLamp}(s_1, s_2, \cdots,s_m) = s_1 \oplus s_2 \oplus \cdots \oplus s_m$$

普通灯（亮）的逻辑式：

$$\mathrm{OnLamp}(s_1, s_2, \cdots,s_m) = \lnot (s_1 \oplus s_2 \oplus \cdots \oplus s_m)$$

或者可写为：

$$\mathrm{OnLamp}(s_1, s_2, \cdots,s_m) = s_1 \oplus s_2 \oplus \cdots \oplus s_m \oplus 1$$

普通灯的逻辑通式：

$$\mathrm{Lamp}(s_1, s_2, \cdots,s_m; l_0) = s_1 \oplus s_2 \oplus \cdots \oplus s_m \oplus l_0$$

$l_0$ 是逻辑灯状态，灭灯为 0，亮灯为 1。


:::: {.admonition .tip}
应用异或的可控非逻辑定义。

::::
故障灯的逻辑式：

$$\mathrm{FaultLamp}(s_1, s_2, \cdots, s_m) = s_1 \lor s_2 \lor \cdots \lor s_m$$

:::

::: {.admonition .example}
![](chapters/images/2/2/1/logic_gate_regions.png)

这些紧密排列的逻辑门中，相同颜色的区域是同一个逻辑门。

:::
##### 逻辑门

当逻辑门上没有故障灯时，逻辑门被称为 **普通逻辑门**，简称 **普通门**；当逻辑门上有故障灯时，逻辑门变成蓝色，被称为 **故障逻辑门**，简称 **故障门**。


::: {.admonition .quote}
![](chapters/images/2/2/1/logic_gate.png)

普通逻辑门（亮）、普通逻辑门（灭）、普通逻辑门（故障）。

:::
逻辑门是电源，输入是其上逻辑灯状态，输出是逻辑门自身状态。

普通门是状态电源，状态取决于其上普通灯状态；故障门是激活电源，激活取决于其上普通灯和故障灯状态，并且只有可能在其上故障灯激活时激活。逻辑门的状态只取决于其上逻辑灯状态，与自身状态无关。

一个逻辑灯只对应一个逻辑门，而一个逻辑门可以对应任意多个逻辑灯。

##### 全逻辑门

由逻辑门和其上逻辑灯组成的整体被称为 **全逻辑门**。全逻辑门的输入是全部逻辑灯的全部输入，既：全部逻辑灯上全部电线连接的全部电源状态和其上普通灯自身状态；全逻辑门的输出是逻辑门的的输出，既：逻辑门的状态。

全逻辑门的逻辑式是将每个逻辑灯关于输入电源的逻辑式对应带入逻辑门关于输入逻辑灯的逻辑式，得到逻辑门关于输入电源的逻辑式。

#### 2.2.2 普通逻辑门

普通门有 **与、与非、或、或非、异或、同或** 六种。普通门有亮和灭两种状态，由其上普通灯状态决定。普通灯是输入，普通门是输出，亮灯/门是 1，灭灯/门是 0，除异或门和同或门外，输入与输出的关系与上一章所述同名逻辑运算相同，异或门和同或门的逻辑是独热和独热非。


::: {.admonition .quote}
![](chapters/images/2/2/2/normal_logic_gate.png)

与、与非、或、或非、异或、同或六种普通门。

:::

::: {.admonition .example}
![](chapters/images/2/2/2/normal_logic_gate_2.png)

六种三输入普通逻辑门。

:::
##### 逻辑等价的普通门


::: {.admonition .quote}
![](chapters/images/2/2/2/normal_logic_gate_equal_1.png)

等价前的普通门。

:::
由于线非的存在，我们可以直接令输入电源普通门的状态和输出状态用电器的状态相反，令与门和与非门、或门和或非门、异或门和同或门等价。


::: {.admonition .quote}
![](chapters/images/2/2/2/normal_logic_gate_equal_2.png)

利用线非令与门和与非门、或门和或非门、异或门和同或门等价。

:::
上一章已经证明过或逻辑可以通过取反输入和输出与与逻辑等价，表述如下：

$$\lnot(a \land b) = \lnot a \lor \lnot b$$

$$\lnot(a \lor b) = \lnot a \land \lnot b$$


::: {.admonition .tip}
对于三项及三项以上仍然是成立的，可自行证明。

:::
将或门的逻辑表达式进行两次取反，然后可将或逻辑转换为与逻辑：

$$y = a \lor b = \lnot \lnot (a \lor b) = \lnot (\lnot a \land \lnot b)$$

将与门的逻辑表达式进行两次取反，然后可将与逻辑转换为或逻辑：

$$y = a \land b = \lnot \lnot (a \land b) = \lnot (\lnot a \lor \lnot b)$$

由此我们可以直接令输入状态电源的状态与输出用电器普通灯的状态相反，令与门和或非门、或门和与非门等价，然后再利用前述结论，可令与门和或门等价。


::: {.admonition .quote}
![](chapters/images/2/2/2/normal_logic_gate_equal_3.png)

利用前述结论令与门和或非门、或门和与非门等价，再利用线非令与门和或门、与非门和或非门等价。

:::

::: {.admonition .question}
那么我们是否能将与门和异或门等价呢？

不可能，原因会在下一章介绍。

:::
这样我们就可以将六种普通门等价为与门和异或门两种普通门，与门在其上所有普通灯点亮时点亮，异或门在其上只有一个普通灯点亮时点亮。在任何电路中，都可以只使用这两种普通门实现全部逻辑，而不需要其它普通门。


::: {.admonition .example}
![](chapters/images/2/2/2/normal_logic_gate_equal.png)

对于所有可能的输入，左侧四种逻辑门、右侧两种逻辑门的输出一致，证明其等价。

:::
##### 普通灯的性质

普通灯是状态用电器，普通灯切换状态时，下方普通门会根据上方所有普通灯状态决定自己状态；而普通灯同时切换多次状态，下方普通门只会考虑普通灯的最后状态（即线异或），而不考虑中间状态。普通门是状态电源，在由亮到灭和由灭到亮切换状态时都会激活其上电线。


::: {.admonition .example}
![](chapters/images/2/2/2/normal_logic_gate_settle.png)

左侧普通灯激活一次和三次时，线异或结果是 1，输出 1；激活二次和四次时，线异或结果是 0，输出 0；
右侧故障灯激活大于等于一次时，线或结果都是 1，输出 1。

:::

::: {.admonition .quote}
设一个普通门有 $n$ 个普通灯输入，普通灯的状态分别是 $l_1, l_2, \dots, l_m$，则： 

与门的逻辑通式：

$$\mathrm{AndGate}(l_1, l_2,\dots,l_m) = l_1 \land l_2 \land \cdots \land l_n$$

异或门的逻辑通式：

$$\mathrm{XorGate}(l_1, l_2,\dots,l_m) = \mathrm{onehot}(l_1, l_2, \cdots, l_n)$$

:::

::: {.admonition .quote}
设普通门上第 $j$ 个普通灯表达式如下：

$$l_j = \mathrm{Lamp}(s_{j1},\dots,s_{jk_j};l_{0j})$$

全与门逻辑式如下：

$$\mathrm{FullAndGate}\Big(\{s_{ji}\}_{\substack{1\le j\le n\\1\le i\le k_j}}; \{l_{0j}\}_{j=1}^{n}\Big) \\ = \\ (s_{11} \oplus \cdots \oplus s_{1k_1} \oplus l_{01}) \land \cdots \land (s_{j1} \oplus \cdots \oplus s_{jk_j} \oplus l_{0j})$$

全异或门逻辑式如下：

$$\mathrm{FullXorGate}\Big(\{s_{ji}\}_{\substack{1\le j\le n\\1\le i\le k_j}}; \{l_{0j}\}_{j=1}^{n}\Big) \\ = \\ \mathrm{OneHot}(s_{11} \oplus \cdots \oplus s_{1k_1} \oplus l_{01}, \cdots, s_{j1} \oplus \cdots \oplus s_{jk_j} \oplus l_{0j})$$


:::: {.admonition .tip}
将普通门逻辑式中的全部 $l_j$ 用对应普通灯逻辑式代替

::::
:::

::: {.admonition .tip}
代入法是一种常见的代数运算方法。当某个逻辑量已知等价于一个由其他变量构成的代数式时，可以在任意逻辑式中用该表达式直接替换原变量，而不改变逻辑结果。

逻辑灯的输入是其上全部电线连接的全部电源状态和其本身状态，输出是逻辑灯状态；逻辑门输入是其上全部逻辑灯状态，输出是逻辑门状态。

全逻辑门是由逻辑门和其上逻辑灯组成的，所以将逻辑灯的代数式代入逻辑门的代数式就可以得到全逻辑门的代数式，输入是逻辑门上逻辑灯上全部电线连接的全部电源状态和逻辑灯状态，输出是逻辑门状态。

:::

::: {.admonition .example}

:::: {.admonition .question}
写出下列全与门的逻辑式：

![](chapters/images/2/2/2/full_and.png)

::::
* $y_1 = \lnot (a \oplus b) \land (a \oplus b \oplus c) \land a$

* $y_2 = \lnot ((a \oplus c) \land \lnot (a \oplus b \oplus c) \land c)$

* $y_3 = \lnot (\lnot b \land \lnot (a \oplus b \oplus c) \land \lnot c)$

* $y_4 = b \land (a \oplus b \oplus c) \land \lnot a$

使用 $\oplus 1$ 代替非逻辑：

* $y_1 = (a \oplus b \oplus 1) \land (a \oplus b \oplus c) \land a$

* $y_2 = (a \oplus c) \land (a \oplus b \oplus c \oplus 1) \land c \oplus 1$

* $y_3 = (b \oplus 1) \land (a \oplus b \oplus c \oplus 1) \land (c \oplus 1) \oplus 1$

* $y_4 = b \land (a \oplus b \oplus c) \land (a \oplus 1)$

:::
#### 2.2.3 故障逻辑门

当在普通门上堆叠故障灯时，普通门会变成蓝色的故障门，所有故障门逻辑都是一样的，尽管它们看起来不同。


::: {.admonition .quote}
![](chapters/images/2/2/3/fault_logic_gate.png)

故障逻辑门，尽管贴图不同，但是逻辑相同。

:::
故障门与其上最靠下的故障灯之间的普通灯称为 **有效逻辑灯**，简称 **有效灯**。当故障逻辑门上有任意一个故障逻辑灯被激活时，故障门会按照有效灯中亮灯的数量比有效灯总数为概率激活。


::: {.admonition .example}
![](chapters/images/2/2/3/fault_logic_gate_example.png)

当激活图中五个故障门的故障灯时，故障门激活的概率分别是：

A: $ 1 \over 7$; B: $2 \over 7$; C: $6 \over 7$; D: $1 \over 2$; E: $1$;

:::
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_fault.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    其他故障灯（激活效果与最下方故障灯相同）
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_on.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    其他普通灯（不影响概率）
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_off.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_on.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_on.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_fault.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    最下方故障灯（下方为有效灯）
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_off.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    有效灯（激活故障灯时故障门激活概率为有效亮灯比全部有效灯）
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_lamp_on.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    
  </div>
</div>
<div style="display: flex; align-items: center; margin-bottom: 0;">
  <img src="chapters/images/2/2/3/logic_gate_fault.png" style="display: block; margin: 0;" />
  <div style="margin-left: 10px;">
    故障门
  </div>
</div>
</br>


::: {.admonition .tip}
由于故障门是概率激活的，所以又被叫做随机门。

:::
故障门上的故障灯为激活用电器，而普通灯为状态用电器。改变普通灯的状态不会使故障门激活，而激活故障灯有可能会使故障门激活。一个故障逻辑门上的所有故障灯都是相同的，而除有效灯以外的普通灯的状态不会影响故障逻辑门的概率，除有效灯以外的普通灯可以看做不存在。故障灯每次激活时，故障门都有概率激活；而故障灯同时被激活多次，下方故障门只会尝试判断激活一次（即严格线或）。故障门是激活电源，在成功激活时会激活其上电线。

### 2.3 逻辑结算

#### 2.3.1 逻辑结算

##### 帧结算

泰拉瑞亚中每一帧中，除电路外所有的游戏机制会依一定顺序结算，电路结算的位置和触发电路的物理电源结算位置有关。也就是说，当实体触发电路时，会在实体所在结算，触发电路的位置，插入一个电路结算，插入的电路结算被称为 **逻辑结算**。


::: {.admonition .example}
由某人物触发的压力板，会在该人物结算的压力板结算位置处，触发一个逻辑结算；由某射弹触发的垫板，会在该射弹结算的垫板结算位置处，触发一个逻辑结算。

:::

::: {.admonition .info}
有些电路会受物理电源的类型影响，例如计时器作为物理电源时，不会直接激活自己，但可以用逻辑门绕开；逻辑感应器（玩家）作为物理电源时无法触发传送机，需要更换电源类型；加重压力板作为物理电源时，触发传送机会导致传送否定等等，详细内容会在后文介绍。

:::
##### 逻辑结算

当一个物理电源激活一次时，会新建一个逻辑结算，逻辑电源无法新建逻辑结算。

每帧内逻辑结算的数量没有限制，在逻辑结算结算完成前，后续的代码不会运行。无论逻辑结算的规模有多大，有多少逻辑门和多少电线，都会在一帧内完成。可以说泰拉瑞亚电路是没有频率上限且没有延迟的。


::: {.admonition .tip}
实际上频率会受限于能制作出来的驱动/时钟频率；延迟会受限于电脑性能，当计算量较大时，帧结算需要的时间会增加，物理帧会降低。

:::
在泰拉瑞亚中，逻辑结算被叫做时钟周期，简称 **周期**；而接近现实电路周期概念的电路结算最小单位被叫做逻辑帧，后文将使用上述叫法。能在一个周期内完成计算的电路被称为 **单周期电路**，需要多个周期才能完成计算的电路被称为 **多周期电路**。

##### 逻辑帧结算

对于逻辑门电路，逻辑结算被分步进行，每一步中都进行 **电源（逻辑门）激活判断 $\rightarrow$ 电源（逻辑门）激活 $\rightarrow$ 电线激活 $\rightarrow$ 用电器（逻辑灯）激活** 四小步，我们将这样的四步统称为 **逻辑帧**。一个逻辑电路的结算过程中，反复运行每个逻辑帧中的四小步，直到没有逻辑门需要激活。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/logic_frame_example_1_wiring.png)

激活开关后：

![](chapters/images/2/3/1/logic_frame_example_1_step.png)

第 0 逻辑帧：开关激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活；
第 1 逻辑帧：逻辑门判断 $\rightarrow$ 逻辑门激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活；
第 2 逻辑帧： 逻辑门判断 $\rightarrow$ 逻辑门激活 $\rightarrow$ 电线激活 $\rightarrow$ 火把激活；

:::
在逻辑灯状态改变后，并不会马上进行逻辑灯下逻辑门是否激活的判断，而是在下一逻辑帧再进行激活判断。所以某一逻辑帧逻辑门是否激活只需要考虑逻辑门上逻辑灯在上一逻辑帧的终态，不需要考虑中间态（普通灯考虑亮灭，故障灯考虑被激活）。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/logic_frame_example_2_wiring.png)

激活开关后：

![](chapters/images/2/3/1/logic_frame_example_2_step.png)

第 0 逻辑帧：开关激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活：普通灯由灭到亮，故障灯由稳态到激活态；
第 1 逻辑帧：逻辑门判断：故障灯激活态，普通灯亮，故障门应激活 $\rightarrow$ 逻辑门激活 $\rightarrow$ 电线激活 $\rightarrow$ 火把激活；

:::

::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/logic_frame_example_3_wiring.png)

激活开关后：

![](chapters/images/2/3/1/logic_frame_example_3_step.png)

第 0 逻辑帧：开关激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活：普通灯由亮到灭，故障灯由稳态到激活态；
第 1 逻辑帧：逻辑门判断：故障灯激活态，普通灯灭，故障门不应激活；

:::
逻辑帧是逻辑门电路的最小时间单位，逻辑帧内的事情是同时发生的，所以我们会以逻辑帧为单位分析逻辑门电路。两个相邻逻辑帧间相隔一个逻辑门，令物理电源所在逻辑帧为 **第 0 逻辑帧**，每经过一个逻辑门逻辑帧加一，可以通过数出一个信号从物理电源传递到某个逻辑门时经过的逻辑门数量，来计算该逻辑门在此逻辑结算所在逻辑帧位置。当需要分析一个信号到达两个逻辑门时相差多少逻辑帧时，我们可以上溯到它们最近的公共逻辑帧。在逻辑电路中的延迟指的是逻辑帧延迟，表示信号的先后逻辑帧差，同逻辑结算中没有时间差。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/logic_frame_example_4_wiring.png)

激活开关后：

![](chapters/images/2/3/1/logic_frame_example_4_step.png)

:::

::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/logic_frame_example_5_wiring.png)

激活开关后：

![](chapters/images/2/3/1/logic_frame_example_5_step.png)

:::
##### 电源结算

每个逻辑帧中，电线会先后激活一些逻辑灯，而这些逻辑灯下的逻辑门可能会在下一逻辑帧被激活。逻辑门激活的顺序取决于其上逻辑灯在上一逻辑帧被激活的顺序，先激活的逻辑灯下的逻辑门先激活，后激活的逻辑灯下的逻辑门后激活。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/source_example_1_wiring.png)

激活开关后：

![](chapters/images/2/3/1/source_example_1_step.png)

第 0 逻辑帧：左边的逻辑灯先被激活，右边的逻辑灯后被激活；
第 1 逻辑帧：左边的逻辑门先激活，右边的逻辑门后激活。

:::
##### 电线结算

每个电源上的每个格子，会按照 **先从左到右，再从上到下** 激活每个格子里的电线。每个格子的四色电线中，会按照 **红 $\rightarrow$ 蓝 $\rightarrow$ 绿 $\rightarrow$ 黄** 的颜色顺序依次进行结算。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/wire_example_1_wiring.png)

激活开关后：

![](chapters/images/2/3/1/wire_example_1_step.png)

电源上每一格的电线会按照 红 $\rightarrow$ 蓝 $\rightarrow$ 绿 $\rightarrow$ 黄 的顺序结算。

:::

::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/wire_example_2_wiring.png)

激活开关后：

![](chapters/images/2/3/1/wire_example_2_step.png)

电源的每一格会按照先从左到右，再从上到下的顺序结算其上电线。

:::
##### 格子结算

每根电线进行结算时，会从电源开始，使用四连通广度优先搜索（BFS）来遍历该电线上连接的所有图格，添加到队列的顺序是 **下 $\rightarrow$ 上 $\rightarrow$ 右 $\rightarrow$ 左** 。

一般情况下，我们只需要知道，电线上各个格子按照沿电线上距离电源的传播距离由近到远的顺序激活。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/1/single_example_1_wiring.png)

激活开关后：

![](chapters/images/2/3/1/single_example_1_step.png)

电线的每一格会按照从电源出发，沿着电线逐格结算。

:::
##### 结算层级

综上，电路结算具有严格的层级结构，其整体顺序为：

**帧结算 > 逻辑结算 > 逻辑帧结算 > 电源结算 > 电线结算 > 格子结算**

上层结算由多个下层结算组成，并通过逐层拆分完成：只有当前层级包含的所有下层结算全部完成后，才会继续执行当前层级的后续流程。


::: {.admonition .tip}
实际应用中，我们常用工具（[电路步进模组 MechScope](https://steamcommunity.com/sharedfiles/filedetails/?id=3232991031)）来观察电路结算顺序，大型时序电路在不使用工具的情况下很难进行测试。

:::
#### 2.3.2 爆门


::: {.admonition .question}
泰拉电路没有延迟，逻辑结算不完成程序不会继续执行，那么激活这样的电路会发生什么？

![](chapters/images/2/3/2/double_active.png)


:::: {.admonition .failure}
开关激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活 $\rightarrow$ 逻辑门激活 $\rightarrow$ 电线激活 $\rightarrow$ 逻辑灯激活 $\rightarrow$ 逻辑门激活 $\rightarrow$ ……

::::
这会陷入死循环，卡死游戏吗？然而实际尝试后我们会发现逻辑门冒烟了，但是游戏并没有卡死，这是怎么回事呢？

![](chapters/images/2/3/2/smoke.png)

:::
泰拉为了防止无延迟的电路出现死循环卡死游戏，为逻辑门添加了一个设定：同一个逻辑门在一次逻辑结算中只能激活一次。如果尝试激活第二次，逻辑门的状态会正常切换，但是不会激活其上电线，并且会有白烟从逻辑门中冒出，这种现象被称为 **爆门**。


::: {.admonition .tip}
上方的示例电路中红线会激活两次，第一次电源是开关，第二次电源是逻辑门，而逻辑门只会激活一次。

:::
实际上，使用爆门来防止死循环，也会产生一些副作用，有些不会死循环的电路也会发生爆门。在实际应用中，爆门经常导致电路出问题，这是因为我们往往希望逻辑门在不同逻辑帧多次状态切换时可以多次激活，但实际上不会。学会了预测爆门，就可以想办法避免爆门，甚至利用爆门。


::: {.admonition .example}
考虑这样的电路：

![](chapters/images/2/3/2/smoke_example_wiring.png)

左右逻辑一样，区别是左侧两个信号没有延迟同时到达；右侧的下方信号会延迟两个逻辑帧到达。

激活开关后：

![](chapters/images/2/3/2/smoke_example_step.png)

第一行是左侧电路激活后情况，火把不会点亮；
第二行是右侧电路激活后情况，上方信号先激活逻辑门点亮火把，下方信号第二次激活逻辑门失败，触发爆门，逻辑门没有发出信号；逻辑门状态改变但火把状态未改变，逻辑门和火把状态不一致；
第三行是假设没有爆门时右侧电路激活后情况，上方信号先激活逻辑门点亮火把，下方信号第二次激活逻辑门熄灭火把，与左侧电路结果一致。

:::
##### 竞争和冒险

输入信号通过两条或以上路径到达同一个逻辑门时，由于两条路径上的延迟（逻辑帧）不同，出现了到达先后时间差，被称为 **竞争**；由于竞争的存在，先到达的信号激活逻辑门后，后到达的信号再想激活逻辑门会导致逻辑门爆门，出现错误，被称为 **冒险**。

我们通常使用两个方法来避免爆门：

- 给先到达的信号添加逻辑延迟，让两个信号同时到达同一个逻辑门；

- 使用寄存器暂存信号，需要时再将它们同时发送给同一个逻辑门；


::: {.admonition .example}
![](chapters/images/2/3/2/delay.png)

给先到达的信号（上方信号）添加逻辑延迟，让两个信号同时到达逻辑门。

![](chapters/images/2/3/2/register.png)

使用寄存器暂存信号，需要时再将它们同时发送给逻辑门。

:::
### 2.4 逻辑电路

#### 2.4.1 组合逻辑与时序逻辑

逻辑电路中，所有电线全部为状态电线的电路被称为 **组合逻辑电路**；有至少一根电线为激活电线的电路称为 **时序逻辑电路**。

组合逻辑电路中只有与门和异或门，并且每根电线只在某个固定的逻辑帧激活，每个输出对应一个逻辑函数。时序逻辑电路中同一根电线可能在不同逻辑帧激活，并且不同逻辑帧激活可能表示不同信号。


::: {.admonition .example}
![](chapters/images/2/4/1/adder.png)

组合逻辑加法器，所有电线都是状态表示。

![](chapters/images/2/4/1/accumulator.png)

时序逻辑加法器（累加器），部分电线是状态表示，部分电线是激活表示。

:::

::: {.admonition .info}
与现实数电不同，泰拉的普通灯有记忆，触发器可只由一个逻辑门实现，时序逻辑电路相较组合逻辑电路不会有更大的面积和更多的延迟。

组合逻辑电路中每一个数据需要独立的逻辑延迟，这会占用大量的面积；而时序逻辑电路中可以让所有数据使用共享的逻辑延迟，只需要一个公共逻辑延迟链。

组合逻辑电路的状态可以直接在电路中读出；但时序逻辑电路不能，通常需要借助工具进行调试。

通常在泰拉电路中，绝大部分是时序逻辑电路；组合逻辑电路仅占其中的很小一部分。

:::
#### 2.4.2 最简逻辑电路

我们将一个逻辑门、该逻辑门上所有逻辑灯、连接该逻辑门与其上逻辑灯的所有电线组成的逻辑电路称为 **最简逻辑电路**。类似最简电路，任何逻辑电路也是由一个或多个最简逻辑电路组成。


::: {.admonition .example}
![](chapters/images/2/4/2/simplest_logic_wiring.png)

最简逻辑电路，由一个异或门（逻辑门）、其上普通灯（逻辑灯）、连接该逻辑门与其上逻辑灯的所有电线（电线）组成。

最简逻辑电路不包括除最简逻辑电路的逻辑门外的电源、除最简逻辑电路的逻辑灯外的用电器。

:::
当最简逻辑电路的逻辑门是普通门时，被称为 **最简状态逻辑电路**，或 **最简组合逻辑电路**；当最简逻辑电路的逻辑门是故障门时，被称为 **最简激活逻辑电路**，或 **最简时序逻辑电路**。


::: {.admonition .example}
![](chapters/images/2/4/2/simplest_logic_state_active_wiring.png)

最简状态（组合）电路和最简激活（时序）电路。

:::

::: {.admonition .info}
最简逻辑电路又被称为 **电路元件**。

:::
#### 2.4.3 电路模块

##### 模块化

模块化是简化逻辑电路分析的有效方法，对于任意电路需求，我们都可以将其拆分成多个较简单的步骤，然后再将每个步骤继续拆分成更简单的步骤，直到将电路需求拆分到每一个步骤都可由最简逻辑电路实现的最简步骤；再使用最简逻辑电路实现最简步骤，使用多个最简步骤实现较复杂的步骤，然后再使用多个步骤实现更复杂的步骤，直到完整实现电路需求。


::: {.admonition .example}
```mermaid
graph LR
    subgraph 贪吃蛇电路
        subgraph 储存
            subgraph 位图
                地图
            end

            subgraph 队列
                蛇身方向
            end

            subgraph 坐标
                蛇头坐标
                蛇尾坐标
                食物坐标
            end

            subgraph 方向
                蛇头方向
                蛇尾方向
            end
        end

        subgraph 输入
            控制器
        end

        subgraph 输出
            显示屏
        end

        subgraph 计算
            坐标运算
            撞蛇身
            吃食物
            随机生成食物
        end

        地图 --> 显示屏

        控制器 -->|与当前方向不同| 蛇头方向

        蛇头方向 -->|新坐标 = 旧坐标 + 方向| 坐标运算
        蛇头坐标 <--> 坐标运算
        蛇头坐标 -->|绘制蛇头| 地图

        蛇头坐标 <-->|与食物重合| 吃食物
        食物坐标 <--> 吃食物
        蛇头坐标 <-->|与蛇身重合| 撞蛇身 
        地图 <--> 撞蛇身

        蛇尾方向 -->|新坐标 = 旧坐标 + 方向| 坐标运算
        蛇尾坐标 <--> 坐标运算
        蛇尾坐标 -->|擦除蛇尾| 地图

        蛇头方向 -->|入队| 蛇身方向
        蛇身方向 -->|出队（没有吃食物时）| 蛇尾方向

        食物坐标 <-->|设置食物坐标| 随机生成食物 
        地图 <-->|绘制食物| 随机生成食物 
    end
```
贪吃蛇电路的流程图，逻辑电路可以被分为 **输入、输出、储存、计算、控制（在箭头上体现）** 五部分。

:::
上述的每一个步骤，都对应逻辑电路的构成部分。电路元件是逻辑电路的最基础构成部分，由单个逻辑门构成；多个电路元件可以构成更大的逻辑电路部分，被称为 **电路部件**，由多个逻辑门构成；而多个电路部件可以构成更大的逻辑电路部分，被称为 **电路模块**，电路模块也可以构成更大的电路模块；逻辑电路通常由多个电路模块构成。


::: {.admonition .tip}
对于逻辑电路和步骤的划分，可根据需要任意进行。

:::

::: {.admonition .example}

:::: {.admonition .quote}
**Quote 1**

![](chapters/images/2/4/3/wiring_example.png)

逻辑电路，计算机电路；

::::

:::: {.admonition .quote}
**Quote 2**

![](chapters/images/2/4/3/module_example_1.png)

电路模块，嵌入式中央处理器（CPU） CS161E；

::::

:::: {.admonition .quote}
**Quote 3**

![](chapters/images/2/4/3/module_example_2.png)

电路模块，算术逻辑单元（ALU）；

::::

:::: {.admonition .quote}
**Quote 4**

![](chapters/images/2/4/3/component_example.png)

电路部件，时序逻辑加法器（累加器）；

::::

:::: {.admonition .quote}
**Quote 5**

![](chapters/images/2/4/3/element_example.png)

电路元件，T 触发器。

::::
在这个例子中，每一级逻辑电路部分中都能找到下一级逻辑电路部分。

:::
##### 组成

对于逻辑电路部分，由一个或多个全逻辑门构成，这些逻辑门（灯）被称为 **内部逻辑门（灯）**，简称 **内部门（灯）**；而不包括在该逻辑电路部分的逻辑门（灯）被称为 **外部逻辑门（灯）**，简称 **外部门（灯）**。连接的所有逻辑门（灯）都是内部门（灯），且其下没有物理电源和用电器的电线，被称为 **内部电线**；连接的逻辑门（灯）中存在外部门（灯），或其下有物理电源或用电器的电线，被称为 **外部电线**。

逻辑电路部分是由 **内部逻辑门、内部逻辑灯、内部电线、外部电线** 组成的。


::: {.admonition .example}
![](chapters/images/2/4/3/module_example.png)

示例电路模块。

![](chapters/images/2/4/3/module_example_composition.png)

电路模块由内部逻辑门、内部逻辑灯、内部电线、外部电线组成。

:::
##### 端口

每个外部电线都是逻辑电路部分与外部电路交流的 **端口**，外部电路对逻辑电路部分、逻辑电路对外部电路施加的影响完全通过端口进行。

端口分为 **输入端口、输出端口、输入输出端口**。数据通过输入端口输入逻辑电路部分，通过输出端口从逻辑电路部分输出，输入输出端口可以输入数据也可以输出数据。

* 当外部电线连接的电源中只有外部电源，或用电器中只包括内部逻辑灯时，其端口为输入端口；
* 当外部电线连接的电源中只有内部逻辑门，或用电器中只包括外部用电器时，其端口为输出端口；
* 当外部电线同时连接内部逻辑灯、内部逻辑门与外部电源、外部用电器 ，其端口为输入输出端口。


::: {.admonition .tip}
本教程中，会使用火把表示电路模块的输出端口，会同时使用开关和火把表示电路模块的输入端口和输入输出端口。

:::

::: {.admonition .example}
![](chapters/images/2/4/3/port_example.png)

上述示例模块中，可以将外部电线分为输入端口和输出端口。

:::
在分析逻辑电路部分时，我们可以应用黑箱理论，只需要考虑端口的输入输出间的关系，而完全不需要考虑其内部实现。当我们使用外部电路产生满足输入端口格式的数据，并接受满足输出端口格式的数据，即可正常使用逻辑电路部分，像其在其它电路中一样。


::: {.admonition .example}

:::: {.admonition .question}
以下上述示例模块在不同电路中的应用，你能找出它们吗？

::::

:::: {.admonition .quote}
**Quote 1**

![](chapters/images/2/4/3/module_example_application_1.png)

::::

:::: {.admonition .quote}
**Quote 2**

![](chapters/images/2/4/3/module_example_application_2.png)

::::

:::: {.admonition .quote}
**Quote 3**

![](chapters/images/2/4/3/module_example_application_3.png)

::::

:::: {.admonition .quote}
**Quote 4**

![](chapters/images/2/4/3/module_example_application_4.png)

::::

:::: {.admonition .quote}
**Quote 5**

![](chapters/images/2/4/3/module_example_application_5.png)

::::

:::: {.admonition .quote}
**Quote 6**

![](chapters/images/2/4/3/module_example_application_6.png)

::::
:::
##### 标准电路

在逻辑电路中，存在大量重复的部分，我们将多个逻辑电路中会多次用到的部分逻辑电路总结为 **标准电路元件、标准电路部件、标准电路模块**，统称标准电路。通常大部分电路需求都可以完全使用标准电路实现。


::: {.admonition .tip}
越大的标准电路的泛用性越差，并且通常需要根据具体情况调整。

:::
对于标准电路，我们需要关注它的输入与输出端口格式，以及输入与输出间的关系。当我们掌握某一标准电路的这两点后，我们可以在任何需要它的电路中一致的使用它。后续章节中出现的电路元件、电路部件、电路模块都是总结出的标准电路。


::: {.admonition .example}
上述示例模块就是标准电路部件组合逻辑加法器，是最常用的标准组合逻辑部件之一，在大部分计算电路中都有使用，将会在下文详细介绍。
:::


<div STYLE="page-break-after: always;"></div>

