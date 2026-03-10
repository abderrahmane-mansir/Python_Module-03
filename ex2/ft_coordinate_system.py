import math


def create_coords(x: int, y: int, z: int) -> tuple:
    print(f"Position created: ({x}, {y}, {z})")
    return (x, y, z)


def unpack_coords(cords: str) -> tuple:
    print("Unpacking demonstration:")
    try:
        x, y, z = cords.split(',')
        x, y, z = int(x), int(y), int(z)
    except Exception as e:
        print(f"Error unpacking coordinates: {e}")
        print(f"Error details: Type: {e.__class__.__name__}"
              f", Args: {e.args}\n")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
    return (x, y, z)


def parse_coords(cords: str) -> tuple:
    print(f"Parsing coordinates: \"{cords}\"")
    try:
        x, y, z = cords.split(',')
        x, y, z = int(x), int(y), int(z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details: Type: {e.__class__.__name__}"
              f", Args: {e.args}\n")
        return (0, 0, 0)
    if x is not None and y is not None and z is not None:
        print(f"Parsed position: ({x}, {y}, {z})")
        cor = (x, y, z)
        return cor


def distance_calculator(cor: tuple) -> None:
    try:
        x1, y1, z1 = (0, 0, 0)
        x2, y2, z2 = cor
        distance = math.sqrt((x2 - x1) ** 2 +
                             (y2 - y1) ** 2 +
                             (z2 - z1) ** 2)
    except Exception as e:
        print(f"Error calculating distance: {e}")
        return
    if distance.is_integer():
        print(f"Distance between (0,0,0) and {cor}: {distance}\n")
    else:
        print(f"Distance between (0,0,0) and {cor}: {distance:.2f}\n")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    cor1 = create_coords(10, 20, 5)
    distance_calculator(cor1)
    cor2 = parse_coords("3,4,0")
    distance_calculator(cor2)
    try:
        parse_coords("abc,def,ghi")
    except Exception as e:
        print(e)
    unpack_coords("3,4,0")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred in main: {e}")
