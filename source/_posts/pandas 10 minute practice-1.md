---
title: pandas 10 minute practice-1
tag: pandas 10 minute practice-1
date: 2022-06-03
categories: Pandas
---

매일 'Python'만 다루다가

오늘은 오랜만에 

'Pandas' 만 따로 

'pandas 10 minute' 사이트에 들어가서 

연습을 했다. 

한꺼번에 다 코딩하는 건 무리 같아서

'Missing data(결측치)' 까지만 코딩을 하고 

나머지는 내일 오전에 해야겠다.

아래의 코드는 내가 실습한 코드들이다.

```python
import numpy as np
import pandas as pd
```

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8 ])
s
```

```python
dates = pd.date_range("20130101", periods=6)
dates
```

```python
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
```

```python
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
df2
```

```python
df2.dtypes
```

```python
df2.A
```

```python
df2.bool
```

```python
df.head()
```

```python
df.tail(3)
```

```python
df.index
```

```python
df.columns
```

```python
df.to_numpy()
df2.to_numpy()
```

```python
df.describe()
```

```python
df.T
```

```python
df.sort_index(axis=1, ascending=False)
```

```python
df.sort_values(by="B")
```

```python
df["A"]
```

```python
df[0:3]
```

```python
df["20130102" : "20130104"]
```

```python
df.loc[:, ["A", "B"]]
```

```python
df.loc["20130102", ["A", "B"]]
```

```python
df.loc[dates[0], "A"]
```

```python
df.at[dates[0], "A"]
```

```python
df.iloc[3]
```

```python
df.iloc[3:5, 0:2]
```

```python
df.iloc[[1, 2, 4], [0, 2]]
```

```python
df.iloc[1:3, :]
```

```python
df.iloc[:, 1:3]
```

```python
df.iloc[1, 1]
```

```python
df[df["A"] > 0]
```

```python
df[df > 0]
```

```python
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
df2
```

```python
df2[df2["E"].isin(["two", "four"])]
```

```python
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
s1
```

```python
df["F"] = s1
s1
```

```python
df.at[dates[0], "A"] = 0
```

```python
df.iat[0, 1] = 0
```

```python
df.loc[:, "D"] = np.array([5] * len(df))
df
```

```python
df2 = df.copy()
df2[df2 > 0] = -df2
df
```

```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
df1.loc[dates[0] : dates[1], "E"] = 1
df1
```

```python
df1.dropna(how="any")
```

```python
df1.fillna(value=5)
```

```python
pd.isna(df1)
```

```python
df.mean()
```

```python
df.mean(1)
```