import subprocess
import sys
import os


def run_behave_tests(tags=None, format_type="pretty"):
    """
    Run Behave tests with optional tags and format

    Args:
        tags: String like "@smoke" or "@smoke and @login"
        format_type: Output format (pretty, progress, json, html)
    """
    cmd = ["behave"]

    # Add tags if specified
    if tags:
        cmd.extend(["--tags", tags])

    # Add format
    if format_type == "html":
        cmd.extend([
            "-f", "behave_html_formatter:HTMLFormatter",
            "-o", "reports/behave_report.html"
        ])
    elif format_type == "json":
        cmd.extend([
            "-f", "json",
            "-o", "reports/behave_report.json"
        ])
    else:
        cmd.extend(["-f", format_type])

    # Add JUnit report
    cmd.extend(["--junit", "--junit-directory", "reports"])

    # Run tests
    result = subprocess.run(cmd)
    return result.returncode


if __name__ == "__main__":
    # Examples:
    # Run all tests: python run_tests.py
    # Run smoke tests: python run_tests.py @smoke
    # Run with HTML report: python run_tests.py @smoke html

    tags = sys.argv[1] if len(sys.argv) > 1 else None
    format_type = sys.argv[2] if len(sys.argv) > 2 else "pretty"

    exit_code = run_behave_tests(tags, format_type)
    sys.exit(exit_code)