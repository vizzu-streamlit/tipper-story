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

vchart = VizzuChart(chart, key="vizzu")

#speed = st.select_slider("Speed", options=("Slow", "Medium", "Fast"), value="Medium")

config = {
    "y": ["Name"],
    "label": ["Points"],
    "x": ["Points"],
	"color" : ["Name"],
	"sort": "byValue"
}

style = {'plot' : 
			{'paddingLeft' : '10em',
			'yAxis' :{ 'title' :{ 'color' : '#00000000'}},
			'xAxis' :{ 'title' :{ 'color' : '#00000000'}},
			},
			'legend' : {'width' : '12em'},
		
}

st.set_page_config(
	page_title="Powerade VB Tippverseny Bar Chart Race",
	layout="wide",
)


st.title("Powerade VB Tippverseny Bar Chart Race")

st.markdown("Here you can just lay back and enjoy the show. If you move to the other pages and get back, the race restarts. Will try to add interactivity later, e.g. to set the speed.")

speed = "Medium"
if speed == "Slow":
	wait = 2
elif speed == "Medium":
	wait = 1
else: 
	wait = 0.2

for i in range(1, 57):
	j = 19*i-2
	f = data_frame.loc[j].at["Match"],
	config["title"] = f"{f}" 
	vchart.animate(
		Data.filter(f"parseInt(record.Match_no) <= {i}"),
		Config(config),
		Style(style),
		duration=0.7,
		delay = 0,
		x={"easing": "linear", "delay": 0},
		y={"delay": 0},
		show={"delay": 0},
		hide={"delay": 0},
		title={"duration": 0, "delay": 0},
)

output = vchart.show()
st.write(output)