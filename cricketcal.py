def Strike_Rate(runs, balls):
    if balls == 0:
        return 0
    else:
        strike_rate = (runs / balls) * 100
        print(f"Batting Strike Rate: {strike_rate:.2f}")
        return strike_rate

def Economy_Rate(runs, overs):
    if overs == 0:
        return 0
    else:
       
        economy_rate = runs / overs
        print(f"Bowling Economy Rate: {economy_rate:.2f}")
        return economy_rate

def Average(runs, wickets):
    if wickets == 0:
        return runs  
    else:
        average = runs / wickets
        print(f"Bowling/Batting Average: {average:.2f}")
        return average

def Run_rate(runs, overs):
    if overs == 0:
        return 0
    else:
        run_rate = runs / overs
        print(f"Team Run Rate: {run_rate:.2f}")
        return run_rate

print("--- TESTING YOUR FUNCTIONS ---")
Strike_Rate(30, 15)   
Economy_Rate(24, 4)   