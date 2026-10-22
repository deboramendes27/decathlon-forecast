# Decathlon – Forecast de vendas do gorro de ski

Competição: https://www.kaggle.com/competitions/centrale-lille-decathlon-forecast-project-10-2026

## 0. Setup e entendimento do problema
- [x] Baixar os dados do Kaggle
- [x] Alvo: total semanal de vendas (soma das 55 lojas), `ID` = `week_id`
- [x] Horizonte: 40 semanas, 27/08/2023 → 26/05/2024 (202335 → 202422)
- [x] Métrica: MSE (segundo o deck) – [ ] confirmar na aba *Evaluation* do Kaggle
- [x] Prazo: submissões até sexta 13h30, apresentação em inglês (15–20 min) sexta à tarde
- [ ] Ver o limite de submissões por dia no Kaggle
- [x] Ambiente Python (`.venv` + kernel "Python (decathlon)")

## 1. Análise estatística dos dados (EDA) – `notebooks/01_eda.ipynb`
- [x] Colunas, tipos, período, nulos, duplicados
- [x] Linhas só existem com venda ≥ 1 → semanas ausentes = 0
- [x] Série agregada, comparação entre temporadas, sazonalidade mensal
- [x] Férias escolares zona C e Black Friday
- [x] Análise por loja (tamanho, estabilidade entre temporadas)
- [x] `n_stores` por semana (conhecido no teste) × vendas
- [x] ADF / KPSS, ACF / PACF
- [x] Conclusões escritas no notebook

## 2. Estratégia de validação
- [x] Fold que imita o teste: treino até 21/08/2022, validação de 28/08/2022 a 28/05/2023 (40 semanas)
- [x] Funções de métrica em `src/data.py` (mse, rmse, wape)
- [ ] Opcional: um segundo fold mais curto (ex.: prever só jan–mai/2023) para ter mais de um ponto de avaliação

## 3. Métodos de base (baselines)
- [x] Seasonal naive (mesma semana do ano anterior) – `notebooks/02_modeles.ipynb`
- [x] Seasonal naive ajustado por `n_stores`
- [x] Arquivos gerados em `submissions/`
- [ ] Primeira submissão no Kaggle com o melhor baseline

## 4. Métodos clássicos: ARIMA / SARIMA
- [ ] ARIMA com parâmetros a partir do ACF/PACF
- [ ] SARIMA com sazonalidade (semanal e/ou anual)
- [ ] `auto_arima` (pmdarima) para busca de parâmetros
- [ ] Opcional: SARIMAX com variáveis exógenas
- [ ] Análise dos resíduos (Ljung-Box)
- [ ] Comparar com os baselines

## 5. Métodos simples de ML: Random Forest / XGBoost
- [ ] Feature engineering:
  - [ ] Features de calendário (dia da semana, mês, semana do ano, feriados, férias)
  - [ ] Lags (t-1, t-7, t-52…) e janelas móveis (média, desvio)
  - [ ] Variáveis externas disponíveis
- [ ] Random Forest
- [ ] XGBoost (e/ou LightGBM)
- [ ] Estratégia de previsão multi-passo (recursiva vs. direta)
- [ ] Tuning de hiperparâmetros com a validação temporal
- [ ] Importância das features

## 6. Deep learning simples: LSTM
- [ ] Normalizar os dados e criar janelas (sequências de entrada → saída)
- [ ] LSTM simples (1–2 camadas)
- [ ] Early stopping, ajuste de tamanho de janela e unidades
- [ ] Comparar com ML e clássicos

## 7. Deep learning mais complexo: TFT (Temporal Fusion Transformer)
- [ ] Preparar o dataset no formato da biblioteca (pytorch-forecasting ou darts)
- [ ] Treinar o TFT com covariáveis conhecidas no futuro (calendário) e passadas
- [ ] Interpretar a atenção / importância de variáveis
- [ ] Comparar com os outros modelos

## 8. Comparação, ensemble e submissão final
- [ ] Tabela comparativa de todos os modelos (mesma validação, mesma métrica)
- [ ] Gráfico real vs. previsto para os melhores modelos
- [ ] Testar ensemble (média dos melhores modelos)
- [ ] Re-treinar o modelo final com todos os dados
- [ ] Gerar a submissão final no formato correto

## 9. Entrega
- [ ] Limpar e comentar os notebooks
- [ ] Relatório / apresentação: problema, EDA, metodologia, resultados, conclusões e limitações
