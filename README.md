# 📦 StockIQ — AI-Powered Stock Inventory Management System

A full-stack inventory management system with an AI-powered Natural Language Query engine. Users can query the entire database in plain English — no SQL knowledge needed.

## 🚀 Live Demo
[Coming Soon — Railway Deployment]

## ✨ Features
- 🤖 **AI Natural Language Query** — Ask questions in plain English, get instant results
- 📊 **Real-time Dashboard** — Stock levels, alerts, and total inventory value
- ⚠️ **Low Stock Alerts** — Automatic warnings when products fall below reorder level
- 📦 **Stock Management** — Full inventory tracking with 13 database tables
- 🔔 **Alert System** — Real-time notifications for critical stock events
- 🏭 **Supplier & Warehouse Tracking** — Complete supply chain visibility

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | React.js |
| Backend | Python Flask |
| Database | MariaDB |
| AI Engine | Groq API (LLaMA 3.3) |
| Deployment | Railway |

## 📁 Project Structure
stock-inventory/
├── backend/
│   ├── app.py          # Flask API + NL to SQL engine
│   ├── db.py           # Database connection
│   └── .env            # Environment variables
├── frontend/
│   └── src/
│       └── App.js      # React UI
└── README.md
## 🗄️ Database Schema
13 tables covering complete inventory operations:
- **stock** — Product inventory with pricing and locations
- **supplier** — Supplier information and contacts
- **customer** — Customer records
- **orders** — Order tracking and status
- **sales** — Sales transactions
- **alert** — System alerts for low stock
- **reorder_request** — Automated reorder management
- **stock_audit** — Complete audit trail
- **manager** — Warehouse manager assignments
- **warehouse_location** — Multi-warehouse support
- **stock_change_log** — Stock change history
- **user** — Role-based access (Admin/Salesperson/Supplier)
- **stock_supplier_view** — Joined view for reporting

## 🤖 AI Query Examples
Ask anything in plain English:
- *"Which products have low stock?"*
- *"Show me pending reorder requests"*
- *"Which supplier has the most products?"*
- *"Top 3 customers by total orders"*
- *"Products that triggered alerts this month"*

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x
- Node.js
- MariaDB

### Backend
```bash
cd backend
pip install flask flask-cors pymysql python-dotenv groq
# Create .env file with your DB credentials and GROQ_API_KEY
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📊 Database Features
- **42 SQL queries** including complex JOINs and aggregations
- **5 Stored Procedures** for common operations
- **6 Functions** for calculations
- **4 Triggers** for automated stock management
- **4 Cursors** for batch operations
- **2 Views** for simplified reporting
- Full **3NF normalization**

## 👩‍💻 Author
**Purnima**
- 2nd Year B.Tech Student
