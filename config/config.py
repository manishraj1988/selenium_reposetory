import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    BASE_URL: str = os.getenv("BASE_URL", "https://example.com")
    BROWSER: str = os.getenv("BROWSER", "chrome")
    HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"
    IMPLICIT_WAIT: int = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT: int = int(os.getenv("EXPLICIT_WAIT", "20"))
    SCREENSHOT_PATH: str = "screenshots"
    REPORT_PATH: str = "reports"

config = Config()