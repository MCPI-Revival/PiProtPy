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

take_item_entity = {
    "id": 0x8f, # Byte
    "target": None, # Int
    "entity_id": None # Int
}

move_entity = {
    "id": 0x90, # Byte
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None # Float
}

move_entity_posrot = {
    "id": 0x93, # Byte
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "yaw": None, # Float
    "pitch": None # Float
}

move_player = {
    "id": 0x94, # Byte
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "yaw": None, # Float
    "pitch": None # Float
}

place_block = {
    "id": 0x95, # Byte
    "entity_id": None, # Int
    "x": None, # Int
    "z": None, # Int
    "y": None, # Byte
    "block": None, # Byte
    "meta": None, # Byte
    "face": None # Byte
}

remove_block  = {
    "id": 0x96, # Byte
    "entity_id": None, # Int
    "x": None, # Int
    "z": None, # Int
    "y": None # Byte
}

update_block = {
    "id": 0x97, # Byte
    "entity_id": None, # Int
    "x": None, # Int
    "z": None, # Int
    "y": None, # Byte
    "block": None, # Byte
    "meta": None # Byte
}

add_painting = {
    "id": 0x98, # Byte
    "entity_id": None, # Int
    "x": None, # Int
    "y": None, # Int
    "z": None, # Int
    "direction": None, # Int
    "title": None # String
}

explode = {
    "id": 0x99, # Byte
    "x": None, # Float
    "y": None, # Float
    "z": None, # Float
    "radius": None, # Float
    "count": None, # Int
    "records": None, # Byte
    "has_counts": None, # Byte
    "has_records": None # Byte
}

level_event = {
    "id": 0x9a, # Byte
    "event_id": None, # Short
    "x": None, # Short
    "y": None, # Short
    "z": None, # Short
    "data": None # Int
}

tile_event = {
    "id": 0x9b, # Byte
    "x": None, # Int
    "y": None, # Int
    "z": None, # Int
    "case_1": None, # Int
    "case_2": None # Int
}

entity_event = {
    "id": 0x9c, # Byte
    "entity_id": None, # Int
    "event": None # Byte
}

request_chunk = {
    "id": 0x9d, # Byte
    "x": None, # Int
    "z": None # Int
}

chunk_data = {
    "id": 0x9e, # Byte
    "x": None, # Int
    "z": None # Int
    "data": None # byte[]
}

player_equipment = {
    "id": 0x9f,
    "block": None, # Short
    "meta": None # Short
}
