# IYAMAM Engineering Tools

A new, small Python toolkit for unit conversion and basic engineering arithmetic, created on 29 October 2026. Associated websites: https://www.iyamam.in and https://www.iyamam.com.

This repository starts a public code project. It is not a migration of the existing website calculators and does not claim their usage, historical contributions, independent validation, or community adoption. Initial implementation was prepared with AI assistance and includes automated checks.

## Run

Requires Python 3.9 or later. No third-party dependencies.

```python
from engineering_tools import convert, rectangular_area, velocity, air_changes_per_hour

print(convert(1000, 'cfm', 'L/s'))  # 471.9474432
print(velocity(1, rectangular_area(.4, .5)))  # 5 m/s
print(air_changes_per_hour(.5, 300))  # 6 ACH
```

Run checks with `python -m unittest -v` from this folder.

## Methods and units

- Length: m, mm, ft, in. One international foot is 0.3048 m; one inch is 0.0254 m.
- Volumetric flow: m3/s, L/s, m3/h, cfm. Cubic feet use the international foot.
- Pressure: Pa, kPa, bar (1 bar = 100,000 Pa).
- Absolute temperature: C, F, K; values below absolute zero are rejected. Temperature differences are not supported.
- Circular area: pi * diameter squared / 4.
- Rectangular area: width * height.
- Mean velocity: volumetric flow / area.
- Air changes per hour: volumetric flow * 3600 / room volume.

Geometric inputs use metres, volumes use m3, and flow inputs use m3/s. Dimensions must be positive and finite; flow may be zero. Conversions preserve signed values except physically invalid absolute temperatures.

## Scope

These are arithmetic utilities, not code-compliance or design-approval tools. They do not select required ventilation rates, size complete HVAC systems, calculate pressure loss, or certify engineering designs. Independently review inputs, assumptions, and outputs for any practical use.

## Contributing

Issues and pull requests with reproducible examples are welcome. Include units, expected results, and references where relevant. No external adoption or contribution history is claimed at launch.

## License

MIT; see LICENSE.
