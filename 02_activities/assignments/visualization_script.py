# ASSIGNMENT-3
# SELECTED DATASET: WELLBEING YOUTH MENTAL HEALTH
# DATASET LINK: https://open.toronto.ca/dataset/wellbeing-youth-mental-health/


#STEP 1: IMPORT NEEDED LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#STEP 2: LOAD DATASET
df = pd.read_csv("/Users/jojo/Desktop/DSI PROJECT/visualization/02_activities/assignments/Mental Health - 4326.csv")

# ADDING STYLE SETTINGS TO PRESENT A MORE PROFESSIONAL REPORT LIKE VISUAL 

mpl.rcParams["font.family"] = "sans-serif"
mpl.rcParams["font.sans-serif"] = ["Arial", "Helvetica", "DejaVu Sans"]

mpl.rcParams["axes.titlesize"] = 14
mpl.rcParams["axes.labelsize"] = 11
mpl.rcParams["xtick.labelsize"] = 10
mpl.rcParams["ytick.labelsize"] = 10

mpl.rcParams["figure.facecolor"] = "white"
mpl.rcParams["axes.facecolor"] = "white"
mpl.rcParams["axes.edgecolor"] = "#dddddd"

#STEP 3: COUNT SERVICES PER MUNICIPALITY
municipality_counts = df['MUNICIPALITY'].value_counts()
print("Number of mental health services per municipality is:", municipality_counts)

#STEP 4: SORT FROM HIGHEST TO LOWEST 
municipality_counts = municipality_counts.sort_values(ascending=True)

#STEP 5:SET UP THE FIGURE
fig, ax = plt.subplots(figsize=(10,6)) 

#STEP 6: CHOOSE COLORS
bar_color = "#003DA5" 

#STEP 7: DRAW THE BAR CHART (HORIZONTAL)
bars = ax.barh(
    municipality_counts.index,
    municipality_counts.values,
    color=bar_color,
    edgecolor="white",
    height=0.6
    )

#STEP 8: ADD DATA LABELS
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va='center',
        ha='left',
        fontsize=11,
        color="#000000"
    )

#STEP 9: ADD TITLES AND AXIS LABELS

ax.set_title("Distribution of Mental Health Services Across Former Toronto Municipalities 2020",
             fontsize=14,
             fontweight='bold',
             pad=15,
             loc='left'
             )

ax.set_xlabel(
    "Number of Services",
    fontsize=11,
    labelpad=10
    )

ax.set_ylabel(
    "Former Municipality",
    fontsize=11,
    labelpad=10
    )

#STEP 10: IMPROVE THE AESTHETICS

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.xaxis.grid(True, color='#eeeeee', linewidth=0.8)
ax.set_axisbelow(True)

ax.set_xlim(0, municipality_counts.max() +8)
ax.tick_params(axis='both', labelsize=10)

#STEP 11: ADD A CAPTION NOTE
fig.text(
    0.66, 0.01,
    "Source: City of Toronto Open Data Portal - Mental Health Services Dataset",
    fontsize=7,
    color="#000000"
    )

#STEP 12: SAVE THE CHART AS PNG IMAGE FILE
plt.tight_layout()
plt.savefig(
    "visual_1_services_by_municipality.png",
    dpi=150,
    bbox_inches='tight'
    )
#STEP 13: DISPLAY THE CHART ON SCREEN
plt.show()
