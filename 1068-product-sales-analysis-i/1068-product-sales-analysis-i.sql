SELECT P.product_name ,S.`year` ,S.price
From Product P
JOIN Sales S ON S.product_id =P.product_id