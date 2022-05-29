import os
import json
import pathlib

from tests.e2e.Config import Config

class ConfigManager:

    @staticmethod
    def get_config():
        dir_path = pathlib.Path.home()
        file_name = os.environ.get('CONFIG_FILE', 'config.json')

        full_path = os.path.join(dir_path, 'hipaa-autotests', 'configs', file_name)

        data = ConfigManager.read_content(full_path)

        return  ConfigManager.map_config(data)

    @staticmethod
    def read_content(full_path):
        with open(full_path, 'r') as config:
            return json.load(config)

    @staticmethod
    def map_config(data):
        config = Config()

        config.staging_url = data['stagingUrl']

        config.driver_path = data['driverPath']

        config.secure_email = data['secure_email']

        config.password = data['password']

        config.secure_email_second = data['secure_email_second']

        config.password_second = data['password_second']

        config.unregistered_email = data['unregistered_email']

        config.wrong_password = data['wrong_password']

        config.without_alternative_email = data['without_alternative_email']

        config.alternative_email_for_secure = data['alternative_email_for_secure']

        config.unprotected_email = data['unprotected_email']

        config.alternative_email_for_unprotected = data['alternative_email_for_unprotected']

        config.email_subject_empty = data['email_subject_empty']

        config.email_body = data['email_body']

        return config


