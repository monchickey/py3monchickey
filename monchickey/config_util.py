# -*- coding: utf-8 -*-
"""配置文件读取工具
"""
import yaml

def get_yaml_config(file_path):
    """获取yaml/yml配置文件的配置
    Args:
        file_path: 配置文件路径
    Returns:
        python dict
    yaml Loader:
        BaseLoader - Only loads the most basic YAML
        SafeLoader <=> yaml.safe_load(input)
        FullLoader <=> yaml.full_load(input), default
        UnsafeLoader <=> yaml.unsafe_load(input)
        See: https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
    """
    with open(file_path) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
