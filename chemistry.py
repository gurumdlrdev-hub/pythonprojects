def chemistry_formula_generator():
   
    compounds_db = {
        ("H", "O"): ("H2O", "Water - Essential for all life."),
        ("H", "CL"): ("HCl", "Hydrochloric Acid - Strong stomach acid."),
        ("H", "F"): ("HF", "Hydrofluoric Acid - Used for etching glass."),
        ("H", "BR"): ("HBr", "Hydrobromic Acid - Used in chemical synthesis."),
        ("C", "O"): ("C2O", "Dicarbon Monoxide - Highly reactive carbon oxide."),
        ("C", "O2"): ("CO2", "Carbon Dioxide - Greenhouse gas used by plants."),
        ("C", "H"): ("CH4", "Methane - Main component of natural gas."),
        ("C", "CL"): ("CCl4", "Carbon Tetrachloride - Formerly used in fire extinguishers."),
        ("NA", "CL"): ("NaCl", "Sodium Chloride - Common Table Salt!"),
        ("NA", "O"): ("Na2O", "Sodium Oxide - Used in ceramics and glasses."),
        ("NA", "H"): ("NaH", "Sodium Hydride - Strong base used in organic synthesis."),
        ("NA", "F"): ("NaF", "Sodium Fluoride - Used in toothpaste to prevent cavities."),
        ("K", "CL"): ("KCl", "Potassium Chloride - Used as a fertilizer and in medicine."),
        ("K", "I"): ("KI", "Potassium Iodide - Used to protect the thyroid from radiation."),
        ("FE", "O"): ("Fe2O3", "Iron Oxide (Rust) - Formed by iron reacting with oxygen."),
        ("FE", "S"): ("FeS", "Iron Sulfide - Pyrite-like mineral compound."),
        ("S", "O"): ("SO2", "Sulfur Dioxide - Pungent gas from volcanic activity."),
        ("CA", "CL"): ("CaCl2", "Calcium Chloride - Used for de-icing roads."),
        ("CA", "O"): ("CaO", "Calcium Oxide (Quicklime) - Used in making cement."),
        ("MG", "O"): ("MgO", "Magnesium Oxide - Used as an antacid for heartburn."),
        ("MG", "CL"): ("MgCl2", "Magnesium Chloride - Used in dust control and road stabilization."),
        ("N", "H"): ("NH3", "Ammonia - Used in fertilizers and cleaning products."),
        ("N", "O"): ("NO", "Nitric Oxide - Important signaling molecule in the body."),
        ("N", "O2"): ("NO2", "Nitrogen Dioxide - Reddish-brown toxic gas.")
   
    }

    print("=" * 50)
    print("    ULTIMATE CHEMISTRY FORMULA GENERATOR    ")
    print("=" * 50)
    print("Type 'EXIT' at any prompt to stop the program.")
    print("-" * 50)

    
    while True:
        
        element1 = input("\nEnter 1st Element Symbol: ").strip().upper()
        if element1 == 'EXIT':
            print("\n Thank you for learning Chemistry with me! See you soon!")
            break

        
        element2 = input("Enter 2nd Element Symbol: ").strip().upper()
        if element2 == 'EXIT':
            print("\n Thank you for learning Chemistry with me! See you soon!")
            break

        search_pair_1 = (element1, element2)
        search_pair_2 = (element2, element1)

        print("-" * 50)

     
        if search_pair_1 in compounds_db:
            formula, description = compounds_db[search_pair_1]
            print(f" Match Found: {formula}")
            print(f" Info: {description}")
        elif search_pair_2 in compounds_db:
            formula, description = compounds_db[search_pair_2]
            print(f" Match Found: {formula}")
            print(f" Info: {description}")
        else:
            print(" Compound combination not found in current DB!")
            print(" Tip: Try H + O, Na + Cl, C + H, etc.")
            
        print("-" * 50)
        
        
        choice = input("Do you want to try another combination? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("\n Thank you for learning Chemistry with me! See you soon!")
            break 

    print("=" * 50)

if __name__ == "__main__":
    chemistry_formula_generator()