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


def get_quarters_hiring_data():
    session = SessionLocal()

    query = text("""
        with base as (
        select
            e.id,
            e.department_id,
            e.job_id,
            extract(year
        from
            to_date(e.datetime,
            'YYYY-MM-DD"T"HH24:MI:SS"Z"')) as year,
            extract(quarter
        from
            to_date(e.datetime,
            'YYYY-MM-DD"T"HH24:MI:SS"Z"')) as q
        from
            public.employees e
        )
        select
            d.department,
            j.job,
            sum(case when q = 1 then 1 else 0 end) as q1,
            sum(case when q = 2 then 1 else 0 end) as q2,
            sum(case when q = 3 then 1 else 0 end) as q3,
            sum(case when q = 4 then 1 else 0 end) as q4
        from
            base b
        left join public.departments d on
            b.department_id = d.id
        left join public.jobs j on
            b.job_id = j.id
        where
            b.year = 2021
        group by
            d.department,
            j.job;
    """)

    rows = session.execute(query).fetchall()

    session.close()

    return [{'department': row[0], 'job': row[1], 'q1': row[2], 'q2': row[3], 'q3': row[4], 'q4': row[5]} for row in rows]