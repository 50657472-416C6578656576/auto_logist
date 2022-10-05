from os import environ, getcwd

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class DefaultSettings(BaseSettings):
    ENV: str = environ.get("ENV", "local")
    URL: str = environ.get("URL", "https://system.logist-pro.su/")
    LOGIN: str = environ.get("LOGIN", "some_empty_login")
    PASSWORD: str = environ.get("PASSWORD", "some_empty_pass")
    DRIVER_PATH: str = environ.get("DRIVER_PATH", f"{getcwd()}\driver\chromedriver.exe")
