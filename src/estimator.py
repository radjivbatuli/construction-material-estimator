
from __future__ import annotations

from dataclasses import dataclass


class ValidationError(ValueError):
    """Raised when an estimator input is invalid."""


def _validate_positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValidationError(f"{name} must be greater than zero.")


@dataclass(frozen=True)
class ConcreteEstimate:
    cubic_yards: float
    cubic_yards_with_waste: float
    bags_80_lb: int


@dataclass(frozen=True)
class AggregateEstimate:
    cubic_yards: float
    cubic_yards_with_waste: float
    tons: float


@dataclass(frozen=True)
class SoilEstimate:
    cubic_yards: float
    cubic_yards_with_waste: float
    compacted_cubic_yards: float


class MaterialEstimator:
    """Performs common construction-material calculations."""

    CUBIC_FEET_PER_CUBIC_YARD = 27
    CONCRETE_BAG_YIELD_CUBIC_FEET = 0.6
    DEFAULT_AGGREGATE_TONS_PER_CUBIC_YARD = 1.4

    @staticmethod
    def concrete(
        length_ft: float,
        width_ft: float,
        depth_in: float,
        waste_percent: float = 10,
    ) -> ConcreteEstimate:
        for name, value in (
            ("length_ft", length_ft),
            ("width_ft", width_ft),
            ("depth_in", depth_in),
        ):
            _validate_positive(name, value)

        if waste_percent < 0:
            raise ValidationError("waste_percent cannot be negative.")

        depth_ft = depth_in / 12
        cubic_feet = length_ft * width_ft * depth_ft
        cubic_yards = cubic_feet / MaterialEstimator.CUBIC_FEET_PER_CUBIC_YARD
        cubic_yards_with_waste = cubic_yards * (1 + waste_percent / 100)

        total_cubic_feet_with_waste = (
            cubic_yards_with_waste * MaterialEstimator.CUBIC_FEET_PER_CUBIC_YARD
        )
        bags = int(
            -(
                total_cubic_feet_with_waste
                // -MaterialEstimator.CONCRETE_BAG_YIELD_CUBIC_FEET
            )
        )

        return ConcreteEstimate(
            cubic_yards=round(cubic_yards, 2),
            cubic_yards_with_waste=round(cubic_yards_with_waste, 2),
            bags_80_lb=bags,
        )

    @staticmethod
    def aggregate(
        length_ft: float,
        width_ft: float,
        depth_in: float,
        waste_percent: float = 10,
        tons_per_cubic_yard: float = DEFAULT_AGGREGATE_TONS_PER_CUBIC_YARD,
    ) -> AggregateEstimate:
        for name, value in (
            ("length_ft", length_ft),
            ("width_ft", width_ft),
            ("depth_in", depth_in),
            ("tons_per_cubic_yard", tons_per_cubic_yard),
        ):
            _validate_positive(name, value)

        if waste_percent < 0:
            raise ValidationError("waste_percent cannot be negative.")

        depth_ft = depth_in / 12
        cubic_yards = (
            length_ft * width_ft * depth_ft
            / MaterialEstimator.CUBIC_FEET_PER_CUBIC_YARD
        )
        cubic_yards_with_waste = cubic_yards * (1 + waste_percent / 100)
        tons = cubic_yards_with_waste * tons_per_cubic_yard

        return AggregateEstimate(
            cubic_yards=round(cubic_yards, 2),
            cubic_yards_with_waste=round(cubic_yards_with_waste, 2),
            tons=round(tons, 2),
        )

    @staticmethod
    def soil(
        length_ft: float,
        width_ft: float,
        depth_ft: float,
        waste_percent: float = 10,
        compaction_percent: float = 15,
    ) -> SoilEstimate:
        for name, value in (
            ("length_ft", length_ft),
            ("width_ft", width_ft),
            ("depth_ft", depth_ft),
        ):
            _validate_positive(name, value)

        if waste_percent < 0:
            raise ValidationError("waste_percent cannot be negative.")
        if not 0 <= compaction_percent < 100:
            raise ValidationError(
                "compaction_percent must be between 0 and 100."
            )

        cubic_yards = (
            length_ft * width_ft * depth_ft
            / MaterialEstimator.CUBIC_FEET_PER_CUBIC_YARD
        )
        cubic_yards_with_waste = cubic_yards * (1 + waste_percent / 100)
        compacted_cubic_yards = cubic_yards_with_waste * (
            1 - compaction_percent / 100
        )

        return SoilEstimate(
            cubic_yards=round(cubic_yards, 2),
            cubic_yards_with_waste=round(cubic_yards_with_waste, 2),
            compacted_cubic_yards=round(compacted_cubic_yards, 2),
        )
