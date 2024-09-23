from dataclasses import dataclass
from environs import Env


@dataclass
class UserBotConfig:
    api_id: str
    api_hash: str


@dataclass
class Config:
    userbot: UserBotConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        userbot=UserBotConfig(
            api_id=env('API_ID'),
            api_hash=env('API_HASH')
        )
    )
