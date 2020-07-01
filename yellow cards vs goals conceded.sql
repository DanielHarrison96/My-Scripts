select p1.hometeam, sum(p1.HY)+ sum(p2.Ay) , sum(p1.ftag)+ sum(p2.fthg), sum(p1.HY)+ sum(p2.Ay) -sum(p1.HR)- sum(p2.AR) 
from prem p1, prem p2 
where p1.hometeam = p2.awayteam and p1.awayteam=p2.hometeam 
group by p1.hometeam