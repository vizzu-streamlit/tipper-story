import pandas as pd
import streamlit as st
from ipyvizzu.animation import Config, Data, Style
from ipyvizzu.chart import Chart

from streamlit_vizzu import VizzuChart

data_frame = pd.read_csv("https://raw.githubusercontent.com/vizzu-streamlit/tipper-story/main/tipper.csv")
data = Data()
data.add_data_frame(data_frame)

chart = Chart(width="100%", height="400px", display="manual")

chart.animate(data)
chart.feature("tooltip", True)

vchart = VizzuChart(chart, key="vizzu")

rounds: list[str] = st.multiselect(
    "Rounds",
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
)

col1, col2, col3, col4 = st.columns(4)

compare_by = col1.radio("Compare by", ["Name", "Match"])
show = col2.radio("Show",["Total","Stages"])
order = col3.radio("Order items", ["Alphabetically / by time", "By value"])
split = col4.radio("Split items", ["True","False"],index=1)


filter = " || ".join([f"record['Round'] == '{rounds}'" for rounds in rounds])
#title =  ", ".join(rounds) + by f"{compare_by}

if show == "Total":
	measure:str = "Points"
	lightness = None

	
else: #show == "Stages":
	measure = ["Round","Points"]
	lightness = ["Round"]

if compare_by == "Name":
    y = ["Name"]
    x = measure
	
else:# compare_by == "Match":
    y = measure
    x = ["Match"]


config = {
  #  "title": title,
    "y": y,
    "label": ["Points"],
    "x": x,
	"lightness" : lightness,
	"split" : split,
}

style = {
	'plot' : {'paddingLeft' : '10em', 'xAxis': {'label': {'angle': '2.5'}},
			#'marker' :{ 'label' :{ 'position' : 'top'}}
			},
	'legend' : {'width' : '12em'},
}
    
if order == "Alphabetically / by time":
    config["sort"] = "none"
else:
    config["sort"] = "byValue"


if split == "False":
    config["split"] = False
else:
    config["split"] = True
	
vchart.animate(Data.filter(filter), Config(config), Style(style), delay=0.1)


output = vchart.show()
st.write(output)
