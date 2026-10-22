# Decathlon – Forecast de vendas do gorro de ski

Projeto Centrale Lille × Decathlon (Kaggle, 10/2026).

**Objetivo:** prever o total semanal de vendas (soma das 55 lojas) do gorro `model_id 8641631`
para as 40 semanas de 27/08/2023 a 26/05/2024. Métrica: **MSE**.
Entrega: submissões até **sexta 13h30**, apresentação em inglês de 15–20 min na sexta à tarde.

## Estrutura
```
centrale-lille-decathlon-forecast-project-10-2026/   dados do Kaggle (train, test, submission, stores)
notebooks/01_eda.ipynb         análise exploratória
notebooks/02_modeles.ipynb     modelos (baselines, ARIMA/SARIMAX, RF/XGBoost, MLP/LSTM, TFT/N-HiTS)
submissions/                   arquivos .csv para enviar ao Kaggle
src/data.py                    funções auxiliares (os notebooks não dependem dele)
TODO.md                        plano de trabalho
```

## Ambiente
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Como contribuir
**Regra do grupo: ninguém faz push direto na `main`.** Toda mudança passa por Pull Request
e só entra na `main` depois da aprovação da Débora.
1. Atualize sua cópia: `git checkout main` e `git pull`
2. Crie uma branch: `git checkout -b nome-da-tarefa`
3. Faça commits e envie a branch: `git push -u origin nome-da-tarefa`
4. Abra um Pull Request no GitHub e peça a revisão da Débora (`deboramendes27`).
