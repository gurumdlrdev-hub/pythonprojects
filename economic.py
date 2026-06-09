# --- 1. Debt to GSDP Ratio Calculation ---
def calculate_debt_to_gsdp(total_debt, total_gsdp):
    """
    This function calculates the debt ratio of a state.
    It checks if the debt is in the safe limit or danger limit.
    """
    # Check for zero to avoid math errors
    if total_gsdp == 0:
        return "Error: GSDP cannot be zero."
    
    ratio = (total_debt / total_gsdp) * 100
    
    print(f"-> Debt to GSDP Ratio: {ratio:.2f}%", end=" - ")
    if ratio <= 15:
        print("Status: Safe. Debt is very low.")
    elif ratio <= 25:
        print("Status: Normal. Debt is under control.")
    elif 25 < ratio <= 30:
        print("Status: Warning. Debt is getting high.")
    else:
        print("Status: Danger. Debt is too high.")

    return ratio


# --- 2. Interest to Revenue Ratio Calculation ---
def calculate_interest_to_revenue(total_interest, total_revenue):
    """
    This function calculates how much interest the state pays 
    from its total income.
    """
    if total_revenue == 0:
        return "Error: Revenue cannot be zero."

    ratio = (total_interest / total_revenue) * 100
    
    print(f"-> Interest to Revenue Ratio: {ratio:.2f}%", end=" - ")
    if ratio < 10:
        print("Status: Safe. The state has money for development.")
    elif 10 <= ratio <= 15:
        print("Status: Normal. Standard spending for a developing state.")
    elif 15 < ratio <= 20:
        print("Status: High Risk. High interest payments are hurting the budget.")
    else:
        print("Status: Danger. Debt Trap! The state is borrowing money just to pay interest.")

    return ratio


# --- 3. Main Function ---
def fiscal_main():
    """
    This is the main function that takes input from the user 
    and runs the analysis.
    """
    print("\n===============================================")
    print("             STATE BUDGET ANALYZER             ")
    print("===============================================")
    try:
        debt = int(input("Enter total state debt: "))
        gsdp = int(input("Enter total state GSDP: "))
        interest = int(input("Enter annual interest payment: "))
        revenue = int(input("Enter total state revenue income: "))
        
        print("\n================ FINAL REPORT ================")
        calculate_debt_to_gsdp(debt, gsdp)
        calculate_interest_to_revenue(interest, revenue)
        print("==============================================\n")

    except ValueError:
        print("\n[Error] Please enter numbers only. Do not use commas or dots.")


if __name__ == "__main__":
    fiscal_main()
