def calculate_range(weight_jet, weight_fuel, drag_coefficient, sfc):
    """
    Calculate the range of a jet fighter using the Breguet range equation.

    Parameters:
    weight_jet (float): Weight of the jet fighter in kg.
    weight_fuel (float): Weight of the fuel in kg.
    drag_coefficient (float): Drag coefficient (dimensionless).
    sfc (float): Specific fuel consumption in kg/(N·s).

    Returns:
    float: Range of the aircraft in meters.
    """
    g = 9.81  # acceleration due to gravity in m/s^2

    # Total initial weight
    weight_total = weight_jet + weight_fuel

    # Calculate the lift-to-drag ratio (simplified assumption)
    lift_drag_ratio = 0.174 / drag_coefficient  # Example relationship

    # Calculate the range using the Breguet range equation
    range_meters = (lift_drag_ratio / sfc) * (weight_total / weight_jet) * (weight_fuel / g)

    return range_meters

# F-14B example parameters
weight_jet = 29000  # kg (empty weight of the F-14B)
weight_fuel = 7348  # kg (maximum fuel load)
drag_coefficient = 0.022  # example drag coefficient
sfc = .0007  # specific fuel consumption in kg/(N·s)

# Calculate range
range_of_aircraft = calculate_range(weight_jet, weight_fuel, drag_coefficient, sfc)

# Convert range to kilometers
range_km = range_of_aircraft / 1000

print(f"The range of the F-14B with maximum fuel is approximately {range_km:.2f} kilometers.")

