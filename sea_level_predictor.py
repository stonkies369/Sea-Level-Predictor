import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    fig, ax = plt.subplots(figsize=(12, 6))  # Adjusted figure size for better aspect ratio
    ax.scatter(x, y, label='Data', color='blue')

    # Create first line of best fit for all data
    res = linregress(x, y)
    print(res)
    x_forecast = pd.Series(range(1850, 2051))  # Years from 1850 to 2050
    y_forecast = res.slope * x_forecast + res.intercept
    ax.plot(x_forecast, y_forecast, 'r-', label='Best Fit Line (All Data)')

    # Create second line of best fit for data from 2000 onwards
    df_forc = df[df["Year"] >= 2000]
    new_x = df_forc["Year"]
    new_y = df_forc["CSIRO Adjusted Sea Level"]

    new_res = linregress(new_x, new_y)
    new_x_forecast = pd.Series(range(2000, 2051))  # Years from 2000 to 2050
    new_y_forecast = new_res.slope * new_x_forecast + new_res.intercept
    ax.plot(new_x_forecast, new_y_forecast, 'orange', label='Best Fit Line (2000 Onwards)')

    # Set x-ticks to only show years from 1850 to 2050
    ax.set_xticks(range(1850, 2051, 25))  # Set x-ticks every 25 years
    ax.set_xticklabels([float(year) for year in range(1850, 2051, 25)])  # Convert to float

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()