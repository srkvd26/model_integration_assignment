# AI Model Test Framework

## Smart Time Normalization Function
This project includes a **smart function** that accepts a time string in **mixed formats** and normalizes it into a consistent **12-hour AM/PM format**.  

### Example Inputs & Outputs:
- `105620` → `10:56:20 AM`  
- `1530` → `3:30 PM`  
- `07:05:00` → `7:05:00 AM`  
- `25:00` → `1:00 AM` (auto-corrects invalid hour `25` into `01`)  

The function is designed to **auto-correct malformed inputs** where possible and gracefully return an error for unsupported formats.

Assuming this smart function as one AI model I've implemented my automation framework where I'm loading the data from a excel file which contains the input value and expected output. I'm passing this input to the smart function and verifying whether the expected output and produced output are matching or not. A report is generated with the results.

## Setup Instructions

1. **Download the repository to a local folder.**

2. **Install Python**

3. **Create & activate virtual environment**  
   **Windows**
   python -m venv venv
   venv\Scripts\activate

   **macOS/Linux**
   python3 -m venv venv
   source venv/bin/activate

4. **Install dependencies**  
   pip install -r requirements.txt


## How to Run Tests

Run all tests:
pytest -v -s

Generate an HTML report (saved under `reports/`):
pytest -v -s --html=reports/report.html --self-contained-html


## Logs
- Console output shows test progress.  
- A file `testlogs.log` is created/updated automatically with detailed logs:  

Example:
2025-09-28 14:10:05 [INFO] Running test case | input='105620' | expected='10:56:20 AM' | actual='10:56:20 AM'
2025-09-28 14:10:05 [INFO] Running test case | input='1530' | expected='3:30 PM' | actual='3:30 PM'


## Viewing Test Reports
After running tests with the HTML option, open the generated report in a browser:  

1. Navigate to the `reports/` folder in your project.  
2. Open `report.html` in any modern web browser.