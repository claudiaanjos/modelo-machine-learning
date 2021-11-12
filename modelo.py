from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import plotly.graph_objects as go
from fbprophet.plot import add_changepoints_to_plot
import pandas as pd
from datetime import datetime
import holidays
import utils
from fbprophet import Prophet
import fbprophet
from sklearn.metrics import mean_squared_error
import math
import re
import numpy as np

#Dados Disponíveis

path = "sessions.csv"
 
df = pd.read_csv(path, parse_dates=['date'])
print(df.columns)
df.head()

df.describe()

#Valores faltante em cada variável

fig, ax = plt.subplots( figsize=(15,9))
sns.heatmap(df.isna())

df.info()

# Visualizando rapidamente os dados históricos e ao longo do tempo

import matplotlib.pyplot as plt
import seaborn as sns

# criando um df com a data como index

df_data = pd.read_csv(path, parse_dates=['date'], index_col=1)
df_data.head()

# Observando os acessos ao longo de 2 anos aproximadamente

df_data['totals_visits'].resample('D').sum().plot(figsize=(20,5))

# Evolutivo do volume de acessos agrupados por semana

df_data['totals_visits'].resample('W').sum().plot(figsize=(20,5))

# Evolutivo do volume de acessos agrupados por mês

df_data['totals_visits'].resample('M').sum().plot(figsize=(20, 5))

# Analisando a evolução de outras métricas relevantes ao longo do tempo, como visualização de páginas, novas visitas e receita

df_date = df.groupby(['date']).agg({'totals_visits': 'sum', 'totals_pageviews': 'sum',
                                    'totals_newVisits': 'sum', 'totals_totalTransactionRevenue': 'sum'}).reset_index()


fig, ax = plt.subplots(4, figsize=(20, 10), sharex=True)


sns.lineplot(data=df_date, x="date", y="totals_pageviews", ax=ax[0])
sns.lineplot(data=df_date, x="date", y="totals_visits", ax=ax[1])
sns.lineplot(data=df_date, x="date", y="totals_newVisits", ax=ax[2])
sns.lineplot(data=df_date, x="date",
             y="totals_totalTransactionRevenue", ax=ax[3])

fig.show()

# Escolha do modelo de forecast: **Prophet**

# Base de Dados

# O dataframe está na granularidade de Usuário (ID) e acesso (visitStartTime)

df

# Agrupando as métricas relevantes em função da data para estar no formato certo na hora de rodar o modelo

df_date = df.groupby(['date']).agg({'totals_visits': 'sum', 'fullVisitorId': 'count', 'totals_pageviews': 'sum',
                                    'totals_newVisits': 'sum', 'totals_totalTransactionRevenue': 'sum'}).reset_index()
df_date.head()

# Salvando o nome das colunas de target e data para facilitar a execução e criando nossa baseline para o modelo

target = 'totals_visits'
datetime = 'date'
baseline_prophet = df_date[[datetime, target]]
baseline_prophet

# A série temporal e sua tendência mensal

X = baseline_prophet.index.values
Y = baseline_prophet[target]

fig, ax = plt.subplots(1, figsize=(22, 7))

ax = sns.lineplot(x=X, y=Y)
ax.set_title(label="{}".format(target))
baseline_week = Y.resample('W').mean()
baseline_month = Y.resample('M').mean()

ax.plot(baseline_week, label='Tendência')
ax.set_figure
for item in ax.get_xticklabels():
  item.set_rotation(45)
ax.legend()

# Análise unidimensional da variável target totals_visits(acessos)

# Frequência diária
fig, ax = plt.subplots(figsize=(9, 6))

sns.distplot(df_date[target], color='green', kde=False)

# Frequência relativa
fig, ax = plt.subplots(figsize=(10, 6))

sns.distplot(df_date[target], color='green', kde=True)


fig, ax = plt.subplots(figsize=(10, 6))

sns.boxplot(x=df_date[target], data=df_date, color='green')

baseline_prophet.describe()

# Preparando o modelo

#2.2 Formatando os dados de acordo com o formato requerido pelo Prophet
baseline_prophet.reset_index(inplace=True)
baseline_prophet.rename(columns={datetime: 'ds', target: 'y'}, inplace=True)
baseline_prophet.head()

# Separando as bases de treino e teste
time_forecasting = 30

train_index = baseline_prophet.index[-1]-time_forecasting+1
test_index = train_index
base_train, base_test = baseline_prophet.loc[:train_index,
                                             ], baseline_prophet.loc[test_index:, ]


# Trabalhando com base de feriados (e inserções externas quando houver)
holidays1 = pd.DataFrame(holidays.UnitedStates(
    years=[2016, 2017, 2018]).items(), columns=['ds', 'holiday'])
holidays1.sort_values(by='ds', inplace=True)
holidays1.reset_index(drop=True, inplace=True)
holidays1['ds'] = pd.to_datetime(holidays1['ds'])
insercoes_e_feriados = holidays1
insercoes_e_feriados.sort_values(by='ds', inplace=True)
insercoes_e_feriados.head()

# Rodando o modelo

# Configurando e criando um objeto m para o modelo no prophet
m = Prophet(holidays = insercoes_e_feriados, weekly_seasonality=20, yearly_seasonality=True)

# Rodando o fit para a base de treino
m.fit(base_train)

# Utilizando o fit para prever o futuro, de acordo com o período estipulado e salvando num dataframe forecast
future = m.make_future_dataframe(periods=time_forecasting)
forecast = m.predict(future)
forecast

forecast.describe()

# Visualizando toda a série e o mês previsto
fig1 = m.plot(forecast, xlabel='ds', ylabel=target, figsize=(20, 8))
a = add_changepoints_to_plot(fig1.gca(), m, forecast, cp_color='r')
fig1.set_label('{}'.format(target))
fig1.legend()

fig2 = m.plot_components(forecast)

# Avaliando o modelo
forecast_abril = forecast[forecast['ds'] > '2018-03-31']
forecast_abril = forecast_abril[[
    'ds', 'trend', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_abril.head()

forecast_test = forecast_abril.merge(base_test, how='left', on='ds')
forecast_test.head()


fig = go.Figure()

fig.add_trace(go.Scatter(x=forecast_test['ds'], y=forecast_test['yhat'],
                         line=dict(color='blue', width=1),
                         name='Previsto'))

fig.add_trace(go.Scatter(x=forecast_test['ds'], y=forecast_test['y'],
                         line=dict(color='black', width=2),
                         name='REAL'))

fig.add_trace(go.Scatter(x=forecast_test['ds'], y=forecast_test['yhat_upper'],
                         line=dict(color='blue', width=1.5, dash='dot'),
                         name='Previsto máximo'))

fig.add_trace(go.Scatter(x=forecast_test['ds'], y=forecast_test['yhat_lower'],
                         line=dict(color='blue', width=1.5, dash='dot'),
                         name='Previsto mínimo'))


fig.show()

# Métricas de avaliação de modelo para regressão

# Comparar o previsto com o observado. Nesse primeiro momento é feito a diferença entre o fitting do modelo e a base de treino
value_metrics = [0]*4
metrics = ['MAE', 'MSE', 'RMSE', 'R2']
value_metrics[0] = mean_absolute_error(
    base_train['y'], forecast['yhat'][:train_index+1])
value_metrics[1] = mean_squared_error(
    base_train['y'], forecast['yhat'][:train_index+1])
value_metrics[2] = math.sqrt(value_metrics[1])
value_metrics[3] = r2_score(base_train['y'], forecast['yhat'][:train_index+1])
d = {'metrics': metrics, 'value': value_metrics}
evaluate_train_model = pd.DataFrame(d)

#Comparar o teste com o previsto
value_metrics = [0]*4
metrics = ['MAE', 'MSE', 'RMSE', 'R2']
value_metrics[0] = mean_absolute_error(
    base_test['y'], forecast['yhat'][test_index+1:])
value_metrics[1] = mean_squared_error(
    base_test['y'], forecast['yhat'][test_index+1:])
value_metrics[2] = math.sqrt(value_metrics[1])
value_metrics[3] = r2_score(base_test['y'], forecast['yhat'][test_index+1:])
d = {'metrics': metrics, 'value':value_metrics}
evaluate_test_model = pd.DataFrame(d)














