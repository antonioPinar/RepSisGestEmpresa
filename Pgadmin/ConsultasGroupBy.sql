/*consulta 1*/
SELECT anno as año, sum(caida_motocicleta) as "Caida Motocicleta", sum(caida_ciclomotor) as "Caida Ciclomotor",
		sum(caida_bicicleta)as "Caida Bicicleta", sum(caida_viajero_bus) as "Caida Viajero" 
FROM accidentes 
GROUP BY anno 
ORDER BY anno asc;


/*consulta 2*/
SELECT anno, sum(caida_motocicleta) as "Caida Motocicleta", sum(caida_ciclomotor)as "Caida Ciclomotor",
			sum(caida_bicicleta)as "Caida Bicicleta", sum(caida_viajero_bus) as "Caida Viajero",
			sum(caida_motocicleta+caida_ciclomotor+caida_bicicleta+caida_viajero_bus) as "Caidas Totales" 
FROM accidentes 
GROUP BY anno 
ORDER BY anno asc;


/*consulta 3*/
SELECT distrito, sum(colision_doble) as "Colision Doble", sum(colision_multiple) as "Colision Multiple",
			sum(choque_con_objeto_fijo) as "Choque con Objeto", sum(colision_doble+colision_multiple+choque_con_objeto_fijo) as "Total Colisiones"
FROM accidentes 
GROUP BY distrito;


/*consulta 4*/
SELECT distrito,anno, 
		sum(colision_doble+colision_multiple+choque_con_objeto_fijo+atropello+vuelco+caida_motocicleta+caida_ciclomotor+caida_bicicleta+caida_viajero_bus+otras_causas) as "Accidentes" 
FROM accidentes 
GROUP BY (distrito,anno) 
ORDER BY anno;