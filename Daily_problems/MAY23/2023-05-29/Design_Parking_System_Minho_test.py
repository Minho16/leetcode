from Design_Parking_System_Minho import ParkingSystem


def test_parking_system() -> None:
    parking = ParkingSystem(1, 0, 0)
    check = parking.addCar(1)
    assert check


def test_not_enough_parking_zones_for_big() -> None:
    parking = ParkingSystem(1, 0, 0)
    parking.addCar(1)
    check = parking.addCar(1)
    assert not check


def test_enough_parking_zones() -> None:
    parking = ParkingSystem(10, 10, 10)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    parking.addCar(1)
    check = parking.addCar(1)
    assert check

    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    parking.addCar(2)
    check_2 = parking.addCar(2)
    assert check_2
