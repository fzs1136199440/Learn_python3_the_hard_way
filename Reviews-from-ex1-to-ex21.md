# Reviews-from-ex1-to-ex21

### **ex1** to ex5

| names                                    | what it does                                                 |
| ---------------------------------------- | ------------------------------------------------------------ |
| `print()`                                | 输出参数的值。                                               |
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



### **ex6 to **

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
| `\t`                              | Tab键，在python中意为“四个空格”。                            |
| `\r`                              | 回车键                                                       |
| `input()`                         | 提示用户输入点什么，也可以输入提示信息，例如，`input("Please enter a phone number: ")`, 返回结果为：`Please enter a phone number: ......`。 |
| `int()`                           | 将参数转换为整数，参数得是数字才行。                         |

