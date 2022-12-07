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

rounds: list[str] = st.multiselect(
    "Rounds",
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
    ["Group stage 1", "Group stage 2", "Group stage 3", "Round of 16"],
)

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

f = data_frame.loc[1].at["Match"]
st.write(f)

for i in range(1, 57):
	j = 18*i
	f = data_frame.loc[j].at["Match"],
	config["title"] = f"{f}" 
	vchart.animate(
		Data.filter(f"parseInt(record.Match_no) <= {i}"),
		Config(config),
		Style(style),
		duration=0.3,
		delay = 0.1,
		x={"easing": "linear", "delay": 0},
		y={"delay": 0},
		show={"delay": 0},
		hide={"delay": 0},
		title={"duration": 0, "delay": 0},
)

output = vchart.show()
st.write(output)