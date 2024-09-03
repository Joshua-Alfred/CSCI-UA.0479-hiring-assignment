-- The given question expects a left join between tables t1 and t2. 
-- A LEFT JOIN on t1 and t2 will contain all rows of t1 and have t2 columns merged to it if a record existed in t2.t1_id (foreign key). Otherwise, NULL is returned in the columns of t2.

SELECT t1.a, t1.b, t2.d
FROM t1
LEFT JOIN t2 ON t1.id = t2.t1_id;
