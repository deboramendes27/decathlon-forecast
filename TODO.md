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
- [x] ARIMA (ordem por AIC) – MSE ≈ 1,9 mi, inadequado
- [x] SARIMAX: AR(1) + const. no log, exógenas n_stores + Fourier + pré-Natal – MSE ≈ 307 mil
- [x] Seleção de ordem e exógenas por AIC (statsmodels)
- [x] Teste de sensibilidade d=1 vs d=0
- [x] Análise dos resíduos (Ljung-Box)
- [x] Comparar com os baselines (SARIMAX −25% de MSE)

## 5. Métodos simples de ML: Random Forest / XGBoost
- [x] Features conhecidas no futuro: semana da temporada, semanas até o Natal / desde a Black Friday, férias zona C, log(n_stores)
- [x] Lags não usados (o lag 52 não existe para a 1ª temporada, que é todo o treino do fold)
- [x] Previsão direta das 40 semanas (sem recursão)
- [x] Random Forest – MSE ≈ 368 mil
- [x] XGBoost – MSE ≈ 371 mil
- [x] Hiperparâmetros fixos (sem tuning: só 50 semanas de treino no fold)
- [x] Importância das features (log_stores domina)
- [x] Teste de overfitting (MSE treino × validação) a partir do ML
- [x] Versões regularizadas: features suaves (Fourier + eventos), RF/XGB mais restritos, restrição monotônica
- [x] XGBoost regularizado – MSE ≈ 319 mil, o melhor modelo de ML

## 6. Deep learning simples: LSTM
- [x] LSTM sobre a sequência de features conhecidas (calendário + log n_stores), janelas de 40 semanas
- [x] 1 camada de 16 neurônios, ensemble de 5 seeds, 300 épocas
- [x] Sensibilidade a janela × neurônios (MSE entre ≈ 363 e 406 mil)
- [x] LSTM – MSE ≈ 363 mil (melhor que baseline e árvores, pior que SARIMAX)
- [x] LSTM regularizado (dropout, rede menor, weight decay, menos épocas) – MSE ≈ 325 mil
- [ ] MLP (não feito, só o LSTM foi pedido)

## 7. Deep learning mais complexo: TFT (Temporal Fusion Transformer)
- [ ] Preparar o dataset no formato da biblioteca (pytorch-forecasting ou darts)
- [ ] Treinar o TFT com covariáveis conhecidas no futuro (calendário) e passadas
- [ ] Interpretar a atenção / importância de variáveis
- [ ] Comparar com os outros modelos

## 8. Comparação, ensemble e submissão final
- [x] Ensemble SARIMAX + XGBoost reg. + LSTM reg. – MSE ≈ 273 mil (melhor na validação)
- [ ] Tabela comparativa de todos os modelos (mesma validação, mesma métrica)
- [ ] Gráfico real vs. previsto para os melhores modelos
- [ ] Testar ensemble (média dos melhores modelos)
- [ ] Re-treinar o modelo final com todos os dados
- [ ] Gerar a submissão final no formato correto

## 9. Entrega
- [ ] Limpar e comentar os notebooks
- [ ] Relatório / apresentação: problema, EDA, metodologia, resultados, conclusões e limitações
