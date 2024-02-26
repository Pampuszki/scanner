# scanner

This project uses Python version 3.12

## Installation

### <ins>1. Create a Virtual Environment</ins>

    python -m venv .venv

### <ins>2. Activate the Virtual Environment</ins>

- #### On Windows:</ins>

        .\.venv\Scripts\activate

- #### On Unix:</ins>

        source .venv/bin/activate 

### 3. <ins>Install Dependencies</ins>

Install tesseract [link](https://tesseract-ocr.github.io/tessdoc/Installation.html):

    sudo apt install tesseract-ocr libtesseract-dev

Install requirements:

    pip install -r requirements.txt

### <ins>4. Running Tests with tox</ins>

Tox will automatically create and configure virtual environments for different Python versions and run the test suite.

    tox