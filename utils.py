import uuid
import pymysql
import time

def generate_unique_email(prefix="testuser", domain="dongo.hu"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}@{domain}"

def get_verification_code(email, timeout=10, interval=1):
    deadline = time.time() + timeout

    while time.time() < deadline:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="test1234",
            database="hotel"
        )
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT vt.verification_code
            FROM verification_token vt
            JOIN user u ON vt.user_user_id = u.user_id
            WHERE u.email = %s
            ORDER BY vt.token_id DESC
            LIMIT 1
            """,
            (email,)
        )
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            full_code = result[0]
            return full_code[-4:]

        time.sleep(1)

    raise TimeoutError(f"Nem érkezett meg a verifikációs kód ehhez: {email}")