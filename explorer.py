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
chart.feature("tooltip", True)

vchart = VizzuChart(chart, key="vizzu")

st.set_page_config(
	page_title="Powerade VB Tippverseny Data Explorer",
	layout="wide",
)

st.markdown("### Powerade VB Tippverseny Data Explorer :heart_eyes::soccer::trophy::blue_heart:")
st.markdown("Mobilon nem az igazi, laptopon jobb.")
st.markdown("Kattingasd bátran a gombokat, simogasd az egérrel a grafikon elemeit.")
st.markdown("Van még két másik cucc is, amit a bal oldali menüben érsz el, mobilon a bal felső sarokban lévő nyílra kattints!")

rounds: list[str] = st.multiselect(
    "Rounds",
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
)

col1, col2, col3, col4 = st.columns(4)

compare_by = col4.radio("Compare by", ["Names", "Matches"])
show = col1.radio("Show",["Total","by Stages"])
order = col3.radio("Order items", ["ABC / Time", "Value"])
split = col2.radio("Split by stages", ["True","False"],index=1, help="Switch to by Stages to make this work")


filter = " || ".join([f"record['Round'] == '{rounds}'" for rounds in rounds])
#title =  ", ".join(rounds) + by f"{compare_by}

if show == "Total":
	measure:str = "Points"
	lightness = None

else: 
	measure = ["Round","Points"]
	lightness = ["Round"]

if compare_by == "Names":
	y = ["Name"]
	x = measure
	bottomPadding = None
	position = None
	
else:
	y = measure
	x = ["Match"]
	bottomPadding = "10em"
	position = "top"


config = {
	#  "title": title,
	"y": y,
	"label": ["Points"],
	"x": x,
	"lightness" : lightness,
	"split" : split,
}

style = {'plot' : {
			'paddingLeft' : '10em', 
			'paddingBottom' : bottomPadding,
			'yAxis' :{ 'title' :{ 'color' : '#00000000'}},
			'xAxis' :{ 'title' :{ 'color' : '#00000000'},'label': {'angle': '-45deg'}},
			'marker' :{ 'label' :{ 'position' : position}},
			},
			'legend' : {'width' : '12em'},
		
}
    
if order == "ABC / Time":
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
