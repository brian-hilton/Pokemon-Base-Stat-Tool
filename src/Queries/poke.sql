select Pokemon,(HP + Attack + Defense + SpAttack + SpAttack + Speed) as bstat from dbo.pokemon2 
select * from dbo.pokemon2

select Pokemon, Attack from dbo.pokemon2 where Attack > 100
order by Attack ASC

select avg(cast(HP as float)) as Hpavg, 
avg(cast(Attack as float)) as AttackAvg,
avg(cast(Defense as float)) as DefenseAvg,
avg(cast(SpAttack as float)) as SpAttackAvg,
avg(cast(SpDefense as float)) as SpDefenseAvg,
avg(cast(Speed as float)) as SpeedAvg from dbo.pokemon2

exec getBaseStatAvg

