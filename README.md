# PyScripts

A curated collection of small yet powerful automation scripts and utilities designed to simplify and speed up your daily tasks.

## Structure

```
PyScripts/
├── main.py          # Main entry point
├── scripts/         # Individual script functions
│   ├── __init__.py
│   ├── audio_book.py
│   ├── data_faker.py
│   ├── more files ...
├── .gitignore        # Git ignore file
├── README.md         # README file
└── requirements.txt  # Requirements for the scripts

```

## Installation

Before using any script, make sure to install the required dependencies. Each script has its own set of dependencies listed in `requirements.txt`. The dependencies are organized by script, making it easy to install only what you need.

To install all dependencies:
```bash
pip install -r requirements.txt
```

Or install specific script dependencies by copying the relevant section from `requirements.txt`.

## Usage

1. Import the desired function from the scripts module
2. Call the function with appropriate parameters

Example:
```python
from scripts import url_shortener
short_url = url_shortener.shorten_url("https://example.com")
```

See `main.py` for more examples and documentation.
