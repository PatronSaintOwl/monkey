# Without these imports pytests can't use fixtures,
# because they are not found
import json
import os

import pytest
from tests.unit_tests.monkey_island.cc.mongomock_fixtures import *  # noqa: F401,F403,E402
from tests.unit_tests.monkey_island.cc.server_utils.encryption.test_password_based_encryption import (  # noqa: E501
    MONKEY_CONFIGS_DIR_PATH,
    STANDARD_PLAINTEXT_MONKEY_CONFIG_FILENAME,
)

from monkey_island.cc.server_utils.encryption import initialize_datastore_encryptor
from monkey_island.cc.services.authentication import AuthenticationService


@pytest.fixture
def monkey_config(data_for_tests_dir):
    plaintext_monkey_config_standard_path = os.path.join(
        data_for_tests_dir, MONKEY_CONFIGS_DIR_PATH, STANDARD_PLAINTEXT_MONKEY_CONFIG_FILENAME
    )
    plaintext_config = json.loads(open(plaintext_monkey_config_standard_path, "r").read())
    return plaintext_config


@pytest.fixture
def monkey_config_json(monkey_config):
    return json.dumps(monkey_config)


MOCK_USERNAME = "m0nk3y_u53r"
MOCK_PASSWORD = "3cr3t_p455w0rd"


@pytest.fixture
def uses_encryptor(data_for_tests_dir):
    secret = AuthenticationService._get_secret_from_credentials(MOCK_USERNAME, MOCK_PASSWORD)
    initialize_datastore_encryptor(data_for_tests_dir, secret)
