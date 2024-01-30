# Environment setup

Python 3 is required to run the tests. Use venv to create a virtual environment in this folder:

```python -m venv .venv```

To activate the environment:

```source .venv/bin/activate```

# Install dependencies

Once the environment is active, install library dependencies:

```pip install -r requirements.txt```

Also install the browser packages for playwright:

```playwright install```

# Running tests

To run all tests simply use:

```pytest```

# Cross-browser compatibility

Tests are executed in Chromium, Firefox and Webkit. Chrome is Chromium-based and Safari is Webkit-based, while IE is not supported by Playwright. Change the browser options by editing the `addopts` parameter in `pytest.ini`.

# Issues

The Magento website seems to be unable to handle input if it's too fast, making some tests flaky. and failing with the "Invalid Form Key. Please refresh the page." error message.

The tests can be ran with retries activated to improve passing rate in exchange of execution time. Use this command with `n` as the maximum number of retries for each test:

```pytest --reruns n```
