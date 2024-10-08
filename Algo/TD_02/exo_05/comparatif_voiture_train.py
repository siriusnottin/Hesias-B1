travel_distance_km = int(input('Longueur du trajet (en km) : '))
nbr_passengers = int(input('Nombre de passagers : '))
passengers_type = input('Selectionner nature passagers \n Famille/Groupe(F/g)')

sncf_travel_cost = 1;
cheapest_travel_type = '' #car|sncf

if 1 <= nbr_passengers <= 4:
    car_travel_cost = 1 * travel_distance_km
    sncf_travel_cost *= travel_distance_km 

    print('Cout trajet voiture :', car_travel_cost)
    print('Cout trajet sncf :', sncf_travel_cost)
elif nbr_passengers == 5:
    car_travel_cost = 2 * travel_distance_km 
    sncf_travel_cost *= travel_distance_km
elif 6 >= nbr_passengers <= 9:
    sncf_travel_cost = sncf_travel_cost  

if car_travel_cost < sncf_travel_cost:
    cheapest_travel_type = 'car' 
else:
    cheapest_travel_type = 'sncf' 
print('Moyen de transport le moins onereux :', cheapest_travel_type)
