# 📦 SuperKart Sales Forecasting — Deployed ML App
### XGBoost | Flask | Streamlit | Docker | Hugging Face | End-to-End Deployment

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-2.x-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?logo=flask)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Deployed-yellow)
![Status](https://img.shields.io/badge/Status-Complete%20%26%20Deployed-brightgreen)
![Domain](https://img.shields.io/badge/Domain-Retail%20%7C%20Forecasting-blue)

---

## 🛒 Business Context

**SuperKart** is a retail chain operating supermarkets and food marts across various tier cities, offering a wide range of products. Accurate sales forecasting is essential for:

- **Inventory optimization** — Avoid overstock and stockouts
- **Regional strategy** — Make informed decisions on store expansions and product mix
- **Supply chain planning** — Help procurement teams plan ahead
- **Revenue forecasting** — Support financial planning across the organization

SuperKart partnered with a data science firm to not just build a predictive model, but **deploy a complete, production-ready forecasting solution** that business users can interact with directly.

---

## 🎯 Objective

> **Accurately forecast sales revenue of SuperKart outlets for the upcoming quarter** and deploy the model as an interactive application accessible to non-technical business stakeholders.

---

## 📊 Dataset

| Property | Value |
|---|---|
| Rows | 8,763 records |
| Columns | 12 features |
| Target Variable | `Product_Store_Sales_Total` |
| Missing Values | None |
| Data Types | Mix of float64, int64, object |

**Key Features:**
- `Product_Id` — Unique product identifier
- `Product_Weight` — Product weight
- `Product_Sugar_Content` — Low sugar / Regular / No sugar
- `Product_Allocated_Area` — Display area ratio
- `Product_Type` — 16 product categories (Meat, Snacks, Fruits & Vegetables, etc.)
- `Product_MRP` — Maximum Retail Price
- `Store_Id` — Unique store identifier
- `Store_Size` — Small / Medium / Large
- `Store_Location_City_Type` — Tier 1 / Tier 2 / Tier 3
- `Store_Type` — Supermarket Type 1/2/3 / Grocery Store
- `Store_Establishment_Year` — Year store was established

---

## 🔬 Approach & Methodology

```
Data → EDA → Feature Engineering → Model Building → Tuning → Flask API → Streamlit UI → Docker → HuggingFace
```

### 1. Exploratory Data Analysis (EDA)
- Analyzed sales distribution across product types, store sizes, and city tiers
- Key findings:
  - **"Low Sugar" products** and **"Fruits & Vegetables"** are top revenue generators
  - **Tier 3 cities** show significant sales potential
  - Store type significantly impacts sales volume
- Identified correlations between Product_MRP and total sales
- Visualized seasonal and store-level patterns

### 2. Data Preprocessing & Feature Engineering
- Handled object and float columns appropriately
- Created store age feature from `Store_Establishment_Year`
- Standardized `Product_Sugar_Content` categories (multiple naming conventions)
- Encoded categorical variables for model training
- Train/test split for model validation

### 3. Model Building
Built and compared multiple regression models:
- Linear Regression (baseline)
- Decision Tree Regressor
- Random Forest Regressor
- **XGBoost Regressor** (best performance)
- Gradient Boosting Regressor

### 4. Hyperparameter Tuning
- Applied GridSearchCV and cross-validation for XGBoost
- Tuned: `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree`
- Selected best configuration based on RMSE and R² score

### 5. Model Deployment — Full Stack

#### Flask REST API
```python
# API endpoint for sales prediction
POST /predict
Input: JSON with product and store features
Output: {"predicted_sales": 1234.56}
```

#### Streamlit Dashboard
- Interactive web UI for non-technical business users
- Input product and store parameters via dropdowns and sliders
- Instant sales forecast visualization
- No coding required for business users

#### Docker Containerization
```dockerfile
FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

#### Hugging Face Spaces Deployment
- Deployed Streamlit app on Hugging Face Spaces
- Publicly accessible for stakeholder demos
- UI loads successfully with predict button functionality confirmed

---

## 📈 Key Results

| Aspect | Result |
|---|---|
| Best Model | XGBoost with hyperparameter tuning |
| Key Finding | Low Sugar products + Fruits & Vegetables drive most revenue |
| Deployment | Live on Hugging Face Spaces |
| UI Validation | "UI loaded successfully; forecast returned on predict click" |
| Accessibility | Business stakeholders can use app without technical knowledge |

---

## 💡 Business Insights & Recommendations

1. **Low Sugar & Fruits/Vegetables** — These categories generate the most revenue; prioritize shelf allocation and stock levels
2. **Tier 3 City Opportunity** — Significant untapped sales potential in Tier 3 cities; consider expansion strategy
3. **Product MRP Optimization** — Strong correlation between MRP and total sales; pricing strategy should be data-driven
4. **Store Type Impact** — Supermarket Type 1 consistently outperforms; analyze operational differences for replication
5. **Seasonal Stocking** — Use quarterly forecasts to pre-position inventory before peak demand periods

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| XGBoost | Primary forecasting model |
| Scikit-learn | Model evaluation, preprocessing, GridSearchCV |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | EDA visualizations |
| Flask | REST API for model serving |
| Streamlit | Interactive business dashboard |
| Docker | Containerization for portable deployment |
| Hugging Face Spaces | Cloud deployment and public hosting |
| Google Colab | Development and experimentation |

---

## 📁 Project Structure

```
superkart-sales-forecasting/
│
├── Sapna_SuperKart_Model_Deployment_Notebook.ipynb  # Full notebook
├── app.py                                            # Streamlit app
├── api.py                                            # Flask REST API
├── model.pkl                                         # Trained model (generated)
├── Dockerfile                                        # Container configuration
├── requirements.txt                                  # Dependencies
└── README.md                                         # Documentation
```

---

## 🚀 How to Run

---

## 🔐 Configuration & Secrets (Required)

- Environment variables used by the scripts and generated apps:
  - `HF_HUB_TOKEN` or `HF_TOKEN` — Hugging Face access token (keep secret; do not commit).
  - `HF_REPO_ID` — Hugging Face Space repo id (format: `username/space-name`) used for uploads.
  - `BACKEND_API_URL` — Backend API URL the Streamlit frontend posts to (e.g. `https://<user>-<space>.hf.space`).

- Example PowerShell commands to set these locally:
```powershell
$env:HF_HUB_TOKEN="hf_..."
$env:HF_REPO_ID="your-username/your-space-name"
$env:BACKEND_API_URL="https://your-backend.hf.space"
```

- For Streamlit deployments on Hugging Face Spaces, prefer adding `BACKEND_API_URL` as a Space secret (Settings → Secrets) and access it via `st.secrets["BACKEND_API_URL"]` in the app.

- Behavior notes:
  - If `HF_HUB_TOKEN` is not set, the scripts will prompt for the token securely (via `getpass`).
  - If `HF_REPO_ID` is not set the upload step will warn — set it to upload files automatically.

- Security: never store tokens in source control. Use environment variables or platform secrets.

---

**Option 1: Run Locally**
```bash
git clone https://github.com/sapna-ai-qe/superkart-sales-forecasting
cd superkart-sales-forecasting
pip install -r requirements.txt
streamlit run app.py
```

**Option 2: Run with Docker**
```bash
docker build -t superkart-app .
docker run -p 8501:8501 superkart-app
```

**Option 3: Notebook**
```bash
# Open in Google Colab
# Mount Google Drive with dataset
# Run all cells sequentially
```

---

## 👩‍💻 Author

**Sapna** | Senior AI Quality Engineer  
Post Graduate in AI/ML — University of Texas at Austin  
GitHub: [@sapna-ai-qe](https://github.com/sapna-ai-qe)

---
*Part of AI/ML Portfolio — UT Austin Post Graduate Program*
