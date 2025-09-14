select p.name, pr.name
from products p
INNER JOIN categories c ON c.id=p.id_categories
INNER JOIN providers pr ON pr.id=p.id_providers 
WHERE p.id_categories=6