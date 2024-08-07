
# NEO Analysis Project

This project analyses Near-Earth Object (NEO) close-approach data to identify trends, visualise distance metrics, and explore velocity relationships. The analysis includes data cleaning, processing, and visualisation using static and interactive plots.

## Project Overview

This repository contains scripts for:
- **Data Cleaning**: Processing and standardising date and distance information.
- **Data Analysis**: Calculating percentage changes in distance and summarising statistics.
- **Data Visualisation**: Creating static and interactive plots to visualise NEO data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Visualisations](#visualisations)
- [Licence](#licence)

## Installation

To set up this project, ensure you have Python 3.7 or higher installed, and install the necessary dependencies:

```bash
pip install pandas matplotlib seaborn plotly
```

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/neo_analysis.git
   cd neo_analysis
   ```

2. **Prepare Your Data**

   Ensure you have a CSV file named `neo_data.csv` in the project directory with the required columns.

3. **Run the Analysis**

   Execute the script to perform data cleaning, analysis, and visualisation:

   ```bash
   python neo_analysis.py
   ```

   The script will:
   - Clean and parse the date information.
   - Calculate percentage changes in distance.
   - Save a summary of results to `neo_summary.csv`.
   - Generate visualisations as both static and interactive plots.

## Data

The input data should be a CSV file named `neo_data.csv` with the following columns:
- `Close-Approach (CA) Date`: Date and time of the close approach.
- `CA DistanceMinimum (au)`: Minimum distance of the close approach (in astronomical units).
- `V relative(km/s)`: Relative velocity (if available).
- `V infinity(km/s)`: Velocity at infinity (if available).

## Visualisations

The script generates the following visualisations:

- **Static Plots**:
  - Line plot of minimum distance of close approaches over time.
  - Histogram of minimum distances.
  - Scatter plot of relative velocity vs. velocity at infinity.

- **Interactive Plots** (using Plotly):
  - Line plot of minimum distance of close approaches over time.
  - Histogram of minimum distances (if added).
  - Scatter plot of relative velocity vs. velocity at infinity (if added).

## Licence

This project is licensed under the MIT Licence. Please take a look at the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the contributors and open-source libraries used in this project.

---

Feel free to adjust any section as needed for your specific project details.
