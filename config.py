CROCUS_NODES = {
    'CSU CROCUS Node (W08E)': {
        'CROCUS Node': [
            "env.temperature", 
            "env.relative_humidity", 
            "env.pressure", 
            "env.raingauge.event_acc"
        ],
        'Sap Flow Sensors': [
            "uncorrected_inner", 
            "uncorrected_outer", 
            "battery_voltage", 
            "signal.rssi", 
            "signal.snr", 
            "signal.spreadingfactor"
        ]
    },
    'NEIU CROCUS Node (W08D)': {
        'CROCUS Node': [
            "env.temperature", 
            "env.relative_humidity", 
            "env.pressure", 
            "env.raingauge.event_acc",
            "aqt.gas.co",
            "aqt.gas.no",
            "aqt.gas.no2",
            "aqt.gas.ozone",
            "aqt.particle.pm1",
            "aqt.particle.pm10",
            "aqt.particle.pm2.5"
        ]
    },
    'NU CROCUS Node (W099)': {
        'CROCUS Node': [
            "env.temperature", 
            "env.relative_humidity", 
            "env.pressure", 
            "env.raingauge.event_acc",
            "aqt.gas.co",
            "aqt.gas.no",
            "aqt.gas.no2",
            "aqt.gas.ozone",
            "aqt.particle.pm1",
            "aqt.particle.pm10",
            "aqt.particle.pm2.5"
        ]
    },
    'UIC CROCUS Node (W096)': {
        'CROCUS Node': [
            "env.temperature", 
            "env.relative_humidity", 
            "env.pressure", 
            "env.raingauge.event_acc",
            "aqt.gas.co",
            "aqt.gas.no",
            "aqt.gas.no2",
            "aqt.gas.ozone",
            "aqt.particle.pm1",
            "aqt.particle.pm10",
            "aqt.particle.pm2.5",
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
            "h2o.mole_fraction",
            "sonic.u",
            "sonic.v",
            "sonic.w"
        ]
    }
}

SAP_FLOW_SERIAL_NUMBERS = [
    "SX61NA0D (Cottonwood)",
    "SX61NA0W (Cottonwood)",
    "SX61NA0E (Cottonwood)",
    "SX61NA0P (American Elm)",
    "SX61NA0H (American Elm)",
    "SX61NA08 (Maple)",
    "SX61NA0T (Maple)",
    "SX61NA0Q (Maple)"
]

DATA_UNITS = {
    "env.temperature": "°C",
    "env.relative_humidity": "%",
    "env.pressure": "Pa",
    "env.raingauge.event_acc": "mm",
    "uncorrected_inner": "cm/hr",
    "uncorrected_outer": "cm/hr",
    "battery_voltage": "V",
    "signal.rssi": "dBm",
    "signal.snr": "dB",
    "signal.spreadingfactor": "",
    "aqt.gas.co": "ppm",
    "aqt.gas.no": "ppm",
    "aqt.gas.no2": "ppm",
    "aqt.gas.ozone": "ppm",
    "aqt.particle.pm1": "µg/m³",
    "aqt.particle.pm10": "µg/m³",
    "aqt.particle.pm2.5": "µg/m³",
    "co2.absolute_water": "g/m³",
    "co2.absolute_water_offset": "g/m³",
    "co2.density": "kg/m³",
    "co2.mg_per_m3": "mg/m³",
    "co2.raw": "ppm",
    "co2.signal_strength": "%",
    "h2o.absolute_water": "g/m³",
    "h2o.absolute_water_offset": "g/m³",
    "h2o.density": "kg/m³",
    "h2o.g_per_m3": "g/m³",
    "h2o.raw": "ppm",
    "co2.mole_fraction": "ppm",
    "h2o.mole_fraction": "ppm",
    "sonic.u": "m/s",
    "sonic.v": "m/s",
    "sonic.w": "m/s"
}

NODE_PORTAL_LINKS = {
    'UIC CROCUS Node (W096)': 'https://crocus.sagecontinuum.org/node/W096',
    'CSU CROCUS Node (W08E)': 'https://crocus.sagecontinuum.org/node/W08E',
    'NEIU CROCUS Node (W08D)': 'https://crocus.sagecontinuum.org/node/W08D',
    'NU CROCUS Node (W099)': 'https://crocus.sagecontinuum.org/node/W099'
}
