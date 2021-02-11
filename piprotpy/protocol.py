login = {
    "id": 0x82,
    "username": None,
    "protocol_1": None,
    "protocol_2": None
}

login_status = {
    "id": 0x83,
    "status": None
}

ready = {
    "id": 0x84,
    "status": None
}

message = {
    "id": 0x85,
    "message": None
}

set_time = {
    "id": 0x86,
    "time": None
}

start_game {
    "id": 0x87,
    "seed": None,
    "generator": None,
    "gamemode": None,
    "entity_id": None,
    "x": None,
    "y": None,
    "x": None
}

add_mob = {
    "id": 0x88,
    "entity_id": None,
    "type": None,
    "x": None,
    "y": None,
    "z": None,
    "yaw": None,
    "pitch": None,
    "metadata": None
}

add_player = {
    "id": 0x89,
    "client_id": None,
    "username": None,
    "entity_id": None,
    "x": None,
    "y": None,
    "z": None,
    "yaw": None,
    "pitch": None,
    "item": None,
    "meta": None,
    "metadata": None
}

remove_player = {
    "id": 0x8a,
    "entity_id": None,
    "client_id": None
}

add_entity_packet = {
    "id": 0x8c,
    "entity_id": None,
    "type": None,
    "x": None,
    "y": None,
    "z": None,
    "has_speed": None,
    "speed_x": None,
    "speed_y": None,
    "speed_z": None
}

remove_entity_packet = {
    "id": 0x8d,
    "entity_id": None
}
