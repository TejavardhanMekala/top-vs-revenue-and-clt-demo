
# top-vs-revenue-and-clt-demo

This repo contains two parts:

1) **Brief PDF analysis** of the relationship between **time on page (`top`)** and **revenue (`revenue`)** using your dataset.  
   We report both the simple association and the **adjusted** relationship controlling for `browser`, `platform`, and `site` (as fixed effects).  
   - Main report: `Report.pdf` (short, readable to anyone; no raw console dumps)  
   - Full code (openable anywhere): `code_appendix.html`  
   - Reproducible script: `analyze.py`  
   - Dependencies: `requirements.txt`

2) **Streamlit app** demonstrating an interesting statistical property: the **Central Limit Theorem** and when it **fails** (Cauchy, infinite variance).  
   - App file: `streamlit_app.py`  
   - ##Live Demo - https://top-vs-revenue-and-clt-demo-hpfdhpyxypjoxmnxxjuryw.streamlit.app/
3) Shows both unadjusted and adjusted relationships (controls: browser, platform, site fixed effects).
4) Reports standardized effect (β) and robust (HC3) standard errors so units don’t matter and inference is stable.
5) Charts include 95% intervals and a residuals check; no raw software output in the main PDF.
6) Streamlit app clearly demonstrates CLT and the Cauchy failure case (variance infinite → no Normal convergence).
---

## Quick Start — Analysis (local)
```bash
pip install -r requirements.txt
python analyze.py --csv "YOUR_DATA.csv" --time-col "top" --revenue-col "revenue" --controls "browser,platform,site"


