.read data.sql


CREATE TABLE number_of_options AS
  SELECT COUNT(*) AS number_of_options FROM main_course;


CREATE TABLE calories AS
  SELECT COUNT(*) FROM main_course AS m, pies AS p WHERE m.calories + p.calories < 2500;


CREATE TABLE healthiest_meats AS
  SELECT m.meat AS 'meat',MIN(m.calories+p.calories) AS 'total calories'
  FROM main_course AS m, pies AS p 
  GROUP BY m.meat HAVING m.calories+p.calories <= 3000;

