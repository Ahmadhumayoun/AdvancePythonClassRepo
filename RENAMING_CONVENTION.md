# File Renaming Convention Guide

This document tracks all file renames and relocations in the repository.

---

## Renaming Summary

| Category | Old Names | New Names |
|----------|-----------|------------|
| **Notebooks** | 11 files | 11 files |
| **Python Scripts** | 7 files | 7 files |
| **CSV Data** | 10 files | 10 files |
| **Excel Data** | 3 files | 3 files |
| **Scraped Data** | 5 files | 5 files |

---

## Notebooks

| Old Name | New Name & Location |
|----------|---------------------|
| `RevisionNotebook.ipynb` | `notebooks/basics/Python_Basics_Revision.ipynb` |
| `Problems.ipynb` | `notebooks/basics/Python_Practice_Exercises.ipynb` |
| `DataStructures.ipynb` | `notebooks/basics/Python_Data_Structures_Basics.ipynb` |
| `AdvancePythonLearning.ipynb` | `notebooks/advanced/OOP_Python_Class_Learning.ipynb` |
| `NumpyTutorial.ipynb` | `notebooks/advanced/NumPy_Array_Tutorial.ipynb` |
| `PandasLearning.ipynb` | `notebooks/data/Pandas_Data_Analysis_Tutorial.ipynb` |
| `DataAnalasis40.ipynb` | `notebooks/data/Data_Cleaning_Analysis_Project.ipynb` |
| `WEBSCRAPPINGLEARNING.ipynb` | `notebooks/web_scraping/Web_Scraping_With_BeautifulSoup.ipynb` |
| `ApiScrapping_Calling.ipynb` | `notebooks/web_scraping/API_Data_Fetching.ipynb` |
| `WebAutomation.ipynb` | `notebooks/web_scraping/Web_Automation_Selenium.ipynb` |
| `unitconersionBySher.ipynb` | `notebooks/utilities/Unit_Conversion_Calculator.ipynb` |

---

## Python Scripts

| Old Name | New Name & Location |
|----------|---------------------|
| `QuizSystem.py` | `scripts/quiz_system/Quiz_System_Pandas_Implementation.py` |
| `DataScrapingClassLearning.py` | `scripts/web_scraping/Country_Data_Web_Scraper.py` |
| `numpyTutorial.py` | `scripts/numpy/NumPy_3D_Array_Slicing.py` |
| `TestingFile.py` | `scripts/numpy/NumPy_Array_Reshape_Test.py` |
| `FirstCode.py` | `scripts/bank/Bank_Account_Menu_System.py` |
| `Tasks.py` | `scripts/tasks/Age_Calculator_Task.py` |
| `Sel.py` | `scripts/web_automation/Selenium_Login_Automation.py` |

---

## CSV Data Files

| Old Name | New Name & Location |
|----------|---------------------|
| `CountryInfo.csv` | `data/csv/countries/World_Countries_Data.csv` |
| `FinalItemSheet.csv` | `data/csv/products/Store_Products_Catalog_Final.csv` |
| `FinalItems.csv` | `data/csv/products/Store_Products_Extended_Catalog.csv` |
| `QuestionareDummy.csv` | `data/csv/quiz/Quiz_Questions_Bank.csv` |
| `StudentScore.csv` | `data/csv/quiz/Quiz_Student_Scores.csv` |
| `StudentData.csv` | `data/csv/students/Student_Records_Database.csv` |
| `ClasFirstTable.csv` | `data/csv/students/Names_Ages_Table.csv` |
| `UserData.csv` | `data/csv/users/User_Records_Basic.csv` |
| `UserData1.csv` | `data/csv/users/User_Records_With_Index.csv` |
| `Bank.csv` | `data/csv/users/Bank_Accounts_Data.csv` |

---

## Excel Data Files

| Old Name | New Name & Location |
|----------|---------------------|
| `PandasTabularData/VendorProducts.xlsx` | `data/excel/Vendor_Products_Data.xlsx` |
| `PandasTabularData/business-operations-survey-2023-CSV-notes.xlsx` | `data/excel/NZ_Business_Operations_2023.xlsx` |
| `PandasTabularData/~$VendorProducts.xlsx` | `data/excel/Vendor_Products_Temp.xlsx` |

---

## Scraped Data Files

| Old Name | New Name & Location |
|----------|---------------------|
| `TableData.html` | `scraped_data/web_pages/NHL_Hockey_Teams_Stats.html` |
| `Table.html` | `scraped_data/web_pages/NHL_Teams_Data_Page.html` |
| `CardsUrl.html` | `scraped_data/games/Clash_Royale_Cards_List.html` |
| `PageSource.txt` | `scraped_data/misc/Countries_World_Scraped_Page.txt` |
| `AmaZonWatchesPage1.text` | `scraped_data/misc/Amazon_Watches_Product_Page.txt` |

---

## Naming Conventions Used

### File Naming
- All file names use **snake_case** (underscores between words)
- Names are descriptive and indicate content purpose
- Extensions remain unchanged

### Folder Organization
```
root/
├── data/           # All data files
│   ├── csv/        # CSV data organized by type
│   └── excel/      # Excel/spreadsheet files
├── notebooks/     # Jupyter notebooks
│   ├── advanced/   # Advanced topic notebooks
│   ├── basics/     # Beginner notebooks
│   ├── data/       # Data analysis notebooks
│   ├── utilities/  # Utility tool notebooks
│   └── web_scraping/  # Web scraping notebooks
├── scripts/        # Python scripts
│   ├── bank/       # Banking related scripts
│   ├── numpy/      # NumPy related scripts
│   ├── quiz_system/    # Quiz system scripts
│   ├── tasks/      # Task/practice scripts
│   ├── web_automation/  # Selenium web automation scripts
│   └── web_scraping/  # Web scraping scripts
└── scraped_data/   # Raw scraped data
    ├── games/      # Game related data
    ├── misc/       # Miscellaneous scraped data
    └── web_pages/  # Web page snapshots
```

---

## Date
Renamed on: April 8, 2026
