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



#title =  ", ".join(rounds) + by f"{compare_by}

config = {
    "y": ["Name"],
    "label": ["Points"],
    "x": ["Points"],
	"color" : ["Name"],
}

style = {'plot' : 
			{'paddingLeft' : '10em', 'xAxis': {'label': {'angle': '2.5'}},
			'yAxis' :{ 'title' :{ 'color' : '#00000000'}},
		#	'marker' :{ 'label' :{ 'position' : 'top'}},
			},
			'legend' : {'width' : '12em'},
		
}
    
for i in range(1, 56):
    config["title"] = f"Music Revenue by Format {i}"
    vchart.animate(
        Data.filter(f"parseInt(record.Match_no.) == {i}"),
        Config(config),
		Style(style),
        duration=0.2,
        x={"easing": "linear", "delay": 0},
        y={"delay": 0},
        show={"delay": 0},
        hide={"delay": 0},
        title={"duration": 0, "delay": 0},
    )


output = vchart.show()
st.write(output)