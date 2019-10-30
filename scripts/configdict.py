import configparser as ConfigParser
import configparser
from collections import defaultdict


class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop("__name__", None)
        return d


def merge_two_dicts(x, y):
    z = x.copy()  # start with x's keys and values
    z.update(y)  # modifies z with y's keys and values & returns None
    return z


def read(file):
    f = MyParser()
    f.read("config.ini")
    d = f.as_dict()
    return d


def dict2ini(d, root):
    for k, v in d.items():
        if isinstance(v, dict):
            _key = "%s.%s" % (root, k) if root else k
            if v:
                dict2ini(v, _key)
            else:
                res[_key] = {}
        elif isinstance(v, (basestring, int, float)):
            res[root] = {k: v}


def write(current, new):
    data = Pmerge_two_dicts(current, new)
    config = configparser.ConfigParser()
    for key1, data1 in data.items():
        config[key1] = {}
        for key2, data2 in data1.items():
            for key3, data3 in data2.items():
                config[key1]["{}_{}".format(key2, key3)] = str(data3)
