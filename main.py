from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

# FastAPIアプリケーションの初期化
app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],  # 全てのHTTPメソッドを許可
    allow_headers=["*"],  # 全てのHTTPヘッダーを許可
)

# SQLiteデータベース接続
DATABASE = "data.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            loginName TEXT,
            graduateYear TEXT,
            companionMiddleSchool INTEGER,
            companionElementarySchool INTEGER,
            companionInfant INTEGER,
            allergies TEXT,
            otherAllergies TEXT,
            zokusei TEXT
        )
        """)
        conn.commit()


init_db()

# Pydanticモデル


class Record(BaseModel):
    name: str = ""
    loginName: str = ""
    graduateYear: str = ""
    companionMiddleSchool: int = 0
    companionElementarySchool: int = 0
    companionInfant: int = 0
    allergies: list[str] = []
    otherAllergies: str = ""
    zokusei: str = ""

# データを登録するPOSTエンドポイント


@app.post("/record")
async def create_record(record: Record):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO records (name, loginName, graduateYear, companionMiddleSchool, companionElementarySchool, companionInfant, allergies, otherAllergies, zokusei)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record.name,
            record.loginName,
            record.graduateYear,
            record.companionMiddleSchool,
            record.companionElementarySchool,
            record.companionInfant,
            ",".join(record.allergies),  # リストを文字列に変換
            record.otherAllergies,
            record.zokusei
        ))
        conn.commit()
    return {"success": True, "message": "Record added successfully"}

# データを取得するGETエンドポイント


@app.get("/records")
async def get_records():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT id, name, loginName, graduateYear, companionMiddleSchool, companionElementarySchool, companionInfant, allergies, otherAllergies, zokusei
        FROM records
        """)
        rows = cursor.fetchall()
        records = [
            {
                "id": row[0],
                "name": row[1],
                "loginName": row[2],
                "graduateYear": row[3],
                "companionMiddleSchool": row[4],
                "companionElementarySchool": row[5],
                "companionInfant": row[6],
                "allergies": row[7].split(",") if row[7] else [],  # 文字列をリストに変換
                "otherAllergies": row[8],
                "zokusei": row[9]
            }
            for row in rows
        ]
    return {"success": True, "records": records}
