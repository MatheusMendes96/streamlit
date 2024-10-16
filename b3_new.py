import streamlit as st
import yfinance as yf
from requests import get
from requests.exceptions import HTTPError

st.set_page_config(
    page_title='DASHBOARD FINANCEIRO - AÇÕES',
    layout='wide'
)

st.header('**Painel de Preço de Fechamento e Dividendos - Ações Brasileiras da B3**')

#ticker = st.text_input('Digite o ticker da ação', 'BBAS3')
ticker = st.text_input('Digite o ticker da ação')
empresa = yf.Ticker(f"{ticker}.SA")

try:
    # Tentando buscar os dados da empresa
    headers = {'User-Agent': 'Mozilla/5.0'}
    empresa_info = get(f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}.SA?modules=summaryProfile', headers=headers)
    empresa_info.raise_for_status()  # Checa se há algum erro de autorização
    empresa_data = empresa.info  # Usando yfinance para acessar info da empresa
except HTTPError as e:
    st.error(f"Erro ao tentar acessar os dados de {ticker}. Detalhes: {e}")
    empresa_data = None

# Exibir informações apenas se os dados forem carregados com sucesso
if empresa_data:
    try:
        tickerDF = empresa.history(period='1d', start='2023-01-01', end='2024-10-14')

        col1, col3 = st.columns([1, 1])
        with col3:
            st.write(f"**Preço Atual:** R$ {empresa_data['currentPrice']}")

        st.line_chart(tickerDF.Close)
        # st.bar_chart(tickerDF.Dividends)  # Opcional: exibir dividendos se houver

    except KeyError as e:
        st.error(f"Erro ao acessar dados históricos ou de preço. Detalhes: {e}")
else:
    st.warning(f"Não foi possível obter informações sobre o ticker {ticker}. Verifique o ticker e tente novamente.")
