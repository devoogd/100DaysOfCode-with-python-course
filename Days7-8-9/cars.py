cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return str(', '.join([model for model in cars['Jeep']]))


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_model = [model[0] for model in cars.values()]
    # for brand in cars.keys():
    #     first_model.append(cars[brand][0])
    return first_model


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_models = []
    for brand, models in cars.items():
        for model in models:
            if grep in model.lower():
                print(model)
                trail_models.append(model.lower())
    return sorted(trail_models)

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    cars_models_sorted = {}
    for brands, models in cars.items():
        cars_models_sorted[brands] = sorted(models)
    return cars_models_sorted

print(get_first_model_each_manufacturer())