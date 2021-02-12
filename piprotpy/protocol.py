login = {
    "id": 0x82, # Byte
    "username": None, # String
    "protocol_1": None, # Int
    "protocol_2": None # Int
}

login_status = {
    "id": 0x83, # Byte
    "status": None # Int
}

ready = {
    "id": 0x84, # Byte
    "status": None # Byte
}

message = {
    "id": 0x85, # Byte
    "message": None # String
}

set_time = {
    "id": 0x86, # Byte
    "time": None # Int
}

start_game {
    "id": 0x87, # Byte
    "seed": None, # Int
    "generator": None, # Int
    "gamemode": None, # Int
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "x": None # Float
}

add_mob = {
    "id": 0x88, # Byte
    "entity_id": None, # Int
    "type": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "yaw": None, # Byte
    "pitch": None, # Byte
    "metadata": None # Metadata[]
}

add_player = {
    "id": 0x89, # Byte
    "client_id": None, # Long
    "username": None, # String
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "yaw": None, # Byte
    "pitch": None, # Byte
    "item": None, # Short
    "meta": None, # Short
    "metadata": None # Metadata[]
}

remove_player = {
    "id": 0x8a, # Byte
    "entity_id": None, # Int
    "client_id": None # Long
}

add_entity = {
    "id": 0x8c, # Byte
    "entity_id": None, # Int
    "type": None, # Byte
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "has_speed": None, # Int
    "speed_x": None, # Short
    "speed_y": None, # Short
    "speed_z": None # Short
}

remove_entity = {
    "id": 0x8d, # Byte
    "entity_id": None # Int
}

add_item_entity = {
    "id": 0x8e, # Byte
    "entity_id": None, # Int
    "block": None, # Short
    "stack": None, # Byte
    "meta": None, # Short
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "yaw": None, # Byte
    "pitch": None, # Byte
    "roll": None # Byte
}
