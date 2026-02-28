# 参数化晶格密度生成逻辑
def calculate_lattice_density(pressure_data):
    base_thickness = 1.2
    results = {}
    for zone, pressure in pressure_data.items():
        # 压力越大，晶格密度越高，实现梯度补强
        optimized_thickness = base_thickness + (pressure * 0.05)
        state = "Rigid_Phase" if pressure > 25 else "Flexible_Phase"
        results[zone] = {"thickness": round(optimized_thickness, 2), "state": state}
    return results
