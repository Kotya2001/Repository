import json


class base:
    with open(r'C:\Users\Белозеров Илья\AppData\Roaming\JetBrains\PyCharmCE2020.2\scratches\scratch.json') as js_data:
        data = json.load(js_data)

    def __init__(self, data=data, names=[]):
        self.data = data
        self.names = names

    def __getitem__(self, item):
        return self.get_user_profile(item)

    @property
    def get_user_profile(self):
        names = [list(elem.items())[i][1] for elem in self.data for i in range(5)]
        names1 = [name for name in names if isinstance(name, dict) is False]
        names2 = [list(name.values())[j] for name in names if isinstance(name, dict) is True for j in range(4)]
        common_names = names1 + names2

        return common_names


user_profile = base()
user_profile.get_user_profile
