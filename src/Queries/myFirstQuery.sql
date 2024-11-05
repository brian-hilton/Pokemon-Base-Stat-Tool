--select * from person.person where FirstName = 'John' and LastName = 'Smith'
--select * from person.EmailAddress where BusinessEntityID = 18222

select * from person.person as dawg
left join person.EmailAddress as dawgmail on dawg.BusinessEntityID = dawgmail.BusinessEntityID
where dawg.FirstName = 'John' and dawg.LastName = 'Smith'
order by dawgmail.BusinessEntityID ASC

--select p.FirstName, p.LastName, ps.PasswordHash from person.person as p
--join person.Password as ps on p.BusinessEntityID = ps.BusinessEntityID 
--where p.BusinessEntityID = 7 

update Person.EmailAddress set EmailAddress = 'dawginator@dawg.edu' where BusinessEntityID = 18222 

delete from Person.EmailAddress where EmailAddressID = 19974 

 insert into Person.EmailAddress(BusinessEntityID, EmailAddress) 
 values(18222, 'dawginator@dawg.edu')