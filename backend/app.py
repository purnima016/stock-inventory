from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCHEMA = """
Tables in the 'purnn' database:
- stock(Stock_ID, Product_Name, Quantity_Available, Category, Supplier_ID, Purchase_Price, Selling_Price, Reorder_Level, Stock_Location)
- supplier(Supplier_ID, Supplier_Name, Contact, Address, Supply_Type)
- customer(Customer_ID, Customer_Name, Contact, Email)
- user(User_ID, Username, Password, Role, Last_Login)
- orders(Order_ID, Customer_ID, Stock_ID, Order_Date, Status, User_ID)
- sales(Sale_ID, Stock_ID, Customer_ID, User_ID, Quantity, Sale_Date, Amount, Discount)
- alert(Alert_ID, Stock_ID, User_ID, Alert_Message, Alert_Date)
- reorder_request(Request_ID, Stock_ID, Supplier_ID, User_ID, Quantity_Needed, Request_Date, Status)
- stock_audit(Audit_ID, Stock_ID, User_ID, Change_Type, Timestamp)
- manager(Manager_ID, Manager_Name, Contact, Warehouse_ID)
- warehouse_location(Warehouse_ID, Address, Contact, Manager_ID)
- stock_change_log(Log_ID, Stock_ID, Old_Quantity, New_Quantity, Changed_At)
"""

@app.route('/api/query', methods=['POST'])
def natural_language_query():
    data = request.json
    question = data.get('question', '')
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a MariaDB SQL expert. Convert natural language to valid MariaDB SQL SELECT queries only. Return ONLY the SQL query, no explanations, no markdown, no backticks."},
            {"role": "user", "content": f"Database schema:\n{SCHEMA}\n\nQuestion: {question}"}
        ]
    )
    sql = response.choices[0].message.content.strip()
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
        conn.close()
        return jsonify({"success": True, "sql": sql, "results": results})
    except Exception as e:
        return jsonify({"success": False, "error": str(e), "sql": sql})

@app.route('/api/stock', methods=['GET'])
def get_stock():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM stock")
        results = cursor.fetchall()
    conn.close()
    return jsonify(results)

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM alert")
        results = cursor.fetchall()
    conn.close()
    return jsonify(results)

@app.route('/api/low-stock', methods=['GET'])
def get_low_stock():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM stock WHERE Quantity_Available < Reorder_Level")
        results = cursor.fetchall()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)