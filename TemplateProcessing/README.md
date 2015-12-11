## Python vs VBA/BASIC for Corporate Budget Processing

### Scenario
You distribute Excel spreadsheets for cost center managers to enter their budgets into for submission to Finance.

### Data
Each cost center will submit a 13 column spreadsheet:
```
Account, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
5000
...
7450
```

### Solutions
1. Use Python to save each of these submissions into a single CSV file which produces a sound format for analysis.  Requires user to save each submission in same folder with naming convention "CC[NUM]_Budget.csv"; where [NUM] is the cost center number.
2. Use BASIC to create a macro that can run inside a spreadsheet that has each cost center budget loaded as a different tab within the spreadsheet.  Each tab should be named "Budget[NUM]"; where [NUM] is the cost center number.

### Notes
1. The different nature of document loading doesn't make these examples fully comparable, but does reflect the appropriate setup required to execut each one; specifically that loading the Python files from the folder and placing the LibreOffice spreadsheets within the same spreadsheet file reflect a comparable design.

### Running Python Budget Processor
```
python3 budget_processor.py
```
No requirements, native Python.

### Running BASIC Budget Processor
```
Within your LibreOffice Document
Tools -> Macros -> Organize Macros -> LibreOffice BASIC... -> New...
Paste budget_processor.BASIC
```