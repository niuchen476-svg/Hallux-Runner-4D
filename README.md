# 🦶 Hallux-Runner 4D: 动态步态纠偏与瞬时力矩重构系统
> **Rebuilding propulsion at the moment it matters most.**
> 支撑不应是全时段的束缚，而是在推蹬瞬间（Toe-off）发生的精确介入。

![Project Status](https://img.shields.io/badge/Status-Concept_Proof-blue.svg)
![Field](https://img.shields.io/badge/Field-Industrial_Design_/_Sports_Mechanics-green.svg)
![Technology](https://img.shields.io/badge/Tech-4D_Printing_/_Generative_Design-orange.svg)

---

## 01 | 逻辑起点：推进期失效 (Propulsion Failure)
在针对高频跑步步态的研究中，我发现拇外翻（Hallux Valgus）人群的核心痛点在于**第一射线（First Ray）在推蹬瞬间的刚性丧失**。

**⚠️ 运动损伤链分析：**
1. **结构失稳**：离地瞬间第一跖趾关节无法形成刚性杠杆。
2. **压力逃逸**：负荷被迫向外侧跖骨迁移。
3. **连锁反应**：导致足弓动态塌陷及动力链（Kinetic Chain）断裂。



---

## 02 | 核心命题：响应式结构 (Responsive Architecture)
**“如何设计一个理解‘时间’的支撑系统？”**

Hallux-Runner 4D 拒绝传统矫形器的“全时段刚性”逻辑。它通过材料物理特性的动态切换，实现了针对性的功能补强。

### 技术突破点：
* **4D 打印 SMP (形状记忆聚合物)**：通过跑步时的物理能量触发，实现材料模量（Modulus）的瞬时切换。
* **拓扑优化晶格 (Lattice Optimization)**：利用参数化建模，在有限空间内实现非匀质的力学分布。
* **动态刚度调控**：静止状态保持柔性以适应足部形态；推蹬瞬间转为刚性以提供杠杆推力。

---

## 03 | 系统交互架构 (System Architecture)

```mermaid
graph TD
    A[步态冲击能量采集] --> B{识别推进阶段阈值}
    B --> C[参数化结构受力映射]
    C --> D[4D 打印复合支架]
    D --> E[物理能量触发相变]
    E --> F[结构刚化: 辅助杠杆形成]
    F --> G[力线重构: 恢复第一射线推力]
