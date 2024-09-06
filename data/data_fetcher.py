import sage_data_client
import pandas as pd
from config import CROCUS_NODES

def fetch_data(start, end, node, device, selected_names):
    # Get the available device types for the node
    devices = CROCUS_NODES[node]
    
    # Define filters based on the selected names
    df_list = []
    
    for device_type, device_info in devices.items():
        if any(name in device_info['sensors'] for name in selected_names):
            plugin = device_info['plugin']
            filtered_names = [name for name in selected_names if name in device_info['sensors']]
            
            query_filter = {
                "plugin": plugin,
                "vsn": node.split('(')[-1][:-1],
                "name": "|".join(filtered_names)
            }
            
            # Fetch data using sage_data_client
            df_data = sage_data_client.query(
                start=start,
                end=end,
                filter=query_filter
            )
            df_list.append(pd.DataFrame(df_data))

    # Combine all dataframes into one
    if df_list:
        df = pd.concat(df_list, ignore_index=True)
    else:
        df = pd.DataFrame()

    return df

def filter_data_by_serial(df, serial):
    # Create an empty DataFrame to hold filtered results
    filtered_df = pd.DataFrame()

    # Check if the 'meta.Serial Number_tag' column exists and filter by it
    if 'meta.Serial Number_tag' in df.columns:
        filtered_df = pd.concat([filtered_df, df[df['meta.Serial Number_tag'] == serial]])

    # Check if the 'meta.serial_number_tag' column exists and filter by it
    if 'meta.serial_number_tag' in df.columns:
        filtered_df = pd.concat([filtered_df, df[df['meta.serial_number_tag'] == serial]])

    return filtered_df