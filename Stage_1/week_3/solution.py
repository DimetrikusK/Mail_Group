import os
import csv


class CarBase:
    car_type = ''

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        string = os.path.splitext(self.photo_file_name)
        if isinstance(string, str):
            print(string)
        else:
            print("ERROR")


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
        tmp = body_whl.split('x')
        try:
            if float(tmp[0]) > 0 and float(tmp[1]) > 0 and float(tmp[2]) > 0 and len(tmp) == 3:
                self.body_length = float(tmp[0])
                self.body_width = float(tmp[1])
                self.body_height = float(tmp[2])
        except ValueError:
            print("Невалидное значение")


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = str(extra)


def get_car_list(csv_filename):
    car_list = []
    car_list_2 = []
    with open(csv_filename, encoding='utf-8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            car_list.append([i for i in row if i != ''])
        for row in car_list:
            if len(row) == 5:
                if ('.jpg' in row[2]) or ('.jpeg' in row[2]) or ('.png' in row[2]) or ('.gif' in row[2]) or \
                        ('.jpg' in row[3]) or ('.jpeg' in row[3]) or ('.png' in row[3]) or ('.gif' in row[3]):
                    car_list_2.append(row)
        car_list = []
        for i in car_list_2:
            if i[0] == 'truck':
                car_list.append(Truck(i[1], i[2], i[3], i[4]))
            elif i[0] == 'car':
                car_list.append(Car(i[1], i[2], i[3], i[4]))
            elif i[0] == 'spec_machine':
                car_list.append(Car(i[1], i[2], i[3], i[4]))
        return car_list


spec_machine = SpecMachine('Komatsu-D355', 'sad.png', '93', 'pipelayer specs')
spec_machine.get_photo_file_ext()