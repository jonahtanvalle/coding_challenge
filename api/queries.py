from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL =  'postgresql://postgres:postgres@postgres/postgres'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_average_hiring_data():
    session = SessionLocal()

    query = text("""
        WITH base AS (
            SELECT
                department_id,
                COUNT(id) hired_q
            FROM
                public.employees
            WHERE
                EXTRACT(YEAR FROM TO_DATE(datetime, 'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2021
            GROUP BY
                department_id
        ),
        averages AS (
            SELECT
                AVG(hired_q) average
            FROM
                base
        )
        SELECT
            base.department_id,
            d.department,
            base.hired_q AS hired
        FROM
            base
        LEFT JOIN public.departments d ON base.department_id = d.id
        JOIN averages ON averages.average < base.hired_q
        ORDER BY
            hired_q DESC;
    """)

    rows = session.execute(query).fetchall()

    session.close()

    return [{'department_id': row[0], 'department': row[1], 'hired': row[2]} for row in rows]
