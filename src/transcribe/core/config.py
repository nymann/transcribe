from pydantic import BaseSettings

from transcribe.version import __version__


class Config(BaseSettings):
    title: str = "Transcribe"
    version: str = __version__

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
