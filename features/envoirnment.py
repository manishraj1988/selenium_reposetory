import os
from datetime import datetime

from utils.driver_factory import DriverFactory
from config.config import config

def before_all(context):
    """Runs once before all tests"""
    context.config = config

    # Create directories
    os.makedirs(config.SCREENSHOT_PATH, exist_ok=True)
    os.makedirs(config.REPORT_PATH, exist_ok=True)

    print("Test execution started...")


def before_scenario(context, scenario):
    """Runs before each scenario"""
    context.driver = DriverFactory.get_driver()
    print(f"\nStarting scenario: {scenario.name}")


def after_scenario(context, scenario):
    """Runs after each scenario"""
    if scenario.status == "failed":
        # Take screenshot on failure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        scenario_name = scenario.name.replace(" ", "_")
        filename = f"{scenario_name}_{timestamp}.png"
        filepath = os.path.join(config.SCREENSHOT_PATH, filename)

        context.driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")

        # Attach screenshot to report (for allure)
        try:
            import allure
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name=scenario_name,
                attachment_type=allure.attachment_type.PNG
            )
        except ImportError:
            pass

    context.driver.quit()


def after_all(context):
    """Runs once after all tests"""
    print("\nTest execution completed!")