SELECT EU.unique_id , E.name
From EmployeeUNI EU
RIGHT JOIN Employees E ON E.id=EU.id
