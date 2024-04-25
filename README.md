# Bahar Kargo Parcel Scraper

## Description

This Python script scrapes parcel information from the Bahar Kargo website. It logs into the website, navigates to the parcel index page, and retrieves information about parcels with a specific status. The script then calculates the total number of parcels, as well as the total amount in Manat and Dollar.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium
- Chrome WebDriver
- dotenv

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

or

```bash
pip install selenium
pip install python-dotenv
```

Make sure to download the Chrome WebDriver compatible with your Chrome browser version and place it in the same directory as the script.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/elvinsl/bahar-kargo-scraper.git
```

2. Navigate to the project directory:

```bash
cd bahar-kargo-scraper
```

3. Create a `.env` file in the project directory and add your Bahar Kargo login credentials:

```
EMAIL=your_email@example.com
PASS=your_password
```

4. Run the script:

```bash
python main.py
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).
