import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp

st.set_page_config(page_title="Sampling Distributions & CLT", page_icon="📊", layout="centered")
st.title("📊 Sampling Distributions & the Central Limit Theorem")
st.write("""
Explore how the *distribution of sample means* behaves as sample size grows, across different base distributions.
Try heavy-tailed **Cauchy** to see when the CLT **breaks** (infinite variance).
""")

np.random.seed(0)

dist = st.selectbox("Base distribution", ["Uniform(0,1)","Normal(0,1)","Exponential(λ=1)","Bernoulli(p=0.3)","Pareto(α=2.5)","Cauchy(0,1)"])
n = st.slider("Sample size (n) per draw", 1, 2000, 50, step=1)
m = st.slider("Number of draws (how many sample means)", 100, 10000, 2000, step=100)
bins = st.slider("Histogram bins", 20, 200, 60, step=10)

def draw_means(dist, n, m):
    if dist == "Uniform(0,1)":
        X = np.random.random((m, n))
        mu, var = 0.5, 1/12
    elif dist == "Normal(0,1)":
        X = np.random.normal(0,1,(m,n))
        mu, var = 0.0, 1.0
    elif dist == "Exponential(λ=1)":
        X = np.random.exponential(1,(m,n))
        mu, var = 1.0, 1.0
    elif dist == "Bernoulli(p=0.3)":
        X = (np.random.random((m,n)) < 0.3).astype(float)
        mu, var = 0.3, 0.3*0.7
    elif dist == "Pareto(α=2.5)":
        X = (np.random.pareto(2.5,(m,n)) + 1.0)  # mean finite (α>1), var finite (α>2)
        # true mean = α/(α-1), var = α / ((α-1)^2 (α-2)) for α>2
        alpha = 2.5
        mu = alpha/(alpha-1)
        var = alpha/(((alpha-1)**2)*(alpha-2))
    elif dist == "Cauchy(0,1)":
        X = np.random.standard_cauchy((m,n))
        mu, var = np.nan, np.nan  # undefined
    else:
        raise ValueError("Unknown dist")
    means = X.mean(axis=1)
    return means, mu, var

means, mu, var = draw_means(dist, n, m)
fig, ax = plt.subplots(figsize=(8,4))
ax.hist(means, bins=bins, density=True, alpha=0.7)
ax.set_title("Histogram of Sample Means")
ax.set_xlabel("sample mean")
ax.set_ylabel("density")

# Overlay normal with theoretical mean/variance/n when finite
if not np.isnan(var):
    theo_sd = np.sqrt(var / max(n,1))
    xs = np.linspace(np.min(means), np.max(means), 400)
    # normal density
    pdf = 1/(theo_sd*np.sqrt(2*np.pi)) * np.exp(-0.5*((xs-mu)/theo_sd)**2)
    ax.plot(xs, pdf, linewidth=2)

st.pyplot(fig)

with st.expander("What to look for"):
    st.markdown("""
- For **Uniform / Normal / Exponential / Bernoulli / Pareto(α=2.5)** the histogram of sample means becomes bell-shaped as **n** grows.
- The overlayed Normal curve uses the theoretical variance divided by **n**.
- For **Cauchy**, the CLT **fails** (variance is infinite), so sample means do **not** stabilize to a bell curve.
""")
