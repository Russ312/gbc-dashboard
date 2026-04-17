# GBC Analytics Dashboard (Test Task)

## Overview
This project implements a minimal end-to-end analytics pipeline for order data:

Mock Orders (JSON) → Python ETL → Supabase (PostgreSQL) → Dashboard (Vercel) → Telegram Alert

The goal was to demonstrate practical usage of AI tools and rapid integration of multiple services.

---

## Stack
- Python (data ingestion)
- Supabase (PostgreSQL + REST API)
- HTML + Chart.js (dashboard)
- Vercel (deployment)
- Telegram Bot API (notifications)

---

## Architecture

1. **Data Source**
   - `mock_orders.json` (provided test dataset)

2. **ETL Script**
   - `load_data.py`
   - Parses JSON and inserts records into Supabase

3. **Database**
   - Supabase table: `orders`
   - Fields:
     - `id`
     - `created_at`
     - `total`

4. **Dashboard**
   - `index.html`
   - Fetches data via Supabase REST API
   - Displays order totals using Chart.js

5. **Notifications**
   - Telegram bot sends alert messages (simulated condition)

---

## Features
- JSON → database ingestion pipeline
- Hosted dashboard with live data fetch
- Basic data visualization (line chart)
- Telegram notification integration

---

## AI Usage
AI tools (ChatGPT / Claude-style workflows) were actively used for:

- Debugging Python environment and dependencies
- Resolving encoding issues (`UnicodeDecodeError`)
- Handling Supabase API integration and schema issues
- Fixing RLS and authentication problems
- Generating and refining frontend dashboard code
- Troubleshooting Telegram Bot API interaction

---

## Challenges & Solutions

### 1. JSON Structure Mismatch
- Issue: Missing expected fields (`id`, `created_at`, `total`)
- Solution: Implemented fallback mapping and simplified insertion logic

### 2. Supabase Schema Cache Error (PGRST205)
- Issue: API could not detect table
- Solution:
  - Ensured correct project URL
  - Recreated table in `public` schema
  - Disabled RLS

### 3. Encoding Error (Windows)
- Issue: `UnicodeDecodeError`
- Solution:
  - Explicitly set `encoding="utf-8"` when reading JSON

### 4. Python Environment Issues
- Issue: package resolution mismatch
- Solution:
  - Used consistent interpreter and direct execution via CMD

### 5. Telegram Bot Setup
- Issue: retrieving `chat_id`
- Solution:
  - Used `getUpdates` endpoint after initiating chat with bot

---

## How to Run

### 1. Load data into Supabase
```bash
python load_data.py
