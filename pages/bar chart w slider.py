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

st.title("Powerade VB Tippverseny Interactive Bar Chart")

st.markdown("Here you can select a match with a slider and the chart will show the results of the betting competition up to that match. After clicking on the slider, you can move back and forth with the arrow buttons to see how the race standings changed after each match.)

position = st.slider("Pick a match", min_value=(1), max_value=56, value=1)

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
			},
			'legend' : {'width' : '12em'},		
}

f = data_frame.loc[19*position-2].at["Match"],
config["title"] = f"{f}"
vchart.animate(
	Data.filter(f"parseInt(record.Match_no) <= {position}"),
	Config(config),
	Style(style),
	duration=0.5,
	delay = 0.01,
	x={"easing": "linear", "delay": 0},
	y={"delay": 0},
	show={"delay": 0},
	hide={"delay": 0},
	title={"duration": 0, "delay": 0},
)

output = vchart.show()
st.write(output)