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
