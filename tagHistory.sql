use runtime
select TagName, 
Versions=count(*), 
Descriptions=count(distinct [Description]), 
MinEU=count(distinct MinEU),
MaxEU=count(distinct MaxEU),
First=min(DateCreated),
Last=max(DateCreated),
AvgLife=datediff(second,min(DateCreated),max(DateCreated))/1.0/count(*)
from TagHistory
group by TagName
having count(*)>1
order by Versions desc, Descriptions desc

select Beginning=dateadd(month, datediff(month, 0, DateCreated), 0), Versions=Count(*)
from TagHistory
group by dateadd(month, datediff(month, 0, DateCreated), 0)
order by Versions desc
