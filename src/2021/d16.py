import math


def parse(data: str) -> dict[int, tuple]:
    def hexToBin(hexadecimal):
        return bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4)

    data = hexToBin(data.strip())
    return {1: (data,), 2: (data,)}


def literal_value(packet):
    bin_val = []

    while True:
        bit5 = packet[:5]
        first_bit, val_bits = bit5[0], bit5[1:]
        bin_val.append(val_bits)
        packet = packet[5:]
        if first_bit == "0":
            break

    return int("".join(bin_val), 2), packet


def operator(packet):
    length_type_id = packet[0]
    packet_infos = []

    if length_type_id == "0":
        num_of_bits = int(packet[1:16], 2)
        packet = packet[16:]
        nextPackets = packet[:num_of_bits]
        packet = packet[num_of_bits:]

        while nextPackets:
            packet_info, nextPackets = packet_parser(nextPackets)
            packet_infos.append(packet_info)
    else:
        num_of_packets = int(packet[1:12], 2)
        packet = packet[12:]

        for _ in range(num_of_packets):
            packet_info, packet = packet_parser(packet)
            packet_infos.append(packet_info)

    return packet_infos, packet


def packet_parser(packet):
    version, packet_type_id, packet = (
        int(packet[:3], 2),
        int(packet[3:6], 2),
        packet[6:],
    )
    packet_info = {
        "version": version,
        "versionSum": version,
        "packet_type_id": packet_type_id,
    }

    if packet_type_id == 4:
        value, packet = literal_value(packet)
        packet_info["value"] = value
    else:
        _packet_infos, packet = operator(packet)
        values = [packet_info.get("value", 0) for packet_info in _packet_infos]

        match packet_type_id:
            case 0:
                packet_info["value"] = sum(values)
            case 1:
                packet_info["value"] = math.prod(values)
            case 2:
                packet_info["value"] = min(values)
            case 3:
                packet_info["value"] = max(values)
            case 5:
                packet_info["value"] = 1 if values[0] > values[1] else 0
            case 6:
                packet_info["value"] = 1 if values[0] < values[1] else 0
            case 7:
                packet_info["value"] = 1 if values[0] == values[1] else 0

        packet_info["versionSum"] += sum(
            packet_info.get("versionSum", 0) for packet_info in _packet_infos
        )

    return packet_info, packet


def part1(packet):
    packet_infos = []
    while packet and set(packet) != set(
        "0",
    ):  # stop when packet is empty or there are extra 0 bits
        packet_info, packet = packet_parser(packet)
        packet_infos.append(packet_info)
    return sum(packet_info.get("versionSum", 0) for packet_info in packet_infos)


def part2(packet):
    packet_info, packet = packet_parser(packet)
    return packet_info.get("value")
