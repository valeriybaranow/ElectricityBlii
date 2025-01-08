from faker import Faker

from Model.ElectricMeterModel import ElectricMeter


def choose_electric_meter(electric_meter_data):

    electric_meter = ElectricMeter.get(ElectricMeter.number == electric_meter_data.number)
    electric_meter.payer = f"test{electric_meter.number}"
    electric_meter.save()

    print(print("number =", electric_meter_data.number))
