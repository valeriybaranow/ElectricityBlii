from Model.ElectricMeterModel import ElectricMeter


def choose_electric_meter(electric_meter_data):
    electric_meter = ElectricMeter.get(ElectricMeter.electric_meter_id == electric_meter_data.id)
    if electric_meter.payer is None:
        electric_meter.payer = electric_meter_data.username
        electric_meter.save()
        print(f"счетчик прикреплен к пользователю {electric_meter.payer}")
    else:
        print(f"невозможно закрепить счетчик счетчик уже закреплен за пользователем {electric_meter.payer}")


