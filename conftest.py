import logging
import pytest

@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger("testlogs")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("./logs/testlogs.log", encoding="utf-8")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

#Set custom title for the HTML report
def pytest_html_report_title(report):
    report.title = " Model Validation Test Report"
