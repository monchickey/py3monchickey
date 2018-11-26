# -*- coding:utf-8 -*-
"""http常用工具"""
import urllib

def simple_get(url, timeout=3):
    """简单发送get方式获取url内容
    Args:
        url: 请求url, 支持加参数
        timeout: 超时时间, 默认为3s
    Returns:
        请求响应成功: html内容, 类型: bytes
        失败: None
    """
    response = None
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request, timeout=timeout)
        return response.read()
    except Exception as e:
        return None
    finally:
        if response:
            response.close()

def get(url, params=None, headers=None, timeout=3) -> bytes:
    """发送get请求获取url的内容
    Args:
        url: 请求资源地址
        params: 查询字符串参数, 类型: dict, 默认: None
        headers: 请求头参数, 类型: dict, 默认: None, 示例如下:
            {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            }
        timeout: 请求超时时间, 默认: 3s
    Returns:
        请求响应成功: html内容, 类型: bytes
        失败: None
    """
    response = None
    try:
        if params:
            params_encode = urllib.parse.urlencode(params)
            url = "{}?{}".format(url, params_encode)
        request = urllib.request.Request(url)
        if headers:
            for header in headers:
                request.add_header(header, headers[header])
        response = urllib.request.urlopen(request, timeout=timeout)
        return response.read()
    except Exception as e:
        return None
    finally:
        if response:
            response.close()

def post(url, params=None, headers=None, timeout=3):
    """发送post请求
    Args:
        url: 请求资源地址
        params: post参数, 类型: dict, 默认: None
        headers: 请求头参数, 类型和默认值和上面函数相同.
        timeout: 请求超时时间, 默认: 3
    Returns:
        请求并响应成功: html字符串内容
        失败: None
    """
    response = None
    try:
        post_data = b''
        if params:
            post_data = urllib.parse.urlencode(params).encode('utf-8')
        if headers:
            request = urllib.request.Request(url, data=post_data, headers=headers)
        else:
            request = urllib.request.Request(url, data=post_data)
        response = urllib.request.urlopen(request, timeout=timeout)
        return response.read()
    except Exception as e:
        return None
    finally:
        if response:
            response.close()
