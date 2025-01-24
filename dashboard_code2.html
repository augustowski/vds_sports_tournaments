import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# Load your dataset (replace with the actual path or DataFrame)
@st.cache
def load_data():
    combined_data = pd.read_csv(
        "sports_tournaments/combined_data.csv"
    )  # Replace with actual dataset
    combined_data["year"] = pd.to_numeric(combined_data["year"], errors="coerce")
    combined_data["country_name"] = combined_data["country_name"].fillna("Unknown")
    return combined_data


# Load data
data = load_data()

# Sidebar filters
st.sidebar.header("Filters")

# Add buttons for selecting/deselecting all countries
if st.sidebar.button("Select All Countries"):
    selected_countries = list(data["country_name"].unique())
elif st.sidebar.button("Deselect All Countries"):
    selected_countries = []
else:
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        options=data["country_name"].unique(),
        default=data["country_name"].unique(),
    )

selected_years = st.sidebar.slider(
    "Select Year Range",
    min_value=int(data["year"].min()),
    max_value=int(data["year"].max()),
    value=(int(data["year"].min()), int(data["year"].max())),
)

selected_events = st.sidebar.multiselect(
    "Select Events",
    options=data["event_title"].unique(),
    default=data["event_title"].unique()[:2],  # Default to first 2 events
)

selected_tournament_type = st.sidebar.multiselect(
    "Select Tournament Type",
    options=data["tournament_type"].unique(),
    default=data["tournament_type"].unique(),
)

selected_gender_category = st.sidebar.multiselect(
    "Select Gender Category",
    options=data["gender_category"].unique(),
    default=data["gender_category"].unique(),
)

# Filter data
filtered_data = data[
    (data["country_name"].isin(selected_countries))
    & (data["year"].between(*selected_years))
    & (data["event_title"].isin(selected_events))
    & (data["tournament_type"].isin(selected_tournament_type))
    & (data["gender_category"].isin(selected_gender_category))
]

# Dashboard title
st.title("Event Comparison Dashboard")

# Display filtered data
st.write("Filtered Data:", filtered_data)

# Visualization: Compare Results for Two Events
if len(selected_events) == 2:
    event1, event2 = selected_events

    # Data for each event
    event1_data = filtered_data[filtered_data["event_title"] == event1]
    event2_data = filtered_data[filtered_data["event_title"] == event2]

    # Plot results using Plotly for interactivity
    fig = px.bar(
        filtered_data,
        x="year",
        y="rank_position",
        color="event_title",
        title=f"Comparison of {event1} and {event2}",
        labels={"rank_position": "Rank Position", "year": "Year"},
        barmode="group",
    )
    st.plotly_chart(fig)
else:
    st.warning("Please select exactly 2 events to compare.")

# Additional country participation summary
st.subheader("Country Participation Over the Years")
country_year_counts = filtered_data.pivot_table(
    index="country_name", columns="year", aggfunc="size", fill_value=0
)

# Country Participation Heatmap
fig_heatmap = px.imshow(
    country_year_counts,
    labels=dict(x="Year", y="Country", color="Event Count"),
    title="Country Participation Heatmap",
    color_continuous_scale="YlGnBu",
)
st.plotly_chart(fig_heatmap)

# Display top winning countries
st.subheader("Top Winning Countries")
top_countries = filtered_data[filtered_data["rank_position"] == 1]
win_counts = top_countries["country_name"].value_counts().reset_index()
win_counts.columns = ["Country", "Wins"]
st.write(win_counts)


# ### 1. Describe your modeling approach
# Our approach utilizes **interactive data visualization** to analyze sports tournament participation trends:

# - **Data Loading and Cleaning**:
#   We merged datasets from Olympic Games and FIFA World Cups into a unified dataset, handling missing values and ensuring consistency in column naming.

# - **Dynamic Filtering**:
#   To enable user-driven exploration, we implemented filters for country, event, year range, tournament type, and gender category. This ensures targeted analysis tailored to the user's needs.

# - **Interactive Visualizations**:
#   Using **Plotly**, we generated interactive histograms and heatmaps. These charts display event distributions and country participation trends across years, providing insights at a glance.

# - **Ease of Interaction**:
#   Buttons like "Select All Countries" or "Deselect All Countries" streamline the filtering process, enhancing user experience.

# ---

# ### 2. How would you increase trust of your customers/colleagues in your modeling approach by using data visualization?

# - **Transparent Data Exploration**:
#   Interactive data tables and visualizations allow users to
