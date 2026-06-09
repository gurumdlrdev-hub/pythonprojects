
def analyze_debt_to_gsdp(debt, gsdp):
    if gsdp == 0:
        return "Error: GSDP cannot be zero."
    ratio = (debt / gsdp) * 100
    if ratio <= 15: status = "Safe: Very low debt ratio."
    elif ratio <= 25: status = "Moderate: Acceptable debt ratio."
    elif ratio <= 30: status = "Warning: High debt to GSDP ratio."
    else: status = "Critical: Extremely high debt to GSDP ratio."
    print(f"\n-> Debt to GSDP Ratio: {ratio:.2f}% | Status: {status}")

def analyze_interest_to_revenue(interest, revenue):
    if revenue == 0:
        return "Error: Revenue cannot be zero."
    ratio = (interest / revenue) * 100
    if ratio < 10: status = "Safe: Plenty of budget left for welfare."
    elif 10 <= ratio <= 15: status = "Midsafe: Normal for developing states."
    elif 15 < ratio <= 20: status = "Going Danger: Interest is eating up resources."
    else: status = "Very Danger: 'Debt trap' situation!"
    print(f"-> Interest to Revenue Ratio: {ratio:.2f}% | Status: {status}")

def fiscal_main():
    print("\n--- State Fiscal Health Analyzer ---")
    try:
        debt = int(input("Enter total outstanding debt (in Rupees): "))
        gsdp = int(input("Enter Gross State Domestic Product (in Rupees): "))
        interest = int(input("Enter total interest payment (in Rupees): "))
        revenue = int(input("Enter gross revenue receipts (in Rupees): "))
        print("\n================ FISCAL REPORT ================")
        analyze_debt_to_gsdp(debt, gsdp)
        analyze_interest_to_revenue(interest, revenue)
        print("===============================================")
    except ValueError:
        print("\n[Error] Invalid input! Enter whole numbers only.")


