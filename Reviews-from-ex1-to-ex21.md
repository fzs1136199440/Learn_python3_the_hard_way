# Reviews-from-ex1-to-ex21

### **ex1** to ex5

| names                                    | what it does                                                 |
| ---------------------------------------- | ------------------------------------------------------------ |
| `print()`                                | 输出参数的值，它可以接收多种类型的多个参数。                 |
| `""`  `''`                               | 字符串符号，如果要输出字符串，就要用这两个符号把输出内容的首尾包住，例如，`"kjjhgfd87765"`  `'kjhgf*&^%%'`。 |
| `#`                                      | 注释符号，符号后面的内容是一些解释说明，是给人看的，计算机不会读取和执行这些内容，这些内容不会影响代码的运行。 |
| `+`                                      | 求和                                                         |
| `-`                                      | 求差                                                         |
| `*`                                      | 求积                                                         |
| `/`                                      | 求商                                                         |
| `>`                                      | 符号左边的值大于右边的值，注意**只有同类型的数据才能相互比较。** |
| `<`                                      | 左边的值小于右边的值，同上。                                 |
| `>=`                                     | 左边的值大于或者等于右边的值，同上。                         |
| `<=`                                     | 左边的值小于或者等于右边的值，同上。                         |
| `=`                                      | 赋值符号，变量必须位于符号的左边，值必须位于符号的右边，此符号把左边的值赋予右边的变量，不管左边的表达式如何的复杂，都是先算出左边的值，然后赋予右边的变量。 |
| `f"......{}"`                            | 输出字符串，{}里面的内容是表达式，它会输出表达式的值，这个值会替换{}的位置，如，`f"求和{1 +4}"`，这个表达式会输出结果 `求和5`。 |
| `round(number[,n digits])`（未做完笔记） | 返回number舍入到小数点后n位数精度的值，如果`n digits`被省略或者为`None`，则返回最接近参数number的整数，否则，返回值与number的类型相同。`n digits`必须为整数（正数，负数，零）。例子：`round(1.33, 1)`返回值为`1.3`, `round(1.56)`返回值为`2`。 |



### **ex6 to ex12**

###### `str.format()`

> Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces `{}`. Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
>
> Basic formating for default, positional and keyword arguments:
>
> ```py
> # default arguments
> print("Hello {}, your balance is {}.".format("Jay", 900))
> # output: Hello Jay, your balance is 900.
> 
> # positional arguments
> print("Hello {0}, your balance is {1}.".format("Jay", 900))
> # output: Hello Jay, your balance is 900.
> print("Hello {0}, your balance is {1}, is only {1}.".format("Jay", 900))
> # output: Hello Jay, your balance is 900, is only 900.如此，通过位置来填充字符串，同一个参数还可以填充多次。
> 
> # keyword arguments
> print("Hello {name}, your balance is {blc}.".format(name=Jay, blc=900))
> # output: Hello Jay, your balance is 900.
> 
> # mixed arguments
> print("Hello {0}, your balance is {blc}.".format(Jay, blc=900))
> # output: Hello Jay, your balance is 900.
> # Note: In case of mixed arguments, keyword arguments has to always follow positional arguments.
> ```
>
> There are **more usages** of `str.format()`.  But I can only learn it little by little.

| names                             | what it does                                                 |
| --------------------------------- | ------------------------------------------------------------ |
| `True` and `False`                | 布尔值，代表逻辑上的真与假，如果一个表达式要做出判断，则返回布尔值。所有合法的表达式都可以返回一个布尔值，可以用`bool()`来表达。当`bool()`接收的参数为值为空时，比如`bool(" "), bool(0)`等等，返回`False`, 参数值不为空时，返回`True`. |
| `"""string"""` and `'''string'''` | 当字符串有很多行的时候，可以用这两个符号。                   |
| `\n`                              | 转义符，是换行的意思。                                       |
| `\t`                              | 转义符，Tab键，在python中意为“四个空格”。                    |
| `\r`                              | 转义符，回车键。                                             |
| `\\`                              | 转义符，反斜杠(\)                                            |
| `\'`                              | 转义符，单引号（')                                           |
| `\"`                              | 转义符，双引号（")                                           |
| `input()`                         | 提示用户输入点什么，也可以输入提示信息，例如，`input("Please enter a phone number: ")`, 返回结果为：`Please enter a phone number: ......`。这个函数输出结果是字符串的类型。 |
| `int()`                           | 将参数转换为整数，参数得是数字才行。                         |



### **ex13 to ex18**

| names                                                        | what it does                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `from sys import argv`                                       | 从模块`sys`引入列表`argv`。                                  |
| `sys`                                                        | 该模块提供了一些变量和函数。这些变量可以被解释器使用，也可以由解释器提供。函数和解释器会相互影响。该模块总是可用的。 |
| `sys.argv`                                                   | 一个列表，其中包含了被传给python脚本的命令行参数，除了命令行可以提供参数外，解释器也可以给它提供参数。`argv[0]`为脚本名称（是否是完整的路径名取决于操作系统）。如果是通过python解释器的命令行参数`-c`来执行的，`argv[0]`会被设置成字符串`'-c'`。如果没有脚本名被传递给python解释器，`argv[0]`为空字符串。 |
| `open(file, mode='r', ......)`（它有很多默认参数，暂且记录两个） | 打开一个文件并返回相应的文件对象。如果该文件不能打开，则触发`OSError`。`mode`是可选的，用于指定打开文件的模式，可用的模式有：'r', 读取（默认）；'w', 写入，并先截断文件；'x', 排他性创建，如果文件已存在则失败；'a', 写入，如果文件存在则在末尾追加；'b', 二进制模式；'t', 文本模式（默认）；'+', 打开用于更新（读取和写入）。默认模式为 `'r'` (打开用于读取文本，与 `'rt'` 同义)。 模式 `'w+'` 与 `'w+b'` 将打开文件并清空内容。 模式 `'r+'` 与 `'r+b'` 将打开文件并不清空内容。 |
| `read([size])`                                               | 这个方法要在`open()`后使用，在`open()`打开一个文件并返回相应的文件对象时，`read()`用于从`open()`返回的文件对象中读取指定的字节数，如果参数字节数（size）未给定或为负则读取文件所有的内容。 |
| `truncate([size])`                                           | 它在`open()`打开一个文件之后使用，用于从文件对象首行首字符开始截断，截断的文件长度为从首字符开始到第size个字节，意思是这个文件对象的文件长度现在只有”size个字节”了，“第size个字节”之后的内容就被删除了。如果不提供size参数，就从首字符截断到当前位置（**有疑惑，待定......**） |
| `write()`                                                    | 在`open()`之后，在文件里写入字符串。                         |
| `close()`                                                    | 为了文件安全，使用`close()`是个好习惯。                      |
| `os.path`                                                    | 该模块主要用于获取文件的属性。                               |
| `os.path.exists(path)`                                       | 如果path指向一个已存在的路径或已打开的文件描述符，返回`True`。对于失效的符号链接，则返回`False`。 |
| `def`                                                        | 这是一个命令，用于定义函数。                                 |



