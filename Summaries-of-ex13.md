# Summaries-of-ex13

请看以下这段python代码：

> ```py
> from sys import argv
> # read the What-you-should-see section for how to run this.
> script, first, second, third = argv
> 
> print("The script is called:", script)
> print("Your first variable is:", first)
> print("Your second variable is:", second)
> print("Your third variable is:", third)
> ```
>
> 以上代码来自于书籍《Learn python3 the hard way》的exercise13，保存为文件名`ex13.py`.
>
> **这段代码需要在命令行界面运行，如果直接在解释器里运行就会显示错误。**
>
> 在命令行界面运行，要执行命令行命令`py ......`，在以上代码中，`argv`是个**列表（list）**，里面的元素由命令行命令`py ......`来提供，`argv`这个列表得到的元素个数必须等于赋值符号`=`左边变量的个数，`argv`获得命令行提供的元素后，又把这些元素当作“值”依次赋予左边的变量，比如：
>
> > 上面代码中，`argv`就对应了4个变量，`argv`得到的元素就只能是4个，不能多也不能少，否则就会出错。当在命令行界面执行命令`py ex13.py 1 2 3`时，意思是列表`argv`得到了4个元素`ex13.py ` `1` `2` `3`，`ex13.py`既是被运行的脚本名称也是提供给`argv`的第一个元素，这4个元素被当作“值”按顺序分别赋予左边的4个变量，即`script = ex13.py`, `first = 1`, `second = 2`, `third = 3`,需要注意的是，左边的第一个变量应该恒定为脚本名，在这里就是`ex13.py`，因为要在命令行界面运行python代码，就需要执行命令`py 某某.py`，在这个例子中，就是执行命令`py ex13.py`，这个命令就相当于给`argv`这个列表提供了第一个元素`ex13.py`，等于是给以上的代码中的第一个变量`script`赋值（`script = ex13.py`），并且`ex13.py`的顺序是不能变的，否则命令`py 某某.py`就错了。
> >
> > `argv`也可以在代码中被赋值，不一定非要命令行命令`py ......`赋值。
> >
> > 从书中的ex13,ex14,ex15来看，`argv`赋值给其他的变量的赋值语句中总是会存在一个固定的变量`script`，这个变量有一个固定值就是 ”当前运行的脚本名称“。
> >
> > print()函数也可以接受多个参数，并输出多个值。

