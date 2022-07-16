from pydantic import BaseSettings, Extra
from typing import Dict, Any
import functools 
import yaml

OBLV_CONFIG_PATH = '/usr/runtime.yaml'

def yaml_config(settings: BaseSettings) -> Dict[str, Any]:
    try:
        with open(OBLV_CONFIG_PATH, 'r') as f:
            config_data = yaml.safe_load(f)
    except:
        config_data = {}
    return config_data

class Settings(BaseSettings):

    class Config:
        extra = Extra.allow

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                yaml_config,
                env_settings,
                file_secret_settings,
            )

@functools.lru_cache()
def get_settings() -> Settings:
    return Settings()