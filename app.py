from src.feed_rate import convert_feed_rate


def main():
    print("CAM Feed Rate Converter")
    print("-----------------------")

    value = float(input("Enter feed rate: "))
    from_unit = input("From unit (mm/min or in/min): ")
    to_unit = input("To unit (mm/min or in/min): ")

    try:
        result = convert_feed_rate(value, from_unit, to_unit)
        print(f"\nResult: {result:.3f} {to_unit}")
    except ValueError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()