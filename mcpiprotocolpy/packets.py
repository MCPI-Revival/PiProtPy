import struct

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

start_game = {
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
    "z": None, # Int
    "data": None # byte[]
}

player_equipment = {
    "id": 0x9f, # Byte
    "block": None, # Short
    "meta": None # Short
}

player_armor_equipment = {
    "id": 0xa0, # Byte
    "slot_1": None, # Byte
    "slot_2": None, # Byte
    "slot_3": None, # Byte
    "slot_4": None # Byte
}

interact = {
    "id": 0xa1, # Byte
    "action": None, # Byte
    "entity_id": None, # Int
    "target": None # Int
}

use_item = {
    "id": 0xa2, # Byte
    "x": None, # Int
    "y": None, # Int
    "z": None, # Int
    "face": None, # Int
    "block": None, # Short
    "meta": None, # Byte
    "entity_id": None, # Int
    "fx": None, # Float
    "fy": None, # Float
    "fz": None # Float
}

player_action = {
    "id": 0xa3, # Byte
    "action": None, # int
    "x": None, # Int
    "y": None, # Int
    "z": None, # Int
    "face": None, # Int
    "entity_id": None # Int
}

hurt_armor = {
    "id": 0xa5, # Byte
    "health": None # Byte
}

set_entity_data = {
    "id": 0xa6, # Byte
    "entity_id": None, # Int
    "metadata": None # Metadata[]
}

set_entity_motion = {
    "id": 0xa7, # Byte
    "entity_id": None, # Int
    "x": None, # Short
    "y": None, # Short
    "z": None, # Short
}

set_health = {
    "id": 0xa8, # Byte
    "health": None # Byte
}

set_spawn_position = {
    "id": 0xa9, # Byte
    "x": None, # Int
    "z": None, # Int
    "y": None # Byte
}

animate = {
    "id": 0xaa, # Byte
    "action": None, # Byte
    "entity_id": None # Int
}

respawn = {
    "id": 0xab, # Byte
    "entity_id": None, # Int
    "x": None, # Float
    "y": None, # Float
    "z": None # Float
}

send_inventory = {
    "id": 0xac, # Byte
    "entity_id": None, # Int
    "window_id": None, # Byte
    "count": None, # Short
    "slots": None, # Byte[]
    "armor": None # Byte[]
}

drop_item = {
    "id": 0xad, # Byte
    "entity_id": None, # Int
    "type": None, # Byte
    "block": None, # Short
    "stack": None, # Byte
    "meta": None # Short
}

container_open = {
    "id": 0xae, # Byte
    "window_id": None, # Byte
    "type": None, # Byte
    "slot": None, # Byte
    "title": None # String
}

container_close = {
    "id": 0xaf, # Byte
    "window_id": None # Byte
}

container_set_slot = {
    "id": 0xb0, # Byte
    "window_id": None, # Byte
    "block": None, # Short
    "stack": None, # Byte
    "meta": None # Short
}

container_set_data = {
    "id": 0xb1, # Byte
    "window_id": None, # Byte
    "property": None, # Short
    "value": None # Short
}

container_set_content = {
    "id": 0xb2, # Byte
    "window_id": None, # Byte
    "count": None, # Short
    "items": None # byte[]
}

container_ack = {
    "id": 0xb3, # Byte
    "window_id": None, # Byte
    "count": None, # Short
    "items": None # byte[]
}

chat = {
    "id": 0xb4, # Byte
    "message": None # String
}

sign_update = {
    "id": 0xb5, # Byte
    "x": None, # Short
    "y": None, # Byte
    "z": None, # Short
    "lines": None # String
}

adventure_settings = {
    "id": 0xb6, # Byte
    "flags": None # Int
}

def read_metadata(data):
    metadata = {}
    offset = 0
    while not len(data) <= offset:
        bottom = data[offset] & 0x1f
        data_type = data[offset] >> 5
        offset += 1
        if data_type == 0: # Byte
            value = data[offset]
            offset += 1
        elif data_type == 1: # Short
            value = struct.unpack("<H", data[offset:offset + 2])[0]
            offset += 2
        elif data_type == 2: # Int
            value = struct.unpack("<l", data[offset:offset + 4])[0]
            offset += 4
        elif data_type == 3: # Float
            value = struct.unpack("<f", data[offset:offset + 4])[0]
            offset += 4
        elif data_type == 4: # String
            length = struct.unpack("<H", data[offset:offset + 2])[0]
            offset += 2
            value = data[offset:offset + length].decode()
        elif data_type == 5: # Item
            value = {}
            value["block"] = struct.unpack("<H", data[offset:offset + 2])[0]
            offset += 2
            value["stack"] = data[offset]
            offset += 1
            value["meta"] = struct.unpack("<H", data[offset:offset + 2])[0]
            offset += 2
        elif data_type == 6: # Position
            value = {}
            value["x"] = struct.unpack("<l", data[offset:offset + 4])[0]
            offset += 4
            value["y"] = struct.unpack("<l", data[offset:offset + 4])[0]
            offset += 4
            value["z"] = struct.unpack("<l", data[offset:offset + 4])[0]
            offset += 4
        metadata[bottom] = {"type": data_type, "value": value}
        if (data_type << 5) == 127:
            break
    return metadata

def write_metadata(value):
    data = b""
    for bottom, dtv in value.items():
        data += bytes([(dtv["type"] << 5) & (bottom & 0x1f)])
        if dtv["type"] == 0: # Byte
            data += bytes([dtv["value"]])
        elif dtv["type"] == 1: # Short
            data += struct.pack("<H", dtv["value"])
        elif dtv["type"] == 2: # Int
            data += struct.pack("<l", dtv["value"])
        elif dtv["type"] == 3: # Float
            data += struct.pack("<f", dtv["value"])
        elif dtv["type"] == 4: # String
            data += struct.pack("<H", len(dtv["value"]))
            data += dtv["value"].encode()
        elif dtv["type"] == 5: # Item
            data += struct.pack("<H", dtv["value"]["block"])
            data += bytes([dtv["value"]["stack"]])
            data += struct.pack("<H", dtv["value"]["meta"])
        elif dtv["type"] == 6: # Position
            data += struct.pack("<l", dtv["value"]["x"])
            data += struct.pack("<l", dtv["value"]["y"])
            data += struct.pack("<l", dtv["value"]["z"])
    return data
            
