SELECT d.flavor AS flavor, MIN(p.price)*c.k AS total
FROM donuts AS s, prices AS p, quantity AS q
WHERE d.kind = p.dough AND q.choice = d.flavor
GROUP BY d.flavor;