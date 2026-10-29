"""Small SI-based engineering utilities. Python 3.9+, no dependencies."""
import math


def _positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and greater than zero")
    return value


def convert(value, source, target):
    """Convert compatible units; temperatures are absolute temperatures."""
    if not math.isfinite(value):
        raise ValueError("value must be finite")
    units = {
        "m": ("length", 1), "mm": ("length", .001),
        "ft": ("length", .3048), "in": ("length", .0254),
        "m3/s": ("flow", 1), "L/s": ("flow", .001),
        "m3/h": ("flow", 1/3600), "cfm": ("flow", .3048**3/60),
        "Pa": ("pressure", 1), "kPa": ("pressure", 1000),
        "bar": ("pressure", 100000),
    }
    temperatures = {"C", "F", "K"}
    if source in temperatures and target in temperatures:
        kelvin = {"C": lambda: value + 273.15,
                  "F": lambda: (value - 32)*5/9 + 273.15,
                  "K": lambda: value}[source]()
        if kelvin < 0:
            raise ValueError("temperature must not be below absolute zero")
        return {"C": lambda: kelvin - 273.15,
                "F": lambda: (kelvin - 273.15)*9/5 + 32,
                "K": lambda: kelvin}[target]()
    if source not in units or target not in units:
        raise ValueError("unsupported unit")
    source_kind, source_scale = units[source]
    target_kind, target_scale = units[target]
    if source_kind != target_kind:
        raise ValueError("units must describe the same physical quantity")
    return value * source_scale / target_scale


def circular_area(diameter_m):
    """Circular cross-sectional area in m2, with diameter in metres."""
    return math.pi * _positive(diameter_m, "diameter")**2 / 4


def rectangular_area(width_m, height_m):
    """Rectangular cross-sectional area in m2; dimensions in metres."""
    return _positive(width_m, "width") * _positive(height_m, "height")


def velocity(flow_m3_s, area_m2):
    """Mean velocity in m/s from nonnegative volumetric flow and area."""
    if not math.isfinite(flow_m3_s) or flow_m3_s < 0:
        raise ValueError("flow must be finite and nonnegative")
    return flow_m3_s / _positive(area_m2, "area")


def air_changes_per_hour(flow_m3_s, room_volume_m3):
    """ACH = 3600 * flow / room volume; not a ventilation requirement."""
    if not math.isfinite(flow_m3_s) or flow_m3_s < 0:
        raise ValueError("flow must be finite and nonnegative")
    return flow_m3_s * 3600 / _positive(room_volume_m3, "room volume")
