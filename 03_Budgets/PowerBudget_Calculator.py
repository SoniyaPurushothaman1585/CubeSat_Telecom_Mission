orbit_min = 95
sunlight_frac = 0.65
eclipse_frac = 0.35

subsystems = {
    'OBC': 0.6,
    'ADCS': 0.5,
    'Comm': 2.0,
    'EPS': 0.2,
    'Payload': 0.3,
    'Idle': 0.4
}

total_draw = sum(subsystems.values())
energy_Wh = total_draw * orbit_min / 60
battery_min = total_draw * eclipse_frac * orbit_min / 60
solar_needed = energy_Wh / (sunlight_frac * orbit_min / 60)

print(f"Power Draw: {total_draw:.2f} W")
print(f"Energy/orbit: {energy_Wh:.2f} Wh")
print(f"Battery Min: {battery_min:.2f} Wh")
print(f"Solar Input: {solar_needed:.2f} W")
