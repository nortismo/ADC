import json

from util.models import ConfigDTO


class ConfigManager:


    def loadConfig(self, filePath):
        with open(filePath, 'r') as f:
            config = json.load(f)

            return ConfigDTO(config['USERS'])
