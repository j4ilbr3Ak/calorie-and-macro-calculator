import pandas as pd
import numpy as np
import sqlite3
import os
import sys 
import time


def initialize_database():
    conn = sqlite3.connect("food_database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT,
        calories REAL,
        protein REAL,
        carbs REAL,
        fats REAL,
        fiber REAL    
        )
    """)

    conn.commit()
    conn.close()


def insert_food_item(name, brand, calories, protein, carbs, fats, fiber):


    conn = sqlite3.connect("food_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO food_items (name, brand, calories, protein, carbs, fats, fiber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, brand, calories, protein, carbs, fats, fiber))

    conn.commit()
    conn.close()


def search_food(name):
    
    conn = sqlite3.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_items WHERE name LIKE ?", ('%' + name + '%,'))
    results = cursor.fetchall()
    conn.close()
    return results



if __name__ == "__main__":
    initialize_database()
    print("Database initialized")