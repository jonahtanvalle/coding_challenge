with base as (
select
	department_id,
	COUNT(id) hired_q
from
	public.employees
where
	extract(year
from
	to_date(datetime,
	'YYYY-MM-DD"T"HH24:MI:SS"Z"')) = 2021
group by
	department_id
)
,
averages as (
select
	AVG(hired_q) average
from
	base)
	select
	base.department_id,
		d.department, 
		base.hired_q as hired
from
		base
left join public.departments d on
	base.department_id = d.id
join averages on
	average < base.hired_q
order by
	hired_q desc
