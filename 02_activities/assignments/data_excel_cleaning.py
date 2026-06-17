# DATA CLEANING FOR EXCEL VISUAL


# STEP 1: IMPORT NECESSARY LIBRARY

import pandas as pd 

# STEP 2: LOAD DATA SET

df = pd.read_csv("/Users/jojo/Desktop/DSI PROJECT/visualization/02_activities/assignments/Mental Health - 4326.csv")


# STEP 3: DEFINE FUNCTION TO SORT ENTRIES INTO CATEGORIES

def categorize_accessibility(value):
    text = str(value).lower()
    if "not accessible" in text:
        return "Not Accessible"
    elif "unknown" in text:
        return "Unknown"

    elif "accessible" in text or "barrier-free" in text:
        return "Accessible (Full or Partial)"

    else:
        return "Unknown"

# STEP 4: APPLY FUNCTION TO EACH ROW

df['ACCESS_CAT'] = df['ACCESSIBILITY'].apply(categorize_accessibility)

# STEP 5: CHECKING IF THE FUNCTION WORKS AS INTENDED

print("Checking a sample of categorized rows:")
print(df[['ACCESSIBILITY', 'ACCESS_CAT']].head(10).to_string())

# STEP 6: COUNT HOW MANY ORGANIZATIONS FALL INTO EACH CATEGORY AND PRINT 
category_counts = df['ACCESS_CAT'].value_counts()
print("Final category counts:")
print(category_counts)
print()

# STEP 7: CONVERT TO A TABLE AND RENAME COLUMNS FOR CLARITY
summary_table = category_counts.reset_index()

# STEP 8: SAVE TABLE AS A CSV FILE
summary_table.columns = ['Accessibility Category', 'Number of Services']
print("Summary table saved as: viz2_accessibility_data.csv")
print(summary_table) 
