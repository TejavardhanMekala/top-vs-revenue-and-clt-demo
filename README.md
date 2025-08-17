
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
   - Live demo (after you deploy): _add your Streamlit URL here_

---

## Quick Start — Analysis (local)
```bash
pip install -r requirements.txt
python analyze.py --csv "YOUR_DATA.csv" --time-col "top" --revenue-col "revenue" --controls "browser,platform,site"

##Live Demo - https://top-vs-revenue-and-clt-demo-hpfdhpyxypjoxmnxxjuryw.streamlit.app/
