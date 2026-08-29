# 🕷️ YellowPages India Data Scraper

A high-performance Python web scraper designed to extract business listings, contact information, ratings, addresses, and location links from YellowPages India and export them into structured Excel (`.xlsx`) and text (`.txt`) files.

---

## 📌 Project Overview

This project automates the extraction of public business directory listings from [YellowPages India](http://yellowpages.in/). It parses HTML pages using **BeautifulSoup4**, extracts detailed attributes for each business, cleanses the data, and builds structured datasets using **Pandas**. 

It is ideal for lead generation, market analysis, business directory aggregation, and contact list building.

---

## ✨ Key Features

- 🎯 **Comprehensive Data Mining:** Captures 10 distinct data points per business listing.
- 📱 **Contact Lead Extractor:** Automatically extracts email addresses and direct telephone/mobile numbers into dedicated `.txt` files for quick lead outreach.
- 📍 **Location & Mapping Data:** Captures direct directions/location links alongside complete street addresses.
- 📊 **Structured Excel Export:** Processes extracted data into organized Pandas DataFrames and exports directly to `.xlsx`.
- 🏷️ **Category & Tag Aggregation:** Extracts multi-item categories/hashtags per listing into comma-separated formats.

---

## 📊 Extracted Data Fields

| Field Name | Description | Output Source |
| :--- | :--- | :--- |
| **Titles** | Name of the business or store | Excel |
| **Rating Stars** | Numerical star rating extracted from CSS classes | Excel |
| **Reviews** | User review counts | Excel |
| **Open Status** | Current operating status (e.g., Open Now) | Excel |
| **Images** | Image URL of the listing thumbnail | Excel |
| **Contact Number** | Business phone / mobile numbers | Excel & `yellow_data_numbers.txt` |
| **Emails** | Direct contact email addresses | Excel & `yellow_data_emails.txt` |
| **Addresses** | Street address / physical location text | Excel |
| **Locations** | URL to directions / Google Maps location | Excel |
| **Purpose/Tags** | Business categories and sub-tags | Excel |

---

## 🛠️ Tech Stack & Dependencies

- **Python 3.8+**
- [**Requests**](https://pypi.org/project/requests/) - HTTP library for fetching web pages.
- [**BeautifulSoup4**](https://pypi.org/project/beautifulsoup4/) - HTML parser for web page scraping.
- [**Pandas**](https://pandas.pydata.org/) - Data manipulation and structuring library.
- [**OpenPyXL**](https://pypi.org/project/openpyxl/) - Engine for writing Excel files (`.xlsx`).

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/yellowpages-scraper.git
cd yellowpages-scraper
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

---

## ⚙️ How to Run

1. Open `main.py` (or your script file) and set the target URL:
   ```python
   html = requests.get('http://yellowpages.in/hyderabad/apparels-and-accessories/110497301').text
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Upon execution, the following output files will be automatically generated in your root folder:
   - `yellow_data.xlsx` — Full dataset in Excel format.
   - `yellow_data_emails.txt` — List of extracted email addresses.
   - `yellow_data_numbers.txt` — List of extracted phone numbers.

---

## 📁 Output Files Preview

### Excel Output (`yellow_data.xlsx`)
| Titles | Rating Stars | Reviews | Open status | Contact Number | Emails | Addresses | ... |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sample Store | 4.5 | 12 Reviews | Open Now | +91 9876543210 | info@store.com | Main St, Hitec City | ... |

---

## ⚠️ Legal & Ethical Scraping Disclaimer

This script is created for **educational and portfolio demonstration purposes only**. Always ensure compliance with the target website's `robots.txt` policy and Terms of Service before running web scrapers in automated production environments.

---

## 👨‍💻 Author

Developed by **[Sudip](https://github.com/sudip-python-dev)**  
*Python Developer | Web Scraping & Automation Specialist*  
- 📂 GitHub: [sudip-python-dev](https://github.com/sudip-python-dev)  
- 💼 LinkedIn: [Your LinkedIn Profile Link Here]

