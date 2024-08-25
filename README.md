# CROCUS Node Dashboard

The "CROCUS Node Dashboard" is a Streamlit web app designed to facilitate the visualization and analysis of environmental data collected by various sensors on multiple CROCUS Nodes located in Chicago, IL. The app uses the [sage-data-client](https://github.com/sagecontinuum/sage-data-client) Python library to query and retrieve data, which users can interact with through the web UI.

# Web App
Click [Here](https://crocus-node-dashboard.streamlit.app/ "Here") To View This Dashboard Online!

![image](https://github.com/CROCUS-Urban/crocus-node-dashboard/assets/63890666/d8bd7152-4a70-4b79-aebf-97eb08592566)
![image](https://github.com/CROCUS-Urban/crocus-node-dashboard/assets/63890666/d06950ac-2d42-4ded-82ec-21150e2f36a8)

## Features

-   Real-time and historical data visualization for selected sensors on multiple CROCUS Nodes.
-   Interactive selection of devices and metrics across different nodes.
-   Filtering options for specific date and time ranges with a quick selection for last hour, day, week, or month.
-   Customizable charts with Plotly for in-depth data analysis.
-   Download the filtered data as a CSV file for further analysis.
-   Visualizations include line charts, frequency bar charts, and box plots for deeper data insights.
-   Automatic conversion of UTC timestamps to local time for easier interpretation.

## Usage

After running the app, users are greeted with a selection of CROCUS Nodes and the devices available on those nodes. Users can select the desired node, device, specific sensors, and a range of dates and times for which they want to visualize the data.

### Data Selection and Visualization

-   **Select CROCUS Node**: Choose from available CROCUS Nodes such as "UIC CROCUS Node (W096)", "CSU CROCUS Node (W08E)", etc.
-   **Select Device**: Pick the device from the selected node, including options like "CROCUS Node" or "Sap Flow Sensors."
-   **Select Specific Data**: Choose the sensor data metrics you are interested in, only the selected metrics will be displayed.
-   **Time Range**: Select a predefined time range (Last Hour, Last Day, Last Week, Last Month) or customize your date and time range.
-   **Data Visualization**: View interactive graphs for selected metrics, with options to visualize data as line charts, frequency bar charts, and box plots.

### Download Options

-   **CSV Export**: Download the filtered data as a CSV file for offline analysis, the filename is saved as the specified time range.

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   Pandas
-   sage_data_client
-   Plotly
-   st-theme

## Installation

1.  Clone the repository:

`git clone https://github.com/CROCUS-Urban/crocus-node-dashboard.git`

2.  Install the required packages: To run this app, you will need to install the following dependencies or type `pip install -r requirements.txt` to automatically download:

-   `streamlit`
-   `pandas`
-   `sage_data_client`
-   `plotly`

You can install them using pip:

`pip install -r requirements.txt`

3.  Run the app:

`streamlit run app.py`

## About CROCUS

Community Research on Climate and Urban Science (CROCUS) is an Urban Integrated Field Laboratory established by Argonne National Laboratory. CROCUS aims to understand and address the challenges of Chicago's changing climate, with a focus on environmental justice in the Chicago region.

For more information, visit [CROCUS Urban](https://crocus-urban.org/).