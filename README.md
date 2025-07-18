# Grocery Prices API

Small and simple CRUD project to keep track of the price value of different groceries found in different stores, aiming to support both USD and VES as currency.

## Features

- CRUD for products, categories, stores and prices
- Keeps track of prices over time, up to the last 5 prices
- USD and VES currency support with automatic rate update, saving the current rate when adding a price entry

## Tech stack

- Python with [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/), managed with [uv](https://docs.astral.sh/uv/)
- PostgreSQL/SQLite
- Docker

## Getting started

Clone this repo and install uv as listed [here](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). Then, install all dependencies and run the project.

```
git clone https://github.com/led3zma/grocery-prices-api.git
uv sync
uv run fastapi dev
```

## Motivation

Just to ease my life in remembering and taking note of how expensive or cheap is some product in one store relative to others, and to see how prices change over time in every store (due to inflation).

I mainly planned this part of the logic to be in an API so I can decide later if I want to consume it via a traditional web app or a chat-bot-like front end.
