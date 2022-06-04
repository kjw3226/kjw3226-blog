---
title: pandas 10 minute practice-2
tag: pandas 10 minute practice-2
date: 2022-06-04
categories: Pandas
---

오늘 오전에 영통에 있는 병원에 가야할 일이 있어서 

나갔다가 오느라고 

오전에 어제 하다가 만 'pandas 10 minute'을 

코딩을 못 했다.

그러다가 

오후가 되서야 

코딩 연습을 했고

아래는 내가 코딩한 코드들이다.

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
s
```

```python
df.sub(s, axis="index")
```

```python
df.apply(np.cumsum)
```

```python
df.apply(lambda x: x.max() - x.min())
```

```python
s = pd.Series(np.random.randint(0, 7, size=10))
s
```

```python
s.value_counts()
```

```python
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s
```

```python
s.str.lower()
```

```python
df = pd.DataFrame(np.random.randn(10, 4))
df
```

```python
pieces = [df[:3], df[3:7], df[7:]]
```

```python
pd.concat(pieces)
```

```python
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
left
right
```

```python
pd.merge(left, right, on="key")
```

```python
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
left
right
```

```python
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df
```

```python
df.groupby("A").sum()
```

```python
df.groupby(["A", "B"]).sum()
```

```python
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
tuples
```

```python
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
index
```

```python
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df
```

```python
df2 = df[:4]
df2
```

```python
stacked = df2.stack()
stacked
```

```python
stacked.unstack()
```

```python
stacked.unstack(1)
```

```python
stacked.unstack(0)
```

```python
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
df
```

```python
pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
```

```python
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()
```

```python
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
ts
```

```python
ts_utc = ts.tz_localize("UTC")
ts_utc
```

```python
ts_utc.tz_convert("US/Eastern")
```

```python
rng = pd.date_range("1/1/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
```

```python
ps = ts.to_period()
ps
```

```python
ps.to_timestamp()
```

```python
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
ts.head()
```

```python
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df
```

```python
df["grade"] = df["raw_grade"].astype("category")

df["grade"]
```

```python
df["grade"].cat.categories = ["very good", "good", "very bad"]
```

```python
df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)
```

```python
df["grade"]
```

```python
df.sort_values(by="grade")
```

```python
df.groupby("grade").size()
```

```python
import matplotlib.pyplot as plt

plt.close("all")
```

```python
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot();
```

```python
plt.show();
```

```python
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
df
```

```python
df = df.cumsum()
```

```python
plt.figure();
```

```python
df.plot();
```

```python
plt.legend(loc='best');
```