# Risk Calculation Model

This AI model evaluates a patient’s **age, heart rate, oxygen level, temperature, and diabetic status** to answer one critical question:  

**“How likely is this patient to deteriorate soon (require urgent care, transfer to higher monitoring, or risk readmission)?”**  

## What the model does
- **Does not** read clinical notes or make diagnoses.  
- **Only uses** numeric and yes/no inputs provided.  
- **Returns**:  
  - A **probability** (between `0` and `1`) quantifying the risk.  
    - Example: `0.92` → *“92% chance of deterioration according to the model.”*  
  - A **label** (low, medium, or high risk) derived from that probability, so humans or other systems can act.

## Example  

**Input (patient data):**
is_diabetic = 1
spo2        = 96%
temp        = 98°F
age         = 11
heart_rate  = 112

**Output (model response):**
Probability = 0.91 → "This person is very likely to deteriorate soon."
Label       = high → "Treat this as a high-priority case."

## How to Use the Output  

- **If probability ≥ 0.75** → Automatic escalation or clinician alert.  
- **If probability is 0.5 – 0.75** → Flag for closer monitoring or human review.  
- **If probability < 0.5** → Routine care, no immediate escalation.


**Test Framework flow**
Read input values and expected output from excel sheet -> Normalize the values -> Pass the values to the Model -> Model reads the input values and returns Probability and Label -> Validates the model output with expected output -> Generates report with the results.


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