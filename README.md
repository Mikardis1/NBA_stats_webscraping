# NBA Stats Scraper (Python + Selenium)

This project is a simple and functional web scraper that collects NBA player statistics directly from **nba.com/stats**, using **Python**, **Selenium**, and **Pandas**.

## 🚀 Purpose

The script automates the extraction of the following information:

* Player name
* Points per game (PTS)

All collected data is saved into a `nba.csv` file for further analysis.


## 🧩 How It Works

1. Opens the official NBA stats page using Selenium.
2. Automatically accepts the cookie popup.
3. Navigates to the "All Player Stats" section.
4. Extracts the stats table.
5. Saves the data into a CSV file.

---

## 📁 Project Structure

```
project/
├── scraper.py        # Main scraping script
├── nba.csv           # Script output (ignored by git)
├── .gitignore        # Files and directories to ignore
└── README.md         # This file
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash

pip install -r requirements.txt

```

### 2. Install ChromeDriver

Ensure your ChromeDriver version matches your installed Google Chrome version.

Download from: [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

Place the ChromeDriver executable in your system PATH.

### 3. Run the script

```bash
python scraper.py
```

The browser will open, scrape the data, and generate `nba.csv`.


