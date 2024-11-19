from pydantic import BaseModel, Field
from enum import Enum
import yaml


class Environment(Enum):
    LOCAL = "local"
    DEV = "dev"  # can be test/develop
    PROD = "prod"


class Config(BaseModel):
    env: Environment = Field(default="local")
    database_uri: str


def get_config(env: str = "local") -> Config | None:
    if env == "local":
        with open("config.yml") as config:
            data = yaml.safe_load(config)
        return Config(env=env, **data[env])
    else:
        return None
