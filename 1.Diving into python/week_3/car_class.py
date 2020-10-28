import os
import csv


class CarBase:
    car_type = ''

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        try:
            string = os.path.splitext(self.photo_file_name)
            isinstance(string, str)
            return string[1]
        except ValueError:
            return str


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'
    tmp = []
    body_length = float()
    body_width = float()
    body_height = float()

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if body_whl == 0:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)
        else:
            try:
                tmp = body_whl.split('x')
                if float(tmp[0]) > 0 and float(tmp[1]) > 0 and float(tmp[2]) > 0 and len(tmp) == 3:
                    self.body_length = float(tmp[0])
                    self.body_width = float(tmp[1])
                    self.body_height = float(tmp[2])
            except ValueError:
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    try:
        def __init__(self, brand, photo_file_name, carrying, extra):
            super().__init__(brand, photo_file_name, carrying)
            self.extra = str(extra)
    except:
        list()


def get_car_list(csv_filename):
    car_list = []
    car_list_2 = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            car_list.append([i for i in row if i != ''])
        for row in car_list:
            if len(row) > 0:
                if len(row) == 5 or row[0] == 'truck' and len(row) >= 4:
                    if (row[2][-4:] == ".jpg" and len(row[2]) > 4) or (row[2][-5:] == ".jpeg" and len(row[2]) > 5) or (row[2][-4:] == '.png' and len(row[2]) > 4) \
                            or (row[2][-4:] == '.gif' and len(row[2]) > 4) or (row[3][-4:] == '.jpg' and len(row[3]) > 4) or (row[3][-5:] == '.jpeg' and len(row[3]) > 5) \
                            or (row[3][-4:] == '.png' and len(row[3]) > 4) or (row[3][-4:] == '.gif' and len(row[3]) > 4):
                        car_list_2.append(row)
        car_list = []
        print(car_list_2)
        for i in car_list_2:
            if i[0] == 'truck' and len(i) == 5:
                try:
                    float(i[4])
                    car_list.append(Truck(i[1], i[2], i[4], i[3]))
                except:
                    pass
            elif i[0] == 'truck' and len(i) == 4:
                try:
                    float(i[3])
                    car_list.append(Truck(i[1], i[2], i[3], 0))
                except:
                    pass
            elif i[0] == 'car':
                if i[2].isdigit():
                    try:
                        float(i[4])
                        car_list.append(Car(i[1], i[3], i[4], i[2]))
                    except:
                        pass
            elif i[0] == 'spec_machine':
                try:
                    float(i[3])
                    car_list.append(SpecMachine(i[1], i[2], i[3], i[4]))
                except:
                    pass
        return car_list


# #
# car = get_car_list('/Users/jsabina/PycharmProjects/Mail_Group/Dive into python/week_3/cars.csv')
# print(len(car))
# spec_machine = SpecMachine('Komatsu-D355', 'd355', '93', 'pipelayer specs')
# print(spec_machine.get_photo_file_ext())
# car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
# print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
