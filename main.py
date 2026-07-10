
from __future__ import annotations

from src.estimator import MaterialEstimator, ValidationError


def read_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def choose_material() -> str:
    print("\nConstruction Material Estimator")
    print("1. Concrete")
    print("2. Aggregate")
    print("3. Soil")
    print("4. Exit")

    while True:
        choice = input("Choose an option: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Please choose 1, 2, 3, or 4.")


def run() -> None:
    while True:
        choice = choose_material()

        if choice == "4":
            print("Goodbye.")
            return

        try:
            if choice == "1":
                result = MaterialEstimator.concrete(
                    length_ft=read_float("Length (ft): "),
                    width_ft=read_float("Width (ft): "),
                    depth_in=read_float("Depth (in): "),
                    waste_percent=read_float("Waste percentage: "),
                )
                print(f"Base volume: {result.cubic_yards} cubic yards")
                print(
                    f"Volume with waste: "
                    f"{result.cubic_yards_with_waste} cubic yards"
                )
                print(f"Estimated 80-lb bags: {result.bags_80_lb}")

            elif choice == "2":
                result = MaterialEstimator.aggregate(
                    length_ft=read_float("Length (ft): "),
                    width_ft=read_float("Width (ft): "),
                    depth_in=read_float("Depth (in): "),
                    waste_percent=read_float("Waste percentage: "),
                )
                print(f"Base volume: {result.cubic_yards} cubic yards")
                print(
                    f"Volume with waste: "
                    f"{result.cubic_yards_with_waste} cubic yards"
                )
                print(f"Estimated weight: {result.tons} tons")

            else:
                result = MaterialEstimator.soil(
                    length_ft=read_float("Length (ft): "),
                    width_ft=read_float("Width (ft): "),
                    depth_ft=read_float("Depth (ft): "),
                    waste_percent=read_float("Waste percentage: "),
                    compaction_percent=read_float(
                        "Expected compaction percentage: "
                    ),
                )
                print(f"Base volume: {result.cubic_yards} cubic yards")
                print(
                    f"Volume with waste: "
                    f"{result.cubic_yards_with_waste} cubic yards"
                )
                print(
                    f"Estimated compacted volume: "
                    f"{result.compacted_cubic_yards} cubic yards"
                )

        except ValidationError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    run()
