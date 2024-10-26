import streamlit as st
import datetime
import pandas as pd
import pytz
from streamlit_theme import st_theme
from config import CROCUS_NODES, DATA_UNITS, NODE_PORTAL_LINKS, SENSOR_FULL_NAMES
from data.data_fetcher import fetch_data, filter_data_by_serial
from components.visualization import plot_visualizations
from components.display_data import display_dataframe
from utils.utils import hide_streamlit_footer

# Set the page title & icon
st.set_page_config(
    page_title="CROCUS Node Dashboard",
    page_icon="📊",
)

# Removes streamlit hyperlink at the bottom of the page
hide_streamlit_footer()

# Detect the current theme
theme = st_theme()

# Determine which logo to use based on the theme
if theme and theme['base'] == 'dark':
    logo = 'images/crocus_dark.png'
else:
    logo = 'images/crocus_light.png'

# Sort the CROCUS_NODES dictionary by keys (node names)
sorted_crocus_nodes = dict(sorted(CROCUS_NODES.items()))

# Initialize session state variables
if 'sap_flow_data' not in st.session_state:
    st.session_state['sap_flow_data'] = pd.DataFrame()
if 'mfr_data' not in st.session_state:
    st.session_state['mfr_data'] = pd.DataFrame()
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()
if 'node_option' not in st.session_state:
    st.session_state.node_option = list(sorted_crocus_nodes.keys())[0]
if 'device_option' not in st.session_state:
    st.session_state.device_option = list(sorted_crocus_nodes[st.session_state.node_option].keys())[0]
if 'selected_sensor' not in st.session_state:
    st.session_state.selected_sensor = ''
if 'selected_names' not in st.session_state:
    st.session_state.selected_names = []
if 'start_date' not in st.session_state:
    st.session_state.start_date = datetime.datetime.now().date()
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.datetime.now().time()
if 'end_date' not in st.session_state:
    st.session_state.end_date = datetime.datetime.now().date()
if 'end_time' not in st.session_state:
    st.session_state.end_time = datetime.datetime.now().time()
if 'timezone' not in st.session_state:
    st.session_state.timezone = pytz.timezone("America/Chicago")
if 'time_range_option' not in st.session_state:
    st.session_state.time_range_option = 'Last Day'

# Selection changes
def on_node_change():
    st.session_state.device_option = list(sorted_crocus_nodes[st.session_state.node_option].keys())[0]
    st.session_state.selected_names = []
    st.session_state.df = pd.DataFrame()

def on_device_change():
    st.session_state.selected_names = []
    st.session_state.df = pd.DataFrame()
    if st.session_state.device_option == 'MFR Nodes':
        sensors_dict = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]['sensors']
        st.session_state.selected_sensor = list(sensors_dict.keys())[0]
    elif st.session_state.device_option == 'Sap Flow Sensors':
        st.session_state.selected_sensor = ''

# Title
st.title('CROCUS Node Dashboard 📊')
# Description under the title
st.write("This is an interface to visualize and analyze data from various sensors on different CROCUS Nodes. Select your desired CROCUS Node, device, specific data, date, and time range to display the results. Additionally, users have the option to view and download all the data as a CSV file and the graphs as a PNG file.")

# Display the logo at the top of the sidebar
st.sidebar.image(logo, use_column_width=True)

# Choose CROCUS Node to fetch with hover text
st.session_state.node_option = st.sidebar.selectbox(
    'Select CROCUS Node',
    list(sorted_crocus_nodes.keys()),
    index=list(sorted_crocus_nodes.keys()).index(st.session_state.node_option),
    key='node_option_widget',
    help=f"[View Node Portal]({NODE_PORTAL_LINKS.get(st.session_state.node_option, '')})",
    on_change=on_node_change
)

# Choose device to fetch
st.session_state.device_option = st.sidebar.selectbox(
    'Select Device',
    list(sorted_crocus_nodes[st.session_state.node_option].keys()),
    index=list(sorted_crocus_nodes[st.session_state.node_option].keys()).index(st.session_state.device_option),
    key='device_option_widget',
    on_change=on_device_change
)

# Extract the serial number (without species) for backend processing
def extract_serial_number(full_string):
    return full_string.split(' ')[0]

# Initialize serial number session state if does not exists
if 'sap_flow_serial' not in st.session_state:
    if st.session_state.device_option == 'Sap Flow Sensors' and 'serial_numbers' in sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]:
        available_serials = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]['serial_numbers']
        st.session_state.sap_flow_serial = extract_serial_number(available_serials[0]) if available_serials else ''
    else:
        st.session_state.sap_flow_serial = ''

if 'mfr_serial' not in st.session_state:
    if st.session_state.device_option == 'MFR Nodes' and 'serial_numbers' in sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]:
        available_serials = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]['serial_numbers']
        st.session_state.mfr_serial = extract_serial_number(available_serials[0]) if available_serials else ''
    else:
        st.session_state.mfr_serial = ''

# Show serial number selection if Sap Flow Sensors or MFR Nodes is selected
if st.session_state.device_option == 'Sap Flow Sensors':
    available_serials = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option].get('serial_numbers', [])
    if available_serials:
        sap_flow_serial_full = st.sidebar.selectbox(
            'Select Sap Flow Sensor Serial Number',
            available_serials,
            key='sap_flow_serial_widget'
        )
        sap_flow_serial = extract_serial_number(sap_flow_serial_full)
        st.session_state.sap_flow_serial = sap_flow_serial
        mfr_serial = ""
    else:
        st.warning(f"No Sap Flow Sensors available for {st.session_state.node_option}")
        sap_flow_serial = ""
        mfr_serial = ""
elif st.session_state.device_option == 'MFR Nodes':
    available_serials = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option].get('serial_numbers', [])
    if available_serials:
        mfr_serial_full = st.sidebar.selectbox(
            'Select MFR Node Serial Number',
            available_serials,
            key='mfr_serial_widget'
        )
        mfr_serial = extract_serial_number(mfr_serial_full)
        st.session_state.mfr_serial = mfr_serial
        sap_flow_serial = ""
    else:
        st.warning(f"No MFR Nodes available for {st.session_state.node_option}")
        mfr_serial = ""
        sap_flow_serial = ""
else:
    sap_flow_serial = ""
    mfr_serial = ""

# Multi-select for names so users can view multiple names and values
if st.session_state.device_option == 'MFR Nodes':
    sensors_dict = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]['sensors']
    sensor_list = []
    display_name_to_sensor_id = {}
    for sensor_id in sensors_dict.keys():
        full_name = SENSOR_FULL_NAMES.get(sensor_id, "")
        display_name = f"{sensor_id} ({full_name})"
        sensor_list.append(display_name)
        display_name_to_sensor_id[display_name] = sensor_id

    selected_sensor_display = st.sidebar.selectbox(
        'Select Specific Sensor',
        sensor_list,
        key='selected_sensor_widget'
    )
    selected_sensor = display_name_to_sensor_id[selected_sensor_display]
    st.session_state.selected_sensor = selected_sensor

    # Get the measurements for the selected sensor
    unique_names = sensors_dict[selected_sensor]
else:
    unique_names = sorted_crocus_nodes[st.session_state.node_option][st.session_state.device_option]['sensors']

# 'Select Specific Data' label
select_data_label = 'Select Specific Data'

selected_names = st.sidebar.multiselect(
    select_data_label,
    unique_names,
    default=[],
    key='selected_names_widget'
)

# Time range selection
time_range_option = st.sidebar.selectbox(
    'Select Time Range',
    ['Last Hour', 'Last Day', 'Last Week', 'Last Month', 'Custom'],
    key='time_range_option_widget'
)

if time_range_option == 'Custom':
    start_date = st.sidebar.date_input('Select start date', st.session_state.start_date, key='start_date_widget')
    start_time = st.sidebar.time_input('Select start time', st.session_state.start_time, key='start_time_widget')
    end_date = st.sidebar.date_input('Select end date', st.session_state.end_date, key='end_date_widget')
    end_time = st.sidebar.time_input('Select end time', st.session_state.end_time, key='end_time_widget')

    # Convert local time to UTC
    start_local = datetime.datetime.combine(start_date, start_time)
    start = st.session_state.timezone.localize(start_local).astimezone(pytz.UTC).isoformat()
    
    end_local = datetime.datetime.combine(end_date, end_time)
    end = st.session_state.timezone.localize(end_local).astimezone(pytz.UTC).isoformat()
else:
    end = datetime.datetime.now().astimezone(pytz.UTC)
    if time_range_option == 'Last Hour':
        start = end - datetime.timedelta(hours=1)
    elif time_range_option == 'Last Day':
        start = end - datetime.timedelta(days=1)
    elif time_range_option == 'Last Week':
        start = end - datetime.timedelta(weeks=1)
    elif time_range_option == 'Last Month':
        start = end - datetime.timedelta(days=30)
    start = start.isoformat()
    end = end.isoformat()

# Stop users from choosing the same start and end time & date
if start == end:
    st.warning('Start and end times cannot be exactly the same.')

if st.sidebar.button('Submit'):
    if not selected_names:
        st.warning('Please select specific data.')
    else:
        st.session_state.selected_names = selected_names
        if st.session_state.device_option == 'Sap Flow Sensors':
            st.session_state.sap_flow_serial = sap_flow_serial
        elif st.session_state.device_option == 'MFR Nodes':
            st.session_state.mfr_serial = mfr_serial
            st.session_state.selected_sensor = selected_sensor
        if time_range_option == 'Custom':
            st.session_state.start_date = start_date
            st.session_state.start_time = start_time
            st.session_state.end_date = end_date
            st.session_state.end_time = end_time
        st.session_state.time_range_option = time_range_option

        # Logic to fetch and display data
        with st.spinner('Fetching data...'):
            if st.session_state.device_option == 'Sap Flow Sensors' and 'sap_flow_serial' in st.session_state:
                st.session_state.sap_flow_data = fetch_data(start, end, st.session_state.node_option, st.session_state.device_option, selected_names)
                st.session_state.df = filter_data_by_serial(st.session_state.sap_flow_data, st.session_state.sap_flow_serial)
            elif st.session_state.device_option == 'MFR Nodes' and 'mfr_serial' in st.session_state:
                st.session_state.mfr_data = fetch_data(start, end, st.session_state.node_option, st.session_state.device_option, selected_names)
                st.session_state.df = filter_data_by_serial(st.session_state.mfr_data, st.session_state.mfr_serial)
            else:
                st.session_state.df = fetch_data(start, end, st.session_state.node_option, st.session_state.device_option, selected_names)

df = st.session_state.df

# Convert UTC to local timezone for display
if not df.empty:
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_convert(st.session_state.timezone)

    # Display data as a dataframe along with the device name and entry count in the header
    display_dataframe(df, st.session_state.device_option, st.session_state.selected_names, DATA_UNITS, height=400)

    # Visualize data
    plot_visualizations(df, st.session_state.device_option)

st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'>© 2024 CROCUS. All rights reserved. <br>Learn more at <a href='https://crocus-urban.org'>crocus-urban.org</a></p>", unsafe_allow_html=True)