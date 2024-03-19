# CROCUS Node Dashboard

The "CROCUS Node Dashboard" is a Streamlit web app designed to facilitate the visualization and analysis of environmental data collected by various sensors on the [W039 Waggle Node](https://portal.sagecontinuum.org/node/W039) located at the Argonne National Laboratory. The app uses the [sage-data-client](https://github.com/sagecontinuum/sage-data-client) Python library to query and retrieve data, which users can interact with through the web UI.

# Web App
Click [Here](https://crocus-node-dashboard.streamlit.app/ "Here") To View This Dashboard Online!

![image](https://github.com/CROCUS-Urban/crocus-node-dashboard/assets/63890666/d8bd7152-4a70-4b79-aebf-97eb08592566)
![image](https://github.com/CROCUS-Urban/crocus-node-dashboard/assets/63890666/d06950ac-2d42-4ded-82ec-21150e2f36a8)

## Features

-   Real-time data visualization for selected sensors.
-   Interactive selection of devices and metrics.
-   Filtering options for specific date and time ranges.
-   Option to download the data as a CSV file.
-   Customizable charts with Plotly for data analysis.
-   Line chart, and box plot visualizations for deeper data insights.
-   Automatic refresh in real-time mode for real-time information.
-   Quick conversion table for metric measurements.

## Usage

After running the app, users are greeted with a selection of devices and sensor readings available on the W039 Waggle Node. Users can select the desired device, specific sensors within that device, and a range of dates and times for which they wish to visualize the data.

### Data Selection and Visualization

-   **Select Device**: Choose from available devices such as "MFR Node", "SFM1x Sap Flow", or "Waggle Node".
-   **Select specific names**: Pick the sensor data metrics you are interested in, all sensor data is enabled by default.
-   **Date and Time Range**: Specify the start and end dates and times for the data.
-   **Real-time Data**: Toggle real-time data updates on or off.
-   **Remove Potential Outliers**: Toggle removing potential outliers to remove values that are below -10,000 and above 10,000.
-   **Data Visualization**: View interactive graphs for selected metrics.

### Download Options

-   **CSV Export**: Download the displayed data as a CSV file for offline analysis, the filename is saved as the specified time range.

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   Pandas
-   sage_data_client
-   Plotly

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
