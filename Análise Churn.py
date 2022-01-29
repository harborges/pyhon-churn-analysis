#!/usr/bin/env python
# coding: utf-8

# # Análise de Churn em empresas
# 
# ### Churn analysis
# 
# Database link: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[2]:


#Importar base de dados/ Import database

import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

#Analisar base de dados e entender informações/ analyse database and understand informations
tabela = tabela.drop("Unnamed: 0", axis=1)


# In[3]:


#Tratamento de dados/ data treatment

#Corrigir valores/ correct values
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

#Deletando linhas e colunas vazias/ Deleting empty rows and columns
tabela = tabela.dropna(how="all", axis = 1)
tabela = tabela.dropna(how="any", axis = 0)

print(tabela.info())


# In[7]:


#Análise exploratória/ exploratory analysis
#Análise inicial/ initial analysis

#Cancelamentos/ cancellations
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))


# In[9]:


#Análise aprofundada/ in-depth analysis
import plotly.express as px

#comparar churn com outros dados
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color="Churn")
    grafico.show()


# 

# 
