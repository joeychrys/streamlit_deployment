import streamlit as st
import yfinance as yf
from ta import volume, trend


st.set_page_config(page_title='Technical Analysis',page_icon='📈', layout='wide')
hide_streamlit_style = """
            <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {

                visibility: hidden;
               
               }
            .stDeployButton {display:none;}
            footer {

                visibility: hidden;

                }
            footer:after {

	            content:'Data Source: Yahoo Finance'; 
	            visibility: visible;
	            display: block;
	            position: relative;
	            #background-color: red;
	            padding: 5px;
	            top: 2px;

                }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

stock = st.sidebar.text_input(label="Ticker",value='AAPL')

def get_data(start):
    ticker = yf.Ticker(stock)
    try:
        df = ticker.history(period='max', start=start)
    except:
        pass
    return df

list_of_indicator_types = ['Volume', 'Trend']
volumn_types = ['Volume','Force Index']
trend_types = ["Simple Moving Average", "Exponential Moving Average"]

indicator_types = st.sidebar.selectbox(label='Indicator Type', options = list_of_indicator_types)

st.sidebar.success('All charts are interactive!')

if indicator_types == 'Volume':
    indicator = st.selectbox(label='Indicator', options=volumn_types,key=0)

    start = st.text_input(label='Start Year', value = '2018')
    start = f'{start}-01-01'

    

    df = get_data(start)

    if indicator == 'Volume':
        df = df[['Close','Volume']]

        price_vs_time = st.line_chart(data= df['Close'], width=500, height=400)
        volume_vs_time = st.bar_chart(data=df['Volume'], width=500, height=150)

        df = df.to_csv()
        st.download_button(label=f'Download Data',data=df,file_name=f'{stock}.csv')

    if indicator == 'Force Index':
        window_slider_expander = st.expander(label='Force Index Parameters')
        window_slider = window_slider_expander.slider(label='Window', value=13, min_value=1, max_value=20)
        
        df[f'fi_{window_slider}'] = volume.force_index(close=df['Close'],volume=df['Volume'], window=window_slider)
        
        df = df[['Close','Volume',f'fi_{window_slider}']]

        price_vs_time = st.line_chart(data= df['Close'], width=500, height=400)
        fi_vs_time = st.area_chart(data= df[f'fi_{window_slider}'],width=500, height=200)

        df = df.to_csv()
        st.download_button(label=f'Download Data',data=df,file_name=f'{stock}.csv')

if indicator_types == 'Trend':
    indicator = st.selectbox(label='Indicator', options=trend_types, key=1)

    start = st.text_input(label='Start Year', value = '2018')
    start = f'{start}-01-01'

    df = get_data(start)
    if indicator == 'Simple Moving Average':

        window_slider_expander = st.expander(label='SMA Parameters')
        window_slider_1 = window_slider_expander.slider(label='Window 1', value=30, min_value=1, max_value=200)
        window_slider_2 = window_slider_expander.slider(label='Window 2', value=100, min_value=1, max_value=200)

        df[f'sma{window_slider_1}'] = trend.sma_indicator(close=df['Close'], window=window_slider_1)
        df[f'sma{window_slider_2}'] = trend.sma_indicator(close=df['Close'], window=window_slider_2)        
        
        df = df[['Close',f'sma{window_slider_1}',f'sma{window_slider_2}']]
        
        sma_vs_time = st.line_chart(data=df, width=500, height=550)

        df = df.to_csv()
        st.download_button(label=f'Download Data',data=df,file_name=f'{stock}.csv')

    if indicator == "Exponential Moving Average":

        window_slider_expander = st.expander(label='EMA Parameters')
        window_slider_1 = window_slider_expander.slider(label='Window 1', value=30, min_value=1, max_value=200)
        window_slider_2 = window_slider_expander.slider(label='Window 2', value=100, min_value=1, max_value=200)

        df[f'ema{window_slider_1}'] = trend.ema_indicator(close=df['Close'], window=window_slider_1)
        df[f'ema{window_slider_2}'] = trend.ema_indicator(close=df['Close'], window=window_slider_2)        
        
        df = df[['Close',f'ema{window_slider_1}',f'ema{window_slider_2}']]
        
        sma_vs_time = st.line_chart(data=df, width=500, height=550)

        df = df.to_csv()
        st.download_button(label=f'Download Data',data=df,file_name=f'{stock}.csv')

