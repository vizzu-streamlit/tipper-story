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
		#	'marker' :{ 'label' :{ 'position' : 'top'}},
			},
			'legend' : {'width' : '12em'},
		
}

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
		duration=0.5,
		delay = 1,
		x={"easing": "linear", "delay": 0},
		y={"delay": 0},
		show={"delay": 0},
		hide={"delay": 0},
		title={"duration": 0, "delay": 0},
)

output = vchart.show()
st.write(output)