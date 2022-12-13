import ast
from functools import cmp_to_key

with open("input.txt") as f:
    lines = f.read().splitlines()


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return False
        elif left < right:
            return True
        return None
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            if i == len(left):
                return True
            if i == len(right):
                return False
            new_left = left[i]
            new_right = right[i]
            result = compare(new_left, new_right)
            if result is not None:
                return result

        return None

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)


def part1(lines):
    packets = []
    for i in range(0, len(lines), 3):
        packets.append((
            ast.literal_eval(lines[i]),
            ast.literal_eval(lines[i+1])
        ))
    index_in_right_order = []
    for i in range(len(packets)):
        (left, right) = packets[i]
        result = compare(left, right)
        print(f"Pair {i+1}: {'Right order' if result else 'Not right order'}")
        if result:
            index_in_right_order.append(i+1)

    print(f"Result: {sum(index_in_right_order)}")

def part2(lines):
    packets = []
    for packet in lines:
        if packet == '':
            continue
        packets.append(ast.literal_eval(packet))
    div_packet_2 = ast.literal_eval("[[2]]")
    div_packet_6 = ast.literal_eval("[[6]]")
    packets.append(div_packet_2)
    packets.append(div_packet_6)
    packets = sorted(packets, key=cmp_to_key(lambda left, right: -1 if compare(left, right) else 1))
    for p in packets:
        print(p)
    print(f"[[2]] index: {packets.index(div_packet_2)+1}")
    print(f"[[6]] index: {packets.index(div_packet_6)+1}")
    print(f"Decoder key: {(packets.index(div_packet_2)+1) * (packets.index(div_packet_6)+1)}")


part2(lines)