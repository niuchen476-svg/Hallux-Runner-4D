import math

class HalluxLatticeGenerator:
    """
    Hallux-Runner 4D: 参数化晶格密度生成器
    逻辑：根据第一跖骨（MTP1）的瞬时压力自动调整支架晶格密度
    """
    def __init__(self, pressure_data):
        self.pressure_data = pressure_data  # 输入压力数据 (N/cm^2)
        self.base_thickness = 1.2           # 基础杆件厚度 (mm)

    def calculate_lattice_density(self):
        print("--- 正在进行拓扑优化计算 ---")
        results = {}
        for zone, pressure in self.pressure_data.items():
            # 逻辑：压力越大，晶格厚度越高（补强），实现 4D 打印的梯度分布
            optimized_thickness = self.base_thickness + (pressure * 0.05)
            
            # 限制最大厚度，保证轻量化
            optimized_thickness = min(optimized_thickness, 4.5)
            
            results[zone] = {
                "input_pressure": f"{pressure} N/cm^2",
                "lattice_thickness": f"{round(optimized_thickness, 2)} mm",
                "material_state": "Rigid_Phase" if pressure > 25 else "Flexible_Phase"
            }
        return results

# 模拟跑步推蹬阶段（Toe-off）的实时压力输入
toe_off_pressure = {
    "hallux_zone": 35.5,    # 拇指区：高压，需强支撑
    "medial_arch": 15.2,    # 内侧足弓：中压
    "lateral_edge": 8.5     # 外侧缘：低压，保持柔韧
}

# 执行生成逻辑
generator = HalluxLatticeGenerator(toe_off_pressure)
optimized_config = generator.calculate_lattice_density()

# 输出结果
for zone, config in optimized_config.items():
    print(f"区域: {zone} | 压力: {config['input_pressure']} -> 建议晶格厚度: {config['lattice_thickness']} ({config['material_state']})")

print("\n[Status] 拓扑模型已生成，准备导出至 4D 打印机 (SMP材料)。")
