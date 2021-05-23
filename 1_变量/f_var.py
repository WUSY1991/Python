import struct
# 整型
var_int = 100
print(var_int)

# 浮点
var_float = 100.0
print(var_float)

# 字符串
var_string = "This is string"
print(var_string)

# 字符串截取
print(var_string[1:3])
print(var_string[1:])
print(var_string*2)  
print(var_string + "haha")

# 字符串查找
print("is" in var_string)
print("is" not in var_string)

print(var_string.find("s"))  # 字符串首次出现的位置
print(var_string.rfind("s")) # 字符串最后一次出现的位置
print(var_string.index("s")) 
print(var_string.replace("string","hello"))
print(var_string.lower())
print(var_string.upper())

# 数据类型转换
# chr->integer（16进制)			248
a="f8"
print(a,type(a))
a = int(a,16)
print(a,type(a))  

# integer -> string
a = 0xf8
print(a,type(a))
a = hex(a)
print(a,type(a))
a = str(a)
print(a,type(a))

# intergr -> bytes (写二进制文件)
a = 0xf8
print(a,type(a))
a = struct.pack("L",a)
print(a,type(a))

# “B”   unsigned char   1Byte
# "H"   unsigned short   2byte
# “L”    unsigned long	  4Bytes
# "Q"   unsigned long long 8Bytes

# string -> bytes -> string
a = "aabbccddee"
print(a,type(a))
a = bytes.fromhex(a)
print(a,type(a))
a = a.hex()
print(a,type(a))

# assic -> int
print(ord('A'))

# int -> assic
print(chr(65))

# list
print("list demo")
list1 = [1,2,3]
print(list1)
print(list1[1])
print(list1[1:])
print(list1[-2])

# 删除某个元素
del list1[1]
print(list1)

# 清除
list1.clear()
print(list1)

# 追加 
list1.append("add1")
print(list1)

# Tuple



# Dictionary