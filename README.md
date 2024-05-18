# AirbnbAnalysis-Streamlit-and-PowerBI

# Enhanced Airbnb Listings Map

This Streamlit application provides an interactive map of Airbnb listings with various filters such as  property type, review scores, country, and availability. The application uses data from a database and visualizes it using Pydeck.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive map with ScatterplotLayer
- Filters for  property type, review scores, country, and host location
- Tooltips showing detailed information for each listing
- Customizable map styles

## Installation

To run this application, you need Python and some required packages. Follow these steps to set up the project:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ArovincyJenifer/AirbnbAnalysis-Streamlit-and-PowerBI.git
    cd airbnb-map
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt

    import json
import csv
import pandas as pd
import pydeck as pdk

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st

from sqlalchemy import create_engine
import sqlalchemy
from streamlit import connections
import pymysql
import streamlit as st
import plotly.graph_objects as go
    ```

## Usage

1. **Set up your database connection:**

    Ensure you have the correct database connection string in your script:

    ```python
    engine = create_engine('your_database_connection_string')
    ```

2. **Run the application:**

    ```bash
    streamlit run airbnb.py
    ```

3. **Interact with the application:**

    Open the URL provided by Streamlit in your web browser, and use the sidebar filters to explore the Airbnb listings on the map.

## Configuration

- **Database Connection:**

    Update the `your_database_connection_string` in the script to point to your database.

- **Map Style:**

    You can change the map style by modifying the `map_style` parameter in the `pdk.Deck` constructor. Some available Mapbox styles include:
    - `mapbox://styles/mapbox/streets-v11`
    - `mapbox://styles/mapbox/outdoors-v11`
    - `mapbox://styles/mapbox/light-v10`
    - `mapbox://styles/mapbox/dark-v10`
    - `mapbox://styles/mapbox/satellite-v9`
    - `mapbox://styles/mapbox/satellite-streets-v11`

## Contributing

Contributions are welcome! 

##Learnings Takeaway: Built a map in pdkDeck Layer which is very useful to highlight the countries,cities.
