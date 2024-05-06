import os
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

    @classmethod
    def get_datas(cls, name, level, yaml_name):
        root_path = os.path.dirname(os.path.abspath(__file__))
        system = Utils.get_windos_or_mac()
        if system == "Windows":
            yaml_path = os.sep.join([root_path, '..', f'datas\\{yaml_name}.yaml'])
        else:
            yaml_path = os.sep.join([root_path, '..', f'datas/{yaml_name}.yaml'])
        yaml_datas = Utils.get_yaml_data(yaml_path)
        datas = yaml_datas.get(name).get(level).get("datas")
        ids = yaml_datas.get(name).get(level).get("ids")
        return [datas, ids]
