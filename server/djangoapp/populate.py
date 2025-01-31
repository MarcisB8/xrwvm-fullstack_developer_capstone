from .models import CarMake, CarModel


def initiate():

    car_make_data = [
        {"name": "NISSAN",
         "description": "Great cars. Japanese technology",
         "brand_level": "MEDIUM"},
        {"name": "Mercedes",
         "description": "Great cars. German technology",
         "brand_level": "PREMIUM"},
        {"name": "Audi",
         "description": "Great cars. German technology",
         "brand_level": "PREMIUM"},
        {"name": "Kia",
         "description": "Great cars. Korean technology",
         "brand_level": "MEDIUM"},
        {"name": "Toyota",
         "description": "Great cars. Japanese technology",
         "brand_level": "MEDIUM"},
        {"name": "Bentley",
         "description": "Exclusive cars. British style",
         "brand_level": "LUXURY"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                brand_level=data['brand_level']
            )
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0], "dealer_id": 1,
         "fuel": "GASOLINE", "engine": 3.0,
         "color": "BLACK", "status": "AVAILABLE"},
        {"name": "Q7", "type": "SUV", "year": 2010,
         "car_make": car_make_instances[2], "dealer_id": 2,
         "fuel": "GASOLINE", "engine": 4.5,
         "color": "RED", "status": "AVAILABLE"},
        {"name": "Land Cruiser", "type": "SUV", "year": 2009,
         "car_make": car_make_instances[0], "dealer_id": 3,
         "fuel": "DIESEL", "engine": 3.0,
         "color": "GREY", "status": "RESERVED"},
        {"name": "A6", "type": "SEDAN", "year": 2019,
         "car_make": car_make_instances[4], "dealer_id": 4,
         "fuel": "DIESEL", "engine": 3.0,
         "color": "WHITE", "status": "AVAILABLE"},
        {"name": "Continental", "type": "COUPE", "year": 2022,
         "car_make": car_make_instances[5], "dealer_id": 5,
         "fuel": "GASOLINE", "engine": 6.0,
         "color": "BLUE", "status": "COMING"},
    ]
    print("Populate not implemented. Add data manually")

    print("CarModel data to be created:", car_model_data)

    for data in car_model_data:
        try:
            car_model, created = CarModel.objects.get_or_create(
                name=data['name'],
                defaults={
                    'car_make': data['car_make'],
                    'type': data['type'],
                    'year': data['year'],
                    'dealer_id': data['dealer_id'],
                    'fuel': data['fuel'],
                    'engine': data['engine'],
                    'color': data['color'],
                    'status': data['status']
                }
            )
            if created:
                print(f"Created CarModel: {car_model.name}")
            else:
                print(f"CarModel already exists: {car_model.name}")
        except Exception as e:
            print(f"Error creating CarModel: {e}")
