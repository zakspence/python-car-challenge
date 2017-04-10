makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)

if __name__ == '__main__':

  car_types = dict()
  for make in makes:
    print('in makes with {}'.format(make))
    print('--------------------')
    car_types[make[1]] = {}
    print(car_types[make[1]])
    for model in models:
      print('in models with {}'.format(model))
      print('--------------------')
      if model[2] == make[0]:
        car_types[make[1]][model[1]] = []
        print(car_types[make[1]][model[1]])
        for car_color in available_car_colors:
          print('in available_car_colors with {}'.format(car_color))
          print('--------------------')
          if car_color[0] == model[0]:
            for color in colors:
              print('in colors with {}'.format(color))
              if color[0] == car_color[1]:
                print(car_types)
                car_types[make[1]][model[1]].append(color[1])

  print(car_types)