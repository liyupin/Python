

#  精通Python自动化脚本-运维人员宝典]()







# 第一章 Python脚本概述

## 技术要求

在学习本书前，你应该了解一些 Python 编程的基础知识，比如基础语法、变量类型、元组数据类型、列表字典、函数、字符串和方法。在python.org/downloads/上有3.7.2和2.7.15两个版本可供下载。本书中我们将使用3.7这一版本来作为代表示例和包的安装。

**译者注：**预计 Python 3.7还会发展较长时间，而 Python2则长期止步于 Python2.7了，但小版本号都在不断变化

本章的示例和源代码可通过 [GitHub 仓库](https://github.com/alanhou/python-scripting)进行获取。

## 为什么选择Python？

Python有非常丰富的开源库用于数据分析工具、网站框架、测试等等。Python是一种可在不同平台上使用的编程语言（Windows, Mac, Linux和Linux嵌入式硬件，如树莓派Raspberry Pi）。它也用于开发桌面应用和网页应用。

开发人员如果使用Python可以编写更少行数的代码。原型制作非常快速，因为在解释器系统中运行。Python可被看成是面向对象、面向过程或函数式编程。

Python可以完成各种任务，比如创建网页应用。它和软件一起使用来创建工作流，它连接数据库系统、处理文件、处理大数据并执行复杂数学运算。

## Python语法与其它编程语言的对比

Python编写的代码可读性很强，因为它和英语本身非常相近。要完成一个命令，Python使用新的一行来完成。

Python有一个很棒的特性：缩进。使用缩进我们可以定义决策语句作用域，for循环和while循环、函数和类。

## Python安装

这一部分中我们将学习在不同平台上Python的安装，比如Linux和Windows。

### Linux平台上的安装

大部分Linux发行版本都默认安装了Python 2。有些则直接包含了Python 3。

**译者注：**目前大部分 CentOS 中默认安装的是 Python 2，而 Ubuntu 中则内置了 Python 3

要在Debian系Linux系统中安装Python 3，在命令行终端中可运行如下命令：

```bash
sudo apt install python3
```



要在CentOS 系统中安装Python 3，在命令行终端中可运行如下命令：

```bash
sudo yum install python3
```

如无法使用以上命令安装Python，请从[官方网站](https://www.python.org/downloads/)上下载Python并按照指示进行安装。

**译者注：**本博客有一篇[如何安装Python3.7](https://alanhou.org/python37-installation/)也可供参考

### Windows平台上的安装

在Microsoft Windows上安装Python，我们需要从python.org上下载可执行安装包并执行安装。从[官网下载页面](https://www.python.org/downloads/)下载python.exe文件并选择想要在电脑上安装的Python版本。然后双击所下载的 exe 文件来安装Python。有安装引导页面中，有一个Add Python to the path的复选框，勾选并按照提示一步一步的安装Python 3。

#### Pip安装以及使用pip安装Python包

在 Linux 中安装pip命令如下：

```bash
sudo apt install python-pip # 安装 Python 2的 pipsudo 
apt install python3-pip # 安装 Python 3的 pip
```

**译者注：**以上为 Ubuntu 中的命令，原书作者使用的均为 Ubuntu，CentOS 中将 apt 修改为 yum 即可

Windows中, 使用如下命令安装：

```bash
python -m pip install pip
```



### Mac上的安装

要安装 Python 3，我们要在系统中安装brew。运行如下命令来在系统中安装brew：

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

通过运行以上命令，brew就安装好了。现在使用brew来安装 Python 3：

```bash
brew install python3
```



### 安装Jupyter notebook

要安装Jupyter Notebook，先下载Anaconda。

安装所下载的Anaconda版本，按照向导中的指示进行安装即可。

使用pip安装Jupyter：

```bash
pip install jupyter
```

3在 Linux 中，pip install jupyter安装的是Python 2 的Jupyter。如果想要安装Python 3 的Jupyter，运行如下命令：

```bash
pip3 install jupyter
```



### 安装和使用虚拟环境

下面我们就来看如何安装虚拟环境以及如何进行激活。

在Linux中安装虚拟环境，执行步骤如下：

1、首先检查是否安装了pip。我们来安装Python 3的pip

```bash
sudo apt install python3-pip
```

2、使用pip3安装虚拟环境：

```bash
sudo pip3 install virtualenv
```

3、现在我们来创建虚拟环境。你可以选择任意名称，这里我们使用pythonenv：

```bash
virtualenv pythonenv
```

4、激活虚拟环境：

```bash
source pythonenv/bin/activate
```

5、在完成操作之后，还可通过以下命令来关闭virtualenv：

```bash
deactivate
```

在Windows中， 运行pip install virtualenv命令来安装虚拟环境。virtualenv的安装步骤与Linux相同。

**译者注：**在安装了virtualenv之后，还可安装 Virtualenv Wrapper来更方便管理虚拟环境，关于环境搭建还可参见本博客[Django环境搭建及开发](https://alanhou.org/django/)

### 安装Geany和PyCharm

通过https://www.geany.org/download/releases下载Geany并下载所需的二进制文件。根据指示来进行安装。

通过https://www.jetbrains.com/pycharm/download/下载PyCharm并根据指示来进行安装。

## Python 解释器

Python是一种解释性语言。有一个称为Python解释器或Python shell的交互式终端。这个shell可供我们无需创建脚本来逐行执行程序。

我们可以在这个Python交互式终端中访问Python的内置函数和库、安装模块和命令执行历史。这个终端为我们提供了研究Python的机会。你可以将准备好的代码拷贝到脚本中。

#### Python和Bash脚本的区别

这一部分中，我们将学习Python和Bash脚本的区别。它们的区别如下：

- Python是一种脚本语言，而Bash是一种用于进入和执行命令的shell
- 使用Python更易于处理更大的程序
- Python中大部分的事可通过导入模块来使用一行代码调用函数

### 开启交互终端

我们可以在已安装了Python的电脑上访问Python交互终端。运行如下命令来开启Python交互终端：

```bash
$ python
```

**译者注：**在 Linux 中#号提示符为 root 用户，其它用户为$

以上命令将启动默认的Python交互终端。

Linux中如果在终端中写入 python，开启的是python2.7的终端。如果你想要启动python3的终端，则在终端中输入python3并按下 Enter 键。

在Windows中，我们可以在Command命令行中输入 python，就会在终端中启动所下载的Python版本。

### 使用Python交互终端编写脚本

Python交互终端的起始提示符为>>>。在该终端中可输入Python命令，在>>>之后进行编写。如以下截图所示：

[![Python自动化脚本-运维人员宝典第一章 Python脚本概述](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021602502453.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021602502453.jpg)

现在，我们来看如何为变量赋值，示例如下：

```python
>>> name = 'John'
```

这时我们为name变量赋了一个字符串值John。按下Enter进入了一个以>>>提示符开头的新行：

```
>>> name = 'John'>>>
```

现在，我们来看一个为变量赋值的示例并执行数学运算来获取值：

```python
>>> num1 = 5000
>>> num2 = 3500 # 可在一行中进行赋值num1, num2 = 5000, 3500
>>> num3 = num1 + num2
>>> print(num3)8500
>>> num4 = num3 - 2575
>>> print(num4)5925
>>>
```

这里我们对不同的变量进行赋值，对两个变量进行相加，并将其和存储在了第三个变量中，还在终端(Terminal)中打印出了和。然后，我们对结果变量进行了减法运算，将输出存到了第四个变量中。接着我们将差在终端中进行了打印。这告诉我们可以使用 Python 解释器作为计算器来进行使用。

```python
>>> 509 / 2223.136363636363637
>>>
```

以上，我们执行了除法运算。509除以22并得到了商23.136363636363637。

### 多行模式

在Python解释器中编写多行代码时（比如 if 语句、 for循环、while 循环和函数），解释器会使用三个点(…) 作为二级提示符来延续代码行。要退出这些行，我们需要连续按下两次 Enter 键。我们来看看如下的示例：

```python
>>> val1 = 2500
>>> val2 = 2400
>>> if val1 > val2:...   print("val1大于val2")... else:...   print("val2大于val1")...val1大于val2
>>>
```

本例中，我们对两个变量val1和val2进行了整数值的赋值，并检查val1是否大于val2。上例中val1大于val2，因此 if 代码块中的语句执行了打印。注意 if 和 else 代码块中的语句需要进行缩进。如果不使用缩进，就会得到如下报错：

```python
>>> if val1 > val2:... print("val1大于val2") File "<stdin>", line 2  print("val1大于val2")    ^IndentationError: expected an indented block
```



### 通过Python解释器导入模块

如果你导入任何模块，Python解释器会检查该模块是否存在。我们可通过 import 语句来进行实现。如果该模块存在，在按下 Enter 键之后就可以看到>>> 前置提示符。这表示执行成功。如果该模块不存在，则会在Python解释器中显示报错。

```python
>>> import time
>>>
```

在导入time模块之后，我们获得了>>> 前置提示符，这表示该模块存在并且这条命令成功执行了：

```python
>>> import matplotlib
```

如果模块不存在，就会返回Traceback的报错：

```bash
Traceback (most recent call last): File "<stdin>", line 1, in <module>ImportError: No module named 'matplotlib'
```

这里matplotlib不可用，因此给出了报错：ImportError: No module named ‘matplotlib’。

要解决这一报错，我们需要安装matplotlib（译者注：pip3 install matplotlib）然后再次导入matplotlib。在安装matplotlib之后，就能够导入这一模块了，如下：

```python
>>> import matplotlib
>>>
```



### 退出Python终端

在Python终端有两种方式可以退出：

- 快捷键: Ctrl + D
- 使用quit()或exit()函数

#### 快捷键

使用快捷键Ctrl + D将会得到如下代码：

```python
>>> val1 = 5000
>>> val2 = 2500
>>>>>> val3 = val1 - val2
>>> print (val3)2500
>>>vagrant@ubuntu-xenial:~$
```



#### 使用quit()或exit() 函数

使用quit()可退出Python交互终端，会回到原来的命令终端：

```python
>>> Lion = 'Simba'
>>> quit()
vagrant@ubuntu-xenial:~$
```



### 缩进和制表符Tab

在Python中编写代码块必须使用缩进。缩进有助于编写函数、决策语句、循环语句和类。这让Python程序的读取更为容易。

我们使用缩进来表示Python程序的代码块。对代码块的缩进，可以使用空格或制表符（tab）。参见如下示例：

```python
if val1 > val2: 
    print ("val1大于val2")
    print("这部分代码没有进行缩进")
```

在上例中，我们对print语句进行了缩进，因为它位于 if 代码块中。第二个print语句不在 if 代码块中，所以没有对其进行缩进。

### 变量

类似一些其它编程语言，Python 中无需事先声明变量。Python 中可以想一个任意名称来作为变量名并进行赋值（**译者注：**仅能使用字母、数字和下划线且不能以数字开头）。可以在我们的程序中使用该变量。因此，Python 中我们可以在任何需使用的时候声明变量。

Python 中变量的值以及类型都可以在程序的执行过程中进行修改。以下代码中我们对变量赋值100：

```python
>>> n = 100 # 这里我们对变量 n 赋值100，并在下面对n 的值加1
>>> n = n + 1
>>> print(n)101
>>>
```

以下为在执行过程中变量类型可进行改变的示例：

```python
>>> a = 50 # 数据类型被隐式地设置为整型
>>> a = 50 + 9.50 # 数据类型被修改为浮点型
>>> a = "Seventy" # 现在变成了字符串类型
```

Python处理不同数据类型的展现，也即不同类型的值会存储在不同的内存空间中。变量是我们用于赋值的名称：

```python
>>> msg = 'And now for something completely different'
>>> a = 20
>>> pi = 3.1415926535897932
```

上例中进行了三次赋值。第一次将一个字符串赋值为名为msg的变量。第二次将一个整型赋值为名为a的变量，最后一次是一个圆周率pi的赋值。

变量的类型为它所引用的值的类型，查看以下代码：

```python
>>> type(msg)<class 'str'
>>>> type(a)<class 'int'
>>>> type(pi)<class 'float'>
```



#### 创建变量和赋值

在Python中，变量无需显式地进行声明来保留内存空间。在对变量进行赋值时即会自动完成声明。Python中单个等号=用于为变量赋值。

思考如下示例的执行：

```python
#!/usr/bin/python3
name = 'John'
age = 25
address = 'USA'
percentage = 85.5
print(name)
print(age)
print(address)
print(percentage) 
#输出如下：
John
25
USA
85.5
```

在上例中，我们将John赋值给变量name、25赋值给变量age、USA赋值给变量address以及将85.5赋值给变量percentage。

我们无需像在其它编程语言中那样事先声明变量。因此，查看值的解释器可获得变量的类型。在前例中，name和address是字符串类型，age是整型，percentage是浮点类型。

使用同一值进行多个变量的赋值可以这样做：

```python
x = y = z = 1
```

上例中我们创建了三个变量并使用整数1为它们赋值，会为这三个变量分配同一个内存地址。

在Python中，我们还可以在同一行中对多个变量赋多个值：

```python
x, y, z = 10, 'John', 80
```

这里我们声明一个字符串变量y，将John赋值给它，以及两个整型变量x和z，分别用10和80为它们赋值。

### 数值

Python解释器也可发挥计算器的作用。只需输入表达式，它就会返回值。括号( )用于进行分组，如下例所示：

```python
>>> 5 + 510
>>> 100 - 5*575
>>> (100 - 5*5) / 155.0
>>> 8 / 51.6
```

整型数值是int类型，小数部分是float类型。

> ℹ️在Python中，除法(/) 运算符总是返回浮点值。向下取整运算符(//)获取的是整型结果。%运算符用于计算余数。

思考如下示例：

```python
>>> 14/34.666666666666667
>>> 14//34
>>> 14%32
>>> 4*3+214
```

计算幂值（指数运算），Python使用**运算符，如下例所示：

```python
>>> 8**3512
>>> 5**778125
```

等号(=)用于对变量赋值：

```python
>>> m = 50
>>> n = 8 * 8
>>> m * n3200
```

如果变量不存在，而我们还是使用该变量，那么解释器会显示错误：

```python
>>> kTraceback (most recent call last): File "<stdin>", line 1, in <module>NameError: name 'k' is not defined>>>
```

如果运算符连接不同类型的操作数，那么得到的值将会是浮点数：

```python
>>> 5 * 4.75 - 122.75
```

在Python交互终端中，**_** 包含上一次打印过的表达式值，如下例所示：

```python
>>> a = 18.5 / 100
>>> b = 150.50
>>> a * b27.8425
>>> b + _178.3425
>>> round(_, 2)178.34
```

数值数据类型存储数字，这是一种不可变的数据类型。如果进行改变，Python会为修改的数据类型分配一个新的对象。

我们可以通过赋值来创建数值对象，示例如下：

```
>>> num1 = 50
>>> num2 = 25
```

del语句用于删除单个或多个变量。参考如下示例：

```python
>>> num = num_a = num_b = 1
>>> del num
>>> del num_a, num_b
```



#### 数值类型转换

在一些情况下，我们需要显式地将数字从一种类型转换为另一种类型来满足一些要求。Python在一个表达式中内部实现。

- 输入int(a)来将a转换为整型
- 输入float(a)来将a转换为浮点数
- 输入complex(a)来将a转换复数，实部为a，虚部为0
- 输入complex(a, b)来将a和 b转换为实部为a，虚部为b 的复数。a和 b为数字表达式

## 字符串

和数值类型类似，字符串也是Python中一种数据结构。Python可以操作字符串。字符串可通过如下方式表示：

- 包含在单引号(‘…’)中
- 包含在双引号(“…”)中

参见如下示例：

```python
>>> 'Hello Python''Hello Python'
>>> "Hello Python"'Hello Python'
```

字符串是一组字符。我们可以像下面这样一次访问一个字符：

```python
>>> city = 'delhi'
>>> letter = city[1]
>>> letter = city[-3]
```

在第二条语句中，我们从city中选择数字为1的字符并将其赋值给letter。方括号中的数字为索引。索引表示要访问的字符，它从0开始。因此在前例中执行在赋值后输入 letter，将得到如下输出：

```
city	d e l h i 
索引	0 1 2 3 4	-5 -4 -3 -2 -1 
输出：el
```



#### 字符串拼接(+)和重复(*)

下一步我们来进行字符串的拼接和重复。参照如下代码：

```
>>> 3 * 'hi' + 'hello''hihihihello'
```

上例中，我们进行字符串拼接和重复。3 * ‘hi’表示打印hi三次，使用+符号，我们在hi之后连接了字符串hello。

我们可以通过把字符串连续放在一起自动拼接两个字符串。这两个字符串必须包含在引号之间，如下所示：

```
>>> 'he' 'llo''hello'
```

这一特性在字符串很长又想要分开输入时非常有用，示例如下：

```
>>> str = ('Several strings'... ' joining them together.')
>>> str'Several strings joining them together.'
```



#### 字符串切片

字符串支持切片(slice)操作，这表示从字符串获取指定范围的字符。我们来看看下面的例子。注意起始的索引值是包含在内的，而结束值则**排除在外**。

假设字符串为str = “Programming”：

```
>>> str[0:2]'Pr'>>> str[2:5]'ogr'
```

默认省略不写的第一个索引为0（省略第二个索引默认获取第一个索引到最后的所有字符），如下例所示：

```
>>> str = "Python"
>>> str[:2] + str[2:]'Python'
>>> str[:4] + str[4:]'Python'
>>> str[:2]'Py'
>>> str[4:]'on'
>>> str[-2:]'on'
```



#### 访问字符串中的值

我们可以通过方括号使用切片来访问字符串中的字符。我们还可以访问字符串中指定范围内的字符。参照如下示例：

```python
#!/usr/bin/python3
str1 = 'Hello Python!'
str2 = "Object Oriented Programming"
print("str1[0]: ", str1[0])
print("str2[1:5]: ", str2[1:5]) 
#输出：
str1[0]: H
str2[1:5]: bjec
```



#### 更新字符串

我们可以对一个指定索引重新赋新值来更新字符串。参照如下示例：

```python
#!/usr/bin/python3
str1 = 'Hello Python!'
print("Updated String: - ", str1[:6] + 'John') 
#输出：
Updated String: - Hello John
```



#### 转义字符

Python 支持不可打印的转义字符（escape character），可通过反斜线标记来进行展示。转义字符在单引号和双引号字符串中均可进行解析：

| 标记  | 十六进制字符 | 描述                                     |
| :---- | :----------- | :--------------------------------------- |
| a     | 0x07         | 响铃或警告                               |
| b     | 0x08         | 退格（Backspace）                        |
| cx    |              | Control-x                                |
| n     | 0x0a         | 新起一行                                 |
| C-x   |              | Control-x                                |
| e     | 0x1b         | 转义                                     |
| f     | 0x0c         | 换页                                     |
| s     | 0x20         | 空格                                     |
| M-C-x |              | Meta-control-x                           |
| x     |              | 字符x                                    |
| nnn   |              | 八进行标记，n为0到7范围内的值            |
| r     | 0x0d         | 回车                                     |
| xnn   |              | 十六进制标记，n为0-9, a-f或A-F范围内的值 |
| t     | 0x09         | Tab制表符                                |
| v     | 0x0b         | 垂直制表符                               |

#### 特殊的字符串运算符

下表中显示了字符串的特殊运算符，假定a为Hello，b为World：

| 运算符 | 描述                                                 | 示例                  |
| :----- | :--------------------------------------------------- | :-------------------- |
| +      | 拼接：将运算符两边的值相加                           | a + b将得到HelloWorld |
| []     | 切片：得到给定索引的字符串                           | a[7]将得到r           |
| [ : ]  | 范围切片：得到指定范围内的字符                       | a[1:4]将得到ell       |
| *      | 重复：创建新的字符串，将相同字符串的多个拷贝进行拼接 | a*2将得到HelloHello   |
| not in | 成员：如果字符不在字符串中返回true                   | Z not in a将得到1     |
| in     | 成员：如果字符在字符串中返回true                     | H in a将得到1         |
| %      | 格式化：执行字符串格式化                             |                       |

#### %字符串格式化运算符

%是Python中的一个字符串格式化运算符。参照如下示例：

| 12345 | #!/usr/bin/python3print("Hello this is %s and my age is %d !" % ('John', 25)) 输出：Hello this is John and my age is 25 ! |
| ----- | ------------------------------------------------------------ |
|       |                                                              |

下表显示了配合%使用的符号列表：

| 序号 | 格式符号和转化                         |
| :--- | :------------------------------------- |
| 1    | %c – 字符                              |
| 2    | %s – 在格式化之前通过str()转换的字符串 |
| 3    | %i – 有符号十进制整数                  |
| 4    | %d – 有符号十进制整数                  |
| 5    | %u – 无符号十进制整数                  |
| 6    | %o – 八进制整数                        |
| 7    | %x – 十六进制整数（小写字母）          |
| 8    | %X –十六进制整数（大写字母）           |
| 9    | %e – 指数标记（使用小写 e）            |
| 10   | %E –指数标记（使用大写 E）             |
| 11   | %f – 浮点实数                          |

#### Python中的三引号

Python对字符串使用三引号的表示可跨越多行，包括新行和制表符。三引号的语法包含三个连续的单引号或双引号。参照如下代码：

```python
#!/usr/bin/python3
para_str = """Python is a scripting language which was created byGuido van Rossum in 1991, which is used in various sectors such as GameDevelopment, GIS Programming, Software Development, web development,Data Analytics and Machine learning, System Scripting etc."""
print (para_str) 
#输出内容：
Python is a scripting language which was created byGuido van Rossum in 1991, which is used in various sectors such as GameDevelopment, GIS Programming, Software Development, web development,Data Analytics and Machine learning, System Scripting etc.
```



#### 字符串是不可变的

字符串是不可变的，表示我们不能修改它的值。参照如下示例：

```python
>>> welcome = 'Hello, John!'
>>> welcome[0] = 'Y'Traceback (most recent call last): File "<stdin>", line 1, in <module>TypeError: 'str' object does not support item assignment
```

因为字符串是不可变的（immutable），我们不能修改现有字符串。但我们可以创建一个与原来不同的新字符串：

```python
>>> str1 = 'Hello John'
>>> new_str = 'Welcome' + str1[5:]
>>> print(str1)
Hello John
>>> print(new_str)
Welcome John
>>>
```



## 理解列表

Python支持一种称为列表（list）的数据结构，它是一个可变和有序的元素序列。列表中的每个元素称为列表项。列表通过在方括号[ ]之间插入值定义。列中的每个元素都会给定一个数值，称们称之为位置或索引。索引从0开始，也即，第一个索引为0，第二个索引为1，以此类推。我们可对列表进行如下运算：索引、切片、相加、相乘以及检查是否为列表成员。

Python内置的len函数返回列表的长度。Python还有查找列表中最大项（max）和最小项（min）的函数。列表可以是数值列表、字符串列表或混合列表。

以下是创建列表的代码：

```python
>>> l = list()
>>> numbers = [10, 20, 30, 40]
>>> animals = ['Dog', 'Tiger', 'Lion']
>>> list1 = ['John', 5.5, 500, [100, 450]]
```

这里我们创建了三个列表：第一个是numbers，第二个是animals，第三个是list1。列表中有另一个列表称为嵌套列表。list1是一个嵌套列表。不包含任何元素的列表称为空列表，可通过空的中括号[]来创建空列表。

你可能已经猜到，可将列表赋值给变量：

```python
>>> cities = ['Mumbai', 'Pune', 'Chennai']
>>> numbers_list = [75, 857]
>>> empty_list = []
>>> print(cities, numbers_list, empty_list)
['Mumbai', 'Pune', 'Chennai'] [75, 857] []
```



### 访问列表中的值

我们可以使用索引值来访问列表中的值。我们将索引数字放在[ 和 ]之间。索引从0开始。参见如下示例：

```python
#!/usr/bin/python3
cities = ['Mumbai', 'Bangalore', 'Chennai', 'Pune']
numbers = [1, 2, 3, 4, 5, 6, 7]
print(cities[0])
print(numbers[1:5]) 
输出结果：
Mumbai[2, 3, 4, 5]
```



### 更新列表

可以更新列表中的元素，如以下代码所示：

```python
#!/usr/bin/python3
cities = ['Mumbai', 'Bangalore', 'Chennai', 'Pune']
print('Original Value: ', cities[3])cities[3] = 'Delhi'
print('New value: ', cities[3]) 
输出结果：
Original Value: Pune
New value: Delhi
```



### 删除列表元素

要删除列表中元素，如果知道要具体删除的元素可使用del语句。如果不知道具体要删除的列表项索引可使用remove()。参见如下示例：

```python
#/usr/bin/python3
cities = ['Mumbai', 'Bangalore', 'Chennai', 'Pune']
print("Before deleting: ", cities)del cities[2]# cities.remove("Chennai") # 相同效果的补充
print("After deleting: ", cities) 
输出结果：
Before deleting: ['Mumbai', 'Bangalore', 'Chennai', 'Pune']After deleting: ['Mumbai', 'Bangalore', 'Pune']
```



### 基本列表运算

有五种基本列表运算：

- 拼接
- 重复
- 取长度
- 成员关系
- 迭代

| 描述   | 表达式                                   | 结果                           |
| :----- | :--------------------------------------- | :----------------------------- |
| 拼接   | [30, 50, 60] + ['Hello', 75, 66]         | [30, 50, 60, 'Hello', 75, 66]  |
| 成员   | 45 in [45, 58, 99, 65]                   | TRUE                           |
| 迭代   | for x in [45, 58, 99]: print(x, end=' ') | 45 58 99                       |
| 重复   | ['Python'] * 3                           | ['Python', 'Python', 'Python'] |
| 取长度 | len([45, 58, 99, 65])                    | 4                              |

### 列表运算

在这一部分中，我们将学习基本列表运算：拼接和重复。

+运算符将列表进行拼接：

```python
>>> a = [30, 50, 60]
>>> b = ['Hello', 75, 66]
>>> c = a + b
>>> print(c)[30, 50, 60, 'Hello', 75, 66]
```

相似地，*运算符以给定次数重复列表：

```python
>>> [0] * 4[0, 0, 0, 0]
>>> ['Python'] * 3['Python', 'Python', 'Python']
```



### 索引、切片和矩阵

列表索引与字符串索引的运作方式相同。列表值可通过索引来访问。如果尝试将不存在的元素写入列表，会得到IndexError。如果索引为负值，会从列表的最后开始倒数。

现在我们创建一个名为cities的列表并查看列表的索引运算：

```python
cities = ['Mumbai', 'Bangalore', 'Chennai', 'Pune']
```



| 描述               | 表达式     | 结果                             |
| ------------------ | ---------- | -------------------------------- |
| 索引从0开始        | cities[2]  | ‘Chennai’                        |
| 切片：获取一个片段 | cities[1:] | [‘Bangalore’, ‘Chennai’, ‘Pune’] |
| 负数：从右开始数   | cities[-3] | ‘Bangalore’                      |

## 元组

Python 的元组(tuple)数据结构是不可变的，这表示不能修改元组中的元素。 基本上，元组是一个以逗号分隔的值的序列，以括号( )进行包裹。和列表类似，元组是一个有序的元素序列：

```python
t1 = 'h', 'e', 'l', 'l', 'o'
```

元组以括号( )进行包裹：

```python
t1 = ('h', 'e', 'l', 'l', 'o')
```

我们还可以创建一个只有一个元素的元组，仅需在元组的最后加一个逗号：

```python
>>> t1 = 'h',
>>> type(t1)<class 'tuple'>
```

把值放到括号中并不是元组：

```python
>>> t1 = ('a')
>>> type(t1)<class 'str'>
```

我们可以使用tuple()函数来创建空的元组：

```
>>> t1 = tuple()
>>> print(t1)()
```

如果该函数的参数是一个序列（字符串、列表或元组），结果是这个序列元素组成的元组：

```
>>> t = tuple('mumbai')
>>> print(t)('m', 'u', 'm', 'b', 'a', 'i')
```

元组的值在括号( ) 中以逗号分隔：

```
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])a
```

切片运算符选取一个范围内的元素。

```
>>> print(t[1:3])('b', 'c')
```



#### 访问元组中的值

要访问元组中的值，使用方括号切片与单个或多个索引结合来获取对应索引的值，如下例所示：

```python
#!/usr/bin/python3
cities = ('Mumbai', 'Bangalore', 'Chennai', 'Pune')
numbers = (1, 2, 3, 4, 5, 6, 7)
print(cities[3])
print(numbers[1:6]) 
#输出结果：
#Pune(2, 3, 4, 5, 6)
```



#### 更新元组

在Python中元组是不可更新的，因为元组是不可变的。但是我们通过当前元组来新建一个元组，如下例所示：

```python
#!/usr/bin/python3
cities = ('Mumbai', 'Bangalore', 'Chennai', 'Pune')
numbers = (1, 2, 3, 4, 5, 6, 7)
tuple1 = cities + numbers
print(tuple1) 
#输出结果：
#('Mumbai', 'Bangalore', 'Chennai', 'Pune', 1, 2, 3, 4, 5, 6, 7)
```



### 删除元组元素

我们不能删除单个数据元组。因此要显式地删除整个元组，使用del语句。参照如下示例：

```python
#!/usr/bin/python3
cities = ('Mumbai', 'Bangalore', 'Chennai', 'Pune')
print("Before deleting: ", cities)
del citiesprint("After deleting: ", cities) 
#输出结果：
#Before deleting: ('Mumbai', 'Bangalore', 'Chennai', 'Pune')Traceback (most recent call last): File "test.py", line 5, in <module>  print("After deleting: ", cities)NameError: name 'cities' is not defined
```



### 基本元组运算

和列表相似，有五种基本元组运算：

- 拼接
- 重复
- 取长度
- 成员关系
- 迭代

| 描述   | 表达式                                   | 结果                           |
| :----- | :--------------------------------------- | :----------------------------- |
| 拼接   | (30, 50, 60) + ('Hello', 75, 66)         | (30,50,60,'Hello',75,66)       |
| 成员   | 45 in (45, 58, 99, 65)                   | TRUE                           |
| 迭代   | for x in (45, 58, 99): print(x, end=' ') | 45 58 99                       |
| 重复   | ('Python') * 3                           | ('Python', 'Python', 'Python') |
| 取长度 | len((45, 58, 99, 65))                    | 4                              |

### 索引、切片和矩阵

元组索引的运作方式和列表相同。使用索引可访问元组的值。如果尝试读取或写入不存在的元素，会报出IndexError。如果索引为负值，则从元组的最后向前数。

现在我们创建一个名为cities的元组并查看列表的索引运算：

```
cities = ('Mumbai', 'Bangalore', 'Chennai', 'Pune')
```



| 描述               | 表达式     | 结果                             |
| ------------------ | ---------- | -------------------------------- |
| 索引从0开始        | cities[2]  | ‘Chennai’                        |
| 切片：获取一个片段 | cities[1:] | (‘Bangalore’, ‘Chennai’, ‘Pune’) |
| 负数：从右开始数   | cities[-3] | ‘Bangalore’                      |

#### max()和min()

使用max()和min()函数，我们可以查找元组中的最大值和最小值。这两个函数让我们可以找到量化数据的相关信息。我们来看看下面这个例子：

```
>>> numbers = (50, 80, 98, 110.5, 75, 150.58)
>>> print(max(numbers))
150.58
```

使用max()可以获取元组中的最大值。相似地，我们可以使用min()函数：

```
>>> numbers = (50, 80, 98, 110.5, 75, 150.58)
>>> print(min(numbers))
50
```

因此这里我们获取到了最小值。

## 集合

集合（set）是一个无序且无重复值的元素集。集合的基本用法是检查成员关系和删除重复项。这些集合对象支持数学运算，如并集、交集、差集以及对等差分。我们可以使用大括号{}或函数set()来创建集合。如果想要创建一个空的集合，使用set()而不是{}。

以下是一个简单的演示：

```python
>>> fruits = {'Mango', 'Apple', 'Mango', 'Watermelon', 'Apple', 'Orange'}
>>> print(fruits){'Orange', 'Apple', 'Watermelon', 'Mango'}
>>> 'Orange' in fruitsTrue
>>> 'Onion' in fruitsFalse
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a{'c', 'r', 'b', 'a', 'd'}
>>> a - b{'r', 'b', 'd'}
>>> a \| b{'c', 'l', 'd', 'b', 'z', 'r', 'm', 'a'}
>>> a & b{'c', 'a'}
>>> a ^ b{'l', 'd', 'b', 'z', 'r', 'm'}
```

**译者注：**因集合是无序的，所以读者在执行相同代码时得到的结果顺序可能会略有不同

Python 中还支持集合推导式(set comprehension)，参见如下代码：

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a{'r', 'd'}
```



## 字典

字典（dictionary）是Python中的一种数据类型，它由键值对组成并包裹在大括号{}中。字典是无序的并通过键进行索引，且每个键必须是唯一的。这些键必须为不可变类型。元组在包含字符串、数字或元组时可作为字典的键。

仅仅使用一对大括号{}会创建一个空的字典。字典的主要运算是使用某些键来存储值并通过给定的键来提取值。同样可以使用 del 来删除一个键值对。如果使用了已有的键进行存储，就会抹除该键原来关联的值。使用不存在的键来提取值会报错。以下是使用字典的一个小例子：

```python
>>> student = {'Name':'John', 'Age':25}
>>> student['Address'] = 'Mumbai'
>>> student{'Name': 'John', 'Address': 'Mumbai', 'Age': 25}
>>> student['Age']25
>>> del student['Address']
>>> student{'Name': 'John', 'Age': 25}
>>> list(student.keys())
['Name', 'Age']
>>> sorted(student.keys())
['Age', 'Name']
>>> 'Name' in studentTrue
>>> 'Age' not in studentFalse
```

自选的键值表达式配合字典推导式可用于创建字典：

```python
>>> {x: x**2 for x in (4, 6, 8)}
{4: 16, 6: 36, 8: 64}
```

在键是简单的字符串时，使用关键字参数的方式指定键值对更为容易：

```python
dict(John=25, Nick=27, Jack=28)
{'Nick': 27, 'Jack': 28, 'John': 25}
```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字典的基础使用和练习
author: gxcuizy
date: 2018-10-18
"""

# 程序主入口
if __name__ == '__main__':
    # 定义一个空字典
    dict_none = {}
    print(dict_none)

    # 定义一个非空字典
    score_dict = {'math': 96, 'english': 97, 'chinese': 98}
    print(score_dict)

    # 使用使用dict()创建字典
    tuple_math = ('math', '96')
    tuple_english = ('english', '97')
    tuple_chinese = ('chinese', '98')
    dict_a = dict([tuple_math, tuple_english, tuple_chinese])
    print(dict_a)

    # 使用zip()合并两个列表分别作为字典的key和value
    list_key = ['math', 'english', 'chinese']
    list_value = [96, 97, 98]
    score = dict(zip(list_key, list_value))
    print(score)

    # 读取字典的value
    print(score_dict['math'])

    # 修改字典的value
    score_dict['chinese'] = 100
    print(score_dict)

    # keys()获取字典所有的key
    dict_key = score_dict.keys()
    print(dict_key)

    # values()获取字典所有的value
    dict_value = score_dict.values()
    print(dict_value)

    # 使用get()获取key值对应的value
    math_value = score_dict.get('math')
    print(math_value)

    # in 和 not in 判断key在字典中是否存在
    print('math' in score_dict)
    print('history' not in score_dict)

    # 使用items()把字典的对应的key和value组成一个元组返回一个列表
    score_list = score_dict.items()
    print(score_list)

    # 使用copy()复制一个字典
    score_copy = score_dict.copy()
    print(score_copy)

    # 使用clear()清空字典所有元素
    score_copy.clear()
    print(score_copy)

    # pop()删除一个key对应的元素，key存在，返回对应的value，可以指定不存在时的默认返回值
    pop_result = score_dict.pop('english')
    print(pop_result)
    pop_result = score_dict.pop('history', '不存在')
    print(pop_result)

    # 使用update()更新字典，也就是追加元素的意思
    score_dict.update({'history': 95})
    print(score_dict)

    # 使用fromkyes()创建一个新的字典，key来自序列，value来自自定义（默认为None）
    score_new = score_copy.fromkeys([11, 22, 33, 44], 100)
    print(score_new)

```



```python
#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liyupi
@file: for_dict-1.py
@time: 2022/03/25
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"循环字典的key和value"

# 程序主入口
if __name__ == '__main__':
    # 定义一个字典
    score_dict = {'math': 96, 'english': 97, 'chinese': 98}

    # 循环获取key
    key: str
    for key in score_dict:
        print(key)

    # 循环获取value
    for key in score_dict:
        print(score_dict[key])

    # 循环获取key和value
    for key, value in score_dict.items():
        print(key, value)

```



## 解析命令行参数

在这一部分中，我们将学习参数的解析以及用于解析参数的模块。

#### Python 中的命令行参数

我们可以在命令行中添加额外的参数来启动程序。Python的程序可通过命令行参数来启动。让我们来看看下面这个例子：

```
$ python program_name.py img.jpg
```

这里program_name.py和img.jpg都是参数。我们将使用模块来获取这些参数：

| 模块     | 用法                        | Python版本 |
| -------- | --------------------------- | ---------- |
| optparse | 已淘汰                      | < 2.7      |
| sys      | 所有sys.argv中的参数 (基本) | 所有版本   |
| argparse | 创建一个命令行接口          | >= 2.3     |
| fire     | 自动生成命令行接口(CLI)     | All        |
| docopt   | 创建CLI接口                 | >= 2.5     |

#### Sys.argv

sys模块用于访问命令行参数。len(sys.argv) 函数包含参数的数量。要打印所有的参数，只需执行str(sys.argv)。让们来看看下面这个例子：

```python
# 01.py
import sys
print('Number of arguments: ', len(sys.argv))
print('Argument list: ', str(sys.argv)) 
# 运行
python3 01.py img
# 执行结果Number of arguments: 2Argument list: ['01.py', 'img']
```



## 决策制定

当我们想要在条件为true时执行一个代码时，就需要使用到决策制定（译者注：流程控制语句）了。if…elif…else语句在Python中用于决策制定。

### Python的if语句语法

以下是if语句的语法：

```python
if test expression:    
    statement(s)
```

这里，程序运行了test 表达式并仅在该表达式为true时才执行下面的语句。如果表达式为false，则不会执行语句。

Python中if语句的主体通过缩进来表示。语句主体通过缩进来表示第一行的开始，通过取消缩进表示主体的结束。我们来看看下面这个例子：

```python
a = 10
if a > 0:    
    print(a, "is a positive number.")
    print("This statement is always printed.") 
a = -10
if a > 0:    
    print(a, "is a positive number.") 
#输出结果：
#10 is a positive number.This statement is always printed.
```



### Python的if…else语句语法

在这一部分，我们将学习if..else 语句。else代码块仅在if条件为false时执行。参见如下代码：

```python
if test expression:
        if block
else:
        else block
```

if..else语句运行test表达式，仅在test条件为true时运行主体内容。如果条件为false，else中的主体内容会被执行。缩进用于分割代码块。参见如下示例：

```python
a = 10
if a > 0:
        print("Positive number")
else:
        print("Negative number")
 
 
输出结果：
Positive number
```





### Python的if…elif…else语句语法

elif语句从多条语句中检查true值。只要运行的值为 true 就执行相应的代码块。参见如下代码：

```python
if test expression:
        if block statements
elif test expression:
        elif block statements
else:
        else block statements
```



elif是else if的简写，让我们可以检查多个表达式。如果if语句中的条件为false，它会检查下一个elif代码块的条件，以此类推。如果所有条件均为false，else中的主体内容会被执行。

if…elif…else中仅会根据条件执行其中一个代码块。if代码块仅能带有一个else代码块，但可以有多个elif代码块。我们来看看以下的示例：

```python
a = 10
if a > 50:
        print("a is greater than 50")
elif a == 10:
        print("a is equal to 10")
else:
        print("a is negative")
 
输出结果：
a is equal to 10
```





## 循环

要处理脚本中的所有循环需求，Python支持两类循环：

- for 循环
- while 循环

下面我们就来学习for 循环和while 循环。

### for循环

for循环遍历序列或其它可迭代对象中的每一项，并每次执行for代码块中的语句。参照如下代码：

```python
for i in sequence:    
    for loop body
```

```python

#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:liyupi
@file: logic-1.py
@time: 2022/03/25
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

"if、while逻辑判断的用法"

# 程序主入口
if __name__ == '__main__':
    # 简单if
    name = 'big_brother'
    if name == 'da_biao_guo':
        print('Please take me fly!')

    # if……else 的用法
    if name == 'da_biao_guo':
        print('Please take me fly!')
    else:
        print('Please take us fly!')

    # if……elif……else 的用法
    if name == 'da_biao_guo':
        print('Please take me fly!')
    elif name == 'xiao_biao_mei':
        print('Please take us fly!')
    else:
        print('Please take you fly!')

    # while的用法-计算100以内所有偶数的和
    sum = 0
    n = 0
    while n <= 1000:
        if n % 2 == 0:
            sum += n
        n += 1
    print(sum)


```

此处i 为在每次迭代时获取序列中各项值的变量。在到达序列最后一项之前循环会一直执行。下图中进行了描述：

[![Python自动化脚本-运维人员宝典第一章 Python脚本概述](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021707562267.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021707562267.jpg)

参见如下示例：

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for i in numbers:
        sum = sum + i
        print("The sum is", sum)
 
输出结果：
The sum is 6
The sum is 11
The sum is 14
The sum is 22
The sum is 26
The sum is 28
The sum is 33
The sum is 37
The sum is 48
```





### range()函数

Python的range()函数会生成一个数字的序列。例如，range(10)会生成0到9的数字（共10个数字）。

我们还可以定义起始、结束和步长来作为参数，这时range()函数如下所示：

```python
range(start, stop, step size).
 
如未设置步长默认为1。
```



使用range()函数的 for 循环示例如下：

```python
for i in range(5):
        print("The number is", i)
 
输出结果：
The number is 0
The number is 1
The number is 2
The number is 3
The number is 4
```





### while循环

while是一个在测试表达式为true时不停遍历代码块的循环语句。我们在不知道要迭代多少次时使用这一循环。参见如下代码：

```python
while test_expression:
        while body statements
```



在while循环中，我们首先检查测试表达式。while仅在这个测试表达式为true时执行。在一个迭代后，会重新对表达式进行检查，并在表达式运行值为false前不停重复这一过程。下图中进行了描述：

[![Python自动化脚本-运维人员宝典第一章 Python脚本概述](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021708122270.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/02/2019021708122270.jpg)

以下为while循环的示例：

```python
a = 10
sum = 0
i = 1
while i <= a:
        sum = sum + i
        i = i + 1
        print("The sum is", sum)
 
 
运行结果：
The sum is 1
The sum is 3
The sum is 6
The sum is 10
The sum is 15
The sum is 21
The sum is 28
The sum is 36
The sum is 45
The sum is 55
```





## 迭代器

Python中的迭代器是可进行迭代的对象。这个对象会返回数据，每次返回一个元素。Python的迭代器对象实现了两个方法：__iter__()和__next__()。大多数情况下迭代器在循环、生成器和推导式中实现。

下例中，我们使用了next()函数，它会遍历所有的元素。在到达最后且没有更多数据返回时，会抛出StopIteration，如下例所示：

```python
numbers = [10, 20, 30, 40]
 
numbers_iter = iter(numbers)
 
print(next(numbers_iter))
print(next(numbers_iter))
print(numbers_iter.__next__())
print(numbers_iter.__next__())
 
next(numbers_iter)
 
 
输出结果：
10
20
30
40
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    next(numbers_iter)
StopIteration
```





## 生成器

我们可以使用Python生成器来创建迭代器。Python中生成器是返回一个可以迭代对象的函数。

### 如何在Python中创建生成器

在Python中创建生成器非常容易。我们可以定义一个函数，使用yield语句来代替return语句即可创建生成器。如果函数中至少包含一个yield语句，它就变成了一个生成器函数。yield和return语句会从函数中返回某些值。以下为示例：

```python
def my_gen():
        n = 1
        print("This is printed first")
        yield n
        n += 1
        print("This is printed second")
        yield n
        n += 1
        print("This is printed at last")
        yield n
 
for item in my_gen():
        print(item)
 
输出结果：
This is printed first
1
This is printed second
2
This is printed at last
3
```





## 函数

函数是执行特定任务的一组语句。使用函数有助于将我们的程序分成更小的部分。函数可避免重复并让代码可以复用，因此让程序组织的更好。来看下面的语法：

```python
def function_name:
        statement(s)
```



参见如下示例：

```python
def welcome(name):
        print("Hello " + name + ", Welcome to Python Programming!")
 
welcome("John")
 
输出结果：
Hello John, Welcome to Python Programming!
```





### return语句

return语句用于退出函数。参见如下的语法：

```
return [expression_list]
```



这个语句可能包含返回一个值的表达式。如果没有表达式，函数会返回None对象，如下例所示：

```python
def return_value(a):
        if a >= 0:
                return a
        else:
                return -a
 
print(return_value(2))
print(return_value(-4))
 
输出结果：
2
4
```





### Lambda函数

Python中匿名函数是未定义函数名的函数，称为lambda函数，使用关键字lambda进行定义。在需要短暂使用一个函数时我们使用这类函数。

lambda函数与内置的函数可共同使用，如filter()和map()。

filter()函数返回一个元素列表，并仅接收一个迭代值。以下为使用filter()的示例：

```pytho
numbers = [10, 25, 54, 86, 89, 11, 33, 22]
new_numbers = list(filter(lambda x: (x%2 == 0), numbers))
 
print(new_numbers)
 
输出结果：
[10, 54, 86, 22]
```



在本例中，filter()接收一个lambda函数以及一个列表来作为参数。

map()函数在应用指定函数之后返回一个结果列表。下面我们来看看使用map()的示例：

```python
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)
 
输出结果：
[2, 10, 8, 12, 16, 22, 6, 24]
```



这里，map()函数接收一个lambda函数和一个列表。

**译者补充：**提到 map 一般会想到另一个函数 reduce，同样可配合匿名函数使用，Python 3中使用 reduce 需要手动导入，示例如下

```python
>>> from functools import reduce
>>> reduce(lambda x, y: x+y, [1,2,3,4,5])
15
```





## 模块

模块只是包含Python语句和定义的文件。一个包含Python代码的文件（如sample.py）称为一个模块，并且模块名应为sample。使用模块，我们可以将大型的程序分解成更小和有组织的程序。模块的一个重要特性是复用性。我们无需在不同程序中拷贝经常使用到的函数定义，而是将它们定义在一模块中，然后需要使用时进行导入。

我们来创建一个模块并导入。我们将创建两个脚本：sample.py和add.py。然后在add.py中导入sample模块。现在将如下代码保存到sample.py文件中。我们来看看下面这个示例：

```python
# sample.py
def addition(num1, num2):
        result = num1 + num2
        return result
```



这里我们在名为sample的模块中定义了一个函数addition()。该函数接收两个数值并返回和。这样我们就创建了一个模块。我们可以在任意Python程序中导入该模块。

### 导入模块

在创建模块后，我们来学习如何导入这一模块。上例中我们创建了一个sample模块。现在我们就在add.py脚本中导入sample模块：

```python
# add.py
import sample
sum = sample.addition(10, 20)
print(sum)
 
输出结果：
30
```





## 总结

在本章中，我们概览了Python脚本语言。学习了如何安装Python以及各种工具。我们还学习了Python解释器以及如何使用它。我们学习了Python支持的数据类型、变量、数值和字符串、决策控制语句和Python中的循环语句。我们还学习了函数以及如何在脚本中使用函数，模块以及如何创建和导入模块。

在下一章[**Python脚本调试和性能测试**](https://alanhou.org/debugging-profiling-python-scripts/)中**，**我们将学习Python的调试技巧、错误处理（异常处理）、调试器工具、调试基本的程序崩溃、程序性能和用时测试以及加快程序运行。

☞☞☞ [第二章 Python脚本调试和性能测试](https://alanhou.org/debugging-profiling-python-scripts/)

## 问题

1. 什么是迭代器和生成器？

    迭代器是一个可进行迭代的对象。该对象会返回数据，每次返回一条。生成器是一个返回可进行迭代对象的函数。 

   

2. 列表是否可变？

    列表是可变的 

   

3. Python中的数据结构是什么？

    Python中的数据结构是可以共同存储数据的结构。换句话说，它们用于存储相关数据的集合。 

   

4. 如何访问列表中的值？

    我们可以通过索引来访问列表中的值。 

   

5. 什么是模块？

    模块是那些包含Python语句和定义的文件。 

   

## 扩展阅读

Python的所有文档可通过[官方网站](https://www.python.org/)获取。

还可以阅读如下图书：Learn Python Hard Way和Byte of Python来学习 Python 的基础知识。

**译者补充：**

Python 另一个重要的概念是装饰器，简单的示例如下

| 12345678910111213 | def decorator_demo(func):  def wrap_func(*args, **kwargs):    print("Inside decorator")    return func(*args, **kwargs)  return wrap_func @decorator_demodef func_a(something):  print("I am function a, doing {}".format(something)) if __name__ == "__main__":  func_a("test") |
| ----------------- | ------------------------------------------------------------ |
|                   |                                                              |

 

# 第二章 Python脚本调试和性能测试

## 什么是调试？

调试（debugging）是一个解决代码中错误或导致软件不能正常运行的问题的过程。Python中的调试非常容易。Python调试器设置条件断点并对源码逐行调试。我们将使用Python标准库中的 pdb 模块来对我们的Python脚本进行调试。

### Python 的调试技术

为更好的调试Python程序，可以使用不同的技术。我们就来看看Python调试的四种技术：

- print()语句：这是了解具体发生情况的最简单的方式，这样我们可以检查执行的内容
- logging：这类似于print语句但带更多的上下文信息，因此我们可以更全面的了解情况
- pdb调试器：这是最常使用的调试技术。使用 pdb 的优势是能够在命令行、解释器以及程序中使用 pdb
- IDE调试器：IDE有内置的调试器。这让开发者可以执行自己的代码，然后开发者可以在程序执行过程中检查代码

## 错误处理（异常处理）

在这一部分中我们将学习Python如何处理异常。但首先什么是异常呢？异常是在程序执行过程中发生的错误。每当错误发生时，Python会生成一个异常，使用try…except代码块来进行处理。有时异常程序无法处理，因此会导致报错信息。下面我们就来看一些异常的示例：

在你的终端中，启动python3交互控制台，我们一起来看一些异常示例：

```python
>>> 50 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 6 + abc*5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'abc' is not defined
>>> 'abc' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> import abcd
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'abcd'
```



这就是异常的一些示例。下面我们来看如何处理这些异常。

每当Python程序中发生错误时，就会抛出异常。我们也可使用raise关键字来强制抛出异常。

下来我们来看一个处理异常的try…except代码块。在try代码块中，我们将编写可能生成异常的代码。在except代码块中，我们将编写异常的处理方式。try…except的语法如下：

```python
try:
        statement(s)
except:
        statement(s)
```



一个try代码块可带有多个except语句。我们可通过在except关键字之后输入异常的名称来处理指定的异常。处理指定异常的语法如下：

```python
try:
        statement(s)
except exception_name:
        statement(s)
```



下面我们创建一个exception_example.py脚本来捕获ZeroDivisionError。在脚本中编写如下代码：

```python
a = 35
b = 37
try:
        c = a +b
        print("The value of c is:", c)
        d = b / 0
        print("The value of d is:", d)
except:
        print("Division by zero is not possible")
print("Out of try...except block")
```



像下面这样运行脚本，将会得到如下结果：

```
vagrant@python-scripting:~$ python3 exception_example.py
The value of c is: 72
Division by zero is not possible
Out of try...except block
```





## 调试器工具

Python中支持很多种调试工具：

- winpdb
- pydev
- pydb
- pdb
- gdb
- pyDebug

这一部分中，我们将学习pdb Python调试器。pdb是Python标准库的一部分并一直可以直接使用。

### pdb调试器

pdb模块用于调试Python程序。Python程序使用pdb交互源代码调试器来调试程序。pdb设置断点并检查栈帧，列出源代码。

下面我们将学习如何使用pdb调试器。使用这一调试器有三种方式：

- 在解释器之中
- 通过命令行
- 在Python脚本中

我们将创建一个pdb_example.py脚本并在该脚本中添加如下内容：

```python
class Student:
        def __init__(self, std):
                self.count = std
 
        def print_std(self):
                for i in range(self.count):
                        print(i)
                return
 
if __name__ == "__main__":
        Student(5).print_std()
```



使用这一脚本作为学习Python调试的示例，我们将了解如何启动调试器的细节。

### 解释器内调试

要从Python交互控制台中启动调试器，我们使用run()或runeval()。

启动python3交互控制台。运行如下命令来启动控制台：

```
$ python3
```



导入我们的pdb_example脚本名和pdb模块。下面我们将使用run()，并且我们会传入一个字符串表达式来作为run()的参数，由Python解释器自身进行运行：

```python
>>> import pdb_example
>>> import pdb
>>> pdb.run('pdb_example.Student(5).print_std()')
> <string>(1)<module>()
(Pdb)
```



要继续调试，在(Pdb)提示符之后输入continue并按下Enter（或直接输入 h并回车）。我果想要了解这里可以使用的选项，在(Pdb)提示符之后按下两次Tab键。

在输入continue之后，我们将得到如下的输出：

```python
>>> import pdb_example
>>> import pdb
>>> pdb.run('pdb_example.Student(5).print_std()')
> <string>(1)<module>()
(Pdb) continue
0
1
2
3
4
>>>
```





### 命令行调试

运行调试器最简单也最直接的方式是通过命令行。我们的程序将作为调试器的输入。我们可以这样在命令行中使用调试器：

```
python3 -m pdb pdb_example.py
```



在从命令行运行调试器时，源代码会被载入并在调试器找到的第一行停止执行。输入continue来继续调试。输出如下：

```python
vagrant@python-scripting:~$ python3 -m pdb pdb_example.py
> /home/vagrant/pdb_example.py(1)<module>()
-> class Student:
(Pdb) continue
0
1
2
3
4
The program finished and will be restarted
> /home/vagrant/pdb_example.py(1)<module>()
-> class Student:
(Pdb)
```





### Python脚本内调试

以上两种技术会在Python程序开始时启动调试器。但第三种方法对于长期处理来说最佳。要在脚本中启动调试器，使用set_trace()。

现在修改pdb_example.py文件如下：

```python
import pdb
 
class Student:
        def __init__(self, std):
                self.count = std
 
        def print_std(self):
                for i in range(self.count):
                        pdb.set_trace()
                        print(i)
                return
 
if __name__ == "__main__":
        Student(5).print_std()
```



现在运行程序如下：

```bash
vagrant@python-scripting:~$ python3 pdb_example.py
> /home/vagrant/pdb_example.py(10)print_std()
-> print(i)
(Pdb) continue
0
> /home/vagrant/pdb_example.py(9)print_std()
-> pdb.set_trace()
(Pdb)
```



set_trace()是一个Python函数，因此可以在程序的任意处调用它。所以我们有三种方式来启动调试器。

## 基本程序崩溃调试

在这一部分中，我们来看看trace模块。trace模块有助于追踪程序的执行。因此不论何时程序崩溃，我们都能了解在哪里出现的崩溃。我们可以在脚本中导入也可以通过命令行来使用trace模块。

现在我们将创建一个名为trace_example.py的脚本并在该脚本中编写如下代码：

```bash
class Student:
        def __init__(self, std):
                self.count = std
 
        def go(self):
                for i in range(self.count):
                        print(i)
                return
 
if __name__ == "__main__":
        Student(5).go()
```



输出如下：

```bash
vagrant@python-scripting:~$ python3 -m trace --trace trace_example.py
 --- modulename: trace_example, funcname: <module>
trace_example.py(1): class Student:
 --- modulename: trace_example, funcname: Student
trace_example.py(1): class Student:
trace_example.py(2): 	def __init__(self, std):
trace_example.py(5): 	def go(self):
trace_example.py(10): if __name__ == "__main__":
trace_example.py(11): 	Student(5).go()
 --- modulename: trace_example, funcname: __init__
trace_example.py(3): 		self.count = std
 --- modulename: trace_example, funcname: go
trace_example.py(6): 		for i in range(self.count):
trace_example.py(7): 			print(i)
0
trace_example.py(6): 		for i in range(self.count):
trace_example.py(7): 			print(i)
1
trace_example.py(6): 		for i in range(self.count):
trace_example.py(7): 			print(i)
2
trace_example.py(6): 		for i in range(self.count):
trace_example.py(7): 			print(i)
3
trace_example.py(6): 		for i in range(self.count):
trace_example.py(7): 			print(i)
4
trace_example.py(6): 		for i in range(self.count):
trace_example.py(8): 		return
 --- modulename: trace, funcname: _unsettrace
trace.py(77):         sys.settrace(None)
```



因此通过在命令行中使用trace –trace，开发人员可以对程序逐行追踪。这样在程序崩溃时，开发人员就会知道发生崩溃的实例。

## 程序性能和时耗分析

对Python程序进行性能分析（profiling）表示度量程序的执行时间。它计量每个函数所花的时间。Python的cProfile模块用于对Python程序进行性能分析。

### cProfile模块

正如前文所讲到的，性能分析表示度量程序的执行时间。我们就来使用cProfile Python模块对程序进行性能分析。

现在来编写一个cprof_example.py脚本并加入如下代码：

```python
mul_value = 0
def mul_numbers(num1, num2):
        mul_value = num1 * num2
        print("Local Value:", mul_value)
        return mul_value
 
mul_numbers(58, 77)
print("Global Value:", mul_value)
```



运行程序，将会看到如下的输出：

```
vagrant@python-scripting:~$ python3 -m cProfile cprof_example.py
Local Value: 4466
Global Value: 0
         6 function calls in 0.001 seconds
 
   Ordered by: standard name
 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 cprof_example.py:1(<module>)
        1    0.000    0.000    0.000    0.000 cprof_example.py:2(mul_numbers)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.001    0.000    0.001    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```



因此，使用cProfile，所有调用的函数都被打印，并包含各个函数所消耗的时间。下面我们来看看这些列头的含义：

- ncalls: 调用次数
- tottime: 给定函数花费的总时间
- percall: tottime除以ncalls所得的商
- cumtime: 当前以及其子函数所花费的累计时间
- percall: cumtime除以原始调用所得的商
- filename:lineno(function): 提供函数各自的数据

### timeit

timeit是一个Python模块，用于对Python脚本的各部分进行计时。我们可以在命令行中调用timeit，也可以在脚本中导入timeit模块。下面我们来编写一个脚本来对代码片断进行计时。创建一个timeit_example.py脚本并编写如下内容：

```python
import timeit
 
prg_setup = "from math import sqrt"
prg_code = '''
def timeit_example():
        list1 = []
        for x in range(50):
                list1.append(sqrt(x))
'''
 
# timeit 语句
print(timeit.timeit(setup = prg_setup, stmt = prg_code, number = 10000))
```



运行结果：

```
vagrant@python-scripting:~$ python3 timeit_example.py
0.0010215669999524835
```



使用timeit,，我们可以决定要对哪段代码进行性能的度量。因此，我们可以轻易地定义setup代码来作为我们想单独执行测试的代码片断。主代码默认运行100万次，但setup代码仅运行一次。

## 加速程序运行

有很多方式来让Python程序运行得更快，比如：

- 对认定为瓶颈的代码进行性能分析
- 使用内置函数和库，这样解释器不用执行不同循环
- 避免使用全局变量，因为Python在访问全局变量时速度很慢
- 使用已有的包

## 总结

在本章中，我们学习了调试程序和性能分析的重要性。还学习了用于调试的不同技术。我们学习了pdb Python调试器以及如何处理异常。还学习了如何使用Python中的cProfile和timeit模块来对脚本进行性能和时耗分析。最后我们学习了如何加速脚本的运行。

下一章中，我们将学习Python中的单元测试。我们会学习如何创建和使用单元测试。

☞☞☞ [第三章-单元测试-单元测试框架的介绍](https://alanhou.org/unit-testing-introduction-unit-testing-framework/)

## 课后问题

1. 要调试程序，使用哪个模块？

   点击查看

   

   调试程序，使用pdb模块。

2. 查看如何在ipython中使用所有的别名函数和魔法函数。

   点击查看

   

   使用%lsmagic，在运行ipython3之前，请执行sudo apt-get install ipython3进行安装

3. 什么是全局解释器锁（Global interpreter lock (GIL)）？

   点击查看

   

   全局解释器锁是一种计算机语言解释器用于同步线程执行的机制，这样同一时间只有一个原生线程在执行。

4. PYTHONPATH, PYTHONCASEOK, PYTHONHOME和PYTHONSTARTUP环境变量的目的是什么？

   点击查看

   

   - PYTHONPATH: 作用类似于PATH。该变量告诉Python解释器从何处查找导入程序的模块文件。它应包含Python源代码库目录并包含Python源代码。 PYTHONPATH有时由Python安装器进行预设。
   - PYTHONSTARTUP: 它包含含有Python源代码初始化文件的路径。在每次启动解释器时进行执行。在Unix中名称为.pythonrc.py，包含加载工具类或修改PYTHONPATH的一些命令。
   - PYTHONCASEOK: 在Windows中用于指引Python查找import语句中第一个忽略大小写的匹配文件。可将此变量设为任意值进行启用。
   - PYTHONHOME: 另一个模块搜索路径。通常内嵌于PYTHONSTARTUP或PYTHONPATH目录中来使用得模块库切换更为简易。

5. 以下代码的输出是什么？

   a) [0]

   b) [1]

   c) [1, 0]

   d) [0, 1]

   | 12345 | def foo(k):    k = [1]q = [0]foo(q)print(q) |
   | ----- | ------------------------------------------- |
   |       |                                             |

   点击查看

   

   答案是r:[0]
   在函数中创建了新的列表对象，失去了引用。可通过在k = [1]的前台对比k的 ID 来进行校验。

6. 以下哪个是无效变量？

   a) my_string_1

   b) 1st_string

   c) foo

   d) _

   点击查看

   

   答案是b. 变量量不可以数字开头。

## 扩展阅读

- 如何处理 Python 中的GIL问题：https://realpython.com/python-gil/
- 查看如何在命令行中使用pdb模块：https://fedoramagazine.org/getting-started-python-debugger/

下表转自菜鸟教程：

| 变量名        | 描述                                                         |
| :------------ | :----------------------------------------------------------- |
| PYTHONPATH    | PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。 |
| PYTHONSTARTUP | Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此变量指定的文件中的代码。 |
| PYTHONCASEOK  | 加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写. |
| PYTHONHOME    | 另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。 |

以下内容转自百度百科：

> 全局解释器锁（Global Interpreter Lock）是计算机程序设计语言解释器用于同步线程的工具，使得在同一进程内任何时刻仅有一个线程在执行。常见例子有CPython（JPython不使用GIL）与Ruby MRI。
>
> **详情**
>
> - Python的线程是操作系统线程。在Linux上为pthread，在Windows上为Win thread，完全由操作系统调度线程的执行。一个python解释器进程内有一条主线程，以及多条用户程序的执行线程。即使在多核CPU平台上，由于GIL的存在，所以禁止多线程的并行执行。
> - Python解释器进程内的多线程是合作多任务方式执行。当一个线程遇到I/O任务时，将释放GIL。计算密集型（CPU-bound）的线程在执行大约100次解释器的计步（ticks）时，将释放GIL。计步（ticks）可粗略看作Python虚拟机的指令。计步实际上与时间片长度无关。可以通过sys.setcheckinterval()设置计步长度。
> - 在单核CPU上，数百次的间隔检查才会导致一次线程切换。在多核CPU上，存在严重的线程颠簸（thrashing）。
> - Python 3.2开始使用新的GIL。
> - 可以创建独立的进程来实现并行化。

# 第三章-单元测试-单元测试框架的介绍
对项目进行测试是软件开发的基本部分。本章中，我们将学习如何在Python中进行单元测试。Python中有一个称为unittest的模块，这就是一个单元测试框架。本章中我们将学习unittest这一框架。

本章中我们会学习如下课题：

- 单元测试框架的介绍
- 创建单元测试任务

## 什么是单元测试？

unittest是Python中的一个单元测试框架。它支持多任务，如测试夹具（test fixture）、编写测试用例、聚合测试用例进入一个测试套件，以及运行测试。

unittest支持以下4种主要概念：

- **测试夹具：**这包括执行一个或多个测试的准备和清理活动
- **测试用例：**这包括我们的单个测试。通过使用unittest中的TestCase基类，我们可以新建测试用例
- **测试套件：**这包含一个测试用例、测试套件或两者的合集。用于一起执行测试用例
- **测试运行器：**这包括安排测试执行和向用户给出输出

Python有一个我们可以在脚本中导入的unittest模块。unittest模块有TestCase类用于创建测试用例。

单个测试用例可以方法形式创建。这些方法名以单词 test 开头。因此，测试运行器可以知道哪些方法表示测试用例。

## 创建单元测试

在这一部分，我们来创建单元测试。我们要创建两个脚本来进行实现。一个是普通脚本，另一个是包含测试的代码。

首先，创建一个名为arithmetic.py的脚本并编写如下代码：

```python
# 在这个脚本中，我们将创建4个函数：add_numbers, sub_numbers, mul_numbers, div_numbers
 
def add_numbers(x, y):
        return x + y
 
def sub_numbers(x, y):
        return x - y
 
def mul_numbers(x, y):
        return x * y
 
def div_numbers(x, y):
        return (x / y)
```



在以上脚本中，我们创建了4个函数：add_numbers, sub_numbers, mul_numbers和div_numbers。下面我们将编写这些函数的测试用例。首先，我们将学习如何为add_numbers函数编写测试用例。创建test_addition.py脚本并编写如下代码：

```python
import arithmetic
import unittest
 
# Testing add_numbers function from arithmetic.
class Test_addition(unittest.TestCase):
        # Testing Integers
        def test_add_numbers_int(self):
                sum = arithmetic.add_numbers(50, 50)
                self.assertEqual(sum, 100)
        # Testing Floats
        def test_add_numbers_float(self):
                sum = arithmetic.add_numbers(50.55, 78)
                self.assertEqual(sum, 128.55)
        #Testing Strings
        def test_add_numbers_strings(self):
                sum = arithmetic.add_numbers('hello','python')
                self.assertEqual(sum, 'hellopython')
 
if __name__ == '__main__':
        unittest.main()
```

在以上脚本中，我们为add_numbers函数编写了三个测试用例。第一个是测试整型数字，第二个测试浮点数，第三个测试字符串。字符串的加法表示对字符串进行拼接。类似地，我们可以为减法、乘法和除法编写测试用例。

下面我们将运行test_addition.py测试脚本，在运行脚本后将可以看到运行的结果。

像下面这样运行脚本，可得到如下输出：

```bash
vagrant@python-scripting:~$ python3 test_addition.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
 
OK
```



这里我们得到的结果是OK，表示我们的测试是成功的。

不论何时运行测试脚本，我们可能得到的三种测试结果如下：

| 结果  | 描述                            |
| ----- | ------------------------------- |
| OK    | 成功                            |
| FAIL  | 测试失败-抛出AssertionError异常 |
| ERROR | 抛出AssertionError以外的异常    |

## 单元测试中使用的方法

使用unittest时，有一些方法可以在我们的脚本中使用。这些方法如下：

- assertEqual()和assertNotEqual()：检测预期结果
- assertTrue()和assertFalse()：验证条件
- assertRaises()：验证抛出指定的异常
- setUp()和tearDown()：定义每个测试方法执行之前和之后的指令

我们还可以在命令行中使用unittest模块。因此前述的测试脚本也可以这么运行：

```bash
vagrant@python-scripting:~$ python3 -m unittest test_addition.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s
 
OK
```

下面我们来看另一个示例。我们创建两个脚本：if_example.py和test_if.py。if_example.py 是我们的常规脚本，test_if.py将包含测试用例。在这个测试中，我们检查所输入的数字是否等于100.如果等于100，我们的测试将会成功。否则应显示一个FAILED的结果。

创建一个if_example.py脚本并加入如下代码：

```python
def check_if():
        a = int(input("Enter a number \n"))
        if(a == 100):
                print("a is equal to 100")
        else:
                print("a is not equal to 100")
        return a
```

现在来创建test_if.py测试脚本并编写如下代码：

```python
import if_example
import unittest
 
class Test_if(unittest.TestCase):
        def test_if(self):
                result = if_example.check_if()
                self.assertEqual(result, 100)
 
if __name__ == '__main__':
        unittest.main()
```

运行测试脚本如下：

```bash
vagrant@python-scripting:~/Chapter03$ python3 -m unittest test_if.py
Enter a number
100
a is equal to 100
.
----------------------------------------------------------------------
Ran 1 test in 0.984s
 
OK
```



我们运行脚本获得了一个成功的测试结果。下面我们输入一个100以外的值，会得到一个FAILED的结果。运行脚本如下：

```bash
vagrant@python-scripting:~/Chapter03$ python3 -m unittest test_if.py
Enter a number
50
a is not equal to 100
F
======================================================================
FAIL: test_if (test_if.Test_if)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/vagrant/Chapter03/test_if.py", line 7, in test_if
    self.assertEqual(result, 100)
AssertionError: 50 != 100
 
----------------------------------------------------------------------
Ran 1 test in 0.638s
 
FAILED (failures=1)
```



## 总结

本章中我们学习了unittest，它是Python中的单元测试框架。我们还学习了如何创建单元测试中使用的测试用例和方法。

在下一章中，我们将学习如何自动化系统管理员的常规管理活动。我们将学习接收输入、处理密码、执行外部命令、读取配置文件、向脚本添加警告代码、设置CPU限制、网页浏览器启动、使用os模块以及进行备份。

☞☞☞ [第四章 自动化常规运维活动](https://alanhou.org/automating-regular-administrative-activities/)

## 课后问题

1. 什么是单元测试、自动化测试和手动测试？

   点击查看

   

   单元测试一种软件测试，可对软件中的单个单元/组件进行测试。目的是验证软件的每个单元与执行效果与设计初衷一致。
   自动化测试是种自动化技术，测试人员自己编写脚本并使用相应的软件来进行测试。基本上是一种手动操作的自动化过程。
   手动测试是一种在软件程序中查找故障或 bug 的一种过程。在这种方法中，测试人员起到作为终端用户的重要作用，来验证应用功能是否正常运行。

2. unittest以外还有哪些替代模块？

   点击查看

   

   mock, nose, pytest.

3. 编写测试用例的用处是什么？

   点击查看

   

   测试用例是一组执行用于验证软件应用具体特性或功能的动作。本文中讲解了如何设计测试用例以及各个组件的重要性。

4. 什么是PEP8标准？

   点击查看

   

   PEP 8是Python的样式指南。有一组格式化Python代码的规则，来最大化改善代码可读性。按照规定编写代码有助于让众多代码编写人员编写大型项目。更为符合标准也可预测。

   

## 扩展阅读

- 单元测试文档：https://docs.python.org/3/library/unittest.html
- Python中的PEP8编码标准：https://www.python.org/dev/peps/pep-0008/

#  **[第四章 自动化常规运维活动](https://alanhou.org/automating-regular-administrative-activities/)** 

系统管理员有需要执行的各种各样管理活动。这些活动可能包含文件处理、日志、管理CPU和内存、密码处理以及最为重要的进行备份。需要自动化这些活动。本章中，我们将学习使用Python来自动化这些活动。

本章中，我们将讨论如下课题：

- 通过重定向、管道和输入文件来接收输入
- 脚本中运行时密码处理
- 执行外部命令并获取输出
- 在运行时和验证时弹出密码输入
- 读取配置文件
- 在脚本中添加日志和警告代码
- 为CPU和内存使用设置上限
- 启动网页浏览器
- 使用os模块处理目录和文件
- （使用 rsync）创建备份

## 通过重定向、管道和输入文件来接收输入

在这部分中，我们将学习如何让用户接收通过重定向、管道和外部输入文件的输入。

对于接收重定向的输入，我们使用stdin。管道是另一种形式的重定向。这个概念是指将一个程序的输出作为另一个程序的输入。我们可以通过外部文件以及使用Python来接收输入。

### 通过重定向输入

stdin和stdout是由os模块创建的对象。我们将编写一个脚本来使用到stdin和stdout。

创建一个名为redirection.py的脚本并编写如下代码：

```python
import sys

class Redirection(object):
	def __init__(self, in_obj, out_obj):
		self.input = in_obj
		self.output = out_obj
	def read_line(self):
		res = self.input.readline()
		self.output.write(res)
		return res

if __name__ == '__main__':
	if not sys.stdin.isatty():
		sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)
	a = input("Enter a string: ")
	b = input("Enter another string: ")
	print('Entered strings are:', repr(a), 'and', repr(b))

```

运行以上程序如下：

```bash
Enter a string: aaa
Enter another string: bbb
Entered strings are: 'aaa' and 'bbb'
```



我们将得到如下的输出：

程序在交互会话中运行时，stdin是键盘输入，stdout是用户的终端。input()函数用于从用户接收输入，print()是一种写到终端(stdout)的方式。

### 通过管道输入

管道（pipe）是另一种形式的重定向。 这一技术用于从一个程序向另一个程序传递信息。符号 | 表示管道。通过使用管道技术，我们可以使用两个以上的命令，将一个命令的输出作为下一个命令的输入。

下面我们来看看如何使用管道来接收输入。首先我们要写一个返回向下整除的简单脚本。创建一个名为accept_by_pipe.py的脚本并加入如下代码：

```python
import sys

for n in sys.stdin:
	print(int(n.strip())//2)

```

运行脚本，我们将得到如下输出：

```bash
echo 15|python3 accept_by_pipe.py 
7
```

在以上脚本中，stdin是一个键盘输入。我们执行对运行时中所输入的数字进行向下整除。向下整除仅返回商的整数部分。运行程序时，我们通过管道符号 | 传入了15，然后接我们的脚本名称。因此，我们将15作为脚本的输入。因此执行了向下整除，我们得到的结果是7。

我们可以向脚本传入多个输入。下面一个执行中，我们传入了多个输入值：15, 45和20。为处理多个输入值，我们在脚本中编写了一个 for 循环。因此首先将15作为输入，接着是45，然后是20。每个输入的输出会在新行中打印，因为我们在输入值之间加了\n。为开启对反斜线的解释，我们传入了-e 标记：

```bash
echo -e '15\n45\n20' | python3 accept_by_pipe.py 
7
22
10
```



进行这个运行后，我们分别得到了15, 45和20向下整除的结果7, 22和10，每个结果另起一行。

### 通过输入文件输入

在这一部分中，我们将学习如何从输入文件中接收输入。Python中接收输入文件来作为输入更为容易。我们将通过示例来进行查看。但首先要创建一个名为 sample.txt 的 简单文本文件，并写入如下代码：

```bash
 Hello WorldHello Python
```

下面创建一个名为accept_by_input_file.py的脚本并编写如下的代码：

```python
#!/bin/env python
from datetime import datetime
from genericpath import samefile
import os
if  os.path.exists("sample.txt"):
    print("sample file is exist")
else:
    os.system("touch sample_output.txt sample.txt")
i = open('sample.txt', 'r')
o = open('sample_output.txt', 'w')

a = i.read()
o.write(a)

```





运行程序，我们将得到如下输出：

```bash
python3 accept_by_input_file.py
sample file is exist
[liyupi@localhost Chapter04]$ cat sample_output.txt 
 Hello WorldHello Python[liyupi@localhost Chapter04]$ 
```







## 脚本中运行时密码处理

在这一部分中，我们来看看一个脚本中处理密码的简单示例。我们将创建一个名为handling_password.py的脚本并编写如下内容：

```python
import sys
import paramiko
import time

ip_address = "192.168.10.241"
username = "liyupi"
password = "liyupi"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address, username=username, password=password)
print("Successful connection", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd Desktop; mkdir work\n')
remote_connnection = ssh_client.exec_command('mkdir test_folder\n')
# print(remote_connection.read())
ssh_client.close

```



运行以上脚本，将得到如下输出：

```bash
python3 handling_password.py 
```

输出结果:

```bash
Successful connection 192.168.2.106
```

在上述脚本中，我们使用了paramiko模块。这个paramiko模块是一个ssh的Python实现，提供了客户端的功能。安装paramiko命令如下：

```bash
pip3 install paramiko
```



在前面的脚本中，我们远程连接了主机192.168.2.106。在脚本中提供了主机的用户名和密码。

在运行脚本之后，192.168.2.106的桌面上，可在192.168.2.106的home/目录内找到work和test_folder两个文件夹。

**译者注：**
1、IP、用户名、密码等相关信息请自行修改，包括 cd 进入的目录也请根据实际进行修改
2、解决运行中的警告

\# 警告信息

CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.

 \# 原因：

这在 GitHub 是一个已知 issue，主要原因是默认安装的cryptography==2.5弃用了一些 API

\# 解决方法

```bash
pip3 uninstall cryptography

pip3 install cryptography==2.4.2

 


```



## 执行外部命令并获取输出

在这一部分中，我们将学习Python的子进程模块。使用subprocess，可以很容易地生成新的进程并获取它们的返回码，执行外部命令和启用新的应用。

我们来看看如何通过subprocess模块执行外部命令并获取它们的输出。我们将创建一个名为execute_external_commands.py的脚本并编写如下脚本：

```python
import subprocess
subprocess.call(["touch", "sample.txt"])
subprocess.call(["ls"])
print("Sample file created")
subprocess.call(["rm", "sample.txt"])
subprocess.call(["ls"])
print("Sample file deleted")
```



运行程序，我们将得到如下输出：

```bash
$ python3 execute_external_commands.py
accept_by_input_file.py       handling_password.py  sample.txt
accept_by_pipe.py	      redirection.py
execute_external_commands.py  sample_output.txt
Sample file created
accept_by_input_file.py  execute_external_commands.py  redirection.py
accept_by_pipe.py	 handling_password.py	       sample_output.txt
Sample file deleted
```





## 使用子进程模块捕获输出

在这一部分中，我们将学习如何捕获输出。我们可以传递PIPE作为标准输出stdout的参数来捕获输出。。编写名为capture_output.py的脚本并添加如下代码：

```python

import subprocess
res = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE,)
print('returncode:', res.returncode)
print('{} bytes in stdout:\n{}'.format(len(res.stdout), res.stdout.decode('utf-8')))
```



执行如下命令运行脚本：

python3 capture_output.py

通过执行，将得到如下输出：

```bash
python3 capture_output.py
returncode: 0
1491 bytes in stdout:
total 92
```



**译者注：**考虑版面以及与原书一致，以上在运行时去除了代码中的-l 参数

在以上脚本中，我们导入了Python的subprocess模块，有助于输出的捕获。子进程模块用于创建新的进程。它还有且于连接输入/输出管道并获取返回码。subprocess.run()运行作为参数传入的命令。returncode 是子进程的返回状态。在输出中，如果得到了返回码0，表示成功运行。

## 在运行时和验证时弹出密码输入

这一部分我们将学习getpass模块来在运行时处理密码。Python中的getpass()模块弹出让用户输入密码并不进行打印。getpass模块用于终端中程序需要处理密码弹出的用户交互。

我们来看看一些有关如何使用getpass模块的示例：

1、创建名为no_prompt.py的脚本并编写如下代码：

```python


import getpass
try:
        p = getpass.getpass()
except Exception as error:
        print('ERROR', error)
else:
        print('Password entered:', p)
```



这个脚本中，我们没为用户提供提示文件。因此默认的提示内容为Password。



运行脚本如下：

```bash
python3 no_prompt.py 
Password: 
Password entered: aaa
```



2、我们将为密码输出添加提示文本。创建一个名为with_prompt.py的脚本并编写如下代码：

```python
import getpass
try:
	p = getpass.getpass("Enter your password:")
except Exception as error:
	print('ERROR', error)
else:
	print('Password entered:', p)

```



这样我们就编写了一个带有密码输入提示文本的脚本。运行程序如下：

```bash
python3 with_prompt.py 
Enter your password:
Password entered: abcd
```



这里，我们为用户提供了一个Enter your password 的提示。

现在我们来编写一个脚本，如果密码输入错误，将打印一条普通消息，并不再弹出输入正确密码的提示。

3、编写一个名为getpass_example.py的脚本并添加如下代码：

```python
import getpass
passwd = getpass.getpass(prompt='Enter your password:')
if passwd.lower() == '#pythonworld':
        print('Welcome!!')
else:
        print('The password entered is incorrect!!')
```



运行程序如下（此处我们输入正确的密码，即#pythonworld）：

.

```bash
python getpass_example.py
Enter your password:
The password entered is incorrect!!
```

如果我们输入一个错误的密码，查看得到的消息：

```bash
python getpass_example.py
Enter your password:
Welcome!!
```

这里我们编写的脚本在密码输入错误时不会再要求重新输入密码。

下面我们再来编写一个脚本，在密码输入错误时要求重新输入正确的密码。为获取登录用户，我们使用了getuser()。getuser()函数将返回系统登录的用户。创建一个名为password_prompt_again.py的脚本并编写如下代码：

```python
import getpass
user_name = getpass.getuser()
print('User Name : %s' % user_name)
while True:
        passwd = getpass.getpass('Enter your password : ')
        if passwd == '#pythonworld':
                print('Welcome!!!')
                break
        else:
                print('The password you entered is incorrect.')
```

运行程序，将得到如下输出：

```bash
$ python3 password_prompt_again.py
User Name : student
Enter your password :
The password you entered is incorrect.
Enter your password :
Welcome!!!
```



## 读取配置文件

这一部分中我们将学习Python中的configparser模块。通过使用configparser模块，我们可以管理应用的用户可编辑配置文件。

这些配置文件常用于用户或系统管理人员通过普通文本编辑器来编辑文件设置应用的一些默认值，然后应用会读取并解析文件，根据文件中写入的内容来进行运行。

读取配置文件可使用configparser中的read()方法。下面我们编写一个名为read_config_file.py的普通脚本。在这之前，编写一个名为read_simple.ini 的.ini文件并加入如下内容：

```ini
[bug_tracker]
url = https://www.baidu.com/
```



创建 read_config_file.py并添加如下内容：

```python
from configparser import ConfigParser
p = ConfigParser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))
```

运行read_config_file.py，我们将得到如下输出：

```bash
$ python3 read_config_file.py
 
# 输出结果：
https://www.baidu.com/
```



read()方法可接收一个以上的文件名。对每个文件名进行扫描并且该文件存在时，就会打开并读取。下面我们编写脚本来读取一个以上的文件名。创建名为read_many_config_file.py的脚本并编写如下代码：

```python
from configparser import ConfigParser
import glob
 
p = ConfigParser()
files = ['hello.ini', 'bye.ini', 'read_simple.ini', 'welcome.ini']
files_found = p.read(files)
files_missing = set(files) - set(files_found)
print('Files found: ', sorted(files_found))
print('Files missing: ', sorted(files_missing))
```



运行以上脚本，我们将得到如下输出：

```bash
$ python3 read_many_config_file.py
 
# 输出结果：
Files found:  ['read_simple.ini']
Files missing:  ['bye.ini', 'hello.ini', 'welcome.ini']
```



在上面的例子中，我们使用了Python中的configparser模块，它有助于管理配置文件。首先我们创建一个名为files的列表。read()函数将读取配置文件。在本例中，我们创建了一名为files_found的变量，用于存储目录中存在的配置文件名。接着我们创建了另一个名为files_missing的变量，用于返回目录中不存在的文件名。最后，我们打印出了存在和不存在的文件名。

## 在脚本中添加日志和警告代码

这一部分中我们学习Python中的日志和警告模块。logging模块将记录程序中发生的事件。warnings向编程人员发出语言和库中发生的变化的警告。

下面我们来看一个简单的日志示例。我们将编写一个名为logging_example.py的脚本并编写如下代码：

```python
import logging
 
LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)
logging.debug('This message should go to the log file.')
with open(LOG_FILENAME, 'rt') as f:
        prg = f.read()
print('FILE:')
print(prg)
```



运行程序如下：

```
$ python3 logging_example.py
 
# 输出结果：
FILE:
DEBUG:root:This message should go to the log file.
```



查看 log.txt，我们可以看到脚本中打印的调试信息：

```
$ cat log.txt
 
# 输出结果： 
DEBUG:root:This message should go to the log file.
```



下面我们编写一个名为logging_warnings_codes.py的脚本并添加如下代码：

```python
import logging
import warnings
 
logging.basicConfig(level=logging.INFO,)
warnings.warn('This warning is not sent to the logs')
logging.captureWarnings(True)
warnings.warn('This warning is sent to the logs')
```

运行脚本如下：

```
$ python3 logging_warnings_codes.py
 
# 输出结果：
logging_warnings_codes.py:5: UserWarning: This warning is not sent to the logs
  warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:logging_warnings_codes.py:7: UserWarning: This warning is sent to the logs
  warnings.warn('This warning is sent to the logs')
```





### 生成警告

warn()用于生成警告。下面我们来看一个生成警告的简单示例。编写名为generate_warnings.py的脚本并加入如下代码：

```
import warnings
 
warnings.simplefilter('error', UserWarning)
print('Before')
warnings.warn('Write your warning message here')
print('after')
```



运行脚本如下：

```
python3 generate_warnings.py
 
# 运行结果：
Before
Traceback (most recent call last):
  File "generate_warnings.py", line 5, in <module>
    warnings.warn('Write your warning message here')
UserWarning: Write your warning message here
```



在上面的脚本中，我们通过warn()传入了一条警告消息。我们使用了一个简单过滤器，这样我们的警告会作为 error 来处理，该错误将由编程人员进行相应的处理。

## 为CPU和内存使用设置上限

这部分中我们将学习如何设置 CPU和内存的使用限制。首先编写一个放置CPU使用限制的脚本。创建一个名为put_cpu_limit.py的脚本并添加如下代码：

```python
import resource
import sys
import signal
import time
 
def time_expired(n, stack):
        print('EXPIRED :', time.ctime())
        raise SystemExit('(time ran out)')
signal.signal(signal.SIGXCPU, time_expired)
# Adjust the CPU time limit
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit start as :', soft)
resource.setrlimit(resource.RLIMIT_CPU, (10, hard))
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit changed to :', soft)
print()
# Consume some CPU time in a pointless exercise
print('Starting:', time.ctime())
for i in range(200000):
        for i in range(200000):
                v = i * i
# We should never make it this far
print('Exiting :', time.ctime())
```



运行上述脚本如下：

```shell
$ python3 put_cpu_limit.py
Soft limit start as : -1
Soft limit changed to : 10
 
Starting: Sun Feb 24 23:57:27 2019
EXPIRED : Sun Feb 24 23:57:37 2019
(time ran out)
```



**译者注：**实际运行结果可能不是10秒，Alan 在本地一台资源有限的虚拟机上运行打印时间相关15秒，而 Mac 本机上则刚好10秒

在前面的脚本中，我们使用了setrlimit()来限制CPU的使用。在我们脚本中所设置的限制为10秒。

## 启动网页浏览器

这一部分中，我们将学习Python中的webbrowser模块。这一模块中带有可以在浏览器应用中打开URL的函数。我们来看一个简单的示例。创建一个名为open_web.py的脚本，并添加如下代码：

```
import webbrowser
webbrowser.open('https://www.baidu.com')
```



运行脚本如下：

```
$ python3 open_web.py
 
运行结果如下:
Url mentioned in open() will be opened in your browser.
webbrowser – Command line interface
```



**译者注：**实际在 MacOS 上测试未输出相关信息，命令行仅输出 True，虚拟机命令行进入，未安装浏览器，无返回内容

我们还可以通过命令行来使用Python的webbrowser模块，可以使用所有的功能。要在命令行中使用webbrowser，运行命令如下：

```
python3 -m webbrowser -n https://www.baidu.com/
```



这里，https://www.baidu.com/ 会在一个浏览窗口中进行打开。我们可以使用如下两个选项：

- -n：新窗口打开
- -t：新标签页打开

## 使用os模块处理目录和文件

这一部分中，我们将学习Python中的os模块。Python的os模块有助于实现操作系统任务。要想实现这些操作系统任务，我们需要导入os模块。

我们来看一些处理文件和目录相关示例：

### 创建和删除模块

这一部分中，我们将创建一个脚本来看可在文件系统中处理目录的函数，包含创建、列出和删除其中内容。创建一个名为os_dir_example.py的脚本并编写如下代码：

```python
import os
 
directory_name = 'abcd'
print('Creating', directory_name)
os.makedirs(directory_name)
file_name = os.path.join(directory_name, 'sample_example.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
        f.write('sample example file')
print('Cleaning up')
os.unlink(file_name)
os.rmdir(directory_name) # Will delete the directory
```



运行脚本如下：

```bash
$ python3 os_dir_example.py
 
# 输出结果：
Creating abcd
Creating abcd/sample_example.txt
Cleaning up
```



使用mkdir()创建目录时，其所有父目录必须已经被创建。但在使用makedirs()创建目录时，会创建任意目录，即便是指定的路径并不存在。unlink()会删除文件路径， rmdir()会删除目录路径。

### 检查文件系统内容

这一部分中，我们将使用 listdir()列出目录中的所有内容。创建一个名为list_dir.py的脚本并编写如下代码：

```python
import os
import sys
 
print(sorted(os.listdir(sys.argv[1])))
```

运行脚本如下：

```
$ python3 list_dir.py /home/student
 
# 输出结果：
['.bash_history', '.bash_logout', '.bashrc', '.cache', '.local', '.profile', '.python_history', '.ssh', '.viminfo', 'Chapter01', 'Chapter02', 'Chapter03', 'Chapter04', '__pycache__']
```



通过使用listdir()，我们可以列出文件夹中的所有内容。

## （使用 rsync）创建备份

这是系统运维人员要做的最重要的工作。这一部分中，我们将学习使用rsync来进行备份。rsync命令用于拷贝本地和远程的文件和目录，并使用rsync执行数据备份。为此，我们来编写一个名为take_backup.py的脚本并编写如下代码：

```python
import os
import shutil
import time
from sh import rsync
 
def check_dir(os_dir):
        if not os.path.exists(os_dir):
                print(os_dir, 'does not exist.')
                exit(1)
 
def ask_for_confirm():
        ans = input('Do you want to Continue? yes/no\n')
        global con_exit
        if ans == 'yes':
                con_exit = 0
                return con_exit
        elif ans == 'no':
                con_exit = 1
                return con_exit
        else:
                print('Answer with yes or no.')
                ask_for_confirm()
 
def delete_files(ending):
        for r, d, f in os.walk(backup_dir):
                for files in f:
                        if files.endswith('.' + ending):
                                os.remove(os.path.join(r, files))
 
backup_dir = input('Enter directory to backup\n') # Enter directory name
check_dir(backup_dir)
print(backup_dir, 'saved.')
time.sleep(3)
backup_to_dir = input('Where to backup?\n')
check_dir(backup_to_dir)
print('Doing the backup now!')
ask_for_confirm()
if con_exit == 1:
        print('Aborting the backup process!')
        exit(1)
rsync('-auhv', '--delete', '--exclude=list+found', '--exclude=/sys', '--exclude=/tmp', '--exclude=/proc', '--exclude=/mnt', '--exclude=/dev', '--exclude=/backup', backup_dir, backup_to_dir)
```

运行脚本结果如下：

```bash
$ python3 take_backup.py
Enter directory to backup
/home/student/work
/home/student/work saved.
Where to backup?
/home/student/Desktop
Doing the backup now!
Do you want to Continue? yes/no
yes
```

**译者注：**
1、如提示 ImportError: No module named ‘sh’请执行 pip3 install sh
2、Deskstop目录需自行创建

现在查看Desktop/目录，你会在该目录中发现 work 文件夹。rsync使用了一些选项，具体如下：

- -a: 存档
- -u: 升级
- -h: 易于阅读的格式
- -v: 详细信息（verbose）
- –delete: 在接收端删除不相关文件
- –exclude: 排队规则

## 总结

本章中我们学习了如何来自动化常规的运行任务。学习了通过不同技术来接收输入：运行时提示密码输入、执行外部命令、读取配置文件、在脚本中添加警告、通过脚本和命令行启动浏览器、使用os模块处理文件和目录，以及进行备份。

下一章中，我们将学习os和处理数据的相关知识。同时我们还会学习tarfile模块以及如何进行使用。

☞☞☞ [第五章 文件、目录和数据处理](https://alanhou.org/handling-files-directories-data/)

## 课后问题

1. 如何使用readline模块？

2. 读取、创建新文件、删除文件、列出当前目录文件的Linux命令分别是什么？

   cat、touch、rm、ls

3. Python 中的哪些包可用于运行 Linux/Windows 命令？

   os 

4. 如何读取或为配置文件 init 设置新值？

5. 列出可用于查看 CPU 使用情况的库？

6. 列出从用户接收输入的不同方法？

7. sort和sorted之间的区别是什么？

# 第五章 文件、目录和数据处理


   系统运维人员会执行一些如处理不同文件、目录和数据的任务。本章中，我们将学习os模块。os模块提供了与操作系统进行交互的功能。Python编程人员可轻易地使用os模块来执行文件和目录操作。os模块为程序员提供了处理文件、路径、目录和数据的工具。

   本章中我们将学习如下内容：

   - 使用os模块来处理目录
   - 复制、移动、重命名和删除数据
   - 处理路径、目录和文件
   - 对比数据
   - 合并数据
   - 模式匹配文件和目录
   - 元数据：数据的数据
   - 压缩和还原
   - 使用tarfile模块来创建TAR存档
   - 使用tarfile模块来检查TAR文件内容

   ## 使用os模块来处理目录

   目录或文件夹是一个文件和子目录的集合。os模块提供了允许我们与操作系统交互的不同函数。这一部分中，我们将学习可在处理目录时使用的一些函数。

   ### 获取工作目录

   要开始对目录进行处理，首先我们会获取当前工作目录的名称。os有一个getcwd()函数，使用它我们可以获取到当前的工作目录。启动python3终端并输入如下命令来获取当前目录名：

```python
$ python3
Python 3.5.2 (default, Nov 12 2018, 13:43:14)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/home/student/Chapter05'
>>>
```

   

   ### 更换目录

   使用os模块，我们可以更换当前工作目录。os模块中有一个chdir()函数可用于实现，示例如下：

```python
>>> os.chdir('/home/student')
>>> print(os.getcwd())
/home/student
>>>
```



   

   ### 列出文件和目录

   列出目录内容在Python中也很容易。我们将使用os中带有的listdir()函数，它会返回当前工作目录的文件和目录名：

```python
>>> os.chdir('/home/student')
>>> os.listdir()
['Chapter05', 'Chapter03', '.python_history', '__pycache__', 'Chapter01', 'Desktop', 'Chapter04', 'Chapter02', '.cache', '.local', '.ssh', '.bash_history', '.bash_lo
```



   

   ### 重命名目录

   Python中的os模块有一个rename()函数，可帮助更换目录的名称：

```python
>>> os.mkdir('work')
>>> os.rename('work', 'work1')
>>> os.listdir()
['Chapter05', 'Chapter03', '.python_history', '__pycache__', 'Chapter01', 'Desktop', 'Chapter04', 'Chapter02', '.cache', 'work1', '.local', '.ssh', '.bash_history', '.bash_logout', '.bashrc', '.viminfo', '.profile']
```

   

   ## 复制、移动、重命名和删除数据

   我们将学习系统运维人员处理数据的四个基本操作，即复制、移动、重命名和删除。Python内置一个名为shutil的模块，用于执行这些任务。使用shutil模块，我们也可以对数据执行更高级别的操作。在我们的程序中使用shutil模块，只需要编写import shutil导入语句即可。shutil模块提供了一些支持文件复制和删除操作的函数。我们来逐一学习这些操作。

   ### 复制数据

   这一部分中，我们将来看如何使用shutil模块来复制文件。首先，我们会创建一个hello.py文件并在其它编写一些文本内容。

```python
# hello.py
print("")
print("Hello World\n")
print("Hello Python\n")
```



   现在我们会在shutil_copy_example.py脚本中编写复制的代码。在其中编写如下内容：

```python
import shutil
import os
 
shutil.copy('hello.py', 'welcome.py')
print('Copy Successful')
```



   运行脚本如下：

```bash
$ python shutil_copy_example.py
 
# 输出结果
Copy Successful
```



   查看welcome.py脚本，我们会发现welcome.py中已成功地拷贝了hello.py中的内容。

   ### 移动/剪切数据

   这里我们来看如何剪切数据。实现剪切我们可以使用shutil.move()。shutil.move(source, destination可以将文件从源地址移动到目的地址。下面我们来创建一个shutil_move_example.py脚本并编写如下内容：

```python
import shutil
shutil.move('/home/student/sample.txt', '/home/student/Desktop/.')
```



   运行脚本如下：

```
	
$ python3 shutil_move_example.py
```

   这一脚本中，我们剪切的文件为sample.txt，在/home/student 目录中。/home/student是我们的源文件夹/home/student/Desktop是我们目的文件夹。因此，在运行脚本后，sample.txt会从/home/student剪切到/home/student/Desktop目录中。

   ### 重命名数据

   在前面的部分中，我们学习了如何使用shutil.move()来将文件由源目录移动到目标目录。使用shutil.move()可对文件进行重命名。创建一个shutil_rename_example.py脚本并添加如下内容：

```python
import shutil
shutil.move('hello.py', 'hello_renamed.py')
```



   运行脚本如下：

```bash
$ python3 shutil_rename_example.py
 
# 无输出
```



   现在查看文件名，会被重命名为hello_renamed.py。

   ### 删除数据

   我们将学习如何使用Python中的os模块删除文件和文件夹。os模块中的remove()方法将删除文件。如果尝试使用该方法删除目录将会返回OSError。要删除目录，使用rmdir()。

   下面创建一个os_remove_file_directory.py脚本并编写如下内容：

```python
import os
 
os.chdir('/home/student') # 补充代码?
os.remove('sample.txt')
print("File removed successfully")
os.rmdir('work1')
print("Directory removed successfully")
```



   运行脚本如下：

```bash
$ python3 os_remove_file_directory.py
 
# 输出结果：
File removed successfully
Directory removed successfully
```



   

   ## 处理路径

   下面我们将学习os.path()。它用于路径处理。这一部分中，我们来看os模块中针对路径名的函数。

   **补充：**Alan 对 Python 进行了一下升级，方法如下：

```bash
sudo apt-get update
sudo wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar zxvf Python-3.7.2.tgz
cd Python-3.7.2/
./configure
make && sudo make install
```



   启动python3终端：

```
$ python3
Python 3.7.2 (default, Feb 26 2019, 15:56:02)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>>
```

   

   - os.path.absname(path): 返回路径名的绝对路径

   

```python
>>> os.path.abspath('sample.txt')
'/home/student/work/sample.txt'
>>>
```

   

   - os.path.dirname(path): 返回路径的目录名

     ```python
     >>> os.path.dirname('/home/student/work/sample.txt')
     '/home/student/work'
     ```

     

   

   

   - os.path.basename(path): 返回路径的基本名称

   

```python
>>> os.path.basename('/home/student/work/sample.txt')
'sample.txt'
```



   

   - os.path.exists(path): 如果引用的路径存在则返回 True

   

```python
>>> os.path.exists('/home/student/work/sample.txt')
True
```



   

   - os.path.getsize(path): 以字节数返回输入文件的大小

   

```python
>>> os.path.getsize('/home/student/work/sample.txt')
39
```



   

   - os.path.isfile(path): 检查输入的路径是否为已有文件。如果是文件则返回True。

   

```python
>>> os.path.isfile('/home/student/work/sample.txt')
True
```



   

   - os.path.isdir(path): 检查输入的路径是否为已有目录。如果是目录则返回True。

   

```python
 >>> os.path.isdir('/home/student/work/sample.txt')
    False
```



   

   ## 对比数据

   下面我们将学习如何在Python中比较数据。我们使用pandas模块来进行实现。

   pandas是一个开源的数据分析库，提供易于使用的数据结构和数据分析工具。让我们导入和分析数据更为简单。

   在开始示例之前，确保系统中安装了pandas。安装pandas的方法如下：

```bash
pip3 install pandas # Python3
或
pip install pandas #python2
```



   我们将学习一个使用pandas比较数据的示例。首先，我们来创建两个csv文件：student1.csv和student2.csv。我们将比较这两个csv文件并在结果中返回比较结果。创建以下两个csv文件：

   创建student1.csv文件内容如下：

```
Id,Name,Gender,Age,Address
101,John,Male,20,New York
102,Mary,Female,18,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,22,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
```



   创建student2.csv文件内容如下：

```
Id,Name,Gender,Age,Address
101,John,Male,21,New York
102,Mary,Female,20,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,23,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
```

   下面我们创建compare_data.py脚本并编写如下内容：

```python
import pandas as pd
 
df1 = pd.read_csv('student1.csv')
df2 = pd.read_csv('student2.csv')
s1 = set([tuple(values) for values in df1.values.tolist()])
s2 = set([tuple(values) for values in df2.values.tolist()])
s1.symmetric_difference(s2)
print(pd.DataFrame(list(s1.difference(s2))), '\n')
print(pd.DataFrame(list(s2.difference(s1))), '\n')
```

   运行脚本如下：

```bash
$ python3 compare_data.py
 
# 输出结果：
     0     1       2   3         4
0  104   Leo    Male  22   Chicago
1  101  John    Male  20  New York
2  102  Mary  Female  18    London
 
     0     1       2   3         4
0  102  Mary  Female  20    London
1  104   Leo    Male  23   Chicago
2  101  John    Male  21  New York
```



   在上述的例子中，我们比较两个csv文件的数据：student1.csv和student2.csv。我们首先转化我们的数据帧(df1, df2)为集合 (s1, s2)。然后我们使用了symmetric_difference() 集合。因此它会检查s1和s2的对称性区别，然后我们打印出了结果。

   ## 合并数据

   我们将学习如何在Python合并数据。为此，我们使用Python中的pandas库。要进行数据合并，我们将使用前一部分中使用的两个csv文件：student1.csv和student2.csv。

   下面，创建merge_data.py脚本并编写如下代码：

```python
import pandas as pd
 
df1 = pd.read_csv('student1.csv')
df2 = pd.read_csv('student2.csv')
result = pd.concat([df1, df2])
print(result)
```



   运行脚本如下：

```bash
$ python3 merge_data.py
 
# 输出结果：
    Id    Name  Gender  Age   Address
0  101    John    Male   20  New York
1  102    Mary  Female   18    London
2  103  Aditya    Male   22    Mumbai
3  104     Leo    Male   22   Chicago
4  105     Sam    Male   21     Paris
5  106    Tina  Female   23    Sydney
0  101    John    Male   21  New York
1  102    Mary  Female   20    London
2  103  Aditya    Male   22    Mumbai
3  104     Leo    Male   23   Chicago
4  105     Sam    Male   21     Paris
5  106    Tina  Female   23    Sydney
```



   

   ## 模式匹配文件和目录

   这部分中我们将学习文件和目录的模式匹配。Python有一个glob模块，用于查找与指定模式相匹配的文件和目录名称。

   下面我们来看一个示例。首先，创建一个pattern_match.py脚本并编写如下内容：

```python
import glob
 
file_match = glob.glob('*.txt')
print(file_match)
file_match = glob.glob('[0-9].txt')
print(file_match)
file_match = glob.glob('**/*.txt', recursive=True)
print(file_match)
file_match = glob.glob('**/', recursive=True)
print(file_match)
```



   运行脚本如下：

```bash
$ python3 pattern_match.py
 
# 输出结果
['file1.txt', 'filea.txt', 'fileb.txt', 'file2.txt', '2.txt', '1.txt', 'file.txt']
['2.txt', '1.txt']
['file1.txt', 'filea.txt', 'fileb.txt', 'file2.txt', '2.txt', '1.txt', 'file.txt', 'dir1/3.txt', 'dir1/4.txt']
['dir1/']
```

   **注：**以上目录及文件需自行创建

   在前面的示例中，我们使用了Python模块来进行模式匹配。glob (pathname)将返回匹配pathname的名称列表。在我们的脚本中，我们传入了四个不同的glob()函数。第一个glob()中，我们传入的路径名为*.txt，这将返回所有后缀名为.txt文件名。在第二个glob()中，我们传入了 [0-9].txt，这将返回以数字开始的名称。在第三个glob()中，我们传入了**/*.txt，将返回文件名和路径名。它还会返回这些目录的文件名。在第四个glob()中，我们传入了**/，将仅返回目录名。

   ## 元数据：数据的数据

   这部分我们将学习PyPDF2模块，有助于我们从pdf文件中提取元数据（metadata）。但首先什么是元数据呢？元数据是数据的数据。元数据是描述主要信息的结构性信息。它是一个数据的总结。包含我们实际数据相关的基本信息。帮助查找我们数据中的具体实例。

   > ℹ️确保将需提取信息的pdf文件放在相应目录中

   首先安装PyPDF2模块，命令如下：

```bash
pip3 install PyPDF2
```



   下面我们来编写脚本metadata_example.py，并查看如何获取元数据信息。我们使用Python来编写脚本：

```python
import PyPDF2
 
def main():
        file_name = 'Haltermanpythonbook.pdf'
        pdfFile = PyPDF2.PdfFileReader(open(file_name, 'rb'))
        pdf_data = pdfFile.getDocumentInfo()
        print('----Metadata of the file----')
        for md in pdf_data:
                print(md+ ':' +pdf_data[md])
 
if __name__ == '__main__':
        main()
```



   **译者注：
   **1、随机搜索了一本Python 方面的 pdf 图书[Haltermanpythonbook.pdf](https://www.cs.uky.edu/~keen/115/Haltermanpythonbook.pdf)用于本例测试
   2、原书使用了 Python 2中的pyPdf，为统一版本，Alan 修改为针对 Python 3的PyPDF2

   运行脚本如下：

```bash
$ python3 metadata_example.py
----Metadata of the file----
/Author:
/Title:
/Subject:
/Creator:LaTeX with hyperref package
/Producer:pdfeTeX-1.21a
/Keywords:
/CreationDate:D:20111113221308-05'00'
/PTEX.Fullbanner:This is pdfeTeX, Version 3.141592-1.21a-2.2 (Web2C 7.5.4) kpathsea version 3.5.4
```



   在前述脚本中，我们使用了 Pyhon 3中的PyPDF2模块。首先，我们创建了一个变量file_name来存储 pdf 的路径。使用PdfFileReader() 来提取数据。变量pdf_data会存储pdf的相关信息。最后，我们编写for循环来获取元数据信息。

   ## 压缩和还原

   这部分中我们将学习shutil模块中的make_archive()函数，可压缩整个文件夹。为此我们编写一个compress_a_directory.py脚本并编写如下内容：

```python
import shutil
shutil.make_archive('work', 'zip', 'work/')
```



   运行脚本如下：

```bash
$ python3 compress_a_directory.py
```



   前述脚本shutil.make_archive()函数中，我们传入的第一个参数作为压缩文件的名称，zip是压缩的技术。work/是想要进行压缩的目录名。

   要对压缩文件进行还原（解压缩），我们使用shutil模块中的unpack_archive() 函数。创建一个脚本unzip_a_directory.py并编写如下内容：

```python
import shutil
shutil.unpack_archive('work1.zip')
```



   运行脚本如下：

```bash
$ python3 unzip_a_directory.py
```

   现在检查我们的目录。可以得到解压目录后的所有内容。

   ## 使用tarfile模块来创建TAR存档

   这部分帮助我们学习如何使用Python的tarfile模块来创建tar存档文件。

   tarfile模块用于使用gzip、bz2等压缩技术来读取和写入tar存档文件。确保存在相关的文件和目录。下面创建一个tarfile_example.py脚本并编写如下内容：

```python
import tarfile
 
tar_file = tarfile.open('work.tar.gz', 'w:gz')
for name in ['welcome.py', 'hello.py', 'hello.txt', 'sample.txt', 'sample1.txt']:
        tar_file.add(name)
tar_file.close()
```



   运行脚本如下：

```bash
$ python3 tarfile_example.py
```



   这时检查当前工作目录，可以看到已创建了work.tar.gz。

   ## 使用tarfile模块来检查TAR文件内容

   这部分中我们将学习如何在不提取tar文件的情况下检查tar包里的内容。我们使用Python中的tarfile模块。

   创建脚本examine_tar_file_content.py编写如下内容：

```python
import tarfile
tar_file = tarfile.open('work.tar.gz', 'r:gz')
print(tar_file.getnames())
```



   运行脚本如下：

```bash
$ python3 examine_tar_file_content.py
 
# 输出结果：
['welcome.py', 'hello.py', 'hello.txt', 'sample.txt', 'sample1.txt']
```

   在前面的例子中，我们使用了tarfile模块来查看所创建的tar文件的内容。我们使用了getnames()函数来读取数据。

   ## 总结

   本章中我们学习了如何使用Python脚本来处理文件和目录。还学习了如何使用os模块来处理目录。以及如何拷贝、移动、重命名和删除文件和目录。我们学习了Python中的pandas模块，用于比较和合并数据。同时学习了使用tarfile模块来创建tar文件以及读取tar文件中的内容。我们在搜索文件和目录时还使用了模式匹配。

   下一章中，我们将学习tar包和ZIP的创建。

   ☞☞☞ [第六章 文件存档、加密和解密](https://alanhou.org/file-archiving-encrypting-decrypting/)

   ## 课后问题

   1. 如何在不论什么操作系统中（Windows, Linux）处理不同的路径？
   2. Python 中print()可以使用哪些不同参数？
   3. Python 中dir()关键字的用处是什么？
   4. pandas中的数据帧、序列是什么？
   5. 列表推导式是什么？
   6. 是否可以进行集合推导式和字典推导式？如果是如何做？
   7. 如何使用pandas数据帧打印最前/后的 N 行？
   8. 使用列表推导式来编写程序打印奇数？
   9. sys.argv的类型时什么？
      a) 集合
      b) 列表
      c) 元组
      d) 字符串

   ## 扩展阅读

   - pathlib文档: https://docs.python.org/3/library/pathlib.html
   - pandas文档: https://pandas.pydata.org/pandas-docs/stable/
   - os模块文档: https://docs.python.org/3/library/os.html



# [第六章 文件存档、加密和解密](https://alanhou.org/file-archiving-encrypting-decrypting/)



前一章中我们学习了如何处理文件、目录和数据。我们还学习了tarfile模块。本章中，我们将学习文件的存档、加密和解密。存档在管理文件、目录和数据中扮演重要的角色。但首先什么是存档呢？存档是一个将多个文件和目录存放到一个文件中的过程。Python中有tarfile模块可用于创建这类存档文件。

本章中，我们将学习如下课题：

- 创建和解压存档包
- Tar包
- ZIP的创建
- 文件加密和解密

## 创建和解压存档包

这一部分中，我们将学习如何使用Python中的shutil模块来创建和解压存档包。shutil模块带有make_archive()函数，可以创建一个新的存档文件。使用make_archive()，我们可以对包含的内容的整个目录进行打包。

### 创建存档包

下面我们来编写一个名为shutil_make_archive.py的脚本并加入如下内容：

```python
import tarfile, shutil, sys
 
shutil.make_archive(
        'work_sample', 'gztar',
        root_dir='..',
        base_dir='work'
)
print('Archive contents:')
with tarfile.open('work_sample.tar.gz', 'r') as t_file:
        for names in t_file.getnames():
                print(names)
```



运行程序，将得到如下输出：

```bash
$ python3 shutil_make_archive.py
Archive contents:
work
work/sample.txt
```



| 1234 | $ python3 shutil_make_archive.pyArchive contents:workwork/sample.txt |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

上例中，我们使用了Python中的shutil和tarfile模块来创建存档文件。在shutil.make_archive()中，我们指定了work_sample来作为存档文件的名称并使用 gz 格式。我们还通过基本目录属性指定了工作目录。最后，我们打印出了存档中的文件名称。

### 解压存档包

要解压存档包，可使用shutil中带有的unpack_archive()函数。使用该函数，我们可以提取存档的文件。我们传递存档包名以及想要提取内容的目录名。如果未传递目录名，就会将提取的内容放到当前工作目录中。

下面创建一个名为shutil_unpack_archive.py的脚本并编写如下代码：

```python
import pathlib, shutil, sys, tempfile
 
with tempfile.TemporaryDirectory() as d:
        shutil.unpack_archive('work_sample.tar.gz',
                extract_dir='/home/student/work')
        prefix_len = len(d) + 1
        for extracted in pathlib.Path(d).rglob('*'):
                print(str(extracted)[prefix_len:])
```

运行脚本如下：

```bash
 python3 shutil_unpack_archive.py
```



下面检查work/目录，会在其中发现work/文件夹，并包含提取的文件。

## Tar包

这一部分我们将学习tarfile模块。我们还将学习输入文件名的测试，评估它是否是有效的存档文件名。我们会看如何将一个新文件加入到已有的存档文件中，如何使用tarfile模块读取元数据，以及如何使用extractall() 函数来从存档中提取文件。

首先，我们将测试输入的文件名是否是有效的存档文件。进行这一测试，tarfile模块带有is_tarfile()函数，返回的是布尔值。

创建一个名为check_archive_file.py的脚本并编写如下内容：

```python
import tarfile
 
for f_name in ['hello.py', 'work.tar.gz', 'welcome.py', 'nofile.tar', 'sample.tar.xz']:
        try:
                print('{:} {}'.format(f_name, tarfile.is_tarfile(f_name)))
        except IOError as err:
                print('{:} {}'.format(f_name, err))
```

运行脚本，将得到如下输出：

```bash
$ python3 check_archive_file.py
hello.py False
work.tar.gz True
welcome.py False
nofile.tar [Errno 2] No such file or directory: 'nofile.tar'
sample.tar.xz False
```

因此，tarfile.is_tarfile()会检查列表出的各个文件名。hello.py, welcome.py文件不是tar包，所以得到的是布尔值False，work.tar.gz和sample.tar.xz是tar包，因此得到了布尔值True。并且目录中不存在nofile.tar这一文件，所以抛出了脚本中所编写的异常。

下面我们将向已创建的存档文件中添加一个新文件。创建名为add_to_archive.py的脚本并编写如下代码：

```python
import shutil, os, tarfile
 
print('creating archive')
shutil.make_archive('work', 'tar', root_dir='..', base_dir='work',)
print('\nArchive contents:')
with tarfile.open('work.tar', 'r') as t_file:
        for names in t_file.getnames():
                print(names)
        os.system('touch sample.txt')
        print('adding sample.txt')
        with tarfile.open('work.tar', mode='a') as t:
                t.add('sample.txt')
        print('contents:',)
        with tarfile.open('work.tar', mode='r') as t:
                print([m.name for m in t.getmembers()])
```

运行脚本，我们将得到如下输出：

```bash
$ python3 add_to_archive.py
 
# 输出结果：
creating archive
 
Archive contents:
work
work/work
work/work/sample.txt
adding sample.txt
contents:
['work', 'work/work', 'work/work/sample.txt', 'sample.txt']
```

本例中，首先我们使用shutil.make_archive()创建了一个压缩文件，然后我们打印出了存档文件中的内容。再后我们在下一条语句中创建了一个sample.txt文件。接着我们希望将sample.txt加到已创建的work.tar中。这里我们使用了追加模式。接下来我们再次读取了存档文件中的内容。

下面我们将学习如何读取存档文件的元数据。getmembers() 会加载文件的元数据。创建一个名为read_metadata.py的脚本并编写如下内容：

```python
import tarfile, time
 
with tarfile.open('work.tar', 'r') as t:
        for file_info in t.getmembers():
                print(file_info.name)
                print('Size :', file_info.size, 'bytes')
                print('Type :', file_info.type)
                print()
```

运行脚本，将会得到如下输出：

```bash
$ python3 read_metadata.py
work
Size : 0 bytes
Type : b'5'
 
work/work
Size : 0 bytes
Type : b'5'
 
work/work/sample.txt
Size : 0 bytes
Type : b'0'
 
sample.txt
Size : 0 bytes
Type : b'0'
```

下面我们将使用 extractall() 函数来从存档包中提取内容。为此，创建一个名为extract_contents.py的脚本并在其中编写如下代码：

```python
import tarfile, os
 
os.mkdir('work')
with tarfile.open('work.tar', 'r') as t:
        t.extractall('work')
print(os.listdir('work'))
```

运行脚本，将得到如下输出：

```bash
$ python3 extract_contents.py
 
# 输出结果：
['sample.txt', 'work']
```

查看当前工作目录，我们会看到work/ 目录，进入该目录就可以看到提取的文件。

## ZIP的创建

这部分中，我们将使用ZIP文件。我们将学习Python中的zipfile模块，如何创建ZIP文件，如何测试输入的文件名是否是有效的ZIP文件名，读取元数据等等。

首先我们将学习如何使用shutil模块的make_archive()函数创建zip文件。创建一个名为make_zip_file.py的脚本并编写如下代码：

```python
import shutil
shutil.make_archive('work', 'zip', 'work')
```

运行脚本如下：

```
python3 make_zip_file.py
```

此时查看当前工作目录，就会发现work.zip文件。

接下来我们将测试所输入的zip文件名是否有效。为此可使用zipfile模块中的is_zipfile()函数。

创建一个脚本check_zip_file.py并编写如下内容：

```python
import zipfile
 
for f_name in ['hello.py', 'work.zip', 'welcome.py', 'sample.txt', 'test.zip']:
        try:
                print('{:}        {}'.format(f_name, zipfile.is_zipfile(f_name)))
        except IOError as err:
                print('{:}        {}'.format(f_name, err))
```

运行脚本如下：

```bash
$ python3 check_zip_file.py
 
# 输出结果：
hello.py        False
work.zip        True
welcome.py        False
sample.txt        False
test.zip        False
```

在本例中，我们使用了for循环来检查列表中的文件名。is_zipfile()函数会逐一检查文件名并在结果中返回布尔值。

下面我们将来看如何使用Python中的zipfile模块来读取存档的ZIP文件的元数据。创建一个名为read_zip_metadata.py的脚本，并编写如下内容：

```python
import zipfile
 
def meta_info(names):
        with zipfile.ZipFile(names) as zf:
                for info in zf.infolist():
                        print(info.filename)
                        if info.create_system == 0:
                                system = 'Windows'
                        elif info.create_system == 3:
                                system = 'Unix'
                        else:
                                system = 'UNKNOWN'
                        print('System      :', system)
                        print('Zip Version :', info.create_version)
                        print('Compressed  :', info.compress_size, 'bytes')
                        print('Uncompressed:', info.file_size, 'bytes')
                        print()
 
if __name__ == "__main__":
        meta_info('work.zip')
```

执行脚本如下：

```bash
$ python3 read_zip_metadata.py
make_zip_file.py
System      : Unix
Zip Version : 20
Compressed  : 49 bytes
Uncompressed: 57 bytes
 
sample.txt
System      : Unix
Zip Version : 20
Compressed  : 2 bytes
Uncompressed: 0 bytes
 
add_to_archive.py
System      : Unix
Zip Version : 20
Compressed  : 240 bytes
Uncompressed: 483 bytes
 
shutil_unpack_archive.py
System      : Unix
Zip Version : 20
Compressed  : 196 bytes
Uncompressed: 269 bytes
```



要获取zip文件的元数据信息，我们使用了ZipFile类的infolist()方法。

## 文件加密和解密

这一部分中我们将学习Python中的pyAesCrypt模块。pyAesCrypt是一个文件加密模块，使用AES256-CBC算法来对文件和二进制流文件加密和解密。

安装pyAesCrypt命令如下：

```bash
pip3 install pyAesCrypt
```



创建名为file_encrypt.py的脚本并编写如下代码：

```python
import pyAesCrypt
 
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = '#Training'
with open('sample.txt', 'rb') as fIn:
        with open('sample.txt.aes', 'wb') as fOut:
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
# get encrypted file size
encFileSize = stat('sample.txt.aes').st_size
```

运行脚本如下：

```bash
$ python3 file_encrypt.py
 
# 无输入内容
```

请查看当前工作目录，我们会发现其中有一个sample.txt.aes文件。

本例中，我们首先的提及了缓冲大小和密码。然后涉及了需要加密的文件名。在encryptStream中，我们传入了加密的文件fIn，以及加密后的文件名fOut。我们将加密后的文件存储为sample.txt.aes。

下面我们将对sample.txt.aes文件进行解密来获取文件的内容。创建一个名为file_decrypt.py 的脚本并编写如下内容：

```python
import pyAesCrypt
from os import stat, remove
 
bufferSize = 64 * 1024
password = '#Training'
encFileSize = stat('sample.txt.aes').st_size
with open('sample.txt.aes', 'rb') as fIn:
        with open('sampleout.txt', 'wb') as fOut:
                try:
                        pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                except ValueError:
                        remove('sampleout.txt')
```

运行脚本如下：

```bash
$ python3 file_decrypt.py
```

现在查看当前工作目录。一个名为sampleout.txt的文件会被创建。这就是我们的解密后文件。

本例中，我们涉及到了解密的文件名sample.txt.aes。然后，我们解密后的文件为sampleout.txt。在decryptStream中，涉及到了要解密的文件fIn，以及解密后文件的名称fOut。

## 总结

本章中，我们学习了创建和提取存档文件。在管理文件、目录和数据时存档扮演着重要的角色。它还将许多文件和目录存入一个文件中。

我们深入学习了Python模块tarfile和zipfile，来让我们创建、提取和测试存档文件。我们可以将新文件添加到已有存档文件中、读取元数据、从存档中提取文件。我们还学习了使用pyAescrypt模块来进行文件加密和解密。

下一章中我们将学习Python 中的文本处理和正则表达式。Python有一称作正则表达式的非常强大的库，可以完成搜索和提取数据等任务。

## 课后问题

1. 我们是否可以用加密的方式压缩数据？如果可以，如何进行？
2. Python中的上下文管理器是什么？
3. 什么是pickling和unpickling？
4. Python中不函数类型有哪些？

## 扩展阅读

- 数据压缩和存档: https://docs.python.org/3/library/archiving.html
- tempfile文档: https://docs.python.org/2/library/tempfile.html
- Python加密文档: https://docs.python.org/3/library/crypto.html
- shutil文档: https://docs.python.org/3/library/shutil.html

## with open as f

```
r:	以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+: 打开一个文件用于读写。文件指针将会放在文件的开头。
rb+:以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w:	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb:	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+:	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+:以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a:	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab:	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+:	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+:以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

```



# [第七章 文本处理和正则表达式](https://alanhou.org/text-processing-regular-expressions/)



本章中我们将学习文本处理和正则表达式。文本处理是一个创建和修改文本的过程。Python有一个称为正则表达式的强大的库，可处理搜索和提取数据等任务。我们将学习如何对文件使用它，同时学习如何读取和写入文件。

我们将学习Python的正则表达式模块re，以及在Python中处理文件。同时学习re模块中的match(), search(), findall()和sub()函数。我们还将使用textwrap来学习Python中的文本封装。最后，我们会学习unicode字符。

本章中我们会学习如何课题：

- 文本封装
- 正则表达式
- Unicode字符串

## 文本封装

本章中我们将学习Python的textwrap模块。该模块提供了TextWrapper来完成所有任务。textwrap模块用于格式化或封装普通文本。该模块提供了5个主要的函数：wrap(), fill(), dedent(), indent()和shorten()。下面我们将逐一来学习这些函数。

### wrap()函数

wrap()函数用于将整个段落封装为单个字符串。输出结果是一个输出行列表。

语法为textwrap.wrap(text, width)：

- text: 要封装的文本
- width: 封装行允许的最大长度，默认值为70

下面我们来看一个wrap()的示例。创建一个脚本wrap_example.py并编写如下内容：

```python
import textwrap
 
sample_string = '''Python is an interpreted high-level programming
language.'''
 
w = textwrap.fill(text=sample_string, width=50)
print(w)
```

运行脚本，将会得到如下输出：

```bash
python3 wrap_example.py 
['Python is an interpreted high-', 'level programming language for', 'general-purpose programming.', 'Created by Guido van Rossum', 'and first released in 1991,', 'Python has a design philosophy', 'that emphasizes code', 'readability, notably using', 'significant whitespace.']
```

上例中我们使用了Python中的textwrap模块。首先我们创建一个名为sample_string的字符串。接着我们使用TextWrapper类指定了width。再后使用了wrap函数，字符串被封装长度30。最后我们打印出了各行。

### fill()函数

fill()函数与textwrap.wrap的作用相似，只是它返回的数据是连接的、以新行分隔的字符串。该函数将输入封装为文本并返回包含封装文本的单个字符串。

该函数的语法为：textwrap.fill(text, width)

- text：封装的文本
- width：封装的一行允许的最大长度。默认值为70。

下面我们来看一个fill()的示例。创建一个fill_example.py脚本并编写如下内容：

```python
import textwrap

sample_string = '''Python is an interpreted high-level programming
language.'''

w = textwrap.fill(text=sample_string, width=50)
print(w)

```

运行脚本，我们将得到如下输出;

```bash
python3 fill_example.py
Python is an interpreted high-level programming
language.
```

上例中我们使用了fill()函数。整个过程和我们在wrap()中的操作相同。首先，我们创建了一个字符串变量。接着我们创建了一个textwrap对象。然后，我们应用了fill()函数。最后，我们打印了输出。

### dedent()函数

dedent()是textwrap模块中的另一个函数。该函数将我们文本每一行的普通前置空格进行移除。

该函数的语法如下：

textwrap.dedent(text)

其中text为取消缩进的文本。

下面我们来看一个dedent()的示例。创建一个脚本dedent_example.py并编写如下内容：

```python
import textwrap
 
str1 = '''
        Hello Python World \tThis is Python 101
        Scripting language\n
        Python is an interpreted high-level programming language for general-purpose programming.
'''
print("Original: \n", str1)
print()
 
t = textwrap.dedent(str1)
print("Dedented: \n", t)
```

运行脚本，我们将得到如下输出：

```bash
python3 dedent_example.py
Original: 
 
        Hello Python World      This is Python 101
        Scripting language

        Python is an interpreted high-level programming language for general-purpose programming.


Dedented: 
 
Hello Python World      This is Python 101
Scripting language

Python is an interpreted high-level programming language for general-purpose programming.
```

上例中，我们创建了一个字符串变量str1。然后我们使用了textwrap.dedent()来移除了常见前置空白内容。制表符和空格都可视作空白内容，但两者并不等价。因此，本例中的对唯一空白内容 tag 进行了删除。

### indent()函数

indent()函数用于在文本选择定行的起始处添加指定前置内容。

该函数的语法为：textwrap.indent(text, prefix)

- text: 主字符串
- prefix: 要添加的前置内容

创建一个脚本indent_example.py并编写如下内容：

```python
import textwrap
 
str1 = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, \n\nPython has a design philosophy that emphasizes code readability, notably using significant whitespace."
 
w = textwrap.fill(str1, width=30)
i = textwrap.indent(w , '*')
print(i)
```

运行脚本，我们将得到如下输出：

```bash

[liyupi@localhost Chapter07]$ python3 indent_example.py
*Python is an interpreted high-
*level programming language for
*general-purpose programming.
*Created by Guido van Rossum
*and first released in 1991,
*Python has a design philosophy
*that emphasizes code
*readability, notably using
*significant whitespace.
```

在上例中，我们使用了textwrap模块的fill()和indent()函数。首先，我们使用了fill方法将数据存储在变量w中。接着我们使用了indent方法，输出的每行都会添加一个前缀*。然后我们打印了输出。

### shorten()函数

textwraps模块中的这一函数用于截断文本来适配指定的宽度。例如，我们想要创建摘要或预览时，可使用 shorten()函数。使用 shorten()时，文本中所有的空白内容都会被标准化为单个空格。

该函数的语法为：textwrap.shorten(text, width)

下面我们来看一个shorten()的示例。创建一个脚本shorten_example.py并编写如下内容：

```python
import textwrap
 
str1 = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, \n\nPython has a design philosophy that emphasizes code readability, notably using significant whitespace."
 
s = textwrap.shorten(str1, width=50)
print(s)
```

运行脚本，我们将得到如下输出：

```
python3 shorten_example.py 
Python is an interpreted high-level [...]
```

在上例中，我们使用了shorten()函数来截取文本来适配指定的宽度。首先，所有的空白内容都被截断为单个空格。如果结果符合指定宽度，则会将结果显示在屏幕上。否则，指定宽度的单词会显示在屏幕上，而其余的则放在占位符中。

## 正则表达式

这一部分中，我们将来学习Python中的正则表达式。正则表达式是一种专用编程语言，内置在Python中，用户可通过re来进行使用。我们为想要匹配的字符串集定义规则 。使用正则表达式，我们可以从文件、代码、文档、电子表格等中提取指定的信息。

在Python中，正则表达式由re表示并可通过re模块来进行导入。正则表达式支持4种内容：

- 标识符
- 修饰符
- 空白字符
-  Flag标记

以下表格列出了标识符（identifier），对每一个都有相关的描述：

| 标识符 | 描述                                |
| ------ | ----------------------------------- |
| \w     | 匹配字字母数字字符，包含下划线(_)   |
| \W     | 匹配非字母数字字符，不包含下划线(_) |
| \d     | 匹配一个数字                        |
| \D     | 匹配一个非数字字符                  |
| \s     | 匹配一个空格                        |
| \S     | 匹配空格以外的字符                  |
| .      | 匹配一个点号 (.)，注：应为任意字符  |
| \b     | 匹配任意新行以外的字符              |

下表中列出了修饰符（modifier）以及对应的描述：

| 修饰符 | 描述                 |
| ------ | -------------------- |
| ^      | 匹配字符串的起始处   |
| $      | 匹配字符串的结尾处   |
| ?      | 匹配0次或11次        |
| *      | 匹配0次或多次        |
| +      | 匹配1次或多次        |
| \|     | 匹配两边内容之一x/y  |
| [ ]    | 范围匹配             |
| {x}    | 前面标识符的匹配次数 |

下表中列出了空白字符（whitespace）及相应描述：

| 字符 | 描述          |
| ---- | ------------- |
| \s   | 空格          |
| \t   | 制表符 Tab    |
| \n   | 新起一行      |
| \e   | 回撤Escape    |
| \f   | 换页Form feed |
| \r   | 返回          |

以下表格列出了标记及相应描述：

| Flag 标记     | 描述                       |
| ------------- | -------------------------- |
| re.IGNORECASE | 忽略大小写匹配             |
| re.DOTALL     | 匹配包括新行在内的任意字符 |
| re.MULTILINE  | 多行匹配                   |
| Re.ASCII      | 仅对ASCII字符进行转义匹配  |

下面我们来看看一些正则表达式的示例。我们将学习match(), search(), findall()和sub()函数。

> ℹ️要使用Python中的正则表达式，必须要在脚本中导入re模块，这样才能对正则表达式使用所有的函数和方法。

下面我们就来逐一地学习这些函数。

### match()函数

match()是re模块中的一个函数。该函数会将指定的re模式与字符串相匹配。如果找到了匹配，会返回一个匹配对象。匹配对象中包含匹配的相关信息。如果未找到匹配，我们得到的结果是None。match对象有两个方法：

- group(num): 返回整个匹配
- groups(): 在元组中返回所有匹配的子组

该函数的语法如下：

re.match(pattern, string)

下面我们来看一个re.match()的示例。创建一个脚本re_match.py并编写如下的内容：

```python
import re

str_line = "This is python tutorial. Do you enjoy learning python ?"
obj = re.match(r'(.*) enjoy (.*?) .*', str_line)
if obj:
	print(obj.groups())

```

运行该脚本，将得到如下输出：

```
python3 re_match.py 
('This is python tutorial. Do you', 'learning')
```

在以上脚本中，我们导入了re模块来在Python中使用正则表达式。然后我们创建了一个字符串str_line。接着我们创建了一个匹配对象obj并在其中存储了模式匹配的结果。本例中，(.*) enjoy (.*?) .*模式会打印出enjoy关键字之前的所有内容，以及只打出enjoy关键字之后的一个单词。然后我们使用了匹配对象的groups()方法。它会打印出元组中的所有匹配子字符串。因此，我闪将得到的输出是(‘This is python tutorial. Do you’, ‘learning’)。

### search()函数

re模块中的search()函数会对字符串进行搜索。它会查找re模式中的所有位置。search()会接收一个模式和文本，并在指定的字符串中搜索匹配内容。它会在查找到匹配时会返回一个匹配对象，否则返回None。match对象有两个方法：

- group(num): 返回整个匹配
- groups(): 在元组中返回所有匹配的子组

该函数的语法如下：

re.search(pattern, string)

创建脚本re_search.py 并编写如下内容：

```python
import re
 
pattern = ['programming', 'hello']
str_line = 'Python programming is fun'
for p in pattern:
        print('Searching for %s in %s' % (p, str_line))
        if re.search(p, str_line):
                print('Match found')
        else:
                print('No match found')
```

运行脚本，将会得到如下输出：

```bash
python3 re_search.py 
Searching for programming in Python programming is fun
Match found
Searching for hello in Python programming is fun
No match found
```

上例中，我们使用了匹配对象的search()方法来查找正则模式。在导入re模块后，我们在列表中指定了模式。在该列表中我们编写了两个字符串：programming的hello。接着我们创建了一个字符串：Python programming is fun。我们编写了一个for循环来对指定模式进行逐一检查。如果找到了匹配内容，则执行if代码块，否则执行else代码块。

### findall()函数

这是match对象的另一个方法。findall() 方法查找所有的匹配内容，然后以字符串列表的形式返回。列表中的每一个元素代表一个匹配。该方法搜索模式的匹配，并不重叠。

创建一个脚本 re_findall_example.py并编写如下内容：

```bash
import re

pattern = 'Red'
colors = 'Red, Blue, Black, Red, Green'
p = re.findall(pattern, colors)
print(p)

str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?'
pt = re.findall('pe\w+', str_line)
pt1 = re.findall('pic\w+', str_line)
print(pt)
print(pt1)

line = 'Hello hello HELLO bye'
p = re.findall('he\w+', line, re.IGNORECASE)
print(p)

```

运行脚本，将得到如下输出：

```bash
python3 re_findall_example.py 
['Red', 'Red']
['per', 'peck', 'peppers', 'peppers', 'per']
['picked', 'pickled', 'pickled', 'pick']
['Hello', 'hello', 'HELLO']
```

以上脚本中，我们使用findall() 方法编写了三个示例。第一个示例中，我们定义了一个模式和一个字符串。我们使用findall() 方法在这个字符串查找 该模式，然后进行打印。第二个示例中，我们创建了一个字符串，并使用findall()查找该字符串中前面两个字母为pe的单词，然后进行打印。我们得到了一个前两个字母为pe的单词列表。

此外，我们查找前三个字母为pic的单词并进行打印。这里我们同样将得到一个字符串列表。第三个示例中，我们创建了一个字符串，包含大小写的hello以及单词bye。我们使用findall()查找前两个字母为he的单词。同时在findall()中我们使用了re.IGNORECASE标记来忽略单词的大小写并进行了打印。

### sub()函数

这是re模块中最重要的函数之一。sub()用于将指定的替代文本替换掉re模式。它将以替换字符串来替换掉所有re模式发生的内容。语法如下：

re.sub(pattern, repl_str, string, count=0)

- pattern: re模式
- repl_str: 替换字符串
- string: 主字符串
- count: 进行替换的次数。默认值为0，表示替换所有发生之处。

下面我们来创建脚本re_sub.py并编写如下内容：

```python
import re

str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?'

print('Original: ', str_line)
p = re.sub('Peter', 'Mary', str_line)
print('Replaced: ', p)

p = re.sub('Peter', 'Mary', str_line, count=1)
print('Replacing only one occurence of Peter... ')
print('Replaced: ', p)

```

运行脚本，将得到如下输出：

```bash
python3 re_sub.py
Original:  Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?
Replaced:  Mary Piper picked a peck of pickled peppers. How many pickled peppers did Mary Piper pick?
Replacing only one occurence of Peter... 
Replaced:  Mary Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?
```

上例中，我们使用了sub()来以指定的字符串来替换re模式。我们以Mary替换了Peter。因此，所有的Peter都以Mary进行了替换。接着，我们增加了count参数。传入了count=1，表示只对Peter进行一次替换，其它的Peter都不进行替换。

下面，我们将学习re模块中的subn()函数。subn()函数和sub()作用相同，并包含更多的功能。subn() 函数返回一个包含新字符串和执行的替换次数的元组。我们来看一个subn() 的示例。创建一个脚本re_subn.py并编写如下内容：

```python
import re

print('str1:- ')
str1 = 'Sky is blue. Sky is beautiful.'

print('Original: ', str1)
p = re.subn('beautiful', 'stunning', str1)
print('Replaced: ', p)
print()

print('str_line- :')
str_line = 'Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?'

print('Original: ', str_line)
p = re.subn('Peter', 'Mary', str_line)
print('Replaced: ', p)

```

运行脚本，我们将得到如下输出：

```bash
python3 re_subn.py
str1:- 
Original:  Sky is blue. Sky is beautiful.
Replaced:  ('Sky is blue. Sky is stunning.', 1)

str_line- :
Original:  Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?
Replaced:  ('Mary Piper picked a peck of pickled peppers. How many pickled peppers did Mary Piper pick?', 2)
```

上例中，我们使用了subn()函数来替换RE模式。结果我们得到了一个包含替换后文本和替换次数的元组。

## Unicode字符串

这一部分中我们将学习如何在Python中打印Unicode字符串。Python可以很轻易地处理Unicode字符串。字符串类型中包含的实际上是Unicode字符串，而非字节序列。

在系统中启动python3终端并编写如下内容：

```bash
student@python-scripting:~/Chapter07$ python3
Python 3.7.2 (default, Feb 26 2019, 15:56:02)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('\u2713')
✓
>>> print('\u2724')
✤
>>> print('\u2750')
❐
>>> print('\u2780')
➀
>>> chinese = '\u4e16\u754c\u60a8\u597d!'
>>> chinese
'世界您好!'
>>> s = '\u092E\u0941\u0902\u092C\u0908'
>>> s
'मुंबई'                   ------(印地语中“孟买”的意思)
>>> s = '\u10d2\u10d0\u10db\u10d0\u10e0\u10ef\u10dd\u10d1\u10d0'
>>> s
'გამარჯობა'                   ------(格鲁吉亚语中“Hello”的意思)
>>> s = '\u03b3\u03b5\u03b9\u03b1\u03c3\u03b1\u03c2'
>>> s
'γειασας'                   ------(希腊语中“Hello”的意思)
>>>
```



### Unicode代码点

这一部分中，我们将学习unicode代码点（code point）。Python有一个名为ord() 的强大内置函数，可从指定字符获取Unicode代码点。因此我们来看一个从字符获取Unicode代码点的示例，参见如下代码：

```bash
>>> str1 = u'Office'
>>> for char in str1:
... 	print('U+%04x' % ord(char))
...
U+004f
U+0066
U+0066
U+0069
U+0063
U+0065
>>> str2 = '中文'
>>> for char in str2:
... 	print('U+%04x' % ord(char))
...
U+4e2d
U+6587
```



### 编码

将Unicode代码点转换为字节串称为编码。我们来看一个如何对Unicode代码点编码的示例，参见如下代码：

```
>>> str = u'Office'
>>> enc_str = type(str.encode('utf-8'))
>>> enc_str
<class 'bytes'>
```



#### 解码

由字节串转换为Unicode代码点称为解码。下面我们来看一个如何对字节串解码获取Unicode代码点的示例，参见如下代码：

```bash
>>> str = bytes('Office', encoding='utf-8')
>>> dec_str = str.decode('utf-8')
>>> dec_str
'Office'
```



### 避免UnicodeDecodeError

UnicodeDecodeError在字节串无法解码为Unicode代码点时会报出。要避免这一异常，我们可以向decode中错误参数传递replace, backslashreplace或ignore，如下所示：

```bash
>>> str = b"\xaf"
>>> str.decode('utf-8', 'strict')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xaf in position 0: invalid start byte
>>> str.decode('utf-8', 'replace')
'�'       # 原文是'\ufffd'，测试了3.6和3.7均是前面的结果
>>> str.decode('utf-8', 'backslashreplace')
'\\xaf'
>>> str.decode('utf-8', 'ignore')
```



## 总结

本章中我们学习了正则表达式，使用它我们可以定义一系列想要匹配字符串的规则。我们也学习了re模块中的四个函数：match(), search(), findall()和sub()。

我们学习了textwrap模块，用于对普通文本进行格式化和封装。我们还学习了textwrap模块中的wrap(), fill(), dedent(), indent()和shorten()函数。最后，我们学习了Unicode字符以及如何在Python中打印Unicode字符串。

下一章中，我们将学习Python中的标准文档和信息报告。

## 课后问题

1. Python中的正则表达式是什么？
2. 编写一个Python程序来检查只包含指定字符集合的字符串（本例中为a–z, A–Z和0–9）。
3. Python中的哪个模块支持正则表达式？
   a) re
   b) regex
   c) pyregex
   d) 以上都不是
4. re.match函数的作用是什么？
   a)在字符串起始处匹配模式
   b)在字符中任意位置匹配模式
   c)不存在该函数
   d)以上都不对
5. 以下的输出是什么？
   语句: “we are humans”
   匹配：re.match(r'(.*) (.*?) (.*)’, sentence)
   a) (‘we’, ‘are’, ‘humans’)
   b) (we, are, humans)
   c) (‘we’, ‘humans’)
   d) ‘we are humans’

## 扩展阅读

- 正则表达式: https://docs.python.org/3.2/library/re.html
- Textwrap文档: https://docs.python.org/3/library/textwrap.html
- Unicode文档: https://docs.python.org/3/howto/unicode.html

# [第八章 文档和报告](https://alanhou.org/documentation-reporting/)

> 

本章中我们将学习使用Python来记录和报告信息。我们会学习如何使用Python脚本来接收输入以及如何打印输出。在Python中编写脚本更为容易。我们将学习如何格式化信息。

本章中，我们将学习如下内容：

- 标准输入和输出
- 信息格式化
- 发送email

## 标准输入和输出

这一部分，我们将学习Python中的输入和输出。我们会学习stdin和stdout，以及input()函数。

stdin和stdout是类似文件的对象。这些对象由操作系统提供。当用户在交互会话中运行程序时，stdin作为输入，stdout是用户的终端。因为stdin是类似文件的对象，我们要从stdin中读取数据而不是在运行时读取数据。stdout用于输出。它用作表达式和print()函数的输出，以及input()函数的弹出界面。

接下来，我们来看一个stdin和stdout的示例。为此创建一个脚本stdin_stdout_example.py并编写如下内容：

```python
import sys

print("Enter number1: ")
a = int(sys.stdin.readline())

print("Enter number2: ")
b = int(sys.stdin.readline())

c = a + b
sys.stdout.write("Result: %d " % c)

```

运行脚本，我们将得到如下输出：

```bash
python3 stdin_stdout_example.py
Enter number1: 
10
Enter number2: 
20
Result: 30 
```

在上例中，我们使用了stdin和stdout来接收输入和展示输出。sys.stdin.readline() 会从stdin中进行读取。sys.stdout.write()会写入数据。

下面我们将学习input()和print()函数。input() 函数用于从用户接收输入。该函数有一个可选参数：提示字符串。

语法：input(prompt)

input()函数返回一个字符串值。如果需要数值，仅需在input()之前使用int关键字。可以使用如下方式：

int(input(prompt))

类似地，我们可以书写float来获取浮点值。下面我们来看一个示例。创建一个脚本 input_example.py并编写如下代码：

```python
str1 = input("Enter a string: ")
print("Entered string is : ", str1)
print()

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = a + b
print("Value of c is: ", c)
print()

num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))
num3 = num1/num2
print("Value of num3 is: ", num3)

```

运行脚本，将得到如下结果：

```bash
python3 input_example.py
Enter a string: Hello
Entered string is :  Hello

Enter the value of a: 10
Enter the value of b: 20
Value of c is:  30

Enter num 1: 10.5
Enter num 2: 2.0
Value of num3 is:  5.25
```

上例中我们使用了input()函数来处理三个不同值。第一个为字符串，第二个为整数值，第三个浮点值。要对整型和浮点型使用input()，我们需要用int()和float()类型转换函数来将接收到的字符串分别转换为整型和浮点型。

print()函数用于输出数据。我们需要传入一个逗号分隔的一系列参数。在input_example.py中，要得到输出，我们使用print()函数。使用print()函数，我们可以仅通过在数据两边加上 ” ” 或 ‘ ‘来将数据写到屏幕上。如果仅输出值，只需将变量名写到print()函数中。如果想要在同一个print()函数中编写文本同时获取值，那么将两者使用逗号分隔即可。

我们来看一个print()函数的简单示例。创建脚本print_example.py并在其中编写如下内容：

```python
# 在屏幕上打印简单字符串
print("Hello Python")

# 仅访问值
a = 80
print(a)

# 在屏幕上打印字符串并获取值
a = 50
b = 30
c = a/b
print("The value of c is: ", c)

```

运行脚本，将得到如下输出：

```bash
python3 print_example.py
Hello Python
80
The value of c is:  1.6666666666666667
```

上例中，首先我们简单地在屏幕上打印了一个字符串。然后我们获取了变量 a 的值并在屏幕上进行了打印。最后，我们输入了 a 和 b 的值，进行想加并存储在变量 c 中，然后打印了一个语句并在同一个print()函数访问了变量值。

## 信息格式化

这部分中，我们将学习字符串的格式化。我们将学习格式化信息的两种方式：一种是使用string format()方法，另一种通过使用 %运算符。

首先，我们会学习使用字符串的format()方法来格式化字符串。字符串类的该方法让我们可以对值进行格式化。它也可以让我们进行变量替换。这将通过位置参数来合并元素。

下面我们将学习如何使用格式化器来进行这一格式化。调用该方法的字符串可以包含纯文本或以大括号{}分隔的替换字段。对同一字符串进行格式化时可以使用多组 {}。这一替换字段可包含参数的索引或参数的名称。运行之后，我们将得到一个以参数字符串值对字段进行替换后的字符串的拷贝。

下面我们就来看一个字符串格式化的示例。

创建一个脚本format_example.py并编写如下内容：

```python
# Using single formatter
print("{}, My name is John".format("Hi"))
str1 = "This is John. I am learning {} scripting language."
print(str1.format("Python"))

print("Hi, My name is Sara and I am {} years old!!".format(26))

# Using multiple formatters
str2 = "This is Mary {}. I wark at {} Resource department. I am {} years old!!"
print(str2.format("Jacobs", "Human", 30))

print("Hello {}, Nice to meet you. I am {}.".format("Emily", "Jennifer"))

```

运行脚本如下：

```bash
 python3 format_example.py
Hi, My name is John
This is John. I am learning Python scripting language.
Hi, My name is Sara and I am 26 years old!!
This is Mary Jacobs. I wark at Human Resource department. I am 30 years old!!
Hello Emily, Nice to meet you. I am Jennifer.
```

上例中，我们使用了字符串类的format() 方法并通过一个和多个格式化器进行了字符串格式化。

下面，我们将学习使用%运算符来进行字符串格式化。与%运算符一同使用的还有一些格式化符号。以下是常用的一些符号：

- %d: 数字整型
- %s: 字符串
- %f: 浮点数
- %c: 字符

我们来看一个示例。创建一个脚本string_formatting.py并编写如下内容：

```python
# Basic formatting
a = 10
b = 20
print("The values of a and b are %d %d" % (a, b))
c = a + b
print("The value of c is %d" % c)

str1 = "John"
print("My name is %s" % str1)

x = 10.5
y = 33.5
z = x * y
print("The value of z is %f" % z)
print()

# aligning
name = "Mary"
a = 10
b = 20
print("The values of a and b are %d %d" % (a, b))
c = a + b 
print("The value of c is %d" % c)

str1 = "John"
print("My name is %s" % str1)

x = 10.5
b = 33.5
z = x * y
print("The value of z is %f" % z)
print()

# aligning
name = "Mary"
print("Normal: Hello, I am %s !!" % name)

print("Right aligned: Hello, I am %10s !!" % name)

print("Left aligned: Hello, I am %-10s !!" % name)
print()

# truncating
print("The truncated string is %.4s" % ("Examination"))
print()

# formatting placeholders
students = {'Name' : 'John', 'Address' : 'New York'}
print("Student details: Name:%(Name)s Address:%(Address)s" % students)

```

运行脚本，将得到如下结果：

```bash
python3 string_formatting.py
The values of a and b are 10 20
The value of c is 30
My name is John
The value of z is 351.750000

The values of a and b are 10 20
The value of c is 30
My name is John
The value of z is 351.750000

Normal: Hello, I am Mary !!
Right aligned: Hello, I am       Mary !!
Left aligned: Hello, I am Mary       !!

The truncated string is Exam

Student details: Name:John Address:New York
```

上例中，我们使用了%运算符来格式化字符串：%d为数字，%s为字符串，%f 为浮点数。然后，我们对字符串进行了向左和向右对齐。我们还学习了如何使用%运算符截取字符串。%.4s仅显示前4个字符。然后我们创建了一个名为students的字典，并输入了Name和Address键值对。最后，我们在%运算符之后放置键名来获取这些字符串。

## 发送email

这一部分中，我们将学习通过Python脚本来从Gmail发送邮件。Python带有一个名为smtplib的模块实现这一功能。Python中的smtplib模块提供了SMTP客户端会话对象，用于使用SMTP监听器向互联网上的任意机器发送邮件。

我们来看一个示例。本例中，我们将从Gmail向收件人发送一封包含简单文本的email。

创建一个send_email.py脚本并编写如下内容：

```python
import smtplib
from email.mime.text import MIMEText
import getpass

host_name = 'smtp.gmail.com'
# host_name = 'smtp.exmail.qq.com'
port = 465

u_name = 'username/emailid'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['receiver1_email_address', 'receiver2_email_address']

text = MIMEText('Test mail')
text['Subject'] = 'Test'
text['From'] = sender
text['To'] = ', '.join(receivers)

s_obj = smtplib.SMTP_SSL(host_name, port)
s_obj.login(u_name, password)
s_obj.sendmail(sender, receivers, text.as_string())
s_obj.quit()
print("Mail sent successully")

```

译者注：测试时Gmail和 QQ 邮箱报错：smtplib.SMTPAuthenticationError，应为验证机制所致，腾讯企业邮箱正常

运行脚本如下

```
$ python3 send_email.py 
```

输出结果

```
Password:Mail sent successully
```

上例中，我们通过Gmail ID来向收件人发送邮件。变量u_name会存储你的email ID。对password变量，你可以直接使用密码赋值，也可以使用getpass模块来接收密码输入。这里我们提示输入密码。变量sender中可传入你的姓名。接着我们添加了邮件发送的多个接收人。然后，我们传入了标题、发件人和邮件的接收者。接着我们在login()中放入了u_name和password变量。再后在sendmail()中，我们传入了发件人、收件人和变量text。那么使用这个流程我们成功的发送了邮件。

下面我们再来看一个示例，发送一个带附件的邮件。本例中，我们将向接收人发送一张图片。我们将通过Gmail来发送这一邮件。创建一个脚本send_email_attachment.py并编写如下内容：

```python
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

u_name = 'username/emailid'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['receiver1_email_address', 'receiver2_email_address']

text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = ', '.join(receivers)

txt = MIMEText('sending a sample image.')
text.attach(txt)

f_path = '/home/student/Desktop/mountain.jpg'
with open(f_path, 'rb') as f:
	img = MIMEImage(f.read())

img.add_header('Content-Disposition',
		'attachment',
		filename=os.path.basename(f_path))

text.attach(img)

server = smtplib.SMTP_SSL(host_name, port)
server.login(u_name, password)
server.sendmail(u_name, receivers, text.as_string())
print("Email with attachment sent successfully !!")
server.quit() 

```

运行脚本如下：

```
$ python3 send_email_attachment.py 
```



 输出

```
Password:Email with attachment sent successfully !!
```



上例中，我们向接收人发送了一张带有图片附件的邮件。我们传入了发送人和接收人的email ID。然后，为f_path赋值了作为附件发送的图片的路径。再后我们向接收人发送了以该图片为附件的邮件。

> ℹ️在前面的两个例子中 – send_text.py和send_email_attachment.py – 我们通过 Gmail 发送了邮件。你可以使用任意其它的邮件提供商进行发送。要使用其它的邮件提供商，只需为host_name传入提供商的名称。当然别忘了在前面加上 smtp。在这些示例中，我们使用了smtp.gmail.com，而如果是Yahoo!，你可以使用smtp.mail.yahoo.com。因此可根据邮件提供商的不同来提供对应的主机名和端口。

## 总结

本章中，我们学习了标准输入和输出。我们学习了stdin和stdout如何分别进行键盘输入和用户终端输出。我们还学习了input()和print()函数。此外，我们学习了从Gmail向接收人发送邮件。我们使用普通文本以及附件分别发送了邮件。同时我们学习了使用format()方法和%运算符进行字符串格式化。

下一章中，我们会学习如何处理不同文件，如PDF, Excel和csv。

## 课后问题

1. stdin和输入的区别是什么？

2. SMTP是什么？

3. 以下代码的输出是什么？

   ```bash
   >>> name = "Eric"
   >>> profession = "comedian"
   >>> affiliation = "Monty Python"
   >>> age = 25
   >>> message = (
   ... 	f"Hi {name}. "
   ... 	f"You are a {profession}. "
   ... 	f"You were in {affiliation}."
   ... )
   >>> message
   ```

   

4. 以下代码的输出是什么？

   ```bash
   str1 = 'Hello'
   str2 = 'World!'
   print('str1 + str2 = ', str1 + str2)
   print('str1 * 3 =', str1 * 3)
   ```

   

## 扩展阅读

1. 字符串文档：https://docs.python.org/3.1/library/string.html
2. smptplib文档: https://docs.python.org/3/library/smtplib.html





# [第九章 操作各类文件](https://alanhou.org/working-files/)



本章中我们将学习操作各种文件类型，如PDF文件、Excel、CSV和txt文件。Python有对这些文件执行操作的不同模块。我们将学习如何使用Python来打开、编辑或从这些文件中读取数据。

本章将涉及如下课题：

- 操作PDF文件
- 操作Excel文件
- 操作CSV文件
- 操作txt文件

## 操作PDF文件

这一部分中，我们将学习如何使用Python模块来处理PDF文件。PDF是被广泛使用的一种文件格式，后缀名为.pdf。Python有一个名为PyPDF2的模块，有助于对pdf文件进行各类操作。它是一个第三方模块，是个创建为PDF工具集的Python库。

首先我们必须要安装该模块。要安装PyPDF2，在命令终端运行如下命令：

```bash
pip3 install PyPDF2
```



下面我们来看其中的一些操作来处理PDF文件，比如读取PDF，获取页面数，提取文本和旋转 PDF 页面。

### 读取PDF文档并获取页数

这部分中我们将学习使用PyPDF2模块来读取PDF文件。同时我们会获取到PDF的页面数。该模块带有一个名为PdfFileReader()的函数可进行PDF文件的读取。确保系统里有一个PDF文件。这里我们在系统里有一个Haltermanpythonbook.pdf文件，因此在这一部分中都会使用该文件。使用你的PDF文件名来替换Haltermanpythonbook.pdf。创建脚本read_pdf.py并编写如下内容：

```python
import PyPDF2

with open('Haltermanpythonbook.pdf', 'rb') as pdf:
	read_pdf = PyPDF2.PdfFileReader(pdf)
	print("Number of pages in pdf : ", read_pdf.numPages)

```



运行脚本将得到如下输出：

```bash
python3 read_pdf.py
Number of pages in pdf :  283
```

上例中，我们使用了PyPDF2模块。然后我们创建了一个pdf文件对象。PdfFileReader() 会读取所创建的对象。在读取PDF文件后，我们使用numPages属性来获取PDF文件的页数。本例中为283页。

### 提取文本

要提取PDF文件的页面内容，PyPDF2模块带有一个extractText()方法。创建一个名为extract_text.py的脚本并编写如下内容：

```
import PyPDF2

with open('Haltermanpythonbook.pdf', 'rb') as pdf:
	read_pdf = PyPDF2.PdfFileReader(pdf)
	pdf_page = read_pdf.getPage(2)
	pdf_content = pdf_page.extractText()
	print(pdf_content)

```

运行脚本可得到如下输出：

```
 python3 extract_text.py
i
Contents
1TheContextofSoftwareDevelopment1
1.1Software............................................
2
1.2DevelopmentTools......................................
2
1.3LearningProgrammingwithPython.............................
4
1.4WritingaPythonProgram..................................
5
1.5ALongerPythonprogram..................................
8
1.6Summary...........................................
9
1.7Exercises...........................................
9
2ValuesandVariables11
2.1IntegerValues.........................................
11
2.2VariablesandAssignment...................................
16
2.3...........................................
19
2.4Floating-pointTypes.....................................
23
2.5ControlCodeswithinStrings.................................
24
2.6UserInput...........................................
26
2.7The
eval
Function......................................
27
2.8Controllingthe
print
Function................................
29
2.9Summary...........................................
31
2.10Exercises...........................................
32
3ExpressionsandArithmetic35
3.1Expressions..........................................
35
3.2OperatorPrecedenceandAssociativity............................
40
3.3Comments...........................................
41
3.4Errors.............................................
42
©2011RichardL.Halterman
Draftdate:November13,2011
```

上例中我们创建了一个文件读取器对象。pdf读取器对象有一个名为getPage()的函数，可接收页面数（索引从0开始）来作为参数，并返回页面对象。然后我们使用了extractText()方法，它可提取getPage()中所指定的的页面的文本。页面的索引从0开始。

### 旋转PDF页面

这部分中我们来看看如何对PDF页面进行旋转。我们可以使用PDF对象的rotate.Clockwise()来进行实现。创建一个名为rotate_pdf.py的脚本并编写如下内容：

```python
import PyPDF2

with open('Haltermanpythonbook.pdf', 'rb') as pdf:
	rd_pdf = PyPDF2.PdfFileReader(pdf)
	wr_pdf = PyPDF2. PdfFileWriter()
	for pg_num in range(rd_pdf.numPages):
		pdf_page = rd_pdf.getPage(pg_num)
		pdf_page.rotateClockwise(90)
		wr_pdf.addPage(pdf_page)
	
	with open('rotated.pdf', 'wb') as pdf_out:
		wr_pdf.write(pdf_out)
	
	print("pdf successfully rotated")

```

运行脚本将得到如下输出：

```bash
python3 rotate_pdf.py
pdf successfully rotated
```

上例中为实现pdf的旋转，我们首先创建一个原pdf文件的pdf文件读取器。然后将旋转后的页面写入一个新的pdf文件中。对新pdf文件的定性主，我们使用了PyPDF2模块中的PdfFileWriter()函数。新的pdf文件以rotated.pdf名称进行保存。这时我们使用rotateClockwise()方法来旋转pdf文件的页面。然后，使用addPage()方法，来添加旋转后的页面。接着我们将这些pdf页面写入新的pdf文件。因此，首先我们应打开新的文件对象 (pdf_out)并使用pdf的写入器对象的write()方法来写入 pdf页面。最后，我们将关闭原文件对象（Haltermanpythonbook.pdf）以及新的文件对象(pdf_out)。

## 操作Excel文件

这一部分我们来学习后缀名为.xlsx的Excel文件的处理。这一后缀名是一种Microsoft Excel使用的OpenXML 数据表文件格式。

Python有多个模块可处理Excel文件：xlrd , pandas和openpyxl。这一部分中我们将学习使用这三个模块来处理Excel文件。

首先我们会来看一个使用xlrd模块的示例。xlrd模块用于读取、写入和修改Excel数据表以及其它相关处理。

### 使用xlrd模块

首先我们要安装xlrd模块。在终端中运行如下命令来安装xlrd模块：

```
pip3 install xlrd
```





> ℹ️注意：要确保系统里有Excel文件。我这里系统中有一个sample.xlsx文件。在这一部分中我都会使用该文件。

**译者注：**Alan 使用了一个网上可下载的示例 Excel文件：[Sample – Superstore.xls](https://community.tableau.com/servlet/JiveServlet/previewBody/1236-102-2-15278/Sample - Superstore.xls)

我们来看如何读取Excel文件以及如何从Excel文件中提取行和列。

#### 读取Excel文件

这一部分中，我们来看下如何读取Excel文件。我们需要用到 xlrds模块，创建一个脚本read_excel.py并编写如下内容：

```python
import xlrd

excel_file = (r"Sample - Superstore.xls")
book_obj = xlrd.open_workbook(excel_file)
excel_sheet = book_obj.sheet_by_index(0)
result = excel_sheet.cell_value(0, 1)
print(result) 

```



运行脚本将得到如下输出：

```
 python3 read_excel.py
Order ID
```

上例中，我们导入了xlrd模块来读取Excel文件。我们还传入了Excel文件的位置。然后，创建了一个文件对象，传入了索引值，这样就从会索引处开始读取。最后我们打印出了结果。

#### 提取列名

这一部分我们来从Excel表格中提取列名。创建一个名为extract_column_names.py的脚本并编写如下内容：

```python
import xlrd

excel_file = ('Sample - Superstore.xls')
book_obj = xlrd.open_workbook(excel_file)
excel_sheet = book_obj.sheet_by_index(0)
excel_sheet.cell_value(0,0)
for i in range(excel_sheet.ncols):
	print(excel_sheet.cell_value(0,i))

```



运行脚本，我们将得到如下输出：

```bash
python3 extract_column_names.py
Row ID
Order ID
Order Date
Ship Date
Ship Mode
Customer ID
Customer Name
Segment
Country
City
State
Postal Code
Region
Product ID
Category
Sub-Category
Product Name
Sales
Quantity
Discount
Profit
```

上例中，我们从Excel表章中提取了列名。我们使用ncols属性获取了列名。

### 使用pandas

在使用Pandas读取Excel文件之前，我们首先要安装pandas模块。我们可通过下面的命令安装pandas：

```
pip3 install pandas
```





> ℹ️注意：确保在你的系统里有一个Excel文件。我的系统里有一个sample.xlsx。因此在整个部分中我将使用该文件。

**译者注：**Alan 将继续使用前文下载的文件

下面我们来看看使用pandas的一些示例。

#### 读取Excel文件

这一部分中，我们将使用pandas模块来读取Excel文件。下面我们来看一个读取Excel文件的示例。

创建一个名为 rd_excel_pandas.py的文件并编写如下内容：

```python
import pandas as pd

excel_file = 'Sample - Superstore.xls'
df = pd.read_excel(excel_file)
print(df.head())

```

运行以上脚本将得到如下输出：

```bash
python3 rd_excel_pandas.py
   Row ID        Order ID Order Date  ... Quantity Discount    Profit
0       1  CA-2016-152156 2016-11-08  ...        2     0.00   41.9136
1       2  CA-2016-152156 2016-11-08  ...        3     0.00  219.5820
2       3  CA-2016-138688 2016-06-12  ...        2     0.00    6.8714
3       4  US-2015-108966 2015-10-11  ...        5     0.45 -383.0310
4       5  US-2015-108966 2015-10-11  ...        2     0.20    2.5164

[5 rows x 21 columns]
```

上例中，我们使用了pandas来读取Excel文件。首先我们导入了pandas模块。然后我们创建了一个excel_file字符串来存储打开的文件名，以供pandas做进一步的操作。再后我们创建了一个数据帧对象df。在该例中，我们使用了pandas的read_excel方法来以默认函数从Excel文件中读取数据。读取从索引0处开始。最后，我们打印出了pandas数据帧。

#### 读取Excel文件指定列

在使用pandas模块并通过read_excel方法读取Excel文件时，我们还能够读取该文件中的列名。要读取指定的列名，我们需要在read_excel方法中使用usecols参数。

下面我们来看一个读取Excel文件指定列的示例。创建一个名为rd_excel_pandas1.py的脚本并编写如下内容：

```python
import pandas as panda

excel_file = 'Sample - Superstore.xls'
cols = [1, 2, 3]
df = panda.read_excel(excel_file, sheet_name='Orders', usecols=cols)

print(df.head())

```

运行上述脚本将得到如下输出：

```bash
python3 rd_excel_pandas1.py 
         Order ID Order Date  Ship Date
0  CA-2016-152156 2016-11-08 2016-11-11
1  CA-2016-152156 2016-11-08 2016-11-11
2  CA-2016-138688 2016-06-12 2016-06-16
3  US-2015-108966 2015-10-11 2015-10-18
4  US-2015-108966 2015-10-11 2015-10-18
```

上例中首先我们导入了pandas模块。然后我们创建一个名为excel_file的字符串来存储文件名。再后我们定义了变量cols并传入其中列的索引值。这样在使用read_excel方法时，在该方法内，我们还传入了usecols参数来通过索引获取前面通过变量cols定义的指定列。因此，在运行脚本后，我们从Excel文件中获取的仅为指定列。

我们还可以使用pandas模块进行各种其它操作，比如读取有缺失数据的Excel文件、跳过指定行以及读取多个Excel表单。

### 使用openpyxl

openpyxl是一个用于读取和写入xlsx, xlsm, xltx和xltm文件的Python库。首先，我们要安装openpyxl。运行如下命令：

```
pip3 install openpyxl
```



下面我们将使用openpyxl来看一些示例。

#### 新建Excel文件

这一部分中，我们将学习使用openpyxl来创建一个新的Excel文件。创建一个名为create_excel.py的脚本并编写如下内容：

```python
from openpyxl import Workbook

book_obj = Workbook()
excel_sheet = book_obj.active
excel_sheet['A1'] = 'Name'
excel_sheet['A2'] = 'student'
excel_sheet['B1'] = 'age'
excel_sheet['B2'] = '24'

book_obj.save("test.xlsx")
print("Excel created successfully")

```

运行脚本，我们将得到如下输出：

```bash
python3 create_excel.py
Excel created successfully
```



这时查看当前的工作目录，就可以看到成功地创建了test.xlsx。在上例中，我们向单元格中写入了数据。然后在openpyxl模块中我们导入了Workbook类。工作簿（workbook）是文档其它部分的容器。接着我们我们为活跃表单设置了引用对象，并在A1, A2和B1, B2单元中写入了值。最后，我们通过save() 方法向test.xlsx文件写入了内容。

#### 追加值

这一部分中，我们将在Excel中追加值。这时就要使用到append() 方法。我们可以在想要添加值的当前表单底部添加一组值。创建一个名为append_values.py的脚本并编写如下内容：

```python
from openpyxl import Workbook

book_obj = Workbook()
excel_sheet = book_obj.active
rows = (
	(11, 12, 13),
	(21, 22, 23),
	(31, 32, 33),
	(41, 42, 43)
)
for values in rows:
	excel_sheet.append(values)
	print()
print("values are successfully appended")
book_obj.save('test.xlsx')

```

运行脚本将得到如下输出：

```
 python3 append_values.py
values are successfully appended
```

上例中，我们在test.xlsx文件表单中追加了三列数据。数据以元组内的元组进行存储，通过容器逐行追加数据并使用append()方法插入数据。

#### 读取多个单元格

这一部分中我们将学习读取多个单元格。我们将使用openpyxl模块。创建一个名为read_multiple.py的脚本并编写如下内容：

```python
import openpyxl

book_obj = openpyxl.load_workbook('Sample - Superstore.xlsx')
excel_sheet = book_obj.active
cells = excel_sheet['A1':'C6']
for c1, c2, c3 in cells:
	print("{0:6} {1:6} {2}".format(c1.value, c2.value, c3.value))

```

运行脚本将得到如下输出：

```
$ python3 read_multiple.py
 
# 输出结果
Row ID Order ID Order Date
     1 CA-2016-152156 2016-11-08 00:00:00
     2 CA-2016-152156 2016-11-08 00:00:00
     3 CA-2016-138688 2016-06-12 00:00:00
     4 US-2015-108966 2015-10-11 00:00:00
     5 US-2015-108966 2015-10-11 00:00:00
```

**译者注：**需将前述的 xls 文件转化为 xlsx 格式，因 openpyxl 不支持老版本的格式

前例中，我们通过使用范围运算读取了三列的数据。然后读取 A1 – C6单元格之间的数据。

类似地，我们还可以使用openpyxl模块来对Excel文件进行其它大量操作，如合并单元格、拆分单元格。

### 操作CSV文件

CSV格式表示逗号分隔值（Comma Separated Value）。逗号用于分隔一条记录的各个字段。常用于数据表和数据库中导入导出该格式。

CSV是一种使用特定结构类型排列表格数据的普通文本文件。Python有一个内置的csv模块，由Python来解析这类文件。csv模块多可用于处理从数据表和数据库中导出的带有字段和记录的文本格式文件。

csvs模块内置所有需用到的函数，如下：

- csv.reader: 该函数用于返回一个reader对象，可遍历CSV文件各行
- csv.writer: 该函数用于返回一个writer对象，可向CSV文件写入数据
- csv.register_dialect: 该函数用于注册一个CSV dialect
- csv.unregister_dialect: 该函数用于取消一个CSV dialect的注册
- csv.get_dialect: 该函数用于返回一个给定名称的dialect
- csv.list_dialects: 该函数用于返回所有注册的dialect
- csv.field_size_limit: 该函数用于返回当前解析器所允许的最大字段数

这一部分中，我们仅会来学习csv.reader和csv.writer。

#### 读取CSV文件

Python带有一个内置模块csv，我们将使用它来处理CSV文件。我们会使用csv.reader模块来读取CSV文件。创建一个名为csv_read.py的脚本并编写如下内容：

```python
import csv
 
csv_file = open('Sample - Superstore.csv', 'r', encoding='windows-1252')
with csv_file:
	read_csv = csv.reader(csv_file)
	#for row in read_csv:
		#print(row)
	for index, row in enumerate(read_csv):
		if index <= 5:
			print(row)

```

**译者注：**Alan 使用相同的文件转成了 CSV 格式，运行中出现了报错UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0xa0 in position 2928: invalid start byte，添加了 encoding方能解决，这与 Mac 和 Windows对 CSV 的处理方式相关。同时因原表数据较多，这里修改为仅打印5行数据。

运行脚本，我们将得到如下输出：

```bash
python3 csv_read.py
['Row ID;Order ID;Order Date;Ship Date;Ship Mode;Customer ID;Customer Name;Segment;Country;City;State;Postal Code;Region;Product ID;Category;Sub-Category;Product Name;Sales;Quantity;Discount;Profit']
['1;CA-2016-152156;2016/11/8;2016/11/11;Second Class;CG-12520;Claire Gute;Consumer;United States;Henderson;Kentucky;42420;South;FUR-BO-10001798;Furniture;Bookcases;Bush Somerset Collection Bookcase;261.96;2;0;41.9136']
['2;CA-2016-152156;2016/11/8;2016/11/11;Second Class;CG-12520;Claire Gute;Consumer;United States;Henderson;Kentucky;42420;South;FUR-CH-10000454;Furniture;Chairs;Hon Deluxe Fabric Upholstered Stacking Chairs', ' Rounded Back;731.94;3;0;219.582']
['3;CA-2016-138688;2016/6/12;2016/6/16;Second Class;DV-13045;Darrin Van Huff;Corporate;United States;Los Angeles;California;90036;West;OFF-LA-10000240;Office Supplies;Labels;Self-Adhesive Address Labels for Typewriters by Universal;14.62;2;0;6.8714']
["4;US-2015-108966;2015/10/11;2015/10/18;Standard Class;SO-20335;Sean O'Donnell;Consumer;United States;Fort Lauderdale;Florida;33311;South;FUR-TA-10000577;Furniture;Tables;Bretford CR4500 Series Slim Rectangular Table;957.5775;5;0.45;-383.031"]
["5;US-2015-108966;2015/10/11;2015/10/18;Standard Class;SO-20335;Sean O'Donnell;Consumer;United States;Fort Lauderdale;Florida;33311;South;OFF-ST-10000760;Office Supplies;Storage;Eldon Fold 'N Roll Cart System;22.368;2;0.2;2.5164"]
```

前面的程序中，我们将Sample – Superstore.csv文件打开为csv_file。然后，我们使用了csv.reader()函数来将数据提取到读取器对象，我们可以对该对象进行迭代来获取数据的每一行。下面，我们来看第二个函数csv.Writer()。

#### 写入CSV文件

要将数据写入csv文件，我们使用csv.writer模块。这一部分中，我们将存储一些数据到Python列表中，然后将该数据放到csv文件中。创建一个名为csv_write.py的脚本并编写如下内容：

```python
import csv

write_csv = [['Name', 'Sport'], ['Andres Iniesta', 'Footbal'], ['AB de Villiers', 'Cricket'], ['Vira Kohli', 'Cricket'], ['Lionel Messi', 'Football']]

with open('csv_write.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(write_csv)
	print(write_csv)

```

运行脚本，我们将得到如下输出：

```
python3 csv_write.py
[['Name', 'Sport'], ['Andres Iniesta', 'Footbal'], ['AB de Villiers', 'Cricket'], ['Vira Kohli', 'Cricket'], ['Lionel Messi', 'Football']]
```

以上程序中，我们创建了一个包含姓名和对应运动项目的名为write_csv的列表。接着在创建列表后，我们打开了新创建的csv_write.csvy文件并使用csv.writer() 函数将write_csv列表插入到该文件中。

## 操作txt文件

普通文本文件用于存储仅表示字符或字符串的数据，并且不包含任何结构化的元数据。Python中无需导入任何外部库来读取和写入文本文件。Python提供了内置的函数来创建、打开、关闭、写入和读取文本文件。要进行这些操作，有不同的访问模式来对打开的文件处理可用的操作。

Python中这些访问模式如下：

- 只读模式 (‘r’):该模式以只读打开文本文件。如果该文件不存在，则抛出一个 I/O错误。我们也可称这种模式为打开文件的默认模式。
- 读写模式(‘r+’): 该模式以读写打开文本文件，如果该文件不存在，则抛出一个 I/O错误。
- 只写模式(‘w’): 该模式打开文本文件来进行写入。在文件不存在时则创建文件，对已存在的文件则覆盖原数据。
- 写读模式(‘w+’): 该模式会打开文本文件来进行读取和写入。对已存在的文件会覆盖原数据。
- 追加模式 (‘a’): 该模式会打开文本文件来进行写入。如果文件不存在则会创建文件，数据会在已有数据的最后进行插入。
- 追加读取模式(‘a+’): 该模式会打开文本文件进行读取和客户。如果文件不存在则会创建文件，数据会在已有数据的最后进行插入。

### open()函数

该函数用于打开文件，不需要导入任何外部模块。

语法如下：

Name_of_file_object = open("文件名","访问模式")

对于上述的语法，文件必须要在Python程序相同的目录下。如果文件不在相同目录下，那么我们还需要定义打开文件时的文件路径。这类情况的语法如下所示：

Name_of_file_object = open("/home/……/文件名","访问模式")



#### 打开文件

这里使用open函数打开文件”test.txt”。该文本来相同目录下，并以追加模式打开：

```
text_file = open("test.txt","a")
```

如果文件不在同级目录。我们需在追加模式下定义路径：

```
text_file = open("/home/…../test.txt","a")
```





### close()函数

该函数用于关闭文件，它会释放文件所占用的内存。在无需再使用文件或以不同模式打开文件时使用该函数。

语法如下：

```
Name_of_file_object.close()
```



以下代码可用来简单地打开和关闭一个文件：

```bash
# 打开并关闭test.txt:
text_file = open("test.txt","a")
text_file.close()
```





### 写入文本文件

通过使用Python，我们可以创建一个文本文件（test.txt）。通过代码向文件本文件写入非常容易。打开一个文件进行写入，我们将第二个访问模式参数设为”w”。要向test.txt文件写入数据，我们使用文件句柄对象的write()方法。创建一个名为text_write.py的脚本并编写如下内容：

```
text_file = open("test.txt", "w")
text_file.write("Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\n")
text_file.close()

```

运行以上脚本将会进行文件的创建。这时查看当前工作目录。我们可以发现所创建的test.txt文件。查看文件的内容，我们会发现write()函数写入的星期保存在了test.txt中。

上面的程序中，我们声明了变量text_file来打开名为test.txt.的文件。open函数中传入两个参数：第一个为要打开文件，第二个为表示要对文件进行或应用的权限和操作的访问模式。在程序中，我们在第二参数中使用了字母”w”，即写入模式。然后，我们使用了text_file.close()来关闭存储的test.txt文件实例。

### 读取文本文件

读取文件和写入文件一样简单。要以读取打开一个文件，我们使用”r”代替”w”来作为第二个参数设置访问模式。要从该文件读取数据，我们使用该文件句柄对象的read()方法。创建一个名为text_read.py的脚本并编写如下内容：

```python
text_file = open("test.txt", "r")
data = text_file.read()
print(data)
text_file.close()
```



输出如下：

```
 python3 text_read.py
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
```

在以上程序中，我们定义了一个变量text_file来打开文件test.txt。open函数接收两个参数：第一个为要打开的文件，，第二个为表示要对文件进行或应用的权限和操作的访问模式。在程序中，我们使用了字母”r”作为第二个参数，表示写入操作。然后我们使用了text_file.close()来关闭存储文件test.txt的实例。在运行Python程序之后，我们可以轻易地在终端中查看这一文本文件的内容。

## 总结

本章中，我们学习了各类文件的操作，包括PDF, Excel, CSV和文本文件。我们使用了Python的各模块来执行这类型文件的部分操作。

下一章中，我们将学习Python中的基础网络和因特网模块。

## 课后问题

1. readline()和readlines()之间的区别是什么？
2. open()和with open()之间的区别是什么？
3. 开头的r c:\\Downloads意义何在？
4. 什么是生成器对象？
5. pass的用处是什么？
6. lambda表达式是什么？

## 扩展阅读

- XLRD: https://xlrd.readthedocs.io/en/latest/api.html
- openoyxl: http://www.python-excel.org/
- 生成器函数的概念: https://wiki.python.org/moin/Generators

# [第十章 网络基础 – Socket编程](https://alanhou.org/basic-networking-socket-programming/)



本章中我们将学习sockets和三种互联网协议：http, ftplib和urllib。我们会学习Python中用于网络的socket模块。http是一个用于处理超文本传输协议的包。ftplib用于执行自动化的FTP相关工作。urllib是一个处理URL相关工作的包。

本章中我们将学习如下内容：

- Sockets
- http包
- ftplib模块
- urllib包

## Socket接口

这一部分中， 我们将学习socket（套接字接口）的知识。我们将使用Python的socket模块。socket是本地或远程机器间通过的端点（endpoint）。socket模块有一个socket类，用于处理数据通道。它还包含网络相关操作的函数。要使用socket模块的功能，首先我们要导入socket模块。

我们来看看如何创建一个socket。socket类有一个socket函数，带有两个参数：address_family和socket类型。

语法如下：

```python
import socket
s = socket.socket(address_family, socket type)
```



address_family控制OSI(Open System Interconnection 开放式系统互联)网络分层协议

socket type控制传输层协议

Python支持三种地址类型：AF_INET, AF_INET6和AF_UNIX。最常用的为AF_INET，用于因特网寻址。AF_INET6用于IPv6因特网寻址。AF_UNIX用于Unix域套接字（Unix Domain Sockets – UDS），是一种跨进程通讯协议。

有两种socket类型：SOCK_DGRAM和SOCK_STREAM。SOCK_DGRAM套接字类型用于面向消息的datagram传输，这些与UDP协议相关联。datagram套接字投递单个消息。SOCK_STREAM处理面向数据流的传输，与TCP协议相关联。流套接字接口在客户端和服务器端之间提供字节流。

socket可配置为服务端和客户端接口。在TCP/IP套接字接口都连接时，通讯是双向的。下面我们来探讨一个客户端-服务端通讯的示例。我们会创建两个脚本文件：server.py和client.py。

server.py脚本内容如下：

```python
import socket

host_name  = socket.gethostname()
port = 5000
s_socket = socket.socket()
s_socket.bind((host_name, port))
s_socket.listen(2)

conn, address = s_socket.accept()
print("Connection from: " + str(address))

while True:
        recv_data = conn.recv(1024).decode()
        if not recv_data:
                break
        print("from connected user: " + str(recv_data))
        recv_data = input(' -> ')
        conn.send(recv_data.encode())

conn.close()

```



下面我们来编写客户端脚本。client.py脚本内容如下：

```python
import socket

host_name = socket.gethostname()
port = 5000

c_socket = socket.socket()
c_socket.connect((host_name, port))
msg = input(" -> ")

while msg.lower().strip() != 'bye':
        c_socket.send(msg.encode())
        recv_data = c_socket.recv(1024).decode()
        print('Received from server: ' + recv_data)
        msg = input(" -> ")

c_socket.close()

```



下面我们要在两个不同的终端中运行这两个程序。第一个终端中运行server.py，在第二个终端中运行client.py。

输出结果如下：

![1647504955003](C:\Users\liyupi\AppData\Roaming\Typora\typora-user-images\1647504955003.png)



[![第十章 网络基础 - Socket编程](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031015011266.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031015011266.jpg)

## http包

这部分中，我们将学习http包相关知识。http包有四个模块：

- http.client: 这是一个底层HTTP协议客户端
- http.server: 包含基本HTTP服务器类
- http.cookies: 用于实现带cookie的状态管理
- http.cookiejar: 该模块提供cookie持久化

这一部分中，我们将学习http.client和http.server模块。

### http.client模块

我们将来看两种http请求：GET和POST。我们还会来做一个http连接。

首先，我们来探讨一个进行http连接的示例。为此创建一个脚本make_connection.py并在其中编写如下内容：

```python
import http.client

con_obj = http.client.HTTPConnection("https://www.baidu.com", 80, timeout=20)
print(con_obj)

```



运行脚本，我们将会得到如下输出：

```bash
python3 make_connection.py 
<http.client.HTTPConnection object at 0x7fec0a0cd860>
```

在上例中，我们对传入的 URL 的80端口以一个指定的超时时间进行了连接。

下面我们来看 http GET请求方法，使用GET请求方法我们可以看一个获取返回码以及头部列表的示例。创建一个脚本get_example.py并编写如下内容：

```python
import http.client

con_obj = http.client.HTTPSConnection("www.imdb.com")
con_obj.request("GET", "/")
response = con_obj.getresponse()

print("Status: {}".format(response.status))

headers_list = response.getheaders()
print("Headers: {}".format(headers_list))

con_obj.close()

```



运行脚本如下：

```
$ python3 get_example.py
```

得到的结果如下：

```bash
 python3 get_example.py
Status: 200
Headers: [('Content-Type', 'text/html; charset=utf-8'), ('Content-Length', '876142'), ('Connection', 'keep-alive'), ('Server', 'Server'), ('Date', 'Thu, 17 Mar 2022 08:21:54 GMT'), ('x-amz-rid', 'YX43XR09MXT2E653EBWB'), ('set-cookie', 'session-id=134-0833054-9867934; Domain=.imdb.com; Expires=Tue, 01-Jan-2036 08:00:01 GMT; Path=/'), ('set-cookie', 'session-id-time=2082787201l; Domain=.imdb.com; Expires=Tue, 01-Jan-2036 08:00:01 GMT; Path=/'), ('set-cookie', 'next-sid=XbiCYzrj2yiLB0k-HIECA; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly'), ('x-frame-options', 'SAMEORIGIN'), ('x-xss-protection', '1; mode=block'), ('ETag', '"d5e6e-XaHNAvBZk1Bt7MXm1sfU/0p0xzM"'), ('Cache-Control', 'private, no-cache, no-store, max-age=0, must-revalidate'), ('Vary', 'Accept-Encoding,Content-Type,Accept-Encoding,X-Amzn-CDN-Cache,X-Amzn-AX-Treatment,User-Agent'), ('Strict-Transport-Security', 'max-age=47474747; includeSubDomains; preload'), ('Permissions-Policy', 'interest-cohort=()'), ('X-Cache', 'Miss from cloudfront'), ('Via', '1.1 327f036b81d82ab4a19ea85cef81e3be.cloudfront.net (CloudFront)'), ('X-Amz-Cf-Pop', 'LAX50-C3'), ('X-Amz-Cf-Id', 'z-5YiscFQMXbr8-9NIgbWp7Kxvw1xkpEfIZuwUtmZzeukxu70r4dWQ==')]
```

上例中，我们使用了HTTPSConnection，因为该网站以HTTPS协议提供服务。我们根据网站的具体情况可以使用HTTPSConnection或HTTPConnection。我们传入了一个 URL 并通过连接对象查看了其状态。然后，我们获取到了一个header列表。该header列表中包含服务器返回数据类型的相关信息。getheaders() 方法可获取到header列表。

下面我们来看一个POST请求的示例。我们可以使用HTTP POST来向URL post数据。下面创建一个脚本post_example.py并编写如下内容：

```python
import http.client
import json

con_obj = http.client.HTTPSConnection('www.httpbin.org')
headers_list = {'Content-Type': 'application/json'}
post_text = {'text': 'Hello World'}
json_data = json.dumps(post_text)
con_obj.request('POST', '/post', json_data, headers_list)
response = con_obj.getresponse()
print(response.read().decode())

```

运行脚本如下：

```
 python3 post_example.py
```



我们将得到如下的输出：

```bash

{
  "args": {}, 
  "data": "{\"text\": \"Hello World\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "23", 
    "Content-Type": "application/json", 
    "Host": "www.httpbin.org", 
    "X-Amzn-Trace-Id": "Root=1-6232f02b-476c73ae325dc3fa7a1984d1"
  }, 
  "json": {
    "text": "Hello World"
  }, 
  "origin": "222.209.173.181", 
  "url": "https://www.httpbin.org/post"
}
```

上例中，首先我们创建了一个HTTPSConnection对象。然后，我们创建了一个post_text对象，它post 了Hello World。再后，我们编写了一个POST请求，并接收到了响应信息。

### http.server模块

这一部分中，我们将学习http包中的一个模块：http.server模块。该模块定义用于实现HTTP服务端的类。它有两个方法：GET和HEAD。通过使用该模块，我们可以在网络上分享文件。我们可以在任意端口上运行http服务端。确保该端口号大于1024。默认端口号为8000。

可像下面这样使用http.server。

首先进行到选定的目录，并运行如下命令：

```
$ python3 -m http.server 9000
```



这时打开浏览器，在地址栏中键入localhost:9000并按下Enter键。将会得到如下输出：

```bash
python3 -m http.server 9000
Serving HTTP on 0.0.0.0 port 9000 (http://0.0.0.0:9000/) ...
127.0.0.1 - - [17/Mar/2022 00:46:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [17/Mar/2022 00:46:02] code 404, message File not found
127.0.0.1 - - [17/Mar/2022 00:46:02] "GET /favicon.ico HTTP/1.1" 404 -

```

**译者注：**纯命令行服务器可通过 curl localhost:9000进行访问，或通过服务器 IP 地址来进行访问，以示 Alan 演示了这两种效果

## ftplib模块

ftplibj在Python中提供了包含所有FTP协议各类操作的功能。ftplib包含FTP客户端类，以及一些帮助函数。使用该模块我们可以很容易地连接FTP服务器来获取多个文件并对它们进行处理。通过导入ftplib模块，我们就可以使用其中的所有功能了。

这一部分中，我们将讲解如何使用ftplib模块来进行FTP传输。我们会一起来看各类FTP对象。

### 下载文件

这一部分中，我们将学习使用ftplib从另一台机器上下载文件。为此，创建一个get_ftp_files.py脚本并编写如下内容：

```python
import os
from ftplib import FTP

ftp = FTP('FTP域名或IP')
with ftp:
        ftp.login('用户名', '密码')
        ftp.cwd('/home/student/work/')
        files = ftp.nlst()
        print(files)

        # 打印文件
        for file in files:
                print("Downloading..." + file)
                ftp.retrbinary("RETR " + file, open("/home/student/testing/" + file, 'wb').write)

ftp.close()

```

运行脚本如下：

```
$ python3 get_ftp_files.py
```



得到的结果如下：

```
['hello', 'hello.c', 'sample.txt', 'strip_hello', 'test.py']Downloading...helloDownloading...hello.cDownloading...sample.txtDownloading...strip_helloDownloading...test.py
```

**译者注：**要实现以上，首先要确保存在相关文件和目录并安装了 ftp 服务：sudo apt-get install vsftpdu并对/etc/vsftpd.conf进行相应的配置。

上例中，我们使用ftplib模块从主机上获取了多个文件。首先，我们传入了另一台机器的IP地址、用户名和密码。要从主机上获取所有文件，我们使用了ftp.nlst() 函数，并使用ftp.retrbinary()函数将这些文件下载到了本地电脑。

### 使用getwelcome()获取欢迎信息

一旦建立了初始化连接，服务端通常会返回一条欢迎信息。这一消息来自getwelcome()函数，有时会包含声明信息以及与可能与用户相关的帮助信息。

下面我们来看一个getwelcome()的示例，创建一个脚本get_welcome_msg.py并编写如下内容：

```python
from ftplib import FTP

ftp = FTP('FTP的域名或 IP 地址')
ftp.login('用户名', '密码')

welcome_msg = ftp.getwelcome()
print(welcome_msg)

ftp.close()

```



运行脚本如下：

```
$ python3 get_welcome_msg.py220 (vsFTPd 3.0.3)
```



以上代码中，首先我们传入了另一台机器的IP地址、用户名和密码。我们使用了getwelcome()函数来获取初始化连接建立之后的信息。

### 使用sendcmd()函数向服务器发送命令

这一部分中，我们将学习sendcmd()函数。我们可以使用sendcmd()来发送一个简单字符串命令来获取字符串响应。客户端可以发送STAT, PWD, RETR和STOR等FTP命令。ftplib模块中有多个方法能封装这些命令。这些命令可使用sendcmd()或voidcmd()方法进行发送。作为示例，我们将发送一个STAT命令来查看服务端的状态。

创建一个脚本send_command.py并编写如下内容：

```python
from ftplib import FTP

ftp = FTP('FTP服务器域名或 IP 地址')
ftp.login('用户名', '密码')

ftp.cwd('/home/student')
s_cmd_stat = ftp.sendcmd('STAT')
print(s_cmd_stat)
print()

s_cmd_pwd = ftp.sendcmd('PWD')
print(s_cmd_pwd)
print()

ftp.close()

```



运行脚本如下：

```
$ python3 send_command.py
```



| 1    | $ python3 send_command.py |
| ---- | ------------------------- |
|      |                           |

将得到如下输出：

```bash
211-FTP server status:   Connected to ::ffff:192.168.xxx.xxx   Logged in as student   TYPE: ASCII   No session bandwidth limit   Session timeout in seconds is 300   Control connection is plain text   Data connections will be plain text   At session startup, client count was 1   vsFTPd 3.0.3 - secure, fast, stable211 End of status 257 "/home/student" is the current directory
```

以上代码中，我们首先传入了另一台机器的IP地址、用户名和密码。接着，我们使用了sendcmd()向另一台机器发送了STAT命令。然后使用sendcmd()发送PWD命令。

## urllib包

和http相似，urllib也是包含处理 URL 的诸多模块的一个包。urllib模块允许我们通过脚本访问多个网站。我们可以使用这个模块来下载数据、解决数据、修改header等。

urllib有几个不同的模块，列出如下：

- urllib.request: 用于打开和读取URL
- urllib.error: 包含urllib.request抛出的异常
- urllib.parse: 用于解析URL
- urllib.robotparser: 用于解析robots.txt文件

这一部分中，我们将学习使用urllib来打开URL以及如何从URL读取html文件。我们会看一个urllib用法的简单示例。我们将导入urllib.requests。然后将打开的 URL 分配给一个变量，再后，我们会使用a .read()命令来从URL读取数据。

创建脚本url_requests_example.py并在其中编写如下内容：

```python
import urllib.request
 
x = urllib.request.urlopen('https://baidu.com/')
print(x.read())
```



运行脚本如下：

```
$ python3 url_requests_example.py
```

```
b'\n\n<!DOCTYPE html>\n<html\n  xmlns:og="http://ogp.me/ns#"\n  xmlns:fb="http://www.facebook.com/2008/fbml">\n  <head>\n     \n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\n  \n  \n  \n\n  \n  \n  \n\n  <meta name="apple-itunes-app" content="app-id=342792525, app-argument=imdb:///?src=mdot">\n\n\n\n    <script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:\'java\'};</script>\n\n<script>\n  if (typeof uet == \'function\') {\n   uet("bb", "LoadTitle", {wb: 1});\n  }\n</script>\n <script>(function(t){ (t.events = t.events|| {})["csm_head_pre_title"] = new Date().getTime(); })(IMDbTimer);</script>\n   <title>Ratings and Reviews for New Movies and TV Shows - IMDb</title>\n <script>(function(t){ (t.events = t.events || {})["csm_head_post_title"] = new Date().getTime(); })(IMDbTimer);</script>\n<script>\n  if (typeof uet == \'function\') {\n   uet("be", "LoadTitle", {wb: 1});\n  }\n</script>\n<script>\n if (typeof uex == \'function\') {\n   uex("ld", "LoadTitle", {wb: 1});\n }\n</script>\n\n    <link rel="canonical" href="https://www.imdb.com/" />\n    <meta property="og:url" content="http://www.imdb.com/" />\n    <link rel="alternate" media="only screen and (max-width: 640px)" href="https://m.imdb.com/">\n\n<script>\n  if (typeof uet == \'function\') {\n   uet("bb", "LoadIcons", {wb: 1});\n  }\n</script>\n <script>(function(t){ (t.events = t.events || {})["csm_head_pre_icon"] = new Date().getTime(); })(IMDbTimer);</script>\n    <link href="https://m.media-amazon.com/images/G/01/imdb/images/safari-favicon-517611381._CB483525257_.svg" mask rel="icon" sizes="any">\n    <link rel="icon" type="image/ico" href="https://m.media-amazon.com/images/G/01/imdb/images/favicon-2165806970._CB470047330_.ico" />\n...
```

得到的结果如下：

上例中，我们使用了read()方法，它返回一个字节数组。这会以不易于人类阅读的格式打印Imdb首页返回的数据，但我们可以使用HTML解析器来从中提取有用的信息。

### Python urllib响应头

我们可以对响应对象调用 info()函数来获取响应头。它返回一个字典，这样我们还可以从响应中提取指定的头信息数据。创建一个脚本url_response_header.py并编写如下内容：

```
import urllib.request
 
x = urllib.request.urlopen('https://www.imdb.com/')
print(x.info())
```

运行脚本如下：

```
$ python3 url_response_header.py
```



输出如下：

```bash
python3 url_response_header.py
Content-Type: text/html; charset=utf-8
Content-Length: 724285
Connection: close
Server: Server
Date: Thu, 17 Mar 2022 08:40:13 GMT
x-amz-rid: 1X3N861AS5YYGXZMF279
set-cookie: next-sid=LrwYDFn5HF2hJRGVA0im1; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
ETag: "b0d3d-mxkvTG8DhMI/NDsLfTWGv+f+4Jw"
Cache-Control: private, no-cache, no-store, max-age=0, must-revalidate
Vary: Accept-Encoding,Content-Type,Accept-Encoding,X-Amzn-CDN-Cache,X-Amzn-AX-Treatment,User-Agent
Strict-Transport-Security: max-age=47474747; includeSubDomains; preload
Permissions-Policy: interest-cohort=()
X-Cache: Miss from cloudfront
Via: 1.1 507f0bab9a1278d1632051db230c99d4.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: LAX3-C4
X-Amz-Cf-Id: -d8dxvjyWQMwmoK4soC4CkJq1uHkTGReM2Q26VyNHcS_evIZkg2FLg==

```





## 总结

本章中，我们学习了socket，它用于服务端-客户端双向通讯。我们还学习了三个互联网模块：http, ftplib和urllib。http包中有服务端和客户端模块：分别为http.client和http.server。使用ftplib，我们从另一台机器上下载了文件。我们还看了欢迎消息的知识以及发送send命令。

下一章中将涵盖创建和发送邮件的知识。我们会学习消息格式以及添加多媒体内容。同时，我们会学习SMTP, POP和IMAP服务器。

## 课后问题

1.  什么是socket编程？
2. 什么是RPC？
3. 导入用户定义的模块或文件有哪些不同的方式？
4. 列表和元组之间的区别是什么？
5. 字典中的键是否可以重复？
6. urllib, urllib2和requests模块之间的区别是什么？

## 扩展阅读

- ftpliby文档: https://docs.python.org/3/library/ftplib.html
- xmlrpc文档: https://docs.python.org/3/library/xmlrpc.html

# [第十一章 使用Python脚本处理邮件](https://alanhou.org/handling-emails-python-scripting/)

本章中我们将学习如何使用Python脚本来处理邮件。我们会学习到email消息格式。还将探讨使用smtplib发送和接收email。我们将使用Python的email包来发送带有附件和HTML内容的邮件。我们还将学习用于处理邮件的不同协议。

本章中我们将学习如下内容：

- Email消息格式
- 添加HTML和多媒体内容
- POP3和IMAP服务器

## Email消息格式

这一部分中，我们将学习邮件消息格式。邮件消息有三个主要组成部分：

- 接收人的email地址
- 发送者的email地址
- 消息体

消息格式中还有其它组成部分，如标题、email签名和附件。

下面我们来看从Gmail发送普通文本邮件的一个简单示例，通过本例可以学习到如何编写邮件消息以及发送消息。创建一个脚本write_email_message.py并在其中编写如下内容：

```python
import smtplib, getpass
 
# host_name = 'smtp.gmail.com'
host_name = 'smtp.exmail.qq.com'
# host_name = 'smtp.163.com'
port = 465
 
sender = '发件人 email'
receiver = '收件人 email'
password = getpass.getpass()
 
msg = """\
Subject: Test Mail
Hello from Alan !!!"""
 
s = smtplib.SMTP_SSL(host_name, port)
s.login(sender, password)
s.sendmail(sender, receiver, msg)
s.quit()
 
print("Mail sent Successfully")
```

**译者注：**因在墙内以及安全认证机制的原因，可尝试使用其它国内邮箱服务进行替代

运行脚本如下：

```bash
$ python3 write_email_message2.py
 
# 输出结果
Password:
Mail sent Successfully
```

上例中，我们使用了Python的smtplib模块来发送邮件。确保使用Gmail ID向收件人发送消息。变量sender保存发件人的邮箱。对变量password，我们既可以明文输入也可以使用getpass模块弹出提示输入密码。此处我们选择了后者。接着，我们创建了一个变量msg，即我们的实际邮件消息。在其中，我们首先传入了标题，然后添加了想要发送的消息内容。然后在login()中，我们传入了变量sender和password。接着在sendmail()中，我们传入了发件人、收件人和消息文本的相关变量。通过这一流程，我们成功地发出了邮件。

## 添加HTML和多媒体内容

这部分中，我们将来看如何以附件发送多媒体内容，以及如何添加HTML内容。要实现这一功能，我们需要用到Python的email包。

首先，我们来看如何添加HTML内容。创建脚本add_html_content.py来进行实现，编写内容如下：

```python
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
 
# host_name = 'smtp.gmail.com'
host_name = 'smtp.exmail.qq.com'
# host_name = 'smtp.163.com'
port = 465
 
sender = '发件人 email'
receiver = '收件人 email'
password = getpass.getpass()
 
text = MIMEMultipart()
text['Subject'] = 'Test HTML Content'
text['From'] = sender
text['To'] = receiver
 
msg = """\
<html>
        <body>
                <p>Hello there, <br>
                        Good day !!<br>
                        <a href="http://www.imdb.com">Home</a>
                </p>
        </body>
</html>
"""
 
html_content = MIMEText(msg, "html")
text.attach(html_content)
s = smtplib.SMTP_SSL(host_name, port)
print("Mail sent successfully !!")
 
s.login(sender, password)
s.sendmail(sender, receiver, text.as_string())
s.quit()
```

运行脚本，将得到如下输出：

```bash
$ python3 add_html_content2.py
 
# 输出结果：
Password:
Mail sent successfully !!
```

上例中，我们通过Python脚本使用email包在消息中发送了HTML内容。我们创建了一个变量msg用于存储HTML内容。

下面，我们来看如何添加附件以及通过Python脚本来进行发送。为此我们创建一个脚本add_attachment.py，并在其中编写如下内容：

```python
import os, smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass
 
# host_name = 'smtp.gmail.com'
host_name = 'smtp.exmail.qq.com'
# host_name = 'smtp.163.com'
port = 465
 
sender = '发件人 email'
receiver = '收件人 email'
password = getpass.getpass()
 
text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = receiver
 
txt = MIMEText('Sending a sample image.')
text.attach(txt)
f_path = '文件路径'
with open(f_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition',
                'attachment',
                filename=os.path.basename(f_path))
 
text.attach(img)
s = smtplib.SMTP_SSL(host_name, port)
print("Attachment sent successfully !!")
s.login(sender, password)
s.sendmail(sender, receiver, text.as_string())
s.quit()
```

运行脚本，我们将得到如下输出：

```
$ python3 add_attachment.py
 
# 输出结果
Password:
Attachment sent successfully !!
```

上例中，我们以附件向收件人发送图片。我们传入了发件人和收件人的邮件。然后，在f_path中，我们传入了要以附件发送的图片的路径。接着，我们以附件向收件人发送了该图片。

## POP3和IMAP服务器

这部分中，我们将学习通过POP和IMAP服务接收邮件。Python中提供了poplib和imaplib这两个库来通过Python脚本接收邮件。

### 使用poplib库接收email

POP3表示邮局协议（Post Office Protocol）第3版。这一标准协议帮助我们从远程服务器接收邮件到本地机器。POP3的主要优势是它允许我们将邮件下载到本地机器并在线下读取所下载的邮件。

POP3协议用于两个端口：

端口110: 默认非加密端口

端口995: 加密端口

下面我们来看一些示例。首先，我们来看获取一些邮件的示例。为此创建一个脚本number_of_emails.py并在其中编写如下内容：

```
import poplib, getpass
 
# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'
 
username = 'Email地址'
password = getpass.getpass()
 
email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
 
email_obj.user(username)
email_obj.pass_(password)
email_stat = email_obj.stat()
print("New arrived emails are : %s (%s bytes)" % email_stat)
```



运行脚本如下：

```
$ python3 number_of_emails2.py
 
# 输出参考：
Password:
b'+OK QQMail POP3 Server v1.0 Service Ready(QQMail v2.0)'
New arrived emails are : 2793 (1422058063 bytes)
```

输出中我们会得到当前邮箱中的 email 数量。

上例中，我们首先导入了poplib库，它在Python中用于使用POP3协议来安全地接收邮件。然后，我们添加了指定的的邮件服务器以及邮件验证信息，即用户名和密码。然后，我们从服务器打印了响应信息，并向POP3 SSL服务器传输了用户名和密码。在登录后，我们得到了邮箱的数据并在终端中打印了邮件的数量。

下面我们将编写一个脚本来获取最新的邮件。为此创建一个脚本latest_email.py并编写如下内容：

```python
import poplib, getpass
 
# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'
username = 'Email地址'
password = getpass.getpass()
 
email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)
 
print("\nLatest Mail\n")
latest_email = email_obj.retr(1)
print(latest_email[1])
运行脚本如下：
```

运行脚本如下：

```bash
$ python3 latest_email2.py
 
# 输出结果
Password:
b'+OK QQMail POP3 Server v1.0 Service Ready(QQMail v2.0)'
 
Latest Mail
```

输出结果中将包含邮箱中接收到最新邮件。

上例中，我们导入了Python中使用的poplib库来安全地支持POP3协议的邮件接收。在声明指定服务器和用户名与密码后，我们打印出了服务器的响应消息并向POP3 SSL服务器传递了用户名和密码。然后，我们从邮箱获取到了最新的邮件。

下面，我们编写一下脚本来获取所有邮件。为此我们创建一个脚本all_emails.py，并在其中编写如下内容：

```python
import poplib, getpass
 
# pop3_server = 'pop.gmail.com'
pop3_server = 'pop.exmail.qq.com'
username = 'Email地址'
password = getpass.getpass()
 
email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)
 
email_stat = email_obj.stat()
NumofMsgs = email_stat[0]
for i in range(NumofMsgs):
        for mail in email_obj.retr(i+1)[1]:
                print(mail)
```

运行脚本如下：

```
$ python3 latest_email.py
```

输出中，我们将得到邮箱里接收到的所有邮件。

### 使用imaplib库接收email

IMAP表示因特网邮件访问协议（Internet Message Access Protocol）。它用于在本机上访问远程服务器的邮件。IMAP允许同步地在多个客户端访问邮件。IMAP适用于不同地方访问我们邮件的场景。

IMAP协议使用两个端口：

端口143: 默认非加密端口

端口993: 加密端口

下面我们来看使用imaplib库的一个示例。创建一个脚本imap_email.py并在其中编写如下内容：

输出中我们将得到指定文件夹中的所有邮件。

上例中，首先我们导入了imaplib库，它用于在Python中通过IMAP协议安全地接收邮件。然后，我们声明了指定的邮件服务器和用户登录信息，即用户名和密码。再后，我们向IMAP SSL服务器传递了用户名和密码。我们对imap_obj使用了select(‘Inbox’)函数来显示收件箱中的消息。然后我们使用for循环来显示逐一获取的消息。显示消息时我们使用了“美化打印”，即pprint.pprint()函数，因为它格式化对像，向数据流中写入，并将其作为参数传递。最后，我们关闭了连接。

## 总结

本章中，我们学习了如何在Python脚本中编写邮件消息。我们还学习了Python的smtplib模块，它用于通过Python脚本发送和接收邮件。我们同时学习了如何通过POP3和IMAP协议接收邮件。Python提供了poplib和imaplib库来执行这些任务。

下一章中，我们将学习Telnet和SSH。

## 课后问题

1. 什么是POP3和 IMAP？
2. break和continue的作用是什么？举出适当的例子。
3. pprint是什么？
4. 负值索引是什么以及为何使用负值索引？
5. pyc和py文件扩展名的区别是什么？
6. 使用循环生成如下样式
   1010101
   10101
   101
   1

#  第十二章 使用Telnet和SSH远程监控主机


本章中我们将学习如何在服务器通过配置Telnet和SSH来实现基本配置。我们从Telnet模块开始，然后使用推荐的方法来实现相同的配置：使用Python的不同模块来完成SSH连接。我们还将学习telnetlib, subprocess, fabric, Netmiko和paramiko的运行方式。学习本章，读取必须要有网络的基础知识。

本章将涉及如下课题：

- telnetlib()模块
- subprocess.Popen()模块
- SSH之使用fabric模块
- SSH之使用Paramiko库
- SSH之使用Netmiko库

## telnetlib()模块

这部分中，我们将学习Telnet协议，然后使用telnetlib模块对远程服务器进行Telnet的操作。

Telnet是一个允许用户与远程服务器通讯的网络协议。它多由网络管理员用来远程访问和管理设备。要访问设备，在终端中运行Telnet命令并加上远程服务器的IP地址或主机名。

Telnet使用TCP，默认端口为23。要使用，确保在系统中进行了安装，如未安装，运行如下命令来完成安装：

```
sudo apt-get install telnetd
```

通过终端快速运行Telnet命令，可输入如下命令：

```
$ telnet ip_address_of_your_remote_server
```

Python带有一个telnetlib模块，可通过Python脚本执行Telnet函数。在对远程设备或交换机进行Telnet之前，确保进行了适当的配置，如果未配置，我们可以在交换机终端中使用如下命令：

```
configure terminal
enable password 'set_Your_password_to_access_router'
username '设置用户名' password '设置远程访问密码'
line vty 0 4
login local
transport input all
interface f0/0
ip add 'set_ip_address_to_the_router' 'put_subnet_mask'
no shut
end
show ip interface brief
```

**译者注：**以上代码与交换机相关，Ubuntu 开启 Telnet 命令如下：



```
# 安装openbsd-inetd

sudo apt-get -y install openbsd-inetd

# 安装telnetd

sudo apt-get -y install telnetd

# 重启openbsd-inetd

sudo /etc/init.d/openbsd-inetd restart


```

 下面我们来看一个Telnet远程设备的示例。创建脚本telnet_example.py 并在其中编写如下内容： 

```
import telnetlib, getpass, sys
 
HOST_IP = "你的主机 IP 地址"
host_user = input("Enter your telnet username: ")
password = getpass.getpass()
 
t = telnetlib.Telnet(HOST_IP)
# t.read_until(b"Username:")
# t.read_until(b"login:")
t.write(host_user.encode("ascii") + b"\n")
if password:
        t.read_until(b"Password:")
        t.write(password.encode("ascii") + b"\n")
 
t.write(b"enable\n")
t.write(b"enter_remote_device_password\n") # 远程设备密码
t.write(b"conf t\n")
t.write(b"int loop 1\n")
t.write(b"ip add 10.1.1.1 255.255.255.255\n")
t.write(b"int loop 2\n")
t.write(b"ip add 20.2.2.2 255.255.255.255\n")
t.write(b"end\n")
t.write(b"exit\n")
print(t.read_all().decode("ascii"))
```

运行脚本，我们将得到如下输出：

```
$ python3 telnet_example2.py
Enter your telnet username: student
Password:
 
...
```

**译者注：**原文测试对象为交换机，上例中 Alan 使用了 Ubuntu 进行测试，因此需将第一处的读取改为 login，命令执行部分省略，读者可替换为其它 Linux 命令来进行测试。

上例中，我们使用telnetlib模块访问并配置了Cisco交换机。该脚本中，首先我们接收用户输入用户名和密码来初始化远程设备的Telnet连接。一旦建立了连接，我们对远程设备进行了更进一步的配置。Telnet连接后，我们就能够访问远程服务器或设备。但Telnet协议有一个很重要的缺点，那就是所有的数据，包括用户和密码，都以文本的形式在网络中传输，这就可能会带来安全风险。因此，现在很少会使用Telnet，转而由名为Secure Shell的安全协议在替代，常称为SSH。

### SSH

SSH是一个通过远程访问来管理设备或服务器的网络协议。SSH使用公钥加密来保证安全。Telnet和SSH之间的重要区别是SSH使用了加密，也就是说数据在网络上的传输都受保护不被未授权实时拦截。

用户访问远程服务器或设备时应使用SSH客户端。在终端中通过如下命令可安装SSH：

```
sudo apt install ssh
```

同时在用户要远程连接的远程服务器上需要安装和运行SSH服务端。SSH使用TCP协议并且默认运行在22端口上。

我们可以通过终端运行ssh命令如下：

```
ssh host_name@host_ip_address
```

下面我们来学习使用Python中的不同模块来进行SSH连接，如subprocess, fabric, Netmiko和Paramiko。接下来我们就逐一学习这些模块。

## subprocess.Popen()模块

Popen类处理进程的创建和管理。通过使用这一模块，开发人员可处理不太常见的用例。子程序将在新的进程中进行。要在Unix/Linux上执行子程序，该类会使用os.execvp()函数。要在Windows上执行子程序，该类会使用CreateProcess()函数。

下面我们来看subprocess.Popen()的一些有用的参数：

```
class subprocess.Popen(args, bufsize=-1, executable=None,
    stdin=None, stdout=None, stderr=None,
    preexec_fn=None, close_fds=_PLATFORM_DEFAULT_CLOSE_FDS,
    shell=False, cwd=None, env=None, universal_newlines=False,
    startupinfo=None, creationflags=0,
    restore_signals=True, start_new_session=False,
    pass_fds=(), *, encoding=None, errors=None):
```

我们来看下各个参数：

- args：可以是一个程序参数序列或单个字符串。如果args是一个序列，args中的第一项会被执行。如果args是一个字符，它推荐以序列传入args。
- shell：shell参数默认设为False，它指定是否使用shell来执行程序。如果shell的值为True，它推荐以字符串传入args。在Linux中，如果shell=True，shell默认为/bin/sh。如果args是一个字符串，字符串指定通过shell执行的命令。
- bufsize：如果bufsize为0（默认值为0，译者注：Alan 本地3.6和3.7的默认值均为-1），这表示未缓冲，如果bufsize值为1，则表示行缓冲。若bufsize为任意其它正值，使用指定大小的缓冲。如果bufsize为任意其它负值，表示全量缓冲。
- executable：它指定要执行的替代程序。
- stdin, stdout, and stderr：这些参数分别定义标准输入、标准输出和标准错误。
- preexec_fn：设置为可调用对象，会在执行子进程之前调用。
- close_fds：在Linux中，如果close_fds为真，所以除0, 1和2以外的文件描述符都会在子进程执行之前关闭。在Windows中，如果close_fds为真那么子进程将不继承指针。
- env：如果其值不为None，那么映射会定义新进程的环境变量。
- universal_newlines：若值为True，那么stdout和stderr会以新行模式的文本文件打开。

下面我们来看一个subprocess.Popen()的示例。为此创建一个脚本ssh_using_sub.py并在其中编写如下内容：

```
import subprocess, sys
 
HOST="主机用户名@主机 IP"
COMMAND = "ls"
 
ssh_obj = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
 
result = ssh_obj.stdout.readlines()
if result == []:
        err = ssh_obj.stderr.readlines()
        print(sys.stderr, "ERROR: %s" % err)
else:
        print(result)
```

运行脚本，我们将得到如下输出：

```
$ python3 ssh_using_sub2.py
 
# 输出结果（第一次需确认连接）：
The authenticity of host '192.168.0.14 (192.168.0.14)' can't be established.
ECDSA key fingerprint is SHA256:0Yzjg/Ipsb3ilbpABfih6b55ET6ub0c2MkgtbWqwm/8.
Are you sure you want to continue connecting (yes/no)? yes
student@192.168.0.14's password:
[b'testing\n', b'work\n']
```

上例中，首先我们导入了subprocess模块，然后定义了想要建立SSH连接的主机地址。接着我们添加了一条在远程设备上执行的简单命令。一切设置完成后，我们将这一信息传入到subprocess.Popen()函数中。该函数执行定义在函数内的参数来创建与远程设备的连接。在建立了SSH连接之后，我们所定义的命令被执行并返回结果。然后我们在终端中打印出了SSH的返回结果，参见输出。

## SSH之使用fabric模块

Fabric是一个Python库，并且是一个可用于SSH的命令行工具。它用于系统运维及在网上部署应用。我们也可以在SSH之上执行shell命令。

要使用fabric模块，首先我们要使用如下命令来进行安装：

```
pip3 install fabric3
```

下面我们来看一个示例。创建脚本fabfile.py并在其中编写如下内容：

```
from fabric.api import *
 
env.hosts = ["用户名@主机ip"]
env.password = '你的密码'
 
def dir():
        run('mkdir fabric')
        print('Directory named fabric has been created on your host network')
 
def diskspace():
        run('df')
```

运行脚本，我们将得到如下输出：

```
$ fab -f fabfile.py dir
 
# 输出结果：
[student@192.168.0.14] Executing task 'dir'
[student@192.168.0.14] run: mkdir fabric
...
Directory named fabric has been created on your host network
 
Done.
Disconnecting from student@192.168.0.14... done.
```

上例中，首先我们导入了fabric.api模块，然后我们设置了主机名和密码来与网络上主机进行连接。接着，我们设置了通过SSH执行的任务。因此，执行我们的程序不是使用Python3 fabfile.py，而是要使用fab工具，然后上述的任务就会从fabfile.py文件中进行执行。本例中，我们执行了dir，在远程主机上创建了一个名为fabric目录。你也可以在Python文件中添加你自己的任务。它可通过fabric模块中的fab工具来进行执行。

## SSH之使用Paramiko库

Paramiko是一个实现了安全连接远程设备SSHv2协议的库。Paramiko是针对SSH的纯Python接口。

在使用Paramiko之前，确保正确地在系统中进行了安装。如未安装，我们可以通过在终端中运行如下命令来进行安装：

```
sudo pip3 install paramiko
```

下面我们来看一个使用paramiko的示例。对于paramiko连接，我们使用Cisco设备（译者注：Alan 将继续使用本地虚拟机）。Paramiko既支持密码验证也支持密钥对验来对主机进行安全连接。我们的脚本中，会使用密码验证，也即对密码进行检测，如存在则尝试使用用户名/密码来进行验证。在使用SSH连接远程设备或多层交换机时，首先确保对它们进行了适当的配置，若未配置，可使用如下命令在多层交换机中进行基本配置：

```
configure t
ip domain-name cciepython.com
crypto key generate rsa
How many bits in the modulus [512]: 1024
interface range f0/0 - 1
switchport mode access
switchport access vlan 1
no shut
int vlan 1
ip add 'set_ip_address_to_the_router' 'put_subnet_mask'
no shut
exit
enable password 'set_Your_password_to_access_router'
username 'set_username' password 'set_password_for_remote_access'
username 'username' privilege 15
line vty 0 4
login local
transport input all
end
```

**译者注：**有相应设备的朋友请自行验证配置命令

下面，创建一个脚本pmiko.py并在其中编写如下内容：

```
import paramiko, time
 
ip_address = '主机 IP'
usr = '主机用户名'
pwd = '主机密码'
 
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=ip_address, username=usr, password=pwd)
 
print("SSH connection is successfully established with ", ip_address)
 
rc = c.invoke_shell()
for n in range(2, 6):
        print("Creating VLAN " + str(n))
        rc.send("vlan database\n")
        rc.send("vlan " + str(n) + "\n")
        rc.send("exit\n")
        time.sleep(0.5)
 
time.sleep(1)
output = rc.recv(65535)
print(output)
c.close()
```

运行脚本，我们将得到如下输出：

```
$ python3 pmiko.py
SSH connection is successfully established with  192.168.0.14
Creating VLAN 2
Creating VLAN 3
Creating VLAN 4
 
# 测试连接正常，但会报错OSError: Socket is closed，可考虑修改为其它命令
```

上例中，首先我们导入了paramiko模块，然后定义了需要远程连接设备的SSH认证信息。在传入身份信息后，我们创建了一个paramiko.SSHclient()的实例c，它是用于连接远程设备和执行命令或运算的主客户端。SSHClient对象的创建允许我们使用.connect()函数来建立远程连接。然后，我们设置了 paramiko连接的策略，因为默认paramiko.SSHclientu将SSH策略设置为拒绝状态。这会让策略拒绝任何未验证的SSH连接。我们的脚本中通过使用AutoAddPolicy()函数来自动添加主机的密钥而不进行弹出，忽略了这种SSH连接断掉的可能性。我们使用策略来进行测试，但出于安全目的不推荐在生产环境使用。

SSH连接建立之后，我们可以进行想在设备上进行的配置或运算。这里，我们在远程设备上创建了几个虚拟LAN。在创VLAN之后，我们关闭了连接。

## SSH之使用Netmiko库

这部分中我们将学习Netmiko。Netmiko库是Paramiko的一个高级版本。这是一个基于Paramiko的多供应商（multi_vendor）库。Netmiko简化了网络设备的SSH连接及对设备的具体操作。在通过SSH连接远程设备或多层交换机之前，确保对它们进行了相应的配置，若未配置，我们可以使用在Paramiko一节中使用的命令来进行基本配置。

下面我们来看一个示例。创建一个脚本nmiko.py并在其中编写如下代码：

```
from netmiko import ConnectHandler
 
remote_device = {
        'device_type': 'cisco_ios',
        # 'device_type': 'linux',
        'ip': '远程设备 IP地址',
        'username': '用户名',
        'password': '密码'
}
 
remote_connection = ConnectHandler(**remote_device)
# net_connect.find_prompt()
 
for n in range(2, 6):
        print("Creating VLAN " + str(n))
        commands = ['exit', 'vlan database', 'vlan ' + str(n), 'exit']
        output = remote_connection.send_config_set(commands)
        print(output)
 
command = remote_connection.send_command('show vlan-switch brief')
# command = remote_connection.send_command('ls')
print(command)
```

运行脚本，将得到如下输出：

```
~$ python3 nmiko.py
Output:
Creating VLAN 2
config term
Enter configuration commands, one per line. End with CNTL/Z.
server(config)#exit
server #vlan database
server (vlan)#vlan 2
VLAN 2 modified:
server (vlan)#exit
APPLY completed.
Exiting....
server #
..
..
..
..
switch#
Creating VLAN 5
config term
Enter configuration commands, one per line. End with CNTL/Z.
server (config)#exit
server #vlan database
server (vlan)#vlan 5
VLAN 5 modified:
server (vlan)#exit
APPLY completed.
Exiting....
VLAN Name 
 
----
1 default active Fa0/0, Fa0/1, Fa0/2, Fa0/3,
Fa0/4, Fa0/5, Fa0/6, Fa0/7, Fa0/8, Fa0/9, Fa0/10, Fa0/11, Fa0/12, Fa0/13,
Fa0/14, Fa0/15
2 VLAN0002 active
3 VLAN0003 active
4 VLAN0004 active
5 VLAN0005 active
1002 fddi-default active
1003 token-ring-default active
1004 fddinet-default active
1005 trnet-default active
```

**译者注：**以上代码未验证，仅使用ls 代码进行了简单验证

```
$ python3 nmiko.pyfabric	testing work
```

上例中，我们使用了Netmiko库来代替Paramiko进行SSH连接。该脚本中首先我们从Netmiko库中导入了ConnectHandler，用于以SSH连接远程网络设备，在设备字典中进行传入。本例中的字典为remote_device。在建立了连接之后，我们执行了配置命令来使用send_config_set()函数创建一些虚拟LAN。

在使用这类.send_config_set()函数向远程设备传递命令，它自动设置我们的设备为配置模式。在发送配置命令之后，我们还传递了一些简单命令来获取所配置设备的相关信息。

## 总结

本章中我们学习Telnet和SSH。我们还学习不同的Python模块，如 telnetlib, subprocess, fabric, Netmiko和Paramiko，使用它们我们执行了Telnet和SSH连接。SSH使用公钥加密来保持安全，要比Telnet安全的多。

下一章中我们会使用不同的Python库，通过它们来生成图形化用户界面。

## 课后问题

1. 使用是客户端-服务端架构？

2. 如何在Python代码中运行指定操作系统命令？

3. LAN和VLAN之间的区别是什么？

4. 如下代码的输出是什么？

   | 12   | list = ['a', 'b', 'c', 'd', 'e']print(list[10:]) |
   | ---- | ------------------------------------------------ |
   |      |                                                  |

5. 编写一个Python程序来显示日历（提示：使用calendar模块）

6. 编写一个Python程序来对文本文件的行进行计数

## 扩展阅读

- Paramiko文档: https://github.com/paramiko/paramiko
- Fabric文档: http://www.fabfile.org/

# 第十三章 创建图形化用户界面


本章中我们将学习图形化用户界面(GUI) 的开发。Python有很多库来用于制作GUI。我们将学习PyQt5这一Python库来创建GUI。

本章中我们将学习如下课题：

- GUI图形界面简介
- 使用库来创建基于GUI的应用
- 安装和使用 Apache Log Viewer应用

**译者注：**本章涉及到图形化界面，请在自己的 Windows 或 Mac 上进行测试

## GUI图形界面简介

这一部分中我们将学习GUI。Python有很多图形化界面的框架。这一部分中我们来看看PyQt5。PyQt5有不同的图形组件，也称为对象工具，可以在屏幕上显示并与用户进行交互 。这些组件列出如下：

- PyQt5窗口: PyQt5窗口（window）将创建一个简单的app窗口
- PyQt5按钮: PyQt5按钮（button）是在点击时会触发动作的按钮
- PyQt5文本框: PyQt5文本框（textbox）组件允许用户输入文本
- PyQt5落地签: PyQt5标签（label）组件显示一个单行文本或一张图片
- PyQt5组合框 PyQt5组合框（combo box）组件是组合起来的按钮和弹出列表
- PyQt5复选框: PyQt5复选框（ check box）组件是一个可以勾选和取消勾选的选项按钮
- PyQt5单行按钮: PyQt5单选（radio）按钮组件是一个可以勾选和取消勾选的选项按钮。在一组单选按钮中，同时仅能勾选其中的一个按钮
- PyQt5消息框: PyQt5消息框（message box）组件显示消息
- PyQt5菜单: PyQt5菜单（menu）组件提供显示的不同选择
- PyQt5表格: PyQt5表格（table）组件提供了应用的标准表格显示功能，可以构造为多行多列
- PyQt5信号/槽: 信号（signal）会让我们对发生的事件进行响应，插槽（slot）仅仅是信号发生时调用的函数
- PyQt5布局: PyQt5布局（layout）包含多个组件

PyQt5中有一些可以使用的类，划分成不同的模块。这些模块如下：

- QtGui：QtGui包含事件处理、图形化、字体、文本和基础图像类
- QtWidgets：QtWidgets包含创建桌面样式用户界面的类
- QtCore：QtCore包含非图形化功能，如时间、目录、文件、流、URL、数据类型、线程和进程
- QtBluetooth：QtBluetooth包含连接设备和与设备交互的类
- QtPositioning：QtPositioning包含定位的类
- QtMultimedia：QtMultimedia包含API和多媒体内容的类
- QtNetwork：QtNetwork包含网络编程的类
- QtWebKit：QtWebKit包含web浏览器实现的类
- QtXml：QtXml包含XML文件的类
- QtSql： QtSql包含针对数据库的类

GUI由事件来驱动。那么什么是事件呢？事件是表示程序中发生某一件事的信号，例如：菜单选择、鼠标移动或按钮点击。事件是由函数处理或在对象上用户执行某些操作时触发的。监听器会监听事件并会在事件发生时触发事件处理器。

## 使用库来创建基于GUI的应用

下面我们将使用PyQt5库来创建一个简单的GUI应用。这一部分中我们将创建一个简单的窗口。在该窗口中，我们会添加一个按钮和一个标签。在点击按钮后，会在标签中打印一些消息。

首先来看如何创建一个按钮组件。以下代码可创建一个按钮组件：

```
b = QPushButton('Click', self)
```

下面我们现来看如何创建标签。如下代码可创建一个标签：

```
l = QLabel(self)
```

下面我将来看如何创建按钮和标签以及如何在点击该按钮后执行操作。创建脚本print_message.py并在其中编写如下代码：

```python
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
 
 
class simple_app(QWidget):
    def __init__(self):
            super().__init__()
            self.title = 'Main app window'
            self.left = 20
            self.top = 20
            self.height = 300
            self.width = 400
            self.app_initialize()
 
    def app_initialize(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.height, self.width)
        b = QPushButton('Click', self)
        b.setToolTip('Click on the button!!')
        b.move(100, 70)
        self.l = QLabel(self)
        self.l.resize(100, 50)
        self.l.move(100, 200)
        b.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        self.l.setText("Hello World")
 
if __name__ == "__main__":
    app1 = QApplication(sys.argv)
    ex = simple_app()
    sys.exit(app1.exec_())
```

运行脚本，得到的输出如下：

```bash
$ python3 print_message.py
```

[![第十三章 创建图形化用户界面](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031611190573.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031611190573.jpg)

上例中我们导入了需要使用的PyQt5模块。然后创建了应用。QPushButton创建了一个组件，输入的第一个参数的文件会在按钮上显示。然后，我们添加了一个QLabel组件，其中打印一条消息，在点击按钮后会进行打印。接着我们创建了一个函数on_click()，会在点击按钮后执行打印操作。on_click()是我们创建的插槽。

下面我们来看一个盒子布局的示例。创建一个脚本box_layout.py并在其中编写如下内容：

```python
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
 
app1 = QApplication([])
make_window = QWidget()
layout = QVBoxLayout()
 
layout.addWidget(QPushButton('Button 1'))
layout.addWidget(QPushButton('Button 2'))
 
make_window.setLayout(layout)
make_window.show()
 
app1.exec()
```

运行脚本，我们将得到如下输出：

```bash
$ python3 box_layout.py
```

[![第十三章 创建图形化用户界面](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031615093970.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031615093970.jpg)上例中，我们创建了一个盒子布局。其中我们放置了两个按钮。这个脚本仅用于解释例子布局。layout = QVBoxLayout()将创建一个盒子布局。

## 安装和使用 Apache Log Viewer应用

已经有一个Apache Log Viewer日志查看器应用，可从如下链接下载：https://www.apacheviewer.com/download/

下载之后，在电脑上安装该应用。这一应用可对日志的连接状态，IP 地址等信息进行分析。因此，要分析日志文件，我们只需浏览访问日志文件或错误日志文件。在获取文件之后，我们可以对日志文件进行不同的操作，如添加过滤，过滤出access.log中失败连接或过滤出指定 IP 地址等等.

**译者注：**Apache Log Viewer原生支持 Windows 下，下述截图均使用 Windows 虚拟机

以下截图显示Apache日志查看器未添加过滤对access.log的查看：

[![第十三章 创建图形化用户界面](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031700333867.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031700333867.jpg)

以下截图显示在Apache日志查看器中对access.log文件添加了过滤器：

[![第十三章 创建图形化用户界面](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031700372329.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031700372329.jpg)

第一个例子中，我们获取了access log文件并在Apache日志查看器中打开了该文件。我们可以轻易地通过Apache Logs Viewer看出访问日志中打开的各条记录，比如授权与未授权，包含状态、IP 地址、请求等等。但在第二个例子中我们对访问日志文件应用的过滤，这样可以仅查看日志中未授权请求的记录（Alan 此处过滤的为404，未授权过滤出401即可），如上图所示。

## 总结

本章中我们学习了GUI相关知识。我们学习了GUI中使用的组件。还学习了Python中的PyQt5模块。使用PyQt5模块，我们创建了一个简单的应用来在点击按钮后打印消息。

下一章中，我们将学习如何处理Apache日志文件。

## 课后问题

1. 什么是GUI ？
2. Python中的构造函数和析构函数是什么？
3. self的用处是什么？
4. 对比Tkinter, PyQt和wxPython
5. 创建一个Python程序将一个文件中的内容拷贝到另一个文件中
6. 创建一个Python程序读取文本文件，计算指定字母在文件中出现的次数

## 扩展阅读

- Tkinter GUI库文档: https://docs.python.org/3/library/tk.html
- PyQt GUI库文档: https://wiki.python.org/moin/PyQt

# 第十四章 处理Apache和其它的日志文件
本章中我们将学习日志文件相关知识。我们会学习如何解析日志文件。我们还将学习为什么需要在程序中编写异常。解析不同文件的不同方式也很重要。我们会学习错误日志和访问日志的知识。最后我们将学习如何解析其它日志文件。

本章中我们将学习如下内容：

- 解析复杂的日志文件
- 对异常的需要
- 解析不同文件的技巧
- 错误日志
- 访问日志
- 解析其它日志文件

## 解析复杂的日志文件

首先我们将查看复杂日志文件的概念。解析日志文件是个具有挑战性的工作，因为大部分日志文件都是普通文本格式，并且该格式不遵循任何规则。这些文件可被修改而不产生任何警告。用户和开发应用的人员均可决定在日志文件中存储什么样的数据以及存储为什么格式。

在进入解析或修改日志文件配置的示例之前，首先我们需要理解一个典型的日志文件中有什么内容。据此我们了解如何对其进行操作或从中获取信息。我们还可以看看日志文件中的常用术语，这样我们可以使用这些常用术语来获取数据。

通常我们可以看到日志文件中生成的大部内容都是通过应用容器，以及系统访问状态记录（换句话说是日志开启和日志关闭）或通过网络访问系统的记录。因此，通过远程网络访问系统时，这种远程连接的记录会被保存到日志文件中。我们来获取这种情况的示例。我们已有一个带有日志信息的名为access.log的日志文件。

那么我们来创建一个脚本read_apache_log.py并在其中编写如下内容：

| 123456789 | def read_apache_log(logfile):  with open(logfile) as f:    # log_obj = f.read()    # print(log_obj)    for i in range(5):      print(next(f)) if __name__ == '__main__':  read_apache_log('access.log') |
| --------- | ------------------------------------------------------------ |
|           |                                                              |

**译者注：**read()会读取整个文件，为避免刷屏以上做了修改仅读取前5行

运行脚本将得到如下输出：

| 12345678910 | $ python3 read_apache_log.py117.188.30.192 - - [03/Mar/2019:03:14:30 +0000] "GET /category/odoo/page/4/ HTTP/1.1" 200 8336 "http://alanhou.org/category/odoo/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 117.188.30.192 - - [03/Mar/2019:03:14:31 +0000] "GET / HTTP/1.1" 200 9197 "http://alanhou.org/category/odoo/page/4/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 117.188.30.192 - - [03/Mar/2019:03:14:42 +0000] "GET /category/odoo/page/3/ HTTP/1.1" 200 9256 "http://alanhou.org/category/odoo/page/4/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 117.188.30.192 - - [03/Mar/2019:03:14:44 +0000] "GET /category/odoo/page/3/ HTTP/1.1" 200 9251 "http://alanhou.org/category/odoo/page/4/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 117.188.30.192 - - [03/Mar/2019:03:14:45 +0000] "GET / HTTP/1.1" 200 9197 "http://alanhou.org/category/odoo/page/3/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" |
| ----------- | ------------------------------------------------------------ |
|             |                                                              |

上例中，我们创建了一个read_apache_log函数来读取Apache日志文件。其中，我们打开了日志文件并打印出了日志中的信息。在定义了read_apache_log()函数之后，我们传入了Apache日志文件来调用该函数。本例中的日志文件为access.log。

在读取了access.log文件中的各行之后，我们将从日志文件中解析IP地址。创建一个脚本parse_ip_address.py并在其中编写如下内容：

| 1234567891011 | import refrom collections import Counter r_e = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'with open('access.log') as f:  print('Reading Apache log file')  Apache_log = f.read(50000)  get_ip = re.findall(r_e, Apache_log)  no_of_ip = Counter(get_ip)  for k, v in no_of_ip.items():    print('Available IP Address in log file ' + '=> ' + str(k) + ' ' + 'Count ' + '=> ' + str(v)) |
| ------------- | ------------------------------------------------------------ |
|               |                                                              |

**译者注：**如日志文件较大可像 Alan 这样指定仅读取前 xx 字节

运行脚本，我们将得到如下输出：

| 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556 | $ python3 parse_ip_address.pyReading Apache log fileAvailable IP Address in log file => 117.188.30.192 Count => 65Available IP Address in log file => 66.249.79.227 Count => 1Available IP Address in log file => 111.202.101.7 Count => 1Available IP Address in log file => 46.229.168.146 Count => 1Available IP Address in log file => 46.229.168.133 Count => 1Available IP Address in log file => 54.36.148.177 Count => 1Available IP Address in log file => 23.239.1.95 Count => 1Available IP Address in log file => 91.121.155.172 Count => 4Available IP Address in log file => 64.233.172.168 Count => 1Available IP Address in log file => 54.36.148.58 Count => 1Available IP Address in log file => 116.227.9.111 Count => 1Available IP Address in log file => 207.46.13.34 Count => 1Available IP Address in log file => 66.249.79.203 Count => 1Available IP Address in log file => 40.77.167.115 Count => 4Available IP Address in log file => 136.243.70.151 Count => 2Available IP Address in log file => 37.115.190.120 Count => 3Available IP Address in log file => 42.156.137.108 Count => 8Available IP Address in log file => 42.156.136.64 Count => 1Available IP Address in log file => 42.120.161.64 Count => 2Available IP Address in log file => 42.156.138.64 Count => 1Available IP Address in log file => 42.156.139.108 Count => 1Available IP Address in log file => 207.46.13.33 Count => 1Available IP Address in log file => 1.10.187.34 Count => 9Available IP Address in log file => 66.249.79.229 Count => 3Available IP Address in log file => 109.228.56.115 Count => 1Available IP Address in log file => 66.249.79.231 Count => 2Available IP Address in log file => 183.143.43.108 Count => 9Available IP Address in log file => 42.156.137.83 Count => 2Available IP Address in log file => 42.156.139.83 Count => 2Available IP Address in log file => 42.120.161.83 Count => 1Available IP Address in log file => 42.120.160.95 Count => 1Available IP Address in log file => 42.120.161.95 Count => 1Available IP Address in log file => 182.134.133.186 Count => 1Available IP Address in log file => 157.55.39.109 Count => 1Available IP Address in log file => 42.156.136.22 Count => 2Available IP Address in log file => 42.156.137.22 Count => 3Available IP Address in log file => 42.156.138.22 Count => 2Available IP Address in log file => 42.120.160.22 Count => 4Available IP Address in log file => 42.156.139.22 Count => 4Available IP Address in log file => 37.9.87.213 Count => 4Available IP Address in log file => 54.36.149.17 Count => 1Available IP Address in log file => 54.36.148.229 Count => 1Available IP Address in log file => 54.36.149.22 Count => 1Available IP Address in log file => 168.181.61.154 Count => 1Available IP Address in log file => 125.82.16.199 Count => 2Available IP Address in log file => 123.125.71.95 Count => 1Available IP Address in log file => 111.206.198.79 Count => 1Available IP Address in log file => 111.206.198.100 Count => 1Available IP Address in log file => 54.36.149.64 Count => 1Available IP Address in log file => 42.84.39.146 Count => 1Available IP Address in log file => 180.173.173.168 Count => 1Available IP Address in log file => 125.70.190.216 Count => 7Available IP Address in log file => 54.36.148.104 Count => 1Available IP Address in log file => 42.120.160.114 Count => 2 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                              |                                                              |

上例中，我们创建了Apache日志解析器来获取对应的 IP 地址及其对服务器的请求次数。因此，很明确我们无需整个Apache日志文件的所有行，仅需获取日志文件中的 IP 地址。实现这一获取，我们需要定义一个模式来搜索 IP 地址，我们可通过正则表达式来实现。因此我们导入了 re 模块。然后我们导入了Collection模块来代替 Python 的内置数据类型：字典、列表、集合和元组。该模块有特定的容器数据类型。在导入所需模块后，我们使用正则表达式编写了一个模式来匹配指定条件来从日志文件中映射 IP 地址。

在这个匹配模式中，\d为0到9之间的任意数字，\r表示原生字符串。然后，我们打开了名为access.log的Apache日志文件并进行了读取。之后我们对Apache日志文件应用了正则表达式条件，接着使用Collection模块中的Counter 函数来对以re条件获取到的 IP 地址进行计数。最后，正如在输出中所见我们打印出了执行的结果。

## 对异常处理的需要

这一部分中，我们将来看Python编程中对异常处理的需要。正常的程序流包含事件和信号。异常则是在程序中出现了问题。导演可以是任何类型的，如除零错误、导入错误、属性错误或断言错误。这些异常在函数未能正常执行对应任务时发生。发生异常时程序停止执行，并且编译器会进入异常处理进程。异常处理进程包含在try…except代码块中编写的代码。进行异常处理的原因是程序中出现了预期外的情况。

### 分析异常

这一部分中，我们将来了解异常的分析。每个发生的异常都必须要进行处理。我们日志文件也会包含一些异常。如果类似类型的异常获取到了数次，那么程序存在问题，我们应尽快对其进行必要的修改。

运行如下示例：

| 123  | f = open('logfile', 'r')print(f.read())f.close() |
| ---- | ------------------------------------------------ |
|      |                                                  |

运行程序后将会得到如下输出：

| 1234 | Traceback (most recent call last): File "sample.py", line 1, in <module>  f = open('logfile', 'r')FileNotFoundError: [Errno 2] No such file or directory: 'logfile' |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

这个例子中，我们尝试读取一个目录中不存在的文件，结果得到了如上所示的错误。从错误中我们分析出可以使用什么样的解决方案。处理这类错误，我们可以使用异常处理技术。那么让我们来看一个使用异常处理技术来处理异常的示例。

| 123456 | try:  f = open('logfile', 'r')  print(f.read())  f.close()except:  print("File not found. Please check whether the file is present in you directory or not.") |
| ------ | ------------------------------------------------------------ |
|        |                                                              |

此时再运行脚本，将得到如下输出：

| 1    | File not found. Please check whether the file is present in you directory or not. |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

这个示例中，我们尝试读取目录中不存在的文件。但我们在示例中使用了文件异常技术，将代码放在的try: 和except: 代码块中。因此try: 代码块中发生了任何错误或异常，都会跳过该错误并执行except: 代码块中的代码。这里我们只是在except: 代码块是添加了打印语句。因此在运行脚本后，在try: 代码块中发生异常时，会跳过异常并执行except:代码块中的代码。那么except代码块中的打印语句会被执行，我们在以上的输出中可以看到。

## 解析不同文件的技巧

这一部分中，我们将学习用于解析不同文件的技巧。在开始进行实际解析之前，我们必须先读取数据。我们需要了解从哪里获取数据。但是，必须记住所有的日志文件大小都不同。为简化任务，可遵循以下清单：

- 记住日志文件既可以是普通文本也可以是压缩文件
- 所有的日志文件普通文本后缀名为.log，bzip2文件后缀名为log.bz2
- 我们应根据名称来处理一组文件
- 日志文件的所有解析必须合并为单个报告
- 我们使用的工作应从指定目录和不同目录中操作所有文件。子目录中的日志文件也应包含在内

## 错误日志

这一部分中，我们将学习错误日志。错误日志的相关指令如下：

- ErrorLog
- LogLevel

服务器日志的位置和名称由ErrorLog指令设置。这是最重要的日志文件。Apache httpd服务发送其中的信息以及处理过程中生成的记录。在服务器上发生错误时，首先应看看这里。它包含发生问题的细节以及修复的过程。

错误日志写入到一个文件中。在Unix系统中，错误可以服务器发送到syslog或我们通过管道发送到程序。日志记录行首先是消息的日期和时间，第二条是错误严重级别的记录。

LogLevel指定处理通过限制严重级别发送到错误日志的错误。第三条包含生成错误的客户端的信息。这一信息为 IP 地址。下一条为消息本身。它包含服务器配置拒绝客户端访问的信息。服务端随后报告请求文档的文件系统路径。

消息的不同类型可以在错误日志文件中出现。错误日志文件也包含从CGI脚本调试输出。写入到stderr的所有信息都会直接拷贝到错误日志中。

错误日志不可自定义。处理请求的错误日志中的词条会在访问日志中有对应的词条。我们应一直监控测试时问题的错误日志。在Unix系统中，可以运行如下命令来进行查看：

| 1    | $ tail -f error_log |
| ---- | ------------------- |
|      |                     |



## 访问日志

这部分中，我们将学习访问日志的知识。服务器访问日志将记录所有由服务器处理的请求。CustomLog指令控制访问日志的位置和内容。LogFormat指令用于选取日志的内容。

在访问日志中存储信息表示开启日志管理。下一步是分析有助于获取有用的数据统计的信息。 Apache httpd服务有多个版本。这些版本使用一些其它模块和指定来控制访问日志。我们可以配置访问日志的格式。该格式通过format字符串来指定。

### 常用日志格式

这一部分中，我们将学习常用的日志格式。如下语法显示了访问日志的配置：

| 12   | LogFormat "%h %l %u %t \"%r\" %>s %b" nick_nameCustomLog logs/access_log nick_name |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

这个字符串会定义一个别名，然后将别名 与日志格式字符串进行关联。日志格式字符串由百分号指令组成。每个百分号指令告诉服务器记录一个指定信息。这个字符串中可能包含带含义的字符。这些字符在会直接拷贝到日志输出中。

CustomLog指令将借助定义了的别名设置一个新的日志文件。访问日志的文件名相对路径为ServerRoot，除非在前面加了斜杠。

我们前述的配置会在常用日志格式（Common Log Format (CLF)）中写入日志词条。这是一个标准格式，可由很多不同的web服务器生成。很多日志分析程序可读取这一日志格式。

下面我们来看每个百分号指令的含义：

- %h：这向我们显示向web服务器服务器发送请求的客户端 IP 地址。如果开启了HostnameLookups，那么服务器会确定主机名并在 IP 地址处记录它。
- %l：这一条用于表示请求未能获得的信息（**译者注：**该信息为客户端identd确定，通常无法获取，显示为-）。
- %u：这是请求文档的用户 ID。同一值由CGI脚本在REMOTE_USER环境变量中传递。
- %t：这一条用于检测服务器处理请求结束的时间。格式如下：
  [day/month/year:hour:minute:second zone]

对于day参数接收两个数字。对于month，我们需要定义三个字母。对于year，因为年有4个字符，我们需要接收4个数字。在day, month和year之后，我们需要为小时、分钟和秒分别接收两个数字。

- \”%r\”：用于请求行，由客户端放在双引号中给定。这一请求行有一些有用的信息。请求客户端使用GET，协议使用HTTP。
- %>s：这一条定义客户端的状态码。状态码非常重要且有用，因为它表示客户端向服务端发送的请求是否成功。
- %b：这一条定义返回客户端时对象的总大小。这一总大小不包含响应头的大小。

## 解析其它日志文件

我们系统中还有包含Apache日志文件在内的不同日志文件。在Linux发行版中，日志文件在根文件系统的/var/log/文件夹下，如下所示：

[![第十四章 处理Apache和其它的日志文件](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031712064485.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019031712064485.jpg)

**译者注：**从这个截图开始的数据均直接来自原书

在以上截图中，我们可以很容易的看到针对不同操作的不同日志文件格式（例如，验证日志文件auth.log，系统日志文件syslog和内核日志kern.log）。如前所示，我们对Apache日志文件执行了操作，我们也可以对其它本地日志文件执行同样的操作。下面来看一个解析另一种日志文件的示例。创建一个脚本simple_log.py并编写如下内容：

| 123456 | f=open('/var/log/kern.log','r')lines = f.readlines()for line in lines:  kern_log = line.split()  print(kern_log)f.close() |
| ------ | ------------------------------------------------------------ |
|        |                                                              |

运行脚本，我们将得到如下输出：

| 12345678910 | student@ubuntu:~$ python3 simple_log.py # 输出内容：['Dec', '26', '14:39:38', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815378.2891]', 'device', '(ens33):', 'state', 'change:', 'prepare', '->', 'config', '(reason', "'none')", '[40', '50', '0]']['Dec', '26', '14:39:38', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815378.2953]', 'device', '(ens33):', 'state', 'change:', 'config', '->', 'ip-config', '(reason', "'none')", '[50', '70', '0]']['Dec', '26', '14:39:38', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815378.2997]', 'dhcp4', '(ens33):', 'activation:', 'beginning', 'transaction', '(timeout', 'in', '45', 'seconds)']['Dec', '26', '14:39:38', 'ubuntu', 'NetworkManager[795]:', '<info>','[1545815378.3369]', 'dhcp4', '(ens33):', 'dhclient', 'started', 'with', 'pid', '5221']['Dec', '26', '14:39:39', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815379.0008]', 'address', '192.168.0.108']['Dec', '26', '14:39:39', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815379.0020]', 'plen', '24', '(255.255.255.0)']['Dec', '26', '14:39:39', 'ubuntu', 'NetworkManager[795]:', '<info>', '[1545815379.0028]', 'gateway', '192.168.0.1'] |
| ----------- | ------------------------------------------------------------ |
|             |                                                              |

上例中，首先我们创建了一个简单文件对象f，在其中以只读模式打开了kern.log文件。然后，我们对文件对象应用了readlines()函数来在for循环中逐行读取文件的数据。然后我们对内核日志文件的每一行应用了split()函数并对整个文件使用了print函数，通过输出可以查看。

和读取内核日志文件一样，我们还可以对它执行其它操作，下面我们就将执行一些操作。下面我们将通过索引来访问内核日志文件中的内容。通过split日志可进行实现，因为它将文件中的信息分割为另一个迭代。那么我们来看这一情况的一个示例。创建脚本simple_log1.py并在其中编写如下脚本内容：

| 12345 | f=open('/var/log/kern.log','r')lines = f.readlines()for line in lines:  kern_log = line.split()[1:3]  print(kern_log) |
| ----- | ------------------------------------------------------------ |
|       |                                                              |

运行脚本，我们将得到如下输出：

| 123456789101112131415 | student@ubuntu:~$ python3 simple_log1.py # 输出结果：['26', '14:37:20']['26', '14:37:20']['26', '14:37:32']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38']['26', '14:39:38'] |
| --------------------- | ------------------------------------------------------------ |
|                       |                                                              |

上例中，我们仅仅是在split函数后添加了[1:3]，换句话说，添加了切片。序列的子序列称为切片，这一运算提取的子序列称为切片内容。本例中，我们使用方括号[ ]来作为切片运算符并在其中放置了两个整型值，以冒号:进行分隔。运算符[1:3]返回序列第一到第三个元素这部分内容，包含第一个但排除最后一个。在对序列进行切片时，我们获取的子序列总是与操作的原序列的类型相同，但是列表或元组的元素可以是任意类型，与我们应用的切片无关，获取的切片仍为列表或元组。因此在对日志文件应用切片后，我们获取的结果如上面的输出所示。

## 总结

本章中，我们学习了如何处理不同类型的日志文件。我们还学习了解析复杂的日志文件以及在处理文件时对异常处理的需要。解析日志文件的技巧有助于平滑地执行解析。我们还学习了错误日志和访问日志。

下一章中，我们将学习SOAP和REST通讯。

## 课后问题

1. Python中运行时和编译时的异常有什么区别？
2. 什么是正则表达式？
3. 研究Linux中的head, tail, cat和awk命令
4. 编写一个Python程序将一个文件的内容追加到另一个文件中
5. 编写一个Python程序来倒序读取文件内容
6. 以下表达式的输出是什么？
   1. re.search(r’C\Wke’, ‘C@ke’).group()
   2. re.search(r’Co+kie’, ‘Cooookie’).group()
   3. re.match(r'<.*?>’, ‘<h1>TITLE</h1>’).group()

## 扩展阅读

- Python日志: https://docs.python.org/3/library/logging.html
- 正则表达式: https://docs.python.org/3/howto/regex.html
- 异常处理: https://www.pythonforbeginners.com/error-handling/python-try-and-except

# 第十五章 SOAP和REST API通讯



本章中我们将来看SOAP和REST API的基础知识。我们还会看实现SOAP和REST API的Python库。我们将学习Zeep库来使用SOAP和requests来使用REST API。我们将学习操作JSON数据的知识。接着看一个操作JSON数据的简单示例，比如将JSON字符串转化成Python对象和将Python对象转换成JSON字符串。

本章中我们将学习如下内容：

- SOAP是什么？
- 通过库使用SOAP
- 什么是RESTful API？
- 通过标准库使用RESTful API
- 操作JSON数据

## SOAP是什么？

SOAP是简单对象访问协议（Simple Object Access Protocol）。SOAP是一各路标准通讯协议，允许使用不同操作系统的进程。它通过HTTP和XML进行通讯，是一个web服务技术。SOAP API主要设计用于创建、更新、删除和还原数据的操作。SOAP API使用Web服务描述语言来描述web服务所提供的功能。SOAP描述所有功能和数据类型。它建立一个基于XML的协议。

### 通过库使用SOAP

这一部分中，我们将学习SOAP的Python库。有用于SOAP的不同库列举如下：

- SOAPpy
- Zeep
- Ladon
- suds-jurko
- pysimplesoap

这些是Python中用于SOAP API的库。这一部分中我们仅会学习Zeep库。

要使用Zeep的功能，我们首先需要安装它。在终端中运行如下命令来安装Zeep：

| 1    | $ pip3 install Zeep |
| ---- | ------------------- |
|      |                     |

Zeep模块是用于WSDL（Web Services Description Language）的文档。它生成服务的代码和文档并提供SOAP服务端的编程接口。lxml库用于解析XML文档。

下面我们来看一个示例。创建脚本soap_example.py并在其中编写如下代码：

| 12345 | import zeep w = 'http://www.soapclient.com/xml/soapresponder.wsdl'c = zeep.Client(wsdl=w)print(c.service.Method1('Hello', 'World')) |
| ----- | ------------------------------------------------------------ |
|       |                                                              |

运行脚本，我们将得到如下输出：

| 1234 | $ python3 soap_example.py # 输出结果：Your input parameters are Hello and World |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

上例中，我们首先导入了zeep模块。第一步传入了网站名。然后创建了一个zeep客户端对象。前面使用的WSDL定论了一个简单的Method1函数，由zeep通过client.service.Method1来提供。它接收两个参数并返回一个字符串。

## 什么是RESTful API？

REST表示表述性状态传递（Representational State Transfer）。RESTful API有一种在web服务开发中使用的通讯方法。它是可作为因特网上不同系统间通信的通道的一类web服务。是一个应用接口，用于使用HTTP请求来对数据进行GET, PUT, POST和DELETE。

REST的优点是它使用更少的代码，非常适合在因特网上使用。REST API 使用统一接口。所有的资源通过GET, PUT, POST和DELETE运算处理。REST API使用GET来获取资源、PUT来更新资源或修改资源的状态，使用POST来创建资源，并使用DELETE来删除资源。系统使用REST API来达到更快的性能和可靠性。

REST API独立处理每一个请求。客户端向服务端发送的请求必须包含可用于了解请求内容的所有信息。

### 通过标准库使用RESTful API

这一部分，我们将学习如何使用RESTful API。要进行使用，我们需要用到Python的requests和JSON模块。下面我们来看一个示例。首先，我们将使用requests模块来从API获取信息。会用到GET和POST请求。

我们必须先安装requests库，方法如下：

| 1    | $ pip3 install requests |
| ---- | ----------------------- |
|      |                         |

下面我们会看一个示例。创建脚本rest_get_example.py并在其中编写如下内容：

| 1234 | import requests req_obj = requests.get('https://www.imdb.com/news/top?ref_=nv_tp_nw')print(req_obj) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

运行该脚本，我们将得到如下输出：

| 1234 | $ python3 rest_get_example.py # 输出结果：<Response [200]> |
| ---- | ---------------------------------------------------------- |
|      |                                                            |

上例中，我们导入了requests模块来获取请求。接着我们创建了一个请求对象req_obj，并从想要获取请求之处指定了一个链接。然后，我们进行了打印。所得到的输出是状态码200，表示访问成功。

下面我们将看一个POST请求示例。POST请求用于向服务器发送数据。创建一个脚本rest_post_example.py并在其中编写如下内容：

| 12345678 | import requests, json url_name = 'http://httpbin.org/post'data = {"Name": "John"}data_json = json.dumps(data)headers = {'Content-Type': 'application/json'}response = requests.post(url_name, data=data_json, headers=headers)print(response) |
| -------- | ------------------------------------------------------------ |
|          |                                                              |

运行该脚本，我们将得到如下输出：

| 1234 | $ python3 rest_post_example.py # 输出结果：<Response [200]> |
| ---- | ----------------------------------------------------------- |
|      |                                                             |

在上例中，我们学习了POST请求。首先我们导入了必要的模块requests和JSON。然后传入了URL。同时，我们以字典格式输出想要进行post的数据。然后，我们传入了headers。接着使用POST请求进行了post。我们得到的输出是状态码是200， 是一个成功状态码。

## 操作JSON数据

这一部分中，我们将学习JSON数据。JSON表示JS对象简谱（JavaScript Object Notation）。JSON是一个数据交换格式。它将Python对象以JSON字符串编码，并将JSON字符串解码为Python对象。Python有一个JSON模块来格式化JSON输出。它带有对JSON序列化和反序列化的函数。

- json.dump(obj, fileObj)：这一函数会将对象序列化为JSON格式流
- json.dumps(obj)：这个函数会序列化对象为JSON格式字符串
- json.load(JSONfile)：该函数会将JSON文件反序列化为Python对象
- json.loads(JSONfile)：该函数会将字符串类型JSON文件反序列化为Python对象

这还有两个用于编码和解码的类，列出如下：

- JSONEncoder：用于将Python对象转换为JSON格式
- JSONDecoder：用于将JSON格式文件转换为Python对象

下面我们来看使用JSON模块的一些示例。首先我们来看从JSON到Python的转换。创建一个脚本json_to_python.py 并在其中编写如下内容：

| 123456 | import json j_obj = '{"Name": "Harry", "Age": 26, "Department": "HR"}'p_obj = json.loads(j_obj)print(p_obj["Name"])print(p_obj["Department"]) |
| ------ | ------------------------------------------------------------ |
|        |                                                              |

运行脚本，我们将得到如下输出：

| 12345 | $ python3 json_to_python.py # 输出结果：HarryHR |
| ----- | ----------------------------------------------- |
|       |                                                 |

上例中，我们编写了将一个JSON字符串转换为Python对象的一段代码。json.loads()函数用于将JSON字符串转换为Python对象。

下面我们来看如何将Python对象转换为JSON。创建一个脚本python_to_json.py并在其中编写如下代码：

| 12345 | import json emp_dict1 = '{"Name":"Harry", "Age":26, "Department":"HR"}'json_obj = json.dumps(emp_dict1)print(json_obj) |
| ----- | ------------------------------------------------------------ |
|       |                                                              |

运行脚本，我们将得到如下输出：

| 1234 | $ python3 python_to_json.py # 输出结果："{\"Name\":\"Harry\", \"Age\":26, \"Department\":\"HR\"}" |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

上例中，我们将一个Python对象转换为了一个JSON字符串。 json.dumps()函数用于这一转换。

下面，我们来看如何将不同类型的Python对象转换为JSON字符串。创建一个脚本python_object_to_json.py并在其中编写如下内容：

| 12345678910111213141516171819202122232425262728293031 | import json python_dict = {"Name": "Harry", "Age":26}python_list = ["Numbai", "Pune"]python_tuple = ("Basketball", "Cricket")python_str = ("hello_world")python_int = (150)python_float = (59.66)python_T = (True)python_F = (False)python_N = (None) json_obj = json.dumps(python_dict)json_arr1 = json.dumps(python_list)json_arr2 = json.dumps(python_tuple)json_str = json.dumps(python_str)json_num1 = json.dumps(python_int)json_num2 = json.dumps(python_float)json_t = json.dumps(python_T)json_f = json.dumps(python_F)json_n = json.dumps(python_N) print("json object : ", json_obj)print("json array1 : ", json_arr1)print("json array2 : ", json_arr2)print("json string : ", json_str)print("json number1 : ", json_num1)print("json number2` : ", json_num2)print("json true` : ", json_t)print("json false` : ", json_f)print("json null` : ", json_n) |
| ----------------------------------------------------- | ------------------------------------------------------------ |
|                                                       |                                                              |

运行脚本，我们将得到如下输出：

| 123456789101112 | $ python python_object_to_json.py # 输出结果：('json object : ', '{"Age": 26, "Name": "Harry"}')('json array1 : ', '["Numbai", "Pune"]')('json array2 : ', '["Basketball", "Cricket"]')('json string : ', '"hello_world"')('json number1 : ', '150')('json number2` : ', '59.66')('json true` : ', 'true')('json false` : ', 'false')('json null` : ', 'null') |
| --------------- | ------------------------------------------------------------ |
|                 |                                                              |

上例中，我们使用json.dumps()函数将不同类型的Python对象转换成了JSON字符串。在转换之后，Python列表和元组被转换成了数据。整型和浮点型数字被看作JSON数字类型。下表中显示Python与JSON的对应转换：

| **Python** | **JSON** |
| ---------- | -------- |
| dict       | Object   |
| list       | Array    |
| tuple      | Array    |
| str        | String   |
| int        | Number   |
| float      | Number   |
| True       | true     |
| False      | false    |
| None       | null     |

## 总结

本章中，我们学习了SOAP API和RESTful API。还学习了用于SOAP API的Python库zeep和用于REST API的库requests。同时学习了如何处理JSON数据，如将JSON转换为Python及其反向转换。

下一章中，我们将学习网页爬取和实现这一任务的Python库。

## 课后问题

1. SOAP 和 REST API之间的区别是什么？

2. json.loads和json.load之间的区别是什么？

3. JSON是否支持所有平台？

4. 以下代码片断的输出是什么？

   | 12   | boolean_value = Falseprint(json.dumps(boolean_value)) |
   | ---- | ----------------------------------------------------- |
   |      |                                                       |

5. 以下代码片断的输出是什么？

   | 12   | weird_json = '{"x": 1, "x": 2, "x": 3}'json.loads(weird_json) |
   | ---- | ------------------------------------------------------------ |
   |      |                                                              |

## 扩展阅读

- JSON文档: https://docs.python.org/3/library/json.html
- REST API相关信息: https://searchmicroservices.techtarget.com/definition/REST-representational-state-transfer

# 第十六章  网络抓取 – 从网站上提取有用的信息



本章中我们将学习网页抓取的相关知识。我将还将学习Python中用于从网站上提取信息的beautifulsoup库。

本章主要涉及如下课题：

- 什么是网页抓取？
- 数据提取
- 从维基百科提取信息

## 什么是网页抓取？

网页抓取是一种用于从网站上提取信息的技术。这一技术用于将非结构化数据转化为结构化数据。

网页抓取的用法是从网站是提取数据。提取的数据存储在本地系统的文件中，也可以存储在数据库的数据表中。网页抓取软件使用HTTP或浏览器直接访问万维网（WWW）。这是由网页爬虫或机器人实现的自动化过程。

爬取网页包含获取页面，然后提取数据。网页爬虫获取页面。爬虫是网页抓取中不可或缺的一个组件。在获取页面之后，就需要进行提取了。我们可以对页面进行搜索、解析、保存数据到数据表以及重构页面。

## 数据提取

这一部分，我们来看实际的数据提取过程。Python的beautifulsoup库可执行数据提取任务。我们还将使用Python的requests库。

首先，我们应安装这两个库。运行如下命令来安装requests和beautifulsoup库：

| 12   | $ pip3 install requests$ pip3 install beautifulsoup4 |
| ---- | ---------------------------------------------------- |
|      |                                                      |



### requests库

requests库的用处是以可读的格式使用Python脚本中的HTTP。我们可以在Python中使用requests库下载页面。requests库有不同的请求类型。这里我们将学习GET请求。GET请求用于从web服务器获取信息。web请求下载指定网页的HTML内容。每次请求都有一个状态码。状态码返回我们向服务器发送的每次请求。这些状态码向我们表明所做请求状况的信息。状态码的类型列举如下：

- 200: 表明一切正常并在结果时返回结果
- 301: 表明在域名切换或端点（endpoint）发生变化时服务器重定向到不同的端点
- 400:表明请求有问题
- 401: 表明请求未授权
- 403: 表明在尝试访问禁止访问的资源
- 404: 表明尝试访问的资源在服务器上不存在

### beautifulsoup库

beautifulsoup是一个Python库，用于网页抓取。它带有搜索、导航、变更等简单易用的方法。是一个用于从网页上提取数据的工具集。

下面，要在我们的脚本中使用beautifulsoup的功能，需要使用import语句导入这两具库。我们将来看一个解析网页的示例。这里我们来解析一个IMDb网站的热门新闻面。创建一个脚本parse_web_page.py并在其中加入如下的内容：

| 1234567 | import requestsfrom bs4 import BeautifulSoup page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')parse_obj = BeautifulSoup(page_result.content, 'html.parser') print(parse_obj) |
| ------- | ------------------------------------------------------------ |
|         |                                                              |

运行脚本，我们将得到如下输出：

| 12345678910111213141516171819202122232425 | $ python3 parse_web_page.py # 输出结果：<!DOCTYPE html> <html xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://ogp.me/ns#"><head><meta charset="utf-8"/><meta content="IE=edge" http-equiv="X-UA-Compatible"/><meta content="app-id=342792525, app-argument=imdb:///?src=mdot" name="apple-itunes-app"/><script type="text/javascript">var IMDbTimer={starttime: new Date().getTime(),pt:'java'};</script><script>  if (typeof uet == 'function') {   uet("bb", "LoadTitle", {wb: 1});  }</script>...<div id="servertime" time="33"></div><script>  if (typeof uet == 'function') {   uet("be");  }</script></body></html> |
| ----------------------------------------- | ------------------------------------------------------------ |
|                                           |                                                              |

上例中，我们获取了一个页面并使用beautifulsoup对其进行解析。首先我们导入了requests和beautifulsoup模块。然后，使用GET请求来获取 URL 并将该 URL 赋值给变量page_result。接着我们创建了beautifulsoup对象parse_obj。这一对象接收从requests获取的page_result.content作为参数，然后使用 html.parser对页面进行了解析。

下面我们将从class 和a标签中提取内容。要执行这一操作，打开浏览器并在想要提取的内容上右击，向下滚动可以看到Inspect（查看元素）的选项。点击它可以获取到class名。传入程序中并运行脚本。为此创建一个脚本extract_from_class.py并在其中编写如下内容：

| 12345678 | import requestsfrom bs4 import BeautifulSoup page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')parse_obj = BeautifulSoup(page_result.content, 'html.parser') top_news = parse_obj.find(class_='news-article__content')print(top_news) |
| -------- | ------------------------------------------------------------ |
|          |                                                              |

运行脚本，我们将得到如下输出：

| 1234 | $ python3 extract_from_class.py<div class="news-article__content">        For a second weekend in a row <a href="/company/co0008970/">Disney</a> and <a href="/company/co0051941/">Marvel</a>'s <a href="/title/tt4154664/">Captain Marvel</a> topped the weekend box office as it has now posted over $760 million worldwide in just twelve days in global release. Overall, the weekend ended up topping the same weekend last year for a second straight week as both <a href="/title/tt6428676/">Wonder Park</a> and <a href="/title/tt6472976/">Five Feet Apart</a> outperformed expectations with their opening weekend performance. At the same time <a href="/company/co0173285/">Lionsgate</a>'s release of <a href="/company/co0325194/">Pantelion</a>'s <a href="/title/tt9019352/">No Manches Frida 2</a> delivered a top ten finish from just 472 theaters, topping Focus's disappointing release of <a href="/title/tt5968394/">Captive State</a>, which struggled in its debut in over 2,500 locations. Disney's <a href="/title/tt4154664/">Captain Marvel</a> topped the weekend box office for a second weekend in a row, delivering an estimated $69.3 million sophomore frame, dipping -54.8% and outperforming the -56% average second weekend dip for a film in the Marvel Cinematic Universe. This pushes the film's domestic cume over $266 million after just ten days in domestic release.      </div> |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

上例中，首先我们导入了requests和beautifulsoup模块。然后，我们创建了一个请求对象并传入URL。接着，我们创建了一个beautifulsoup对象parse_obj。该对象从接收请求的page_result.content作为参数，并使用html.parser解析页面。然后我们使用了beautifulsoup的find()方法来从news-article__content这个 class中获取内容。

下面，我们来看一个从指定标签中提取内容的示例。在这个示例中，我们将从<a>标签中提取内容。创建一个脚本extract_from_tag.py并在其中编写如下内容：

| 123456789 | import requestsfrom bs4 import BeautifulSoup page_result = requests.get('https://www.imdb.com/news/top?ref_=nv_nw_tp')parse_obj = BeautifulSoup(page_result.content, 'html.parser') top_news = parse_obj.find(class_='news-article__content')top_news_a_content = top_news.find_all('a')print(top_news_a_content) |
| --------- | ------------------------------------------------------------ |
|           |                                                              |

运行脚本，我们将得到如下输出：

| 12   | $ python3 extract_from_tag.py[<a href="/company/co0008970/">Disney</a>, <a href="/company/co0051941/">Marvel</a>, <a href="/title/tt4154664/">Captain Marvel</a>, <a href="/title/tt6428676/">Wonder Park</a>, <a href="/title/tt6472976/">Five Feet Apart</a>, <a href="/company/co0173285/">Lionsgate</a>, <a href="/company/co0325194/">Pantelion</a>, <a href="/title/tt9019352/">No Manches Frida 2</a>, <a href="/title/tt5968394/">Captive State</a>, <a href="/title/tt4154664/">Captain Marvel</a>] |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

上例中，我们从<a>标签中提取了内容。我们使用了find_all()方法来从news-article__content这个class中提取了所有<a>标签中的内容。

## 从维基百科提取信息

这一部分中，我们将来看一个从维基百科获取舞蹈形式列表的示例。我们将列出所有的传统印度舞。创建一个脚本extract_from_wikipedia.py并在其中编写如下内容：

| 1234567891011 | import requestsfrom bs4 import BeautifulSoup page_result = requests.get('https://en.wikipedia.org/wiki/Portal:History')parse_obj = BeautifulSoup(page_result.content, 'html.parser') h_obj = parse_obj.find(class_='hlist noprint')h_obj_a_content = h_obj.find_all('a') print(h_obj)print(h_obj_a_content) |
| ------------- | ------------------------------------------------------------ |
|               |                                                              |

运行脚本，输出内容如下：

| 123456789101112131415161718 | $ python3 extract_from_wikipedia.py<div class="hlist noprint" id="portals-browsebar" style="text-align: center;"><dl><dt><a href="/wiki/Portal:Contents/Portals" title="Portal:Contents/Portals">Portal topics</a></dt><dd><a href="/wiki/Portal:Contents/Portals#Human_activities" title="Portal:Contents/Portals">Activities</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Culture_and_the_arts" title="Portal:Contents/Portals">Culture</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Geography_and_places" title="Portal:Contents/Portals">Geography</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Health_and_fitness" title="Portal:Contents/Portals">Health</a></dd><dd><a href="/wiki/Portal:Contents/Portals#History_and_events" title="Portal:Contents/Portals">History</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Mathematics_and_logic" title="Portal:Contents/Portals">Mathematics</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Natural_and_physical_sciences" title="Portal:Contents/Portals">Nature</a></dd><dd><a href="/wiki/Portal:Contents/Portals#People_and_self" title="Portal:Contents/Portals">People</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Philosophy_and_thinking" title="Portal:Contents/Portals">Philosophy</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Religion_and_belief_systems" title="Portal:Contents/Portals">Religion</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Society_and_social_sciences" title="Portal:Contents/Portals">Society</a></dd><dd><a href="/wiki/Portal:Contents/Portals#Technology_and_applied_sciences" title="Portal:Contents/Portals">Technology</a></dd><dd><a href="/wiki/Special:RandomInCategory/All_portals" title="Special:RandomInCategory/All portals">Random portal</a></dd></dl></div>[<a href="/wiki/Portal:Contents/Portals" title="Portal:Contents/Portals">Portal topics</a>, <a href="/wiki/Portal:Contents/Portals#Human_activities" title="Portal:Contents/Portals">Activities</a>, <a href="/wiki/Portal:Contents/Portals#Culture_and_the_arts" title="Portal:Contents/Portals">Culture</a>, <a href="/wiki/Portal:Contents/Portals#Geography_and_places" title="Portal:Contents/Portals">Geography</a>, <a href="/wiki/Portal:Contents/Portals#Health_and_fitness" title="Portal:Contents/Portals">Health</a>, <a href="/wiki/Portal:Contents/Portals#History_and_events" title="Portal:Contents/Portals">History</a>, <a href="/wiki/Portal:Contents/Portals#Mathematics_and_logic" title="Portal:Contents/Portals">Mathematics</a>, <a href="/wiki/Portal:Contents/Portals#Natural_and_physical_sciences" title="Portal:Contents/Portals">Nature</a>, <a href="/wiki/Portal:Contents/Portals#People_and_self" title="Portal:Contents/Portals">People</a>, <a href="/wiki/Portal:Contents/Portals#Philosophy_and_thinking" title="Portal:Contents/Portals">Philosophy</a>, <a href="/wiki/Portal:Contents/Portals#Religion_and_belief_systems" title="Portal:Contents/Portals">Religion</a>, <a href="/wiki/Portal:Contents/Portals#Society_and_social_sciences" title="Portal:Contents/Portals">Society</a>, <a href="/wiki/Portal:Contents/Portals#Technology_and_applied_sciences" title="Portal:Contents/Portals">Technology</a>, <a href="/wiki/Special:RandomInCategory/All_portals" title="Special:RandomInCategory/All portals">Random portal</a>] |
| --------------------------- | ------------------------------------------------------------ |
|                             |                                                              |



## 总结

本章中，我们学习了什么是网页抓取。还学习了两个用于从网页提取数据的库。同时从维基百科上提取了信息。

下一章中，我们将学习数据的收集和报表。我们将学习NumPy模块、数据可视化以及使用图表来展示数据。

## 课后问题

1. 什么是网页抓取？
2. 什么是网页爬虫？
3. 你是否能在登录页后爬取数据？
4. 你是否能爬取 Twitter？
5. 是否是爬取 JavaScript 页面？若可以，如何爬取？

## 扩展阅读

- Urllib文档：https://docs.python.org/3/library/urllib.html
- Mechanize: https://mechanize.readthedocs.io/en/latest/
- Scrapemark: https://pypi.org/project/scrape/
- Scrapy: https://doc.scrapy.org/en/latest/index.html

[喜欢 (4)](javascript:;)赏分享 (0)

# 第十七章 数据收集及报表



本章中我们将学习科学计算中统计所使用的高级Python库。我们会学习Python的NumPy, Pandas, Matplotlib和Plotly模块。我们将学习到数据可视化的技术以及如何对收集的数据绘图。

本章中主要学习如下课题：

- NumPy模块
- Pandas模块
- 数据可视化

## NumPy模块

NumPY是一个可对数组进行有效运算的Python模块。NumPy是一个Python科学计算的基础包。这个包常被用作Python的数据分析。NumPy数组是一个多值网格。

在Terminal中使用如下命令安装NumPy：

```
$ pip3 install numpy
```



我们将使用numpy库来对numpy数组执行运算。下面我们来看如何创建一个numpy数组。为此创建一个脚本simple_array.py并在其中编写如下内容：

```
import numpy as np
 
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print(my_list1, type(my_list1))
print(my_array1, type(my_array1))
```



运行脚本，我们将得到如下输出：

```
python3 simple_array.py
[1, 2, 3, 4] <class 'list'>
[1 2 3 4] <class 'numpy.ndarray'>
```



上例中，我们以np导入了numpy库来使用numpy的功能。然后我们创建了一个简单的列表，将其使用np.array()函数将其转化为数组。最后，我们打印了numpy数组及其类型，来学习常规的数组和numpy数组之间的不同。

上例是一个简单的一维数组。下面我们来看一个多维数组的示例。为此我们需要创建另一个列表，让我们一起来看另一个示例吧。创建一个名为mult_dim_array.py的脚本并在其中编写如下内容：

```python
import numpy as np
 
my_list1 = [1,2,3,4]
my_list2 = [11,22,33,44]
 
my_lists = [my_list1, my_list2]
my_array = np.array(my_lists)
print(my_lists, type(my_lists))
print(my_array, type(my_array))
```

运行脚本，我们将得到如下输出：

```bash
$ python3 mult_dim_array.py
[[1, 2, 3, 4], [11, 22, 33, 44]] <class 'list'>
[[ 1  2  3  4]
 [11 22 33 44]] <class 'numpy.ndarray'>
```

上例中我们导入了numpy模块。然后我们创建了两个列表：my_list1和my_list2。接着我们创建了另一个列表（my_list1和my_list2）的列表，并在该列表（my_lists）上应用了np.array()函数，将其存储在一个名为my_array的对象中。最后我们打印出了这个numpy数组。

下面我来看可作用于数组的更多操作。我们将学习如何在知道数组的大小以及我们所创建的数组的数据类型，这里我们使用created array。为此我们仅需应用shape()函数并来获取数组的大小，以及使用dtype() 函数来了解所创建数组的数据类型。下面就来看一个示例。创建一个名为size_and_dtype.py的脚本并在其中编写如下内容：

```python
import numpy as np
 
my_list1 = [1,2,3,4]
my_list2 = [11,22,33,44]
 
my_lists = [my_list1, my_list2]
my_array = np.array(my_lists)
print(my_array)
 
size = my_array.shape
print(size)
 
data_type = my_array.dtype
print(data_type)
```

运行脚本，我们将得到如下输出：

```
$ python3 size_and_dtype.py
[[ 1  2  3  4]
 [11 22 33 44]]
(2, 4)
int64
```

上例中，我们以my_array.shape对数组应用了shape函数来获取数据的大小。输出结果为(2, 4)。然后我们以my_array.dtype对数组应用了dtype函数，得到的输出为int64。

下面我们来看一些特殊数组的示例。

首先，我们会使用np.zeros() 创建一个所值为0的数组，如下所示：

```python
$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> np.zeros(5)
array([0., 0., 0., 0., 0.])
>>>
```

在创建所有值为0的数据之后，我们将使用numpy的 np.ones()函数来创建所有值为1的数组，如下所示：

```python
>>> np.ones((5,5))
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])
>>>
```

np.ones((5,5)) 创建一个 5*5的数组，其中的值均为1。

下面，我们将使用numpy的np.empty()函数创建一个空数组，如下所示：

```
>>> np.empty([2,2])
array([[1.13224202e+277, 1.03103236e-259],
       [0.00000000e+000, 2.78134232e-309]])
>>>
```



np.empty()并不会像np.zeros()函数那样将数组中的值设为0。因此，速度可能会更快。此外，它要求用户手动在数组中输入所有值，所以使用时要格外小心。

下面我们来看如何使用np.eye() 函数来创建单位数组（identity array），它将生成主对角线的值全为1的数组，如下所示：

```
>>> np.eye(5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>>
```

下面我们来看range函数，用于使用numpy中的np.arange()来创建数组，如下所示：

```
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

np.arange(10)函数创建一个0-9的数组。我们定义了范围10，，因此数组的索引值以0开始。

### 使用数组和标量

这一部分中，我们来看使用NumPy对数组进行不同的算术运算。首先要创建一个多维数组，如下：

```
$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> from __future__ import division
>>> arr = np.array([[4,5,6],[7,8,9]])
>>> arr
array([[4, 5, 6],
       [7, 8, 9]])
>>>
```

这里我们导入了numpy模块来使用numpy的功能，接着我们导入了__future__模块来处理浮点数。然后我们创建了一个二维数组，来对其执行不同的操作。

下面我们来看数组上的一些算术运算。首先，我们将学习数组的乘法，如下所示：

```
>>> arr * arr
array([[16, 25, 36],
       [49, 64, 81]])
>>>
```

以上的乘法运算中，我们对arr数组自身进行了相乘来获取到一个相乘后的数组。我们也可以对两个不同的数组进行相乘。

下面我们来看数组的减法运算，如下所示：

```
>>> arr - arr
array([[0, 0, 0],
       [0, 0, 0]])
>>>
```

如前例所示，我们仅仅使用了一个 – 运算符来进行两个数组的减法。在数组相减之后，我们获得了结果数组，如以上代码所示。

下面我们来看含有标量数组的算术运算。我们来看一些示例：

```
>>> 1 / arr
array([[0.25      , 0.2       , 0.16666667],
       [0.14285714, 0.125     , 0.11111111]])
>>>
```

上例中，我们使用1除以了我们的数组并得到了输出。记住，我们导入了__future__ 模块，有助于这类运算，来处理数组中的浮点值。

下面我们来看numpy数组的指数运算，如下所示：

```
>>> arr ** 3
array([[ 64, 125, 216],
       [343, 512, 729]])
>>>
```

上例中，我们对数组进行了立方运算，得到了一个数组中各项值立方的输出。

### 数组索引

数组的索引是通过将数组作为索引来实现的。对于索引数组，原数组的拷贝会被返回。numpy数组可使用除元组外的其它序列或通过使用其它数组来索引。数组的最后一个元素可使用-1作为索引，倒数第二的索引可使用-1，以此类推。

因此，要在数组上执行索引运算，首先我们创建一个numpy数组，我们将使用range()函数来创建一个数组，如下所示：

```
$ python3
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> arr = np.arange(0,16)
>>> arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
>>>
```

上例中，我们创建了一个范围为16的数组arr，即0-15。

下面我们将对数组arr执行一个不同的索引运算。首先，我们来获取数组中指定索引的值：

```
>>> arr[7]
7
>>>
```

上例中，我们通过索引值访问了数组，在向数组arr传递了索引值之后，索引返回了值7，这也正是我们所传入的具体索引数。

在获取具体索引的值之后，我们将获取一个范围内的值。我们来看如下示例：

```
>>> arr[2:10]
array([2, 3, 4, 5, 6, 7, 8, 9])
>>> arr[2:10:2]
array([2, 4, 6, 8])
>>>
```

上例中，首先我们访问了数组并获取一个范围内的值(2-10)。结果以array([2, 3, 4, 5, 6, 7, 8, 9])显示了输出。第二个例子中的arr[2:10:2]，实际上是说以步长间隔2访问范围在2-10的数组。这类索引的语法为arr[_start_value_:_stop_value_:_steps_]。因此，第二条命令的输出结果为array([2, 4, 6, 8])。

我们还可以获取一个数组中从指定索引直到结尾的值，如下例所示：

```
>>> arr[5:]
array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
>>>
```

如我们在上例中所见，我们访问了数组中从第5个开始直到结果的值。结果得到了输出array([ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])。

下面我们来看看numpy数组的切片。在切片中，实际上我们获取了原数组的某一部分并将其存储在指定的数组名中。一起来看一个示例：

```
>>> arr_slice = arr[0:8]
>>> arr_slice
array([0, 1, 2, 3, 4, 5, 6, 7])
>>>
```

上例中，我们获取了原数组的一个切片。结果我们获取了数组的一个切片，值为0,1,2,…..,7。我们还要将更新付下赋给数组的切片。我们来看一个示例：

```
>>> arr_slice[:] = 29
>>> arr_slice
array([29, 29, 29, 29, 29, 29, 29, 29])
>>>
```

上例中，我们设置了数组切片中的所有值为29。但对数组切片赋值的一个重点是赋给切版的值同样会被赋给原数组。

下面我们来看在向数组切片赋值后原数组的效果：

```
>>> arr
array([29, 29, 29, 29, 29, 29, 29, 29,  8,  9, 10, 11, 12, 13, 14, 15])
>>>
```

下面我们来看另一个运算：即数组的复制。数组的切片和拷贝的区别在于在进行数组的切片时，所做的修改会应用到原数组上。在获取数组的拷贝时，则给出一个原数组的明确的拷贝。因此，对数组拷贝所应用的改变不会影响到原数组。让我们来看一个复制数组的示例：

```
>>> cpying_arr = arr.copy()
>>> cpying_arr
array([29, 29, 29, 29, 29, 29, 29, 29,  8,  9, 10, 11, 12, 13, 14, 15])
>>>
```

上例中，我们仅仅接收了一个原数组的拷贝。使用array_name.copy()来实现拷贝，输出为原数组的一个拷贝。

#### 二维数组的索引

二维数组是一个数组的数组。这一数组中的数据元素的位置通常引用两个索引值而非单个，分别表示数据表格的行和列。下面我们将做该类型数组的索引。

下面我们来看一个二维数组的示例：

```
>>> td_array = np.array(([5,6,7],[8,9,10],[11,12,13]))
>>> td_array
array([[ 5,  6,  7],
       [ 8,  9, 10],
       [11, 12, 13]])
>>>
```

上例中，我们创建了一个名为td_array的二维数组。在创建数组后，我们打印出了数组。下面我们还将通过索引获取td_array中的值。一起来看通过索引获取值的示例：

```
>>> td_array[1]
array([ 8,  9, 10])
>>>
```

上例中，我们访问了数组中索引为1的值并获取了输出。在这类索引中，访问值时我们获取到了整个数组。除了获取整个数组外，我们还可获取指定值。来看一个示例：

```
>>> td_array[1,0]
8
>>>
```

上例中，我们通过传入两个值行和列访问了td_array。正如在输出中所见，我们获得的值为8。

我们还可以另一种方式创建二维数组。首先，设置一个长度更大的二维数组。这里我们设置为10。那么我们创建一个值全部为0的示例数组，然后在其中填入值。示例如下：

```
>>> td_array = np.zeros((10, 10))
>>> td_array
array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
>>> for i in range(10):
...     td_array[i] = i
...
>>> td_array
array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [2., 2., 2., 2., 2., 2., 2., 2., 2., 2.],
       [3., 3., 3., 3., 3., 3., 3., 3., 3., 3.],
       [4., 4., 4., 4., 4., 4., 4., 4., 4., 4.],
       [5., 5., 5., 5., 5., 5., 5., 5., 5., 5.],
       [6., 6., 6., 6., 6., 6., 6., 6., 6., 6.],
       [7., 7., 7., 7., 7., 7., 7., 7., 7., 7.],
       [8., 8., 8., 8., 8., 8., 8., 8., 8., 8.],
       [9., 9., 9., 9., 9., 9., 9., 9., 9., 9.]])
>>>
```

上例中，我们创建了一个10*10的二维数组。

下面我人们再对其做一些特别的索引，如下例所示：

```
>>> td_array[[1,3,5,7]]
array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [3., 3., 3., 3., 3., 3., 3., 3., 3., 3.],
       [5., 5., 5., 5., 5., 5., 5., 5., 5., 5.],
       [7., 7., 7., 7., 7., 7., 7., 7., 7., 7.]])
>>>
```

上例中，我们获取了指定的索引值，因此得到以上输出。

### 通用数组函数

能用函数对numpy数组中的每一个元素执行操作。下面我们来看一个在数组上执行多个通用函数的示例。首先，我们获取数组的平方根。创建一个名为sqrt_array.py的脚本并在其中编写如下内容：

```python
import numpy as np
 
array = np.arange(16)
print("The Array is : ", array)
Square_root = np.sqrt(array)
print("Square root of given array is : ", Square_root)
```

运行脚本，我们将得到如下输出：

```
$ python3 sqrt_array.py
The Array is :  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
Square root of given array is :  [0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.         3.16227766 3.31662479
 3.46410162 3.60555128 3.74165739 3.87298335]
```

上例中，我们使用numpy的一个函数range创建了一个简单的数组。然后我们对所生成的数组应用于sqrt()函数，来获取数组的平方根。在获取数组的平方根之后，我们将对数组应另一个能用方法，即指数函数exp()。我来看一个示例。创建一个名为expo_array.py的脚本并编写如下内容：

```
import numpy as np
 
array = np.arange(16)
print("The array is : ", array)
exp = np.exp(array)
print("Exponential of give array is : ", exp)
```

运行脚本，我们将得到如下输出：

```
$ python3 expo_array.py
The array is :  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
Exponential of give array is :  [1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
 2.98095799e+03 8.10308393e+03 2.20264658e+04 5.98741417e+04
 1.62754791e+05 4.42413392e+05 1.20260428e+06 3.26901737e+06]
```

上例中，我们使用numpy的range函数创建了一个简单的数组。然后对所生成的数组应用了exp()函数来获取数组的指数（以 e为底的自然指数）。

## Pandas模块

这一部分中，我们将学习pandas模块。pandas模块提供了快速灵活的数组结构，设计用于处理结构化和时间序列数据。pandas模块用于数据分摊。pandas建立在NumPy 和Matplotlib等包的基础上，让我们可以进行大部的分析和可视化。要使用这一模块，首先需要进行导入。

首先通过运行如下命令来安装示例中所需的包：



```
$ pip3 install pandas
$ pip3 install matplotlib
```

这里，我们将来看一些使用pandas模块的示例。我们会学习两具数据 结构：序列（Series）和数据帧（DataFrames）。我们还将看看如何使用pandas从csv文件中读取数据。

### 序列

pandas序列是一个一维数组。其中可包含任意数据类型。它的标签被称为索引。下面我们来看一个不声明索引的序列和一个声明了索引的序列。首先，我们来看一个未声明索引的序列。创建一个名为series_without_index.py的脚本并在其中编写如下内容：

```
import pandas as pd
import numpy as np
 
s_data = pd.Series([10,20,30,40], name = 'numbers')
print(s_data)
```

运行脚本，我们将得到如下输出：

```
$ python3 series_without_index.py
0    10
1    20
2    30
3    40
Name: numbers, dtype: int64
```

上例中，我们学习未声明索引的序列。首先我们导入了两个模块：pandas和numpy。然后我创建了存储序列数据的对象s_data。在这个序列中，我们创建一个列表而没有声明索引，传入了name属性来为列表赋予一个名称，然后我们打印出了数据。在输出中，左列是数据的索引。即便我们没有传入索引，pandas还是会暗自赋予一个索引。这个索引从0开始。在数据列的下面是序列的名称以及值的数据类型。

下面，我们来看一个声明了索引的序列示例。这里我们还将执行索引和切片操作。为此创建一个名为series_with_index.py的脚本并在其中编写如下内容：

```
import pandas as pd
import numpy as np
 
s_data = pd.Series([10, 20, 30, 40], index = ['a', 'b', 'c', 'd'], name = 'numbers')
print(s_data)
print()
print('The data at index 2 is: ', s_data[2])
print('The data from range 1 to 3 are:\n', s_data[1:3])
```

运行脚本，我们将得到如下输出：

```
$ python3 series_with_index.py
a    10
b    20
c    30
d    40
Name: numbers, dtype: int64
 
The data at index 2 is:  30
The data from range 1 to 3 are:
 b    20
c    30
Name: numbers, dtype: int64
```

上例中，我们在 index 属性中为数据传入了索引值。输出中左列为我们传入的索引值。

In the preceding example, we provided an index value for our data in the index attribute. In the output, the left column is the index values that we provided.

### 数据帧

这一部分中，我们针学习pandas的数据帧（DataFrames）。数据帧是二维的带标签数据结构，它有不同列并可以包含不同的数据类型。数据帧与SQL表格或电子表格类似。在使用pandas时数据帧是最常用的对象。

下面我们来看一个从csv文件读入数据帧的示例。那么我们应该在系统中要有一个 csv 文件。如果你的系统中暂没有csv文件，创建一个名为employee.csv,的文件如下：

```
Id, Name, Department, Country
101, John, Finance, US
102, Mary, HR, Australia
103, Geeta, IT, India
104, Rahul, Marketing, India
105, Tom, Sales, Russia
```

下面，我我将读取这一csv文件到数据帧中。为此创建一个名为read_csv_dataframe.py的脚本并在其中编写如下内容：

```
import pandas as pd
 
file_name = 'employee.csv'
df = pd.read_csv(file_name)
print(df)
print()
print(df.head(3))
print()
print(df.tail(1))
```

运行脚本，我们将得到如下输出：

```
$ python3 read_csv_dataframe.py
    Id    Name  Department     Country
0  101    John     Finance          US
1  102    Mary          HR   Australia
2  103   Geeta          IT       India
3  104   Rahul   Marketing       India
4  105     Tom       Sales      Russia
 
    Id    Name  Department     Country
0  101    John     Finance          US
1  102    Mary          HR   Australia
2  103   Geeta          IT       India
 
    Id  Name  Department  Country
4  105   Tom       Sales   Russia
```

上例中，首先我们创建了一个名为employee.csv的csv文件。我们使用pandas模块创建了一个数据帧。目的是将csv文件读取到数据帧中。接着我们创建了一个df对象，并将我们读取的csv内容赋给它。然后我们打印了数据帧。这里，我们使用了head()和tail()方法来获取指定行数的数据。我们指定了head(3)，表示要打印数据的前三行。还指定了tail(1)，表示要打印数据的最后一行。

## 数据可视化

数据可视化是一个描述努力以视觉方式理解数据意义的词语。这一部分，我们将来看以下的数据可视化技术：

- Matplotlib
- Plotly

### Matplotlib

Matplotlib是一个Python中的数据可视化库，仅需使用几行代码通过它可生成图表、直方图、能量光谱（power spectra）、柱状图、 error charts,、散点图等。Matplotlib通常会简化工作并完成一些非常复杂的图表。

要在Python程序中使用matplotlib，首先要安装matplotlib，在终端中执行如下命令来安装matplotlib：

```
pip3 install matplotlib
```

我们还应安装一个包tkinter来实现图形化展示。使用如下命令来进行安装：

```
$ sudo apt install python3-tk
```

**译者注：**Mac 安装包中已自动集成，无需单独安装

既然已经在系统中安装了matplotlib，就让我们来看一些示例吧。在画图表时，有两个重要的组成部分：figure和数轴。figure是作为画图窗口的容器。可以有不同类型的独立数值。数轴是是我们绘制数据及相关联的标签的区域。数轴包含 x 轴 和 y 轴。

下面，我们来看一些matplotlib的示例。首先看一个简单的示例。创建一个名为simple_plot.py的脚本并在其中编写如下内容：

```
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(0, 5, 10)
y = x**2
plt.plot(x, y)
plt.title('sample plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
```

运行脚本如下：

```
$ python3 simple_plot.py
```

输出结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032102130991.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032102130991.png)

上例中，我们导入了两具模块，matplotlib和numpy来对数据进行可视化以及分别创建数组x和y。然后，我们以及plt.plot(x,y)绘制了两个数据。接着我们使用xlabel(), ylabel()和title()函数对绘图添加了标题和标签，并使用plt.show()函数来显示绘图。因为我们是在Python中使用Matplotlib，要记得在最后一行添加plt.show()来显示绘图。

下面我们将创建两个数组来在绘图中显示两个曲线，并对这两个曲线应用样式。在下例中，我们将使用ggplot样式来绘图。ggplot是一个用于声明式地创建图形的系统，它基于图形的语法。要画图我们只需传入数据，然后告诉ggplot如何映射变量以及使用哪些图形原语（primitive），它就会处理剩下的细节。大多情况下，我们以ggplot()的样式开始。

创建一个名为simple_plot2.py的脚本并在其中编写如下内容：

```
import matplotlib.pyplot as plt
from matplotlib import style
 
style.use('ggplot')
 
x1 = [0,5,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,16,8]
 
plt.subplot(2,1,1)
plt.plot(x1, y1, linewidth=3)
plt.title('sample plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.subplot(2,1,2)
plt.plot(x2, y2, color='r', linewidth=3)
plt.xlabel('x2 axis')
plt.ylabel('y2 axis')
 
plt.show()
```

运行脚本如下：

```
$ python3 simple_plot2.py
```

得到的结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/201903210321184.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/201903210321184.png)

上例中，首先我们导入了所需的模块，然后我们使用了ggplot样式来绘图。我们创建了两组数组：即x1, y1 和 x2, y2。然后使用了subplot函数plt.subplot()，因为它允许我们在同一个画布上绘制不同的图形。如果想要在不同的画布上绘制图形的话，也可以使用plt.figure()来代替plt.subplot()。

下面我们来看使用plt.figure()函数来绘制数组并使用Matplotlib来保存生成的图像。我们能以savefig()方法进行不同格式的保存，如png, jpg, pdf等等。我们会将前面的图像保存在名为my_sample_plot.jpg的文件中。下面我们来看一个示例。为此创建一个名为simple_plot3.py的脚本并在其中编写如下内容：

```
import matplotlib.pyplot as plt
from matplotlib import style
 
style.use('ggplot')
 
x1 = [0,5,10]
y1 = [12,16,6]
x2 = [6,9,11]
y2 = [6,16,8]
 
plt.figure(1)
plt.plot(x1, y1, color='g', linewidth=3)
plt.title('sample plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.savefig('my_sample_plot1.jpg')
 
plt.figure(2)
plt.plot(x2, y2, color='r', linewidth=3)
plt.xlabel('x2 axis')
plt.ylabel('y2 axis')
plt.savefig('my_sample_plot2.jpg')
 
plt.show()
```

运行脚本如下：

```
$ python3 simple_plot3.py
```

输出结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032104054525.jpg)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032104054525.jpg)

**译者注：**执行时如出现如下报错，请安装 Pillow，因 Matplotlib 默认并不支持jpg 格式：

```
ValueError: Format 'jpg' is not supported (supported formats: eps, pdf, pgf, png, ps, raw, rgba, svg, svgz)
 
# 安装 pillow
pip3 install pillow
```

上例中，我们使用了plt.figure()函数来在不同的画布上进行绘制。然后，我们使用了plt.plot()函数。该函数有不同的参数，用于绘图时使用。在上例中，我使用了x1, x2, y1和 y2等参数。这些分别是用于绘图的象限点。

然后我们使用了color参数来为画的线传入具体的颜色，第三个参数我们使用了linewidth，用于给定画线的宽度。接着，我们使用了savefig()方法来以指定的格式保存了图像。你可以在运行Python脚本的当前目录中查看图像（如未指定保存目录）。

我们还可以通过直接访问目录来打开图片，或者使用如下的方法来使用matplotlib打开所生成的图片。下面我们来看一个打开所保存图像的示例。为此创建一个名为open_image.py的脚本并在其中编写如下内容：

```
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
plt.imshow(mpimg.imread('my_sample_plot1.jpg'))
plt.show()
```

运行脚本如下：

```
$ python3 open_image.py
```

我们将得到如下输出：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032105285917.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032105285917.png)下例中，我们使用了Matplotlib的imshow()函数来打开所保存的图像。

下面我们来看绘图的不同类型。Matplotlib允许我们创建不同类型的绘图来处理数组中的数据，比如直方图、散点图、柱状图等等。选取不同类型的绘图取决于数据可视化的目的。下面我们就来看一些示例。

#### 直方图

这类图有助于我们查看数值数据的分布，这是平均值和中位数所无法体现的。我们将使用hist()方法来创建一个简单的直方图。下面来看一个创建简单直方图的示例。为此创建一个名为histogram_example.py的脚本，并在其中编写如下内容：

```
import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.randn(500)
plt.hist(x)
plt.show()
```

运行脚本如下：

```
$ python3 histogram_example.py
```

得到的输出结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/20190321145705100.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/20190321145705100.png)上例中，我们使用numpy创建了一个随机数数组。然后使用plt.hist()方法对这一数值数据进行绘图。

#### 散点图

这类图以一个点状集合展示数据。它提供了一种便捷地视觉查看数值关联的方式。它还有助于理解多个变量之间的关系。我们将使用scatter()方法来将数据绘制到散点图中。在散点图中，点的位置取决于x和y轴的值，即二维数据值，因此数据集中的每个值都是横向或纵向维度上的一个位置。我们来看一个散点图的示例。创建一个名为scatterplot_example.py的脚本，并在其中编写如下内容：

```
import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(-2,2,100)
y = np.random.randn(100)
colors = np.random.rand(100)
plt.scatter(x,y,c=colors)
plt.show()
```

运行脚本如下：

```
$ python3 scatterplot_example.py
```

我们将得到如下输出：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032115051476.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032115051476.png)

上例中，我们获取了x和y的值。然后使用plt.scatter()方法绘制这些值来获取x和y值的散点图。

#### 柱状图

柱状图是将数据展现为矩形状态的图表。我们可以进行纵向或横向的绘制。创建一个名为bar_chart.py的脚本并在其中编写如下内容：

```
import matplotlib.pyplot as plt
from matplotlib import style
 
style.use('ggplot')
 
x1 = [4,8,12]
y1 = [12,16,6]
x2 = [5,9,11]
y2 = [6,16,8]
 
plt.bar(x1,y1,color='g',linewidth=3)
plt.bar(x2,y2,color='r',linewidth=3)
plt.title('Bar plot')
 
plt.xlabel('x axis')
plt.ylabel('y axis')
 
plt.show()
```

运行脚本如下：

```
$ vi bar_chart.py
```

运行结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/201903220807292.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/201903220807292.png)

上例中，我们有两组值：x1, y1和x2, y2。在获取了数值数据之后，我们使用了plt.bar()方法来对现有数据进行了柱状图绘制。

对数据绘图有很多种技术。其中，有一些技术或数据可视化的方法使用matplotlib，我们已经看到了。我们还可以使用其它的数据可视化工具来执行这类操作：如plotly。

### Plotly

Plotly是Python中的一个交互的开源图形库。这一绘图库提供了30多种图表类型，包含科学图表、3D图、数据分析图、金融图表等等。

在Python中使用plotly，首先要在系统中安装它。在Terminal中运行如下命令来安装plotly：

```
$ pip3 install plotly
```

我们可以在线及离线使用plotly。在线使用的话需要有一个plotly账号，然后可以在Python中设置账号信息：

```
plotly.tools.set_credentials_file(username='Username', api_key='APIkey')
```

要离线使用plotly，我们应使用plotly函数：plotly.offline.plot()。

这一部分中我们将离线使用plotly。下面我们来看一个简单的示例。为此创建一个名为sample_plotly.py的脚本并在其中编写如下内容：

```
import plotly
from plotly.graph_objs import Scatter, Layout
 
plotly.offline.plot({
    "data": [Scatter(x=[1, 4, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="plotly_sample_plot")
})
```

运行以上脚本sample_plotly.py如下：

```
 python3 sample_plotly.py
```

我们将得到如下结果：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032208412087.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032208412087.png)

上例中，我们导入了plotly模块，然后设置了离线使用plotly。在其中传入了参数来进行绘图。在例子中，我们使用了一些参数：data和layout。在data参数中，我们为scatter函数定义了数组x和y，来使用值分别在x轴和y轴上绘图。然后我们使用了layout参数，在其中定义了layout函数来传入了图形的标题。以上程序执行的输出被保存为HTML文件，并在默认浏览器中打开。这一HTML文件和我们的脚本在同一目录。

下面我们来看一些可视化数据的不同类型的图表。首先从散点图开始。

#### 散点图

创建一个名为scatter_plot_plotly.py的脚本并在其中编写如下的内容：

```
import plotly
import plotly.graph_objs as go
import numpy as np
 
x_axis = np.random.randn(100)
y_axis = np.random.randn(100)
 
trace = go.Scatter(x=x_axis, y=y_axis, mode='markers')
data_set = [trace]
plotly.offline.plot(data_set, filename='scatter_plot.html')
```

运行脚本如下：

```
$ python3 scatter_plot_plotly.py
```

我们将得到如下输出：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032209341778.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032209341778.png)

上例中，我们导入了plotly，然后使用numpy创建了随机数据，因此在脚本中导入了numpy模块。在生成数据集后，我们创建了一个名为trace的对象并将数值数据插入该对象来绘制散点图。最后，我们将trace对象中的数据放到plotly.offline.plot()函数中，来获取数据的散点图。和第一个示例图一样，这个示例的输出也以HTML格式保存并在默认的浏览器中显示。

#### 线状散点图

我们还可以创建信息量列大的绘图，如线状散点图。下面来看一个示例。创建一个名为line_scatter_plot.py 的脚本并在其中编写如下内容：

```
import plotly
import plotly.graph_objs as go
import numpy as np
 
x_axis = np.linspace(0, 1, 50)
y0_axis = np.random.randn(50)+5
y1_axis = np.random.randn(50)
y2_axis = np.random.randn(50)-5
 
trace0 = go.Scatter(x=x_axis, y=y0_axis, mode='markers', name='markers')
trace1 = go.Scatter(x=x_axis, y=y1_axis, mode='lines+markers', name='line+markers')
trace2 = go.Scatter(x=x_axis, y=y2_axis, mode='lines', name='lines')
 
data_sets = [trace0, trace1, trace2]
plotly.offline.plot(data_sets, filename='line_scatter_plot.hmtl')
```

运行脚本如下：

```
$ python3 line_scatter_plot.py
```

我们将得到如下输出：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032214451257.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032214451257.png)

上例中，我们导入了plotly以及numpy模块。然后为x轴以及三个不同的y轴生成了一些随机值。然后，我们将该数据放到了创建的trace对象中，最后将数据集放入plotly的离线函数中。接着我们获取了散点及线状格式的输出。该示例的输出被保存到当前目录的line_scatter_plot.html文件中。

#### 箱形图

箱形图有益于传递信息量，尤其是在数据很少又想显示很多时，我们来看一个示例。创建一个名为plotly_box_plot.py的脚本并在其中编写如下内容：

```
import random, plotly
from numpy import *
 
N = 50
c = ['hsl('+str(h)+',50%'+',50%)' for h in linspace(0, 360, N)]
data_set = [{
    'y': 3.5*sin(pi*i/N) + i/N + (1.5+0.5*cos(pi*i/N))*random.rand(20),
    'type':'box',
    'marker':{'color': c[i]}
    } for i in range(int(N))]
layout = {'xaxis': {'showgrid':False, 'zeroline':False,
    'tickangle':45, 'showticklabels':False},
    'yaxis': {'zeroline':False, 'gridcolor':'white'},
    'paper_bgcolor': 'rgb(233,233,233)',
    'plot_bgcolor':'rgb(233,233,233)',
    }
 
plotly.offline.plot(data_set)
```

运行脚本如下：

```
$ python3 plotly_box_plot.py
```

得到的结果如下：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032215045165.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032215045165.png)

上例中，我们导入了plotly以及numpy模块。然后我们声明了箱体内的总箱体数N，并通过调整HSL展示的饱和度和亮度以及在色调的变化生成了一组彩虹色。每个箱体由包含数据、类型和颜色的字典来体现。我们使用了列表推导式来描述N个箱体，每个箱体的颜色不同并带有随机生成的数据。接着我们格式化了输出的布局并通过离线plotly函数对数据绘图。

#### 等高线图

等高线图是科学绘图时最常用的，也在显示热力图数据时经常使用。我们来看一个等高线图的示例。创建一个名为contour_plotly.py的脚本并在其中编写如下内容：

```
 from plotly import tools
import plotly
import plotly.graph_objs as go
 
trace0 = go.Contour(
    z=[[1, 2, 3, 4, 5, 6, 7, 8],
    [2, 4, 7, 12, 13, 14, 15, 16],
    [3, 1, 6, 11, 12, 13, 16, 17],
    [4, 2, 7, 7, 11, 14, 17, 18],
    [5, 3, 8, 8, 13, 15, 18, 19],
    [7, 4, 10, 9, 16, 18, 20, 19],
    [9, 10, 5, 27, 23, 21, 21, 21]],
    line=dict(smoothing=0),
)
trace1 = go.Contour(
    z=[[1, 2, 3, 4, 5, 6, 7, 8],
    [2, 4, 7, 12, 13, 14, 15, 16],
    [3, 1, 6, 11, 12, 13, 16, 17],
    [4, 2, 7, 7, 11, 14, 17, 18],
    [5, 3, 8, 8, 13, 15, 18, 19],
    [7, 4, 10, 9, 16, 18, 20, 19],
    [9, 10, 5, 27, 23, 21, 21, 21]],
    line=dict(smoothing=0.95),
)
data = tools.make_subplots(rows=1, cols=2,
    subplot_titles=('Smoothing_not_applied',
    'smoothing_applied'))
data.append_trace(trace0, 1, 1)
data.append_trace(trace1, 1, 2)
 
plotly.offline.plot(data)
```

运行脚本如下：

```
$ python3 contour_plotly.py
This is the format of your plot grid:
[ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
```

我们将得到如下输出：

[![第十七章 数据收集及报表](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032215325922.png)](http://alanhou.org/homepage/wp-content/uploads/2019/03/2019032215325922.png)上例中，我们传入了数据集并对其应用了contour()函数。然后我将等高线数据添加到了data_set中，最后对数据应用了plotly函数来获取输出。这些是plotly中以可视化方式绘制数据的一些技术。

## 总结

本章中，我们学习了NumPy 和Pandas模块，以及数据可视化技术。在NumPy模块一节，我们学习了对数组索引和切片，以及通用数组函数。在pandas模块一节中，我们学习了序列和数据帧。我们还学习了如何将csv文件读取到数据帧中。对于数据可视化，我们学习了Python中用于数据可视化的库：matplotlib和plotly。

下一章中，我们将学习MySQL和SQLite数据库管理。

## 课后问题

1. 什么是NumPy数组？

2. 以下代码片断的输出是什么？

   | 123456789 | import numpy as np# input arrayin_arr1 = np.array([[ 1, 2, 3], [ -1, -2, -3]] )print ("1st Input array : \n", in_arr1)in_arr2 = np.array([[ 4, 5, 6], [ -4, -5, -6]] )print ("2nd Input array : \n", in_arr2)# Stacking the two arrays horizontallyout_arr = np.hstack((in_arr1, in_arr2))print ("Output stacked array :\n ", out_arr) |
   | --------- | ------------------------------------------------------------ |
   |           |                                                              |

3. 如何以比np.sum更快速的方式对小数组求和？

4. 如何从Pandas数据帧删除索引、行或列？

5. 如何将Pandas数据帧写入到文件中？

6. Pandas中的NaN是什么？

7. 如何从Pandas数据帧中删除重复内容？

8. 如何改变Matplotlib中绘制的图形的大小？

9. 使用Python绘图的替代方案有哪些？

## 扩展阅读

- 10分钟pandas文档：http://pandas.pydata.org/pandas-docs/stable/
- NumPy教程: https://docs.scipy.org/doc/numpy/user/quickstart.html
- 使用plotly绘图：https://plot.ly/d3-js-for-python-and-pandas-charts/

# 第十八章 MySQL和SQLite数据库管理
本章中我们将学习MySQL和SQLite数据库管理。我们会安装MySQL和SQLite。我们还将学习如何 创建用户、授权、创建数据库、创建数据表、向表中插入数据以及从指定表记录中查看所有记录、更新和删除数据。

本章中我们将学习如下内容：

- MySQL数据库管理
- SQLite数据库管理

## MySQL数据库管理

这一部分将涵盖使用Python管理MySQL数据库的知识。我们已知Python有各种管理MySQL数据库的模块。这里我们将学习MySQLdb模块。MySQLdb模块是一个MySQL数据库的接口，用于提供Python数据库API。

我们来学习如何安装MySQL以及Python的MySQLdb包。为此在Terminal中运行如下命令：

```bash
$ sudo apt install mysql-server
```



这一命令安装MySQL服务及其它各个包。在安装包时，会弹出让我们输入MySQL的root账号密码：

- 以下命令用于查看是否存在 mysqldb包来供安装

  ```bash
  $ apt-cache search MySQLdb
  # 译者注：安装如下包，否则后续安装可能会报OSError: mysql_config not found
  sudo apt-get install libmysqlclient-dev
  ```

  

- 运行如下命令来安装Python的MySQL接口：

  ```bash
  $ sudo apt-get install python3-mysqldb
  # 译者注：MySQLdb对Python3的支持有些变化，请使用如下方式安装即可导入MySQLdb了
  sudo pip3 install mysqlclient
  # 也可使用 pymysql，此时应为import pymysql
  sudo pip3 install pymysql
  ```

  

- 下面我们将查看是否正确地安装了MySQL，在终端中运行如下命令：

  ```bash
  $ sudo mysql -u root -p
  ```

  

  运行以上命令，我们将得到如下输出：
  
  ```bash
Enter password:
  Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
  Server version: 5.7.25-0ubuntu0.16.04.2 (Ubuntu)
 
  Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.
 
  Oracle is a registered trademark of Oracle Corporation and/or its
  affiliates. Other names may be trademarks of their respective
  owners.
 
  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
  mysql>
  ```
  

  

通过运行sudo mysql -u root -p，我们将进入MySQL控制台。有一些命令可用于列出数据库和数据表，以及使用数据库来存储我们的内容。我们将逐一来看这些命令：



  - 以下为列出所有数据库的命令：
  
    ```mysql
    show databases;
    ```
  
    
  
  - 以下为使用数据库的命令：
  
    ```mysql
    use database_name;
    ```
  
    一旦退出了MySQL控制台并在之后重新登入，我们应再次使用use database_name;ygqk语句。使用该命令的目的在于将内容保存到我们自己的数据库中。可通过以下的示例来清晰地理解这一问题：
  
  - 以下命令可列出所有的数据表：
  
    ```mysql
    show tables;
    ```
    
    

这些就是我们用于列出数据库、使用数据库以及列出数据表的命令。

下面，我们将使用create database语句在MySQL终端中创建一个数据库。使用mysql -u root -p命令并输入密码来打开MySQL终端，密码为我们安装时所设置的。然后创建我们自己的数据库。这一部分中，我们将创建一个名为test的数据库并在整个部分中使用该数据库：

```mysql
$ mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.25-0ubuntu0.16.04.2 (Ubuntu)
 
Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.
 
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
 
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
 
mysql> create database test;
Query OK, 1 row affected (0.00 sec)
 
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
5 rows in set (0.01 sec)
 
mysql> use test;
Database changed
mysql>
```



首先我们使用show databases列出了所有数据库。接着我们使用create database语句创建了数据库test。又再次运行了show databases语句来查看数据库是否成功创建。可以看到数据库已创建。下面我们使用该数据库来存储我们的内容。

下面，我们将创建一个用户并为该用户授权。运行如下命令：

```mysql
mysql> create user 'test_user'@'localhost' identified by 'test123';
Query OK, 0 rows affected (0.00 sec)
 
mysql> grant all on test.* to 'test_user'@'localhost';
Query OK, 0 rows affected (0.00 sec)
 
mysql>
```



我们创建了test_user用户，该用户的密码为test123。接着我们对用户test_user进行了授权。这时我们通过在MySQL终端中quit;或exit;可退出控制台。

下面我们来看一些示例：获取取数据库版本、创建数据表、在数据表中插入数据、更新数据和删除数据。

### 获取数据库版本

首先我们来看一个获取数据库版本的示例。为此创建一个脚本get_database_version.py并在其中编写如下内容：

```python
import MySQLdb as db
# import pymysql as db
import sys
 
con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute('SELECT VERSION()')
version = cur_obj.fetchone()
print('Database version: %s ' % version)
 
con_obj.close()
```



> ℹ️在运行脚本前应按照前述的步骤进行操作，否则将无法正常运行。

运行脚本，我们将得到如下输出：

```bash
$ python3 get_database_version.py
# 输出结果：
Database version: 5.7.25-0ubuntu0.16.04.2
```



上例中，我们获取了数据库的版本。实现获取，我们导入了MySQLdb模块。然后编写了连接字符串。在连接字符串中，我们传入了用户名、密码和数据库名。然后创建了一个游标（cursor）对象用于执行SQL查询。在execute()中我们传入了SQL查询语句。fetchone() 获取查询结果的下一行。然后我们打印出了结果。close()方法关闭了数据库连接。

### 创建数据表和插入数据

下面我们将创建一个数据表并在其中插入数据。为此创建一个脚本create_insert_data.py并在其中编写如下内容：

```python
# import MySQLdb as db
import pymysql as db
 
con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
with con_obj:
        cur_obj = con_obj.cursor()
        cur_obj.execute('DROP TABLE IF EXISTS books')
        cur_obj.execute('CREATE TABLE books(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(100))')
        cur_obj.execute("INSERT INTO books(Name) VALUES('Harry Potter')")
        cur_obj.execute("INSERT INTO books(Name) VALUES('Lord of the rings')")
        cur_obj.execute("INSERT INTO books(Name) VALUES('Murder on the Orient Express')")
        cur_obj.execute("INSERT INTO books(Name) VALUES('The adventures of Sherlock Holmes')")
        cur_obj.execute("INSERT INTO books(Name) VALUES('Death on the Nile')")
 
print('Table Created!!')
print('Data inserted successfully!')
```

运行脚本，我们将得到如下输出：

```bash
$ python3 create_insert_data.py
 
# 输出结果：
Table Created!!
Data inserted successfully!
```



要查看数据表是否成功创建了，打开MySQL控制台并运行如下命令：

```mysql
$ mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 5.7.25-0ubuntu0.16.04.2 (Ubuntu)
 
Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.
 
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
 
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
 
mysql> use test;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
 
Database changed
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| books          |
+----------------+
1 row in set (0.00 sec)
```



可以看到数据表 books 已创建。

### 获取数据

要从数据表获取数据，我们使用select语句。下面我们将从books数据表中获取数据。为此创建脚本retrieve_data.py并在其中编写如下内容：

```python
# import MySQLdb as db
import pymysql as db
 
con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
with con_obj:
        cur_obj = con_obj.cursor()
        cur_obj.execute('SELECT * FROM books')
        records = cur_obj.fetchall()
        for r in records:
                print(r)
```



 

运行脚本，我们将得到如下输出：

```bash
$ python3 retrieve_data.py
# 输出结果
(1, 'Harry Potter')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
(5, 'Death on the Nile')
```



上例中，我们从数据表中获取到了数据。我们使用了MySQLdb模块。编写了一个连接字符串并创建了一个游标对象来执行SQL查询。在execute()中，我们编写了一个SQL select语名。最后，我们打印出了查询到的记录。

### 更新数据

下面我们要对数据表中的记录做一些修改，这时可使用SQL的update语句。我们来看一个update语句的示例。为此创建一个脚本update_data.py并在其中编写如下内容：

```python
# import MySQLdb as db
import pymysql as db
 
con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute('UPDATE books SET Name = "Fantastic Beasts" WHERE Id = 1')
try:
        con_obj.commit()
except:
        con_obj.rollback()
```



运行脚本如下：

```bash
$ python3 update_data.py
```



下面来查看记录是否被更新了，运行retrieve_data.py如下：

```bash
$ python3 retrieve_data.py
# 输出结果：
(1, 'Fantastic Beasts')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
(5, 'Death on the Nile')
```



可以看到ID为1的数据被更新了。上例在execute()中，我们编写了一个update语句来更新ID为1记录的数据。

### 删除数据

要在数据表中删除指定记录，可以使用delete语句。我们来看一个删除数据的示例。创建一个脚本delete_data.py并在其中编写如下内容：

```python
# import MySQLdb as db
import pymysql as db
 
con_obj = db.connect('localhost', 'test_user', 'test123', 'test')
cur_obj = con_obj.cursor()
cur_obj.execute('DELETE FROM books WHERE Id = 5')
try:
        con_obj.commit()
except:
        con_obj.rollback()
```



运行脚本如下：

```bash
$ python3 delete_data.py
```



下面查看记录是否成功删除，运行retrieve_data.py脚本如下：

```bash
$ python3 retrieve_data.py
# 输出结果：
(1, 'Fantastic Beasts')
(2, 'Lord of the rings')
(3, 'Murder on the Orient Express')
(4, 'The adventures of Sherlock Holmes')
```



我们可以看到记录中ID为5的数据已删除。上例中，我们使用了delete语句来删除指定记录。这里我们删除了ID为5的记录。我们还可以根据其它所选的字段名来删除记录。

## SQLite数据库管理

这一部分中，我们将学习如何安装和使用SQLite。Python中有一个sqlite3模块来执行SQLite数据库相关任务。SQLite是一个无服务端、零配置的事务性SQL数据库引擎。SQLite非常快速且轻量。整个数据库存储在单个磁盘文件中。

下面我们首先安装SQLite。在终端中运行如下命令：

```
$ sudo apt install sqlite3
```



这一部分中，我们将学习如下操作：创建数据库、创建数据表、在数据表中插入数据、获取数据、从数据表中更新和删除数据。我们将逐一来看各个操作。

首先我们将来看如何在SQLite中创建数据库。要创建数据库，我们仅需在终端中写入如下命令：

```
$ sqlite3 test.db
```



在运行这一命令后，将会在终端中打开sqlite控制台如下：

```sqlite
$ sqlite3 test.db
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite>
```



于是我们仅仅通过运行sqlite3 test.db就创建了数据库。

### 连接数据库

下面我们来看如何连接数据库。为此我们将创建一个脚本。Python的标准库中已经包含了sqlite3模块。我们只需在要操作SQLite时导入该模块就可以了。创建一个脚本connect_database.py并在其中编写如下内容：

```python
import sqlite3
 
con_obj = sqlite3.connect('test.db')
print('Database connected successfully!!')
```



运行脚本，我们将得到如下输出：

```bash
$ python connect_database.py
 
# 输出结果：
Database connected successfully!!
```



上例中，我们导入了sqlite3模块来执行相关功能。此时查看所在目录，就会看到其中创建了test.db文件。

### 创建数据表

下面我们来数据库中创建数据表。为此创建一个脚本create_table.py并在其中编写如下内容：

```python
import sqlite3
 
con_obj = sqlite3.connect('test.db')
with con_obj:
    cur_obj = con_obj.cursor()
    cur_obj.execute("""CREATE TABLE books(title text, author text)""")
 
print('Table created')
```

运行脚本，我们将得到如下输出：

```
$ python3 create_table.py
Table created
```

上例中我们使用CREATE TABLE语句创建了数据表books。首先，我们使用test.db建立了数据库连接。然后，我们创建一个游标对象用于对数据库执行SQL查询。

### 插入数据

下面我们将在数据表中插入数据。为此创建一个脚本insert_data.py并在其中编写如下内容：

```python
import sqlite3
 
con_obj = sqlite3.connect('test.db')
with con_obj:
    cur_obj = con_obj.cursor()
    cur_obj.execute("INSERT INTO books VALUES ('Pride and Prejudice', 'Jane Austen')")
    cur_obj.execute("INSERT INTO books VALUES ('Harry Potter', 'J.K Rowling')")
    cur_obj.execute("INSERT INTO books VALUES ('The Lord of the Rings', 'J. R. R. Tolkien')")
    cur_obj.execute("INSERT INTO books VALUES ('Murder on the Orient Express', 'Agatha Christie')")
    cur_obj.execute("INSERT INTO books VALUES ('A Study in Scarlet', 'Arthur Conan Doyle')")
    con_obj.commit()
 
print('Data inserted successfully!!')
```

运行脚本，我们将得到如下输出：

```bash
$ python insert_data.py
# 输出结果：
Data inserted successfully!!
```



上例中我们在数据表中插入了一些数据。为此我们在SQL语句中使用了insert。通过使用commit()，我们告诉数据库保存所有的当前事务。

### 获取数据

下面我们将从数据表中获取数据。为此创建一个脚本retrieve_sqlite_data.py并在其中编写如下内容：

```python
import sqlite3
 
con_obj = sqlite3.connect('test.db')
cur_obj = con_obj.execute('SELECT title, author FROM books')
for row in cur_obj:
    print('Title = ', row[0])
    print('Author = ', row[1], '\n')
 
con_obj.close()
```

运行脚本，我们将得到如下输出：

```bash
$ python3 retrieve_sqlite_data.py
# 输出结果：
Title =  Pride and Prejudice
Author =  Jane Austen
 
Title =  Harry Potter
Author =  J.K Rowling
 
Title =  The Lord of the Rings
Author =  J. R. R. Tolkien
 
Title =  Murder on the Orient Express
Author =  Agatha Christie
 
Title =  A Study in Scarlet
Author =  Arthur Conan Doyle
```

上例中，我们导入了sqlite3模块。然后我们连接了test.db数据库。我们使用了select来获取数据。最后，我们打印出了所获取的数据。

我们也可以在sqlite3控制台中获取数据。首先启动SQLite终端并随后获取数据如下：

```sqlite
$ sqlite3 test.db
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> select * from books;
Pride and Prejudice|Jane Austen
Harry Potter|J.K Rowling
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
sqlite>
```



### 更新数据

可以使用update语句来更新数据表中的数据。下面我们来看一个更新数据的示例。为此创建一个脚本update_sqlite_data.py并在其中编写如下内容：

```python
import sqlite3
 
con_obj = sqlite3.connect('test.db')
with con_obj:
    cur_obj = con_obj.cursor()
    sql = """
        UPDATE books
        SET author = 'John Smith'
        WHERE author = 'J.K Rowling'
    """
    cur_obj.execute(sql)
 
print('Data updated successfully!!')
```

运行脚本，我们将得到如下输出：

```
$ python3 update_sqlite_data.py
# 输出结果：
Data updated successfully!!
```

这时要检查是否更新了数据，可以运行retrieve_sqlite_data.py或者进行SQLite控制台并运行select * from books;。我们将得到更新后的输出如下：

```sqlite
# 运行retrieve_sqlite_data.py脚本的输出结果如下：
$ python3 retrieve_sqlite_data.py
Title =  Pride and Prejudice
Author =  Jane Austen
 
Title =  Harry Potter
Author =  John Smith
 
Title =  The Lord of the Rings
Author =  J. R. R. Tolkien
 
Title =  Murder on the Orient Express
Author =  Agatha Christie
 
Title =  A Study in Scarlet
Author =  Arthur Conan Doyle
 
# 在SQLite的终端中查看：
 
$ sqlite3 test.db
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> select * from books;
Pride and Prejudice|Jane Austen
Harry Potter|John Smith
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
sqlite>
```



### 删除数据

下面我们来看一个从数据表中删除数据的示例。我们将使用delete语句来进行实现。创建一个脚本delete_sqlite_data.py并在其中编写如下内容：

```
import sqlite3
 
con_obj = sqlite3.connect('test.db')
with con_obj:
    cur_obj = con_obj.cursor()
    sql = """
        DELETE FROM books
        WHERE author = 'John Smith'
    """
    cur_obj.execute(sql)
 
print('Data deleted successfully!!')
```

运行脚本，我们将得到如下输出：

```
$ python3 delete_sqlite_data.py
# 输出结果：
Data deleted successfully!!
```



上例中，我们从数据表中删除了一条记录。我们使用了SQL中的delete语句。下面来查看数据是否删除成功，可运行retrieve_sqlite_data.py或在SQLite终端中启动如下：

```bash
# 通过运行retrieve_sqlite_data.py后的输出结果：
 
$ python3 retrieve_sqlite_data.py
Title =  Pride and Prejudice
Author =  Jane Austen
 
Title =  The Lord of the Rings
Author =  J. R. R. Tolkien
 
Title =  Murder on the Orient Express
Author =  Agatha Christie
 
Title =  A Study in Scarlet
Author =  Arthur Conan Doyle
```



可以看到作者为 John Smith 的记录被删除了。

```
# 在SQLite终端中查看：
 
$ sqlite3 test.db
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> select * from books;
Pride and Prejudice|Jane Austen
The Lord of the Rings|J. R. R. Tolkien
Murder on the Orient Express|Agatha Christie
A Study in Scarlet|Arthur Conan Doyle
```



## 总结

本章中，我们学习对MySQL和SQLite数据库的管理。我们创建了数据库及数据表。然后在数据表中插入了几条记录。使用select语句我们获取到了记录。我们还学习了更新和删除数据。

## 课后问题

1. 数据库的作用是什么？
2. 数据库中的CRUD是什么？
3. 我们是否可以远程连接数据库？若可以，请用示例进行说明。
4. 是否可在Python代码内编写触发器和存储过程？
5. DML和DDL语句是什么？

## 扩展阅读

- 使用PyMySQL库: http://zetcode.com/python/pymysql/
- MySQLdb, Python连接指南: https://mysqlclient.readthedocs.io/
- SQLite数据库的DB-API 2.0接口: https://docs.python.org/3/library/sqlite3.html