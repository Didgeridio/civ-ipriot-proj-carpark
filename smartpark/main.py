from parking_lot import ParkingLot

def get_message(client, userdata, message):
    msg = message.payload.decode('UTF-8')
    print(msg)
    # if car entering
    #       process the car
    # if car exiting
    #       process the car leaving
    # if xxxx
    # do something

pl = ParkingLot()
pl.create_mqtt_client()



if __name__=='__main__':
    pl.mqtt_client.client.subscribe("carpark//parking-lot/controller")
    pl.mqtt_client.client.on_message = get_message
    print(pl.mqtt_client.name)
    print(pl.mqtt_client.topic)
    print(pl.location)
    print(pl.total_spaces)

    pl.mqtt_client.client.loop_forever()