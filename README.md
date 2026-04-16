# AI Analytics Dashboard

## Overview
Built a simple data pipeline:
Mock Orders → Supabase → Dashboard → Telegram Alerts

## Stack
- Python
- Supabase
- Vercel
- Telegram Bot API

## Features
- Data ingestion from JSON
- Orders dashboard visualization
- Telegram alert for high-value orders

## AI Usage
Used AI tools (ChatGPT / Claude) for:
- debugging Python script
- handling API integration issues
- generating dashboard code
- solving encoding and schema problems

## Challenges
- JSON structure mismatch → solved via flexible parsing
- Supabase schema cache error → fixed via correct project + RLS settings
- Python environment issues → resolved by aligning interpreter

## How to run
1. Run `load_data.py`
2. Open deployed dashboard
3. Run `telegram_test.py`
