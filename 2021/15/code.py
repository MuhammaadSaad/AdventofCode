def hex_to_bin(hex):
    b = ''
    for d in hex:
        b += f'{int(d, 16):04b}'
    return b
with open('input') as f:
    data = hex_to_bin(f.read().strip())
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
def decode_for_versions(b):
    if len(b) == 0 or int(b, 2) == 0:
        return
    version = int(b[:3], 2)
    yield version
    b = b[3:]
    packet_type_id = int(b[:3], 2)
    b = b[3:]
    if packet_type_id == 4:
        ns = ''
        c = 0
        for z, *g in grouper(b, 5):
            c += 5
            ns += ''.join(g)
            if z == '0':
                n = int(ns, 2)
                break
        yield from decode_for_versions(b[c:])
    else:
        length_type_id = b[0]
        b = b[1:]
        if length_type_id == '0':
            len_sub_packets = int(b[:15], 2)
            yield from decode_for_versions(b[15:])
        elif length_type_id == '1':
            num_sub_packets = int(b[:11], 2)
            yield from decode_for_versions(b[11:])
print("Part 1:")
print(sum(decode_for_versions(data)))
Part 1:
965
from math import prod

def operator(packet_type_id, sub_packet_values):
    match packet_type_id:
        case 0:
            return sum(sub_packet_values)
        case 1:
            return prod(sub_packet_values)
        case 2:
            return min(sub_packet_values)
        case 3:
            return max(sub_packet_values)
        case 5:
            return 1 if sub_packet_values[0] > sub_packet_values[1] else 0
        case 6:
            return 1 if sub_packet_values[0] < sub_packet_values[1] else 0
        case 7:
            return 1 if sub_packet_values[0] == sub_packet_values[1] else 0
def decode(b):
    if len(b) == 0 or int(b, 2) == 0:
        return
    version = int(b[:3], 2)
    b = b[3:]
    packet_type_id = int(b[:3], 2)
    b = b[3:]
    if packet_type_id == 4:
        ns = ''
        c = 0
        for z, *g in grouper(b, 5):
            c += 5
            ns += ''.join(g)
            if z == '0':
                n = int(ns, 2)
                break
        yield n
        yield from decode(b[c:])
    else:
        length_type_id = b[0]
        b = b[1:]
        if length_type_id == '0':
            len_sub_packets = int(b[:15], 2)
            b = b[15:]
            sub_packet_values = list(decode(b[:len_sub_packets]))
            yield operator(packet_type_id, sub_packet_values)
            yield from decode(b[len_sub_packets:])
        elif length_type_id == '1':
            num_sub_packets = int(b[:11], 2)
            b = b[11:]
            sub_packet_values = list(decode(b))
            yield operator(packet_type_id, sub_packet_values[:num_sub_packets])
            yield from sub_packet_values[num_sub_packets:]
print("Part 2:")
print(list(decode(data))[0])