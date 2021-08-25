from configparser import ConfigParser
import json


class Config(ConfigParser):
    def __init__(self, file_name='config.ini', **kwargs):
        super().__init__(**kwargs)
        self.read(file_name)


def get_duts(file_name):
    choices = []
    for key, value in Config(file_name).items('DUTs'):
        choices += [(f'{key}_{typ.strip()}', f'{value.split(":")[0]}_{typ.strip()}') for typ in value.split(':')[1].split(',')] if ':' in value else [(key, value)]
    return choices


def get_attenuators(file_name):
    return [('None', 'None')] + [(f'{key}dB_{name}',) * 2 for key, value in Config(file_name).items('Attenuators') for name in json.loads(value)]


def get_hv_supplies(file_name):
    p = Config(file_name)
    n, channels = p.getint('HV Supplies', 'quantity'), json.loads(p.get('HV Supplies', 'channels'))
    return [(f'{i}-{ch}', f'HV{i}-CH{ch}') if ch != '' else (n, f'HV{i}') for i in range(n) for ch in (range(channels[str(i)]) if str(i) in channels else [''])]
