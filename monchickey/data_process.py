# coding=utf-8
"""常用的数据处理工具封装
"""
import time
import json
import binascii
import base64
import random
import hashlib

import xxhash

def text_word_count(text, word):
    """统计所给文本中指定某个单词的个数
    """
    num = 0
    while text.find(word) != -1:
        text = text.replace(word, "", 1)
        num = num + 1
    return num

def text_word_count2(text, word):
    """和上述统计函数功能一样, 另外一种实现
    """
    num = 0
    word_size = len(word)
    for i, _ in enumerate(text[word_size:]):
        if text[i:i + word_size] == word:
            num += 1
    return num

def random_numeric_password(num):
    """获取随机生成的指定位数的数字密码
    """
    password = []
    for n in range(num):
        password.append(str(random.randint(0, 9)))
    return ''.join(password)

def md5hex(src: bytes) -> str:
    """生成字符串的md5 hash值
    Args:
        src: 要生成md5的源, 必须是二进制字节数组(bytes)
    Returns:
        md5的16进制字符串, 长度: 32, 类型: str
    """
    m = hashlib.md5()
    m.update(src)
    return m.hexdigest()

def interval_intersection(a, b):
    """计算两个区间的交集区间, 默认只处理闭区间
    Args:
        a: 区间1, 类型: list 比如: [3.5, 6.2]
        b: 区间2, 类型: list 比如: [5.8, 7.1]
    Returns:
        返回交集区间元组, 比如上面示例将返回: (5.8, 6.2)
        如果交集不存在, 返回None
        注意: 如果两区间的交集恰好为一个点, 则返回元组的两个元素相等
    """
    if b[0] <= a[1] and a[0] <= b[1]:
        left_number = max(a[0], b[0])
        right_number = min(a[1], b[1])
        return left_number, right_number
    return None

def get_function_zero(func, interval, accuracy):
    """计算函数的零点, 即一元方程f(x) = 0的近似解
    依据和方法: 零点定理和二分法
    Args: 
        func: 函数本身, 类型: python函数, 可以直接被调用, 相当于f(x), 传入x返回函数值
        interval: 零点所在区间, 类型: 元组 假设为: (3, 6) 则首先保证: f(3) * f(6) < 0
        accuracy: 精度, 当区间范围缩小至|a - b| < accuracy时, 即返回求解结果
    Returns:
        计算成功返回方程f(x) = 0的一个解
        计算未得到结果返回: None
    """
    a = interval[0]
    b = interval[1]
    ya = func(a)
    yb = func(b)
    if ya * yb > 0:
        return None
    if ya == 0:
        return a
    if yb == 0:
        return b
    num = 0
    while True:
        c = (a + b)/2.0
        yc = func(c)
        if yc == 0:
            return c
        elif ya * yc < 0:
            b = c
            yb = yc
        elif yc * yb < 0:
            a = c
            ya = yc
        num += 1
        if abs(a - b) < accuracy:
            # print('num: %d' % num)
            return a

def timestamp2str(timestamp, time_format):
    """时间戳转时间字符串
    Args:
        timestamp: 浮点数类型的时间戳, 整数部分精确到单位秒
        time_format: 格式化时间的格式 如:'%Y-%m-%d %H:%M:%S'
    Returns:
        返回指定时间格式的字符串
    """
    return time.strftime(time_format, time.localtime(timestamp))

def str2timestamp(time_str, time_format):
    """时间字符串转时间戳
    Args:
       time_str: 时间字符串 
       time_format: 解析字符串的格式 比如:'%Y-%m-%d %H:%M:%S'
    Returns:
        返回unix时间戳, 类型: float, 单位: s
    """
    return time.mktime(time.strptime(time_str, time_format))

def bytes2hex(bytes_data: bytes) -> str:
    """转换二进制字符串数据为十六进制字符串表示
    Args:
        str_data: 字节流, 类型: bytes
    Returns:
        二进制对应的十六进制字符串
    """
    return binascii.b2a_hex(bytes_data).decode()

def hex2bytes(hex_str: str) -> bytes:
    """还原十六进制字符串为原字节流
    是bytes2hex函数的逆函数
    """
    return binascii.a2b_hex(hex_str)

def hex2int(hex_str: str) -> int:
    """转换16进制字符串为整数
    Args:
        hex_str: 16进制字符串
    Returns:
        16进制对应的整数
    """
    return int(hex_str, 16)

def int2hex(integer_number: int) -> str:
    """转换10进制整数为16进制字符串形式
    Args:
        integer_number: 10进制整数, 类型: int
    Returns:
        返回16进制的字符串表示
    """
    hex_content = hex(integer_number)
    return hex_content[2:]

def int2binstr(integer_number: int) -> str:
    """转换10进制整数为二进制显示的字符串
    Args:
        integer_number: 10进制整数, 类型: int
    Returns:
        二进制形式的字符串, 注意不是二进制流本身
    """
    return bin(integer_number)[2:]

def binstr2int(bin_str: str) -> int:
    """转换二进制形式的字符串为10进制数字, 和int2binstr相反
    Args:
        bin_str: 二进制字符串, 比如: '0b0011'或'0011'
    Returns:
        转换后的10进制整数
    """
    return int(bin_str, 2)

def binstr2bytes(bin_str: str) -> bytes:
    """还原二进制形式的字符串为原始字节流
    Args:
        bin_str: 二进制字符串, 比如: '0001100'
    Returns:
        原始字符串(bytes like), 二进制安全, 比如: '\x0c'
    """
    # 以字节为单元对齐转换
    fill = len(bin_str) % 8
    if fill != 0:
        fill_bit = (8 - fill) * '0'
        bin_str = fill_bit + bin_str
    bin_str_length = len(bin_str)
    hex_units = []
    for i in range(0, bin_str_length - 7, 8):
        hex_units.append('%02x' % int(bin_str[i:i + 8], 2))
    return binascii.a2b_hex(''.join(hex_units))

def bytes2binstr(bytes_data : bytes) -> str:
    """转换二进制字节流为二进制形式的字符串表示, binstr2bytes相反
    Args:
        str_data: 字符串(bytes), 比如: '\x03\xe6'
    Returns:
        二进制字符串, 比如: '1111100110'
    """
    # 以字节为单元转换
    bin_units = []
    for b in bytes_data:
        bin_str = bin(b)[2:]
        number_bits = len(bin_str)
        if number_bits != 8:
            high_fill = (8 - number_bits) * '0'
            bin_str = high_fill + bin_str
        bin_units.append(bin_str)
    return ''.join(bin_units)

def int2char(integer_number: int) -> str:
    """[0, 0x110000] 闭区间范围内整数转换为unicode字符(注意不要超过范围)
    Args:
        integer_number: 要转换的整数
    Returns:
        单个unicode字符, 支持汉字
    """
    return chr(integer_number)

def int2bytes(integer_number: int) -> bytes:
    """整数还原为原始的二进制字节流, 默认方式: 大端, 和struct功能一致
    还原方式从高位按位截取
    """
    hex_str = int2hex(integer_number)
    if len(hex_str) % 2 != 0:
        hex_str = '0%s' % hex_str
    return binascii.a2b_hex(hex_str)

def json_parse(json_str):
    """解析json字符串为内置字典(包括嵌套字典或列表)结构
    Args:
        json_str: json交换格式的字符串
    Returns:
        解析成功返回结果
        解析异常返回None
    """
    try:
        return json.loads(json_str)
    except Exception as e:
        return None

def convert_to_json(data, is_format=False):
    """转换python内置结构(包括字典、列表等数据结构)为json交换格式的字符串
    Args:
        data: 原始数据
        is_format: 是否对json进行格式化, 方便阅读, 默认: False
            为True时进行格式化, 默认等级: 4
    Returns:
        转换后的json字符串
    """
    if is_format:
        return json.dumps(data, skipkeys=True, indent=4)
    return json.dumps(data, skipkeys=True)

def base64_encode(bytes_data: bytes) -> str:
    """对字符串(bytes)进行base64编码
    二进制安全, 比如图片读出来之后的字符串
    """
    return base64.b64encode(bytes_data).decode()

def base64_decode(base64_str: str) -> bytes:
    """解码base64字符串为原始字符串"""
    return base64.b64decode(base64_str)

def get_random_partition(row, size):
    """用于集群场景下生成随机桶编号
    用于随机分片存储, 图片存储等
    Args:
        row: 唯一记录值, 字符串类型, 一般是实时流中记录本身
        size: 桶大小
    Returns:
        partition_id: 返回随机桶编号
    """
    partition_id = xxhash.xxh64(row).intdigest() % size
    partition_id = int(partition_id) + 1
    return partition_id
