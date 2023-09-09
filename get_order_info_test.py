#Екатерина Каплан, 8-ая когорта, Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_get_order_info_200():
    order_response = sender_stand_request.get_order(sender_stand_request.track)
    assert order_response.status_code == 200
