import platform

import yaml


class Utils:

    @classmethod
    def get_yaml_data(cls, yaml_path):
        '''
        读取yaml文件的数据
        :param yaml_path: yaml文件的路径
        :return: 返回读取到的数据
        '''
        with open(yaml_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_windos_or_mac(cls):

        system = platform.system()
        if system == 'Darwin':
            return 'macOS'
        elif system == 'Windows':
            return 'Windows'
        else:
            return 'Unknown OS'
