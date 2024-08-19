# PORTOFOLIO MODULE 1
# PERIOD TRACKER PROGRAM
# ELISA HARIYANTI
# JCDS 0408 PURWADHIKA BANDUNG

# IMPORT LIBRARY
from datetime import datetime, timedelta
from tabulate import tabulate

# FUNCTION: DATE VALIDATION
def validate_date(last_period_date):
    try:
        last_period_date = datetime.strptime(last_period_date, "%Y-%m-%d")
        return last_period_date
    except ValueError:
        return None

# FUNCTION: CALCULATE NEXT PERIOD DATE
def calcPeriodDates(last_period_date, cycle_length, number_of_periods):
    period_dates = []
    current_date = last_period_date
    while len(period_dates) < number_of_periods:
        period_dates.append(current_date)
        current_date += timedelta(days=cycle_length)
    return period_dates

# FUNCTION: CALCULATE OVULATION DATE AND FERTILITY WINDOW
def calcFertility(period_dates, cycle_length):
    fertility_window = []
    ovulation_dates = []
    for period_date in period_dates:
        ovulation_date = period_date + timedelta(days=(cycle_length - 14))
        fertile_start = ovulation_date - timedelta(days=5)
        fertile_end = ovulation_date + timedelta(days=1)
        fertility_window.append((fertile_start, fertile_end))
        ovulation_dates.append(ovulation_date)
    return ovulation_dates, fertility_window

# FUNCTION: DISPLAY TABLE
def displayData(period_dates, ovulation_dates, fertility_windows):
    period_table = [["Cycle {}".format(i+1), date.strftime('%Y-%m-%d'), ovulation_dates[i].strftime('%Y-%m-%d'), 
                        fertility_windows[i][0].strftime('%Y-%m-%d'), fertility_windows[i][1].strftime('%Y-%m-%d')] for i, date in enumerate(period_dates)]
    
    print("\nYour predicted menstruation, ovulation, and fertile windows are:")
    print(tabulate(period_table, headers=["Cycle", "Period", "Ovulation Date", "Fertile Start", "Fertile End"], tablefmt="grid"))

# FUNCTION: DISPLAY TABLE
def displayOvulation(period_dates, ovulation_dates):
    ovulation_table = [["Cycle {}".format(i+1), period_dates[i].strftime('%Y-%m-%d'), ovulation_dates[i].strftime('%Y-%m-%d')] 
                       for i in range(len(ovulation_dates))]
    
    print("\nYour predicted menstruation and ovulation dates are:")
    print(tabulate(ovulation_table, headers=["Cycle", "Menstruation Start Date", "Ovulation Date"], tablefmt="grid"))

# FUNCTION: DISPLAY TABLE
def displayBestDatesForPregnancy(fertility_windows):
    best_dates_by_cycle = []
    for i, window in enumerate(fertility_windows):
        best_dates = [window[0] + timedelta(days=j) for j in range((window[1] - window[0]).days)]
        best_dates_by_cycle.append((i+1, best_dates))

    table_data = []
    for cycle, dates in best_dates_by_cycle:
        table_data.append(["Cycle {}".format(cycle), ", ".join(date.strftime('%Y-%m-%d') for date in dates)])

    print("\nThe best dates for intercourse to increase the chance of pregnancy are:")
    print(tabulate(table_data, headers=["Cycle", "Dates"], tablefmt="grid"))

# MAIN PROGRAM
def period_tracker():
    print("""
    ======================================================================================================
          
                            Hello, welcome to the Period Tracker Program!
            This app helps you track your menstrual cycles, ovulation dates, and fertility windows.
                        Please follow the prompts to enter your information.
                                        Let's get started! <3  
          
    ======================================================================================================
          """)
    while True:
        # INPUT LAST PERIOD DATE
        while True:
            last_period_date = input('Please enter the date of your last period [YYYY-MM-DD]: ')
            last_period_date = validate_date(last_period_date)
            if last_period_date:
                break
            else:
                print('Invalid input. Please try again.')
        
        # INPUT AVERAGE CYCLE LENGTH
        while True:
            try:
                cycle_length = int(input('Please enter your average cycle length in days: '))
                if cycle_length > 0:
                    break
                else:
                    print('Invalid input. Cycle length must be a positive number. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a valid number.')
        
        # INPUT NUMBER OF PREDICTED NEXT PERIOD
        while True:
            try:
                number_of_periods = int(input('Please enter the number of future periods to calculate: '))
                if number_of_periods in range(1, 13):
                    break
                else:
                    print('Invalid input. Number of periods must be between 1 and 12. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a valid number.')

        # CALCULATE NEXT PERIOD
        period_dates = calcPeriodDates(last_period_date, cycle_length, number_of_periods)

        # CALCULATE OVULATION DATE AND FERTILITY WINDOW
        ovulation_dates, fertility_windows = calcFertility(period_dates, cycle_length)

        while True:
            sexually_active = input('Are you sexually active? [y/n]: ').lower()
            if sexually_active in ['y', 'n']:
                break
            else:
                print('Invalid input. Please enter y or n.')

        if sexually_active == 'y':
            while True:
                planning_pregnancy = input('Are you planning to get pregnant? [y/n]: ').lower()
                if planning_pregnancy in ['y', 'n']:
                    break
                else:
                    print('Invalid input. Please enter y or n.')

            if planning_pregnancy == 'y':
                displayData(period_dates, ovulation_dates, fertility_windows)
                displayBestDatesForPregnancy(fertility_windows)
            else:
                displayData(period_dates, ovulation_dates, fertility_windows)
        else:
            displayOvulation(period_dates, ovulation_dates)
        
        # INPUT TO RE-RUN PROGRAM
        rerun = input("Do you want to run the program again? (y/n): ").lower()
        if rerun != 'y':
            break

def disclaimer():
    print("""
=========================================================================================================
                                
                                            Disclaimer:
This program is designed to assist in tracking menstrual cycles and fertility windows. It is important to
note that every individual's menstrual cycle may vary, and this program should not replace personalized
medical advice. For any concerns about your menstrual health or fertility, please consult a qualified
healthcare professional, such as a gynecologist or obstetrician.

=========================================================================================================
""")
    inputD = input('Please click enter to continue.')
    if inputD == "":
        period_tracker()
    else:
        exit

# START PROGRAM
disclaimer()
