# Customer Churn Analysis

An exploratory data analysis (EDA) project focusing on customer attrition (churn) patterns in a telecom subscription service.

## Project Overview
Understanding why customers leave is critical for improving service offerings and increasing retention. This project processes customer contract structures, billing levels, and tenure to identify core indicators of customer churn.

### Core Findings
1. **Contract Structure:** Customers on Month-to-Month contracts exhibit a significantly higher churn rate compared to those on One-Year or Two-Year terms.
2. **Pricing Sensitivity:** Churned customers have a substantially higher average monthly charge compared to retained customers.

---

## Technical Stack
* **Language:** Python
* **Libraries:** Pandas (Data manipulation), Matplotlib (Data visualization)

---

## Getting Started

### 1. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

### 2. Run the Analysis
Execute the Python script to perform the calculations and output insights:
```bash
python customer_churn_analysis.py
```

### 3. Output
Running the script will print statistics to the console and generate a visualization image:
* **`churn_by_contract.png`**: A bar chart demonstrating the churn percentage across different contract durations.
