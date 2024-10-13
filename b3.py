import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title = 'DASHBOARD FINANCEIRO - AÇÕES',
    layout = 'wide'
)

st.header('**Painel de Preço de Fechamento e Dividendos - Ações Brasileiras da B3**')

ticker = st.text_input('Digite o ticker da ação', 'BBAS3')
empresa = yf.Ticker(f"{ticker}.SA")

tickerDF = empresa.history(period = '1d', 
                           start = '2023-01-01',
                           end = '2024-10-10')

#col1, col2, col3 = st.columns([1,1,1])
col1, col3 = st.columns([1,1])
with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")
#with col2:
#    st.write(f"**Mercado:** {empresa.info['industryDisp']}")
#     st.write(f"**Mercado:** {empresa.info['industry']}")
with col3:
    st.write(f"**Preço Atual:** R$ {empresa.info['currentPrice']}")

st.line_chart(tickerDF.Close)
st.bar_chart(tickerDF.Dividends)
