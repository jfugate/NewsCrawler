import json,os
class ConfigFile:
    def __init__(self, path="config.json", default=None):
        if default is None:
            default = {}
        self.default = default
        self.path = path
        try:
            self.config = json.loads(open(self.path, "rb").read())
        except FileNotFoundError:
            self.config = default
            self.save()

    def __getitem__(self, key):
        if key in self.config:
            return self.config[key]
        else:
            if key in self.default:
                return self.default[key]

    def __setitem__(self, key, value):
        self.config[key] = value

    def save(self):
        open(self.path, "w").write(json.dumps(self.config, indent=4))


def GetConfig():
    return ConfigFile(
        default={
            "NewsApi_key": os.environ['newsapi_key'],
        }
    )