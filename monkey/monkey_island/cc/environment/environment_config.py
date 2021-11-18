from __future__ import annotations

import json
import os
from typing import Dict


class EnvironmentConfig:
    def __init__(self, file_path):
        self._server_config_path = os.path.expanduser(file_path)
        self.server_config = None
        self.aws = None

        self._load_from_file(self._server_config_path)

    def _load_from_file(self, file_path):
        file_path = os.path.expanduser(file_path)

        with open(file_path, "r") as f:
            config_content = f.read()

        self._load_from_json(config_content)

    def _load_from_json(self, config_json: str):
        data = json.loads(config_json)
        self._load_from_dict(data["environment"])

    def _load_from_dict(self, dict_data: Dict):
        aws = dict_data["aws"] if "aws" in dict_data else None

        self.server_config = dict_data["server_config"]
        self.aws = aws

    def save_to_file(self):
        with open(self._server_config_path, "r") as f:
            config = json.load(f)

        config["environment"] = self.to_dict()

        with open(self._server_config_path, "w") as f:
            f.write(json.dumps(config, indent=2))

    def to_dict(self) -> Dict:
        config_dict = {
            "server_config": self.server_config,
        }
        if self.aws:
            config_dict.update({"aws": self.aws})
        return config_dict
