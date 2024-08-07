# NEO Analysis Project
This project analyzes Near-Earth Object (NEO) close approach data to identify trends, visualize distance metrics, and explore velocity relationships. The analysis includes data cleaning, processing, and visualization using both static and interactive plots.

Project Overview
This repository contains scripts for:

Data Cleaning: Processing and standardizing date and distance information.
Data Analysis: Calculating percentage changes in distance and summarizing statistics.
Data Visualization: Creating static and interactive plots to visualize NEO data.
Table of Contents
Installation
Usage
Data
Visualizations
License
Installation
To set up this project, ensure you have Python 3.7 or higher installed, and install the necessary dependencies:

bash
Copy code
pip install pandas matplotlib seaborn plotly
Usage
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/neo_analysis.git
cd neo_analysis
Prepare Your Data

Ensure that you have a CSV file named neo_data.csv in the project directory with the required columns.

Run the Analysis

Execute the script to perform data cleaning, analysis, and visualization:

bash
Copy code
python neo_analysis.py
The script will:

Clean and parse the date information.
Calculate percentage changes in distance.
Save a summary of results to neo_summary.csv.
Generate visualizations as both static and interactive plots.
Data
The input data should be a CSV file named neo_data.csv with the following columns:

Close-Approach (CA) Date: Date and time of the close approach.
CA DistanceMinimum (au): Minimum distance of the close approach (in astronomical units).
V relative(km/s): Relative velocity (if available).
V infinity(km/s): Velocity at infinity (if available).
Visualizations
The script generates the following visualizations:

Static Plots:

Line plot of minimum distance of close approaches over time.
Histogram of minimum distances.
Scatter plot of relative velocity vs. velocity at infinity.
Interactive Plots (using Plotly):

Line plot of minimum distance of close approaches over time.
Histogram of minimum distances (if added).
Scatter plot of relative velocity vs. velocity at infinity (if added).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to the contributors and open-source libraries used in this project.
