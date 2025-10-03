import re
from typing import Any
from pathlib import Path

import torch
import pandas as pd
import matplotlib.pyplot as plt
from roach.store import Store, iter_stores
from roach.plot import LINE


from torch import Tensor


def stores_to_df(
    parent: str | Path,
) -> pd.DataFrame:
    rows = []
    for store_id, store in iter_stores(parent):
        row = {}
        
        # store all args as columns
        args = store.load("args")
        for k, v in args.items():
            row[k] = v
        rows.append(row)

        # other columns of interest
        row["store_id"] = store_id
        row["store_obj"] = store
        row["store_path"] = Path(parent) / store_id

    df = pd.DataFrame(rows)
    return df