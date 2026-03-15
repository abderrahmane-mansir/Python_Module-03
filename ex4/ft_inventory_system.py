import sys


def main() -> None:

    inventory = {}

    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py"
              " item1:qty1 item2:qty2 ...")
        return

    for arg in sys.argv[1:]:
        name, qty = arg.split(":")
        inventory[name] = int(qty)

    print("=== Inventory System Analysis ===")

    total_items = sum(inventory.values())
    print("Total items in inventory:", total_items)

    print("Unique item types:", len(inventory))

    print("\n=== Current Inventory ===")

    list_items = ["potion", "armor", "shield", "sword", "helmet"]
    for item in list_items:
        if item in inventory:
            qty = inventory[item]
            percent = (qty / total_items) * 100
            print(f"{item}: {qty} units ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")

    most = max(inventory, key=inventory.get)
    least = min(inventory, key=inventory.get)

    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} units)")

    print("\n=== Item Categories ===")

    categories = {
        "Moderate": {},
        "Scarce": {}
    }

    for item, qty in inventory.items():
        if qty >= 5:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty

    for category, items in categories.items():
        print(f"{category}: {items}")

    print("\n=== Management Suggestions ===")

    restock = [item for item, qty in inventory.items() if qty <= 1]

    if restock:
        print("Restock needed:", ", ".join(restock))
    else:
        print("Inventory levels are good.")

    print("\n=== Dictionary Properties Demo ===")

    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))

    print("Sample lookup - 'sword' in inventory:",
          inventory.get("sword") is not None)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", e)
        print("Usage: python3 ft_inventory_system.py"
              " item1:qty1 item2:qty2 ...")
