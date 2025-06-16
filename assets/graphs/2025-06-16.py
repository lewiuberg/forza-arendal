import plotly.graph_objects as go

år = ["2021", "2022", "2023", "2024", "2025"]
mål_for = [2.1, 2.2, 2.1, 1.3, 1.9]
mål_mot = [1.4, 1.4, 1.4, 1.5, 1.4]
poengsnitt = [1.84, 2.33, 1.69, 1.3, 1.3]
seiersprosent = [50, 75, 50, 38, 20]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=år,
        y=mål_for,
        mode="lines+markers",
        name="Mål for (snitt)",
        marker_color="blue",
    )
)
fig.add_trace(
    go.Scatter(
        x=år,
        y=mål_mot,
        mode="lines+markers",
        name="Mål mot (snitt)",
        marker_color="red",
    )
)
fig.add_trace(
    go.Scatter(
        x=år,
        y=poengsnitt,
        mode="lines+markers",
        name="Poengsnitt",
        marker_color="magenta",
    )
)
fig.add_trace(
    go.Bar(
        x=år,
        y=seiersprosent,
        name="Seiersprosent",
        yaxis="y2",
        opacity=0.4,
        marker_color="darkgreen",  # Set bar color to dark green
    )
)

fig.update_layout(
    title="Arendal 2021-2025",
    title_y=0.85,  # Move title further down (default is 0.95)
    xaxis_title="Sesong",
    yaxis={"title": "Snitt (mål/poeng)"},
    yaxis2={
        "title": "Seiersprosent",
        "overlaying": "y",
        "side": "right",
        "range": [0, 100],
    },
    legend={
        "x": 0.5,
        "y": -0.225,
        "xanchor": "center",
        "yanchor": "top",
        "orientation": "h",
        "font": {"size": 14},
        "bgcolor": "rgba(0,0,0,0)",  # transparent legend background
    },
    bargap=0.2,
)

# fig.show()
fig.write_json("docs/assets/graphs/2025-06-16.json")
