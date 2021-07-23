import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Creates list with years until 2050
    last_year = df.iloc[-1, 0]
    y_50 = []
    for year in range(2050 - last_year):
        y_50.append((year+1)+last_year)
    new_x = (df["Year"].tolist())
    new_x.extend(y_50)

    # Calculate line of best fit
    new_y = [x * slope + intercept for x in new_x]


    plt.plot(new_x, new_y)

    # Create second line of best fit
    mask_x = (df["Year"]) >= 2000
    df_second = df[mask_x]

    # Creates second list with years until 2050
    last_year_second = df_second.iloc[-1, 0]
    y_50_second = []
    for year in range(2050 - last_year_second):
        y_50_second.append((year+1)+last_year_second)
    new_x_second = (df_second["Year"].tolist())
    new_x_second.extend(y_50_second)
    slope, intercept, r_value, p_value, std_err = linregress(df_second["Year"], df_second["CSIRO Adjusted Sea Level"])

    # Calculate second line of best fit
    new_y_second = [x * slope + intercept for x in new_x_second]
    plt.plot(new_x_second, new_y_second)

    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()