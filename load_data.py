import json
from supabase import create_client

url = "https://wnxrtuumokuftcljvkht.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndueHJ0dXVtb2t1ZnRjbGp2a2h0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYyODU4OTUsImV4cCI6MjA5MTg2MTg5NX0.7PD6ArULXu6iFQrfV0XKG8iB-DYAaRsa8ylTawuzkNc"

supabase = create_client(url, key)

with open("mock_orders.json", encoding="utf-8") as f:
    orders = json.load(f)

for i, o in enumerate(orders):
    order = o.get("order", o)

    supabase.table("orders").insert({
        "id": str(i),
        "created_at": "2024-01-01",
        "total": 10000
    }).execute()

print("Done")