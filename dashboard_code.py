# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from ipywidgets import interact, widgets


# import matplotlib.pyplot as plt


# # Load your dataset (replace with the actual path or DataFrame)
# @st.cache
# def load_data():
#     combined_data = pd.read_csv(
#         "sports_tournaments\combined_data.csv"
#     )  # Replace with actual dataset
#     combined_data["year"] = pd.to_numeric(combined_data["year"], errors="coerce")
#     combined_data["country_name"] = combined_data["country_name"].fillna("Unknown")
#     return combined_data


# # Load data
# data = load_data()

# # Sidebar filters
# st.sidebar.header("Filters")
# selected_countries = st.sidebar.multiselect(
#     "Select Countries",
#     options=data["country_name"].unique(),
#     default=data["country_name"].unique(),
# )

# selected_years = st.sidebar.slider(
#     "Select Year Range",
#     min_value=int(data["year"].min()),
#     max_value=int(data["year"].max()),
#     value=(int(data["year"].min()), int(data["year"].max())),
# )

# selected_events = st.sidebar.multiselect(
#     "Select Events",
#     options=data["event_title"].unique(),
#     default=data["event_title"].unique()[:2],  # Default to first 2 events
# )

# # Filter data
# filtered_data = data[
#     (data["country_name"].isin(selected_countries))
#     & (data["year"].between(*selected_years))
#     & (data["event_title"].isin(selected_events))
# ]

# # Dashboard title
# st.title("Event Comparison Dashboard")

# # Display filtered data
# st.write("Filtered Data:", filtered_data)

# # Visualization: Compare Results for Two Events
# if len(selected_events) == 2:
#     event1, event2 = selected_events

#     # Data for each event
#     event1_data = filtered_data[filtered_data["event_title"] == event1]
#     event2_data = filtered_data[filtered_data["event_title"] == event2]

#     # Plot results
#     fig, ax = plt.subplots(figsize=(12, 6))
#     ax.bar(event1_data["year"], event1_data["rank_position"], label=event1, alpha=0.6)
#     ax.bar(event2_data["year"], event2_data["rank_position"], label=event2, alpha=0.6)

#     plt.title(f"Comparison of {event1} and {event2}")
#     plt.xlabel("Year")
#     plt.ylabel("Rank Position")
#     plt.legend()
#     st.pyplot(fig)
# else:
#     st.warning("Please select exactly 2 events to compare.")

# # Additional country participation summary
# st.subheader("Country Participation Over the Years")
# country_year_counts = filtered_data.pivot_table(
#     index="country_name", columns="year", aggfunc="size", fill_value=0
# )
# st.dataframe(country_year_counts)

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


# # Load the combined data
# data_path = "sports_tournaments\combined_data.csv"
# combined_data = pd.read_csv(data_path)


# # Filter function
# def filter_data(data, selected_countries=None, selected_events=None, year_range=None):
#     filtered_data = data.copy()

#     if selected_countries:
#         filtered_data = filtered_data[
#             filtered_data["country_name"].isin(selected_countries)
#         ]

#     if selected_events:
#         filtered_data = filtered_data[
#             filtered_data["event_title"].isin(selected_events)
#         ]

#     if year_range:
#         filtered_data = filtered_data[
#             (filtered_data["year"] >= year_range[0])
#             & (filtered_data["year"] <= year_range[1])
#         ]

#     return filtered_data


# # Interactive widgets
# country_widget = widgets.SelectMultiple(
#     options=combined_data["country_name"].unique(),
#     value=["Italy", "Norway"],
#     description="Countries",
# )

# event_widget = widgets.SelectMultiple(
#     options=combined_data["event_title"].unique(),
#     value=["Mixed Doubles", "FIFA World Cup"],
#     description="Events",
# )

# year_range_widget = widgets.IntRangeSlider(
#     value=[2000, 2022],
#     min=int(combined_data["year"].min()),
#     max=int(combined_data["year"].max()),
#     step=1,
#     description="Year Range",
# )


# # Update function for interactive histogram and heatmap
# @interact(countries=country_widget, events=event_widget, year_range=year_range_widget)
# def update_dashboard(countries, events, year_range):
#     filtered_data = filter_data(
#         combined_data,
#         selected_countries=countries,
#         selected_events=events,
#         year_range=year_range,
#     )

#     # Histogram of event distribution by year and tournament type
#     fig_hist = px.histogram(
#         filtered_data,
#         x="year",
#         color="tournament_type",
#         title="Distribution of Events Over the Years by Tournament Type",
#         labels={"year": "Year", "tournament_type": "Tournament Type"},
#         nbins=30,
#         barmode="group",
#     )
#     fig_hist.show()

#     # Heatmap of country participation
#     country_year_counts = filtered_data.pivot_table(
#         index="country_name", columns="year", aggfunc="size", fill_value=0
#     )
#     fig_heatmap = go.Figure(
#         data=go.Heatmap(
#             z=country_year_counts.values,
#             x=country_year_counts.columns,
#             y=country_year_counts.index,
#             colorscale="YlGnBu",
#             colorbar_title="Event Count",
#         )
#     )
#     fig_heatmap.update_layout(
#         title="Country Participation Heatmap", xaxis_title="Year", yaxis_title="Country"
#     )
#     fig_heatmap.show()

#     # Table of countries with the most wins
#     top_countries = filtered_data[filtered_data["rank_position"] == 1]
#     win_counts = top_countries["country_name"].value_counts().reset_index()
#     win_counts.columns = ["Country", "Wins"]

#     fig_table = go.Figure(
#         data=[
#             go.Table(
#                 header=dict(
#                     values=["Country", "Wins"], fill_color="paleturquoise", align="left"
#                 ),
#                 cells=dict(
#                     values=[win_counts["Country"], win_counts["Wins"]],
#                     fill_color="lavender",
#                     align="left",
#                 ),
#             )
#         ]
#     )
#     fig_table.update_layout(title="Top Winning Countries")
#     fig_table.show()


## DASH VERSION

# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from dash import Dash, dcc, html, Input, Output

# # Load the combined data
# data_path = "combined_data.csv"
# combined_data = pd.read_csv("sports_tournaments\combined_data.csv")

# # Initialize Dash app
# app = Dash(__name__)

# # Layout of the dashboard
# app.layout = html.Div(
#     [
#         html.H1("Interactive Event Data Dashboard", style={"textAlign": "center"}),
#         # Dropdown for selecting countries
#         html.Label("Select Country:"),
#         dcc.Dropdown(
#             id="country-dropdown",
#             options=[
#                 {"label": country, "value": country}
#                 for country in combined_data["country_name"].dropna().unique()
#             ],
#             multi=True,
#         ),
#         # Dropdown for selecting event types
#         html.Label("Select Event Type:"),
#         dcc.Dropdown(
#             id="event-dropdown",
#             options=[
#                 {"label": event, "value": event}
#                 for event in combined_data["event_title"].dropna().unique()
#             ],
#             multi=True,
#         ),
#         # Slider for selecting year range
#         html.Label("Select Year Range:"),
#         dcc.RangeSlider(
#             id="year-slider",
#             min=int(combined_data["year"].min()),
#             max=int(combined_data["year"].max()),
#             step=1,
#             marks={
#                 year: str(year)
#                 for year in range(
#                     int(combined_data["year"].min()),
#                     int(combined_data["year"].max()) + 1,
#                     4,
#                 )
#             },
#             value=[int(combined_data["year"].min()), int(combined_data["year"].max())],
#         ),
#         # Histogram output
#         dcc.Graph(id="histogram"),
#     ]
# )


# # Callback to update the histogram based on filters
# @app.callback(
#     Output("histogram", "figure"),
#     [
#         Input("country-dropdown", "value"),
#         Input("event-dropdown", "value"),
#         Input("year-slider", "value"),
#     ],
# )
# def update_histogram(selected_countries, selected_events, year_range):
#     filtered_data = combined_data.copy()

#     if selected_countries:
#         filtered_data = filtered_data[
#             filtered_data["country_name"].isin(selected_countries)
#         ]

#     if selected_events:
#         filtered_data = filtered_data[
#             filtered_data["event_title"].isin(selected_events)
#         ]

#     filtered_data = filtered_data[
#         (filtered_data["year"] >= year_range[0])
#         & (filtered_data["year"] <= year_range[1])
#     ]

#     fig = px.histogram(
#         filtered_data,
#         x="year",
#         color="tournament_type",
#         title="Distribution of Events Over the Years by Tournament Type",
#         labels={"year": "Year", "tournament_type": "Tournament Type"},
#         nbins=30,
#         barmode="group",
#     )

#     return fig


# # Run the app
# if __name__ == "__main__":
#     from werkzeug.serving import run_simple

#     run_simple("localhost", 8050, app, use_reloader=False, use_debugger=True)


# ## PLOTLY VERSION

# combined_data = pd.read_csv("sports_tournaments\combined_data.csv")


# # Filter function
# def filter_data(data, selected_countries=None, selected_events=None, year_range=None):
#     filtered_data = data.copy()

#     if selected_countries:
#         filtered_data = filtered_data[
#             filtered_data["country_name"].isin(selected_countries)
#         ]

#     if selected_events:
#         filtered_data = filtered_data[
#             filtered_data["event_title"].isin(selected_events)
#         ]

#     if year_range:
#         filtered_data = filtered_data[
#             (filtered_data["year"] >= year_range[0])
#             & (filtered_data["year"] <= year_range[1])
#         ]

#     return filtered_data


# # Interactive widgets
# country_widget = widgets.SelectMultiple(
#     options=combined_data["country_name"].unique(),
#     value=["Italy", "Norway"],
#     description="Countries",
# )

# event_widget = widgets.SelectMultiple(
#     options=combined_data["event_title"].unique(),
#     value=["Mixed Doubles", "FIFA World Cup"],
#     description="Events",
# )

# year_range_widget = widgets.IntRangeSlider(
#     value=[2000, 2022],
#     min=int(combined_data["year"].min()),
#     max=int(combined_data["year"].max()),
#     step=1,
#     description="Year Range",
# )


# @interact(countries=country_widget, events=event_widget, year_range=year_range_widget)
# def update_histogram(countries, events, year_range):
#     filtered_data = filter_data(
#         combined_data,
#         selected_countries=countries,
#         selected_events=events,
#         year_range=year_range,
#     )

#     fig = px.histogram(
#         filtered_data,
#         x="year",
#         color="tournament_type",
#         title="Distribution of Events Over the Years by Tournament Type",
#         labels={"year": "Year", "tournament_type": "Tournament Type"},
#         nbins=30,
#         barmode="group",
#     )

#     fig.show()
