"""Carregamento dos dados, agregação semanal e métricas do projeto."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "centrale-lille-decathlon-forecast-project-10-2026"


def load_raw():
    """Retorna (train, test, stores) com as datas já convertidas."""
    train = pd.read_csv(DATA_DIR / "train.csv", parse_dates=["date"])
    test = pd.read_csv(DATA_DIR / "test.csv", parse_dates=["date"])
    stores = pd.read_csv(DATA_DIR / "stores_location.csv")
    return train, test, stores


def weekly_total(train, test=None):
    """Série semanal agregada (todas as lojas) com o nº de lojas que venderam.

    O train só tem linhas com venda >= 1, então semanas ausentes são vendas 0.
    Se `test` for passado, as semanas de teste entram com sales = NaN.
    """
    agg = train.groupby("date").agg(sales=("sales_quantity", "sum"),
                                    n_stores=("bu", "size"))
    if test is not None:
        agg_test = test.groupby("date").agg(n_stores=("bu", "size"))
        agg_test["sales"] = np.nan
        agg = pd.concat([agg, agg_test])
    idx = pd.date_range(agg.index.min(), agg.index.max(), freq="W-SUN")
    agg = agg.reindex(idx)
    is_train = agg.index <= train["date"].max()
    agg.loc[is_train] = agg.loc[is_train].fillna(0)
    agg["n_stores"] = agg["n_stores"].fillna(0).astype(int)
    agg.index.name = "date"
    # A semana Decathlon começa no domingo (`date`): week_id = semana ISO de date + 1 dia
    iso = (agg.index + pd.Timedelta(days=1)).isocalendar()
    agg["week_id"] = (iso.year * 100 + iso.week).values
    return agg


def mse(y_true, y_pred):
    return float(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2))


def rmse(y_true, y_pred):
    return mse(y_true, y_pred) ** 0.5


def wape(y_true, y_pred):
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return float(np.abs(y_true - y_pred).sum() / np.abs(y_true).sum())
