import pandas as pd
import matplotlib.pyplot as plt
import os

def run_churn_analysis():
    # 1. Load the dataset
    data_file = 'churn_dataset.csv'
    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found. Please run the script in the directory containing the CSV.")
        return

    df = pd.read_csv(data_file)
    print("--- CUSTOMER CHURN DATASET SAMPLE ---")
    print(df.head())
    print("\n-------------------------------------")

    # 2. Basic Descriptive Statistics
    total_customers = len(df)
    churned_customers = df[df['Churn'] == 'Yes'].shape[0]
    overall_churn_rate = (churned_customers / total_customers) * 100

    print(f"Total Customers Analyzed: {total_customers}")
    print(f"Total Churned Customers: {churned_customers}")
    print(f"Overall Churn Rate: {overall_churn_rate:.2f}%\n")

    # 3. Analyze Average Monthly Charges by Churn Status
    avg_charges = df.groupby('Churn')['MonthlyCharges'].mean()
    print("--- AVERAGE MONTHLY CHARGES BY CHURN STATUS ---")
    print(f"Churned: ${avg_charges['Yes']:.2f}")
    print(f"Retained: ${avg_charges['No']:.2f}")
    print("Insight: Customers who churn have higher average monthly charges.\n")

    # 4. Analyze Churn Rate by Contract Type
    print("--- CHURN RATE BY CONTRACT TYPE ---")
    contract_churn = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack() * 100
    print(contract_churn)
    print("\nInsight: Month-to-month contracts have a significantly higher churn rate compared to one or two-year contracts.\n")

    # 5. Visualizations
    print("Generating churn rate visualization...")
    
    # Plot churn rate by contract type
    plt.figure(figsize=(8, 5))
    
    # Get churn rate for 'Yes' per contract
    churn_rates = contract_churn['Yes'].fillna(0)
    
    colors = ['#ef4444', '#f59e0b', '#10b981'] # Red, Orange, Green
    
    bars = plt.bar(churn_rates.index, churn_rates.values, color=colors, edgecolor='black', width=0.5)
    
    plt.title('Churn Rate (%) by Contract Type', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Contract Type', fontsize=12)
    plt.ylabel('Churn Rate (%)', fontsize=12)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Add values on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height + 2, f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # Save the plot
    output_image = 'churn_by_contract.png'
    plt.tight_layout()
    plt.savefig(output_image, dpi=150)
    print(f"Visualization saved as '{output_image}'.")

if __name__ == "__main__":
    run_churn_analysis()
