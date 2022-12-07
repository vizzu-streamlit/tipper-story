import pandas as pd
import streamlit as st
from ipyvizzu.animation import Config, Data, Style
from ipyvizzu.chart import Chart

from streamlit_vizzu import VizzuChart

data_frame = pd.read_csv("https://raw.githubusercontent.com/vizzu-streamlit/tipper-story/main/tipper.csv")
data = Data()
data.add_data_frame(data_frame)

chart = Chart(width="100%", height="360px", display="manual")

chart.animate(data)

vchart = VizzuChart(chart, key="vizzu")

rounds: list[str] = st.multiselect(
    "Rounds",
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
)

col1, col2, col3 = st.columns(3)

compare_by = col1.radio("Compare by", ["Name", "Match", "Both"])
show = col2.radio("Show",["Total","Stages","Match"])
order = col3.radio("Order items", ["Alphabetically / by time", "By value"])
split = col4.radio("Split items", ["False","True"])


filter = " || ".join([f"record['Round'] == '{rounds}'" for rounds in rounds])
#title =  ", ".join(rounds) + by f"{compare_by}

if show == "Total":
	measure = ["Points"]
	config["lightness"] = None
	config["color"] = None
	
elif show == "Stage":
	measure = ["Stage","Points"]
	config["lightness"] = ["Stage"]
	config["color"] = None
else
	measure = ["Stage","Match","Points"]
	config["lightness"] = ["Stage"]
	config["color"] = ["Match"]


if compare_by == "Name":
    y = ["Name"]
    x = [measure]
	
else:# compare_by == "Match":
    y = [measure]
    x = ["Match"]


config = {
    "title": title,
    "y": y,
    "label": ["Points"],
    "x": x,
}

if coords == "Polar (mobile)":
    config["coordSystem"] = "polar"
else:
    config["coordSystem"] = "cartesian"
    
if order == "Alphabetically / by time":
    config["sort"] = "none"
else:
    config["sort"] = "byValue"

vchart.animate(Data.filter(filter), Config(config), delay=0.1)
output = vchart.show()

st.write(output)
