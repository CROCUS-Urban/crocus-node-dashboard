CROCUS_NODES = {
    'BIG CROCUS Node (W0A0)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        },
        'Sap Flow Sensors': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': [
                "uncorrected_inner",
                "uncorrected_outer",
                "battery_voltage",
                "signal.rssi",
                "signal.snr",
                "signal.spreadingfactor"
            ],
            'serial_numbers': [
                "SX61NA0U",
                "SX61NA09",
                "SX61NA0I"
            ]
        },        
        'MFR Nodes': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': {
                'ATH-VPD': [
                    "air_temperature",
                    "barometric_pressure",
                    "relative_humidity",
                    "vapour_pressure_deficit"
                ],
                'HFP01-05': [
                    "heat_flux"
                ],
                'SN500': [
                    "in_longwave",
                    "in_shortwave",
                    "out_longwave",
                    "out_shortwave"
                ],
                'Teros54': [
                    "temp_d1",
                    "temp_d2",
                    "temp_d3",
                    "temp_d4",
                    "vwc_d1",
                    "vwc_d2",
                    "vwc_d3",
                    "vwc_d4"
                ],
                'Hydros21': [
                    "water_conductivity",
                    "water_depth",
                    "water_temperature"
                ],                
                'MFR Node': [
                    "battery_voltage",
                    "digital_count",
                    "frequency",
                    "signal.rssi",
                    "signal.snr",
                    "signal.spreadingfactor",
                    "solar_voltage",
                    "uptime",
                    "voltage_adc"
                ]
            },
            'serial_numbers': [
                "MNLA4O10A",
                "MNLA4O10B",
                "MNLA4O10C"
            ]
        }
    },
    'CCICS CROCUS Node (W08B)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        }
    },
    'CSU CROCUS Node (W08E)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        },
        'Sap Flow Sensors': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': [
                "uncorrected_inner",
                "uncorrected_outer",
                "battery_voltage",
                "signal.rssi",
                "signal.snr",
                "signal.spreadingfactor"
            ],
            'serial_numbers': [
                "SX61NA0D (Cottonwood)",
                "SX61NA0W (Cottonwood)",
                "SX61NA0E (Cottonwood)",
                "SX61NA0P (American Elm)",
                "SX61NA0H (American Elm)",
                "SX61NA08 (Maple)",
                "SX61NA0T (Maple)",
                "SX61NA0A (Maple)"
            ]
        },
        'MFR Nodes': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': {
                'ATH-VPD': [
                    "air_temperature",
                    "barometric_pressure",
                    "relative_humidity",
                    "vapour_pressure_deficit"
                ],
                'HFP01-05': [
                    "heat_flux"
                ],
                'SN500': [
                    "in_longwave",
                    "in_shortwave",
                    "out_longwave",
                    "out_shortwave"
                ],
                'Teros54': [
                    "temp_d1",
                    "temp_d2",
                    "temp_d3",
                    "temp_d4",
                    "vwc_d1",
                    "vwc_d2",
                    "vwc_d3",
                    "vwc_d4"
                ],
                'Hydros21': [
                    "water_conductivity",
                    "water_depth",
                    "water_temperature"
                ],
                'MFR Node': [
                    "battery_voltage",
                    "digital_count",
                    "frequency",
                    "signal.rssi",
                    "signal.snr",
                    "signal.spreadingfactor",
                    "solar_voltage",
                    "uptime",
                    "voltage_adc"
                ]
            },
            'serial_numbers': [
                "MNLA4O102 (Non-Prairie)",
                "MNLA4O103 (Prairie)"
            ]
        }
    },
    'NEIU CROCUS Node (W08D)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",                
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        },
        'Sap Flow Sensors': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': [
                "uncorrected_inner",
                "uncorrected_outer",
                "battery_voltage",
                "signal.rssi",
                "signal.snr",
                "signal.spreadingfactor"
            ],
            'serial_numbers': [
                "SX61NA0C (White Oak)",
                "SX61NA0X (White Oak)",
                "SX61NA0V (American Elm)",
                "SX61NA01 (Sugar Maple)",
                "SX61NA0J (Sugar Maple)",
                "SX61NA0N (Sugar Maple)"
            ]
        },
        'MFR Nodes': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': {
                'ATH-VPD': [
                    "air_temperature",
                    "barometric_pressure",
                    "relative_humidity",
                    "vapour_pressure_deficit"
                ],
                'HFP01-05': [
                    "heat_flux"
                ],
                'SN500': [
                    "in_longwave",
                    "in_shortwave",
                    "out_longwave",
                    "out_shortwave"
                ],
                'Teros54': [
                    "temp_d1",
                    "temp_d2",
                    "temp_d3",
                    "temp_d4",
                    "vwc_d1",
                    "vwc_d2",
                    "vwc_d3",
                    "vwc_d4"
                ],
                'MFR Node': [
                    "battery_voltage",
                    "digital_count",
                    "frequency",
                    "signal.rssi",
                    "signal.snr",
                    "signal.spreadingfactor",
                    "solar_voltage",
                    "uptime",
                    "voltage_adc"
                ]
            },
            'serial_numbers': [
                "MNLA4O107",
                "MNLA4O108"
            ]
        }
    },
    'NU CROCUS Node (W099)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        },
        'Sap Flow Sensors': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': [
                "uncorrected_inner",
                "uncorrected_outer",
                "battery_voltage",
                "signal.rssi",
                "signal.snr",
                "signal.spreadingfactor"
            ],
            'serial_numbers': [
                "SX61NA0Y (Maple)",
                "SX61NA0F (Maple)",
                "SX61NA07 (Oak)",
                "SX61NA0G (Oak)",
                "SX61NA0L (Maple)",
                "SX61N501 (Maple)"
            ]
        },
        'MFR Nodes': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': {
                'ATH-VPD': [
                    "air_temperature",
                    "barometric_pressure",
                    "relative_humidity",
                    "vapour_pressure_deficit"
                ],
                'HFP01-05': [
                    "heat_flux"
                ],
                'SN500': [
                    "in_longwave",
                    "in_shortwave",
                    "out_longwave",
                    "out_shortwave"
                ],
                'Teros54': [
                    "temp_d1",
                    "temp_d2",
                    "temp_d3",
                    "temp_d4",
                    "vwc_d1",
                    "vwc_d2",
                    "vwc_d3",
                    "vwc_d4"
                ],
                'Hydros21': [
                    "water_conductivity",
                    "water_depth",
                    "water_temperature"
                ],                
                'MFR Node': [
                    "battery_voltage",
                    "digital_count",
                    "frequency",
                    "signal.rssi",
                    "signal.snr",
                    "signal.spreadingfactor",
                    "solar_voltage",
                    "uptime",
                    "voltage_adc"
                ]
            },
            'serial_numbers': [
                "MNLA4O104"
            ]
        }
    },
    'UIC CROCUS Node (W096)': {
        'Weather Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-wxt536:*.*',
            'sensors': [
                "wxt.env.temp",
                "wxt.env.humidity",
                "wxt.env.pressure",
                "wxt.rain.accumulation",
                "wxt.wind.speed"
            ]
        },
        'Air Quality Sensors': {
            'plugin': 'registry.sagecontinuum.org/jrobrien/waggle-aqt:*.*',
            'sensors': [
                "aqt.env.temp",
                "aqt.env.humidity",
                "aqt.env.pressure",
                "aqt.gas.co",
                "aqt.gas.no",
                "aqt.gas.no2",
                "aqt.gas.ozone",
                "aqt.particle.pm1",
                "aqt.particle.pm10",
                "aqt.particle.pm2.5"
            ]
        },
        'CO2 and H2O Sensors': {
            'plugin': 'registry.sagecontinuum.org/bhupendraraut/licor-smartflux:*.*',
            'sensors': [
                "co2.absolute_water",
                "co2.absolute_water_offset",
                "co2.density",
                "co2.mg_per_m3",
                "co2.raw",
                "co2.signal_strength",
                "h2o.absolute_water",
                "h2o.absolute_water_offset",
                "h2o.density",
                "h2o.g_per_m3",
                "h2o.raw",
                "co2.mole_fraction",
                "h2o.mole_fraction"
            ]
        },
        'Sonic Sensors': {
            'plugin': 'registry.sagecontinuum.org/bhupendraraut/licor-smartflux:*.*',
            'sensors': [
                "sonic.u",
                "sonic.v",
                "sonic.w"
            ]
        },
        'Sap Flow Sensors': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': [
                "uncorrected_inner",
                "uncorrected_outer",
                "battery_voltage",
                "signal.rssi",
                "signal.snr",
                "signal.spreadingfactor"
            ],
            'serial_numbers': [
                "SX61NA0B (American Elm)",
                "SX61NA0R (Honey Locust)",
                "SX61NA0M (Honey Locust)",
                "SX61NA0S (Maple)",
                "SX61NA0K (Maple)",
                "SX61NA05 (Honey Locust)",
                "SX61NA0O (American Elm)"
            ]
        },
        'MFR Nodes': {
            'plugin': 'registry.sagecontinuum.org/flozano/lorawan-listener:*.*',
            'sensors': {
                'ATH-VPD': [
                    "air_temperature",
                    "barometric_pressure",
                    "relative_humidity",
                    "vapour_pressure_deficit"
                ],
                'HFP01-05': [
                    "heat_flux"
                ],
                'SN500': [
                    "in_longwave",
                    "in_shortwave",
                    "out_longwave",
                    "out_shortwave"
                ],
                'Teros54': [
                    "temp_d1",
                    "temp_d2",
                    "temp_d3",
                    "temp_d4",
                    "vwc_d1",
                    "vwc_d2",
                    "vwc_d3",
                    "vwc_d4"
                ],
                'Hydros21': [
                    "water_conductivity",
                    "water_depth",
                    "water_temperature"
                ],                
                'MFR Node': [
                    "battery_voltage",
                    "digital_count",
                    "frequency",
                    "signal.rssi",
                    "signal.snr",
                    "signal.spreadingfactor",
                    "solar_voltage",
                    "uptime",
                    "voltage_adc"
                ]
            },
            'serial_numbers': [
                "MNLA4O105",
                "MNLA4O106"
            ]
        }
    }
}

DATA_UNITS = {
    "wxt.env.temp": "°C",
    "wxt.env.humidity": "%",
    "wxt.env.pressure": "Pa",
    "wxt.rain.accumulation": "mm",
    "wxt.wind.speed": "m/s",
    "uncorrected_inner": "cm/hr",
    "uncorrected_outer": "cm/hr",
    "battery_voltage": "V",
    "digital_count": "Count",
    "frequency": "Hz",
    "heat_flux": "W/m²",
    "in_longwave": "W/m²",
    "in_shortwave": "W/m²",
    "out_longwave": "W/m²",
    "out_shortwave": "W/m²",
    "relative_humidity": "%",
    "signal.rssi": "dBm",
    "signal.snr": "dB",
    "signal.spreadingfactor": "Factor",
    "solar_voltage": "V",
    "temp_d1": "°C",
    "temp_d2": "°C",
    "temp_d3": "°C",
    "temp_d4": "°C",
    "total_net_radiation": "W/m²",
    "uptime": "s",
    "vapour_pressure_deficit": "kPa",
    "voltage_adc": "uV",
    "vwc_d1": "%",
    "vwc_d2": "%",
    "vwc_d3": "%",
    "vwc_d4": "%",
    "water_conductivity": "dS/m",
    "water_depth": "mm",
    "water_temperature": "°C",
    "aqt.env.temp": "°C",
    "aqt.env.humidity": "%",
    "aqt.env.pressure": "Pa",    
    "aqt.gas.co": "ppm",
    "aqt.gas.no": "ppm",
    "aqt.gas.no2": "ppm",
    "aqt.gas.ozone": "ppm",
    "aqt.particle.pm1": "µg/m³",
    "aqt.particle.pm10": "µg/m³",
    "aqt.particle.pm2.5": "µg/m³",
    "co2.absolute_water": "",
    "co2.absolute_water_offset": "",
    "co2.density": "mg/m³",
    "co2.mg_per_m3": "mg/m³",
    "co2.raw": "",
    "co2.signal_strength": "",
    "h2o.absolute_water": "",
    "h2o.absolute_water_offset": "",
    "h2o.density": "g/m³",
    "h2o.g_per_m3": "g/m³",
    "h2o.raw": "",
    "co2.mole_fraction": "ppm",
    "h2o.mole_fraction": "ppm",
    "sonic.u": "m/s",
    "sonic.v": "m/s",
    "sonic.w": "m/s"
}

NODE_PORTAL_LINKS = {
    'UIC CROCUS Node (W096)': 'https://crocus.sagecontinuum.org/node/W096',
    'BIG CROCUS Node (W0A0)': 'https://crocus.sagecontinuum.org/node/W0A0',
    'CCICS CROCUS Node (W08B)': 'https://crocus.sagecontinuum.org/node/W08B',
    'CSU CROCUS Node (W08E)': 'https://crocus.sagecontinuum.org/node/W08E',
    'NEIU CROCUS Node (W08D)': 'https://crocus.sagecontinuum.org/node/W08D',
    'NU CROCUS Node (W099)': 'https://crocus.sagecontinuum.org/node/W099'
}

# Mapping of Sensor IDs to Full Sensor Names for MFR Nodes
SENSOR_FULL_NAMES = {
    'ATH-VPD': 'ATH Temperature and Relative Humidity Sensors',
    'HFP01-05': 'Heat Flux Sensor',
    'SN500': 'Net Radiometer',
    'Teros54': 'TEROS 54 Soil Moisture Profile Probe',
    'Hydros21': 'HYDROS 21 Conductivity, Temperature, Depth Sensor',
    'MFR Node': 'MFR Node'
}
