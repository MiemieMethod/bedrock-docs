# Molang数学函数

本页汇总Molang数学函数。函数名和说明来源于MolangReference。

## 函数列表

当前共收录61个函数。

| 函数 | 说明（官方原文） |
| --- | --- |
| `math.abs(value)` | Absolute value of value |
| `math.acos(value)` | arccos of value |
| `math.asin(value)` | arcsin of value |
| `math.atan(value)` | arctan of value |
| `math.atan2(y, x)` | arctan of y/x. |
| `math.ceil(value)` | Round value up to nearest integral number |
| `math.clamp(value, min, max)` | Clamp value to between min and max inclusive |
| `math.copy_sign(A, B)` | Compose a floating-point value with the magnitude of `x` and the sign of `y`. |
| `math.cos(value)` | Cosine (in degrees) of value |
| `math.die_roll(num, low, high)` | Returns the sum of 'num' random numbers, each with a value from low to high. |
| `math.die_roll_integer(num, low, high)` | Returns the sum of 'num' random integer numbers, each with a value from low to high. |
| `math.ease_in_back(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, overshooting backward before accelerating into the end |
| `math.ease_in_bounce(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting with bounce oscillations and settling into the end |
| `math.ease_in_circ(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating along a circular curve toward the end |
| `math.ease_in_cubic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating rapidly toward the end |
| `math.ease_in_elastic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting with elastic oscillations before accelerating into the end |
| `math.ease_in_expo(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating extremely rapidly toward the end |
| `math.ease_in_out_back(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, overshooting at both start and end, with smoother change in the middle |
| `math.ease_in_out_bounce(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting and ending with bounce oscillations, smoother in the middle |
| `math.ease_in_out_circ(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting and ending slow, with circular acceleration and deceleration in the middle |
| `math.ease_in_out_cubic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow, accelerating rapidly in the middle, then slowing again at the end |
| `math.ease_in_out_elastic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, oscillating elastically at both start and end, with stable change in the middle |
| `math.ease_in_out_expo(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting and ending slow, with extremely rapid change in the middle |
| `math.ease_in_out_quad(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow, accelerating in the middle, then slowing again at the end |
| `math.ease_in_out_quart(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow, accelerating very rapidly in the middle, then slowing again at the end |
| `math.ease_in_out_quint(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow, accelerating extremely rapidly in the middle, then slowing again at the end |
| `math.ease_in_out_sine(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting and ending slow, with smoother change in the middle |
| `math.ease_in_quad(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating toward the end |
| `math.ease_in_quart(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating very rapidly toward the end |
| `math.ease_in_quint(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating extremely rapidly toward the end |
| `math.ease_in_sine(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting slow and accelerating smoothly toward the end |
| `math.ease_out_back(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, overshooting past the end before settling into it |
| `math.ease_out_bounce(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, approaching the end with bounce oscillations that diminish over time |
| `math.ease_out_circ(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating along a circular curve toward the end |
| `math.ease_out_cubic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating rapidly toward the end |
| `math.ease_out_elastic(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, overshooting the end with elastic oscillations before settling |
| `math.ease_out_expo(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting extremely fast and decelerating gradually toward the end |
| `math.ease_out_quad(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating toward the end |
| `math.ease_out_quart(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating very rapidly toward the end |
| `math.ease_out_quint(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating extremely rapidly toward the end |
| `math.ease_out_sine(start, end, 0_to_1)` | Output goes from start to end via 0_to_1, starting fast and decelerating smoothly toward the end |
| `math.exp(value)` | Returns _e_ raised to the `value` power |
| `math.floor(value)` | Round value down to nearest integral number |
| `math.hermite_blend(value)` | Interpolate points on a smooth curve using one of the Hermite Basis functions: `3t^2 - 2t^3`. |
| `math.inverse_lerp(start, end, value)` | Returns the normalized progress between start and end given value |
| `math.lerp(start, end, 0_to_1)` | Computes the linear interpolation between `a` and `b` with interpolation weighting factor `t` in the range `[0, 1]`, where `0 = a` and `1 = b`. |
| `math.lerprotate(start, end, 0_to_1)` | Computes a linear interpolation around a circle in the shortest direction from `a` degrees to `b` degrees with interpolation weighting factor `t` (see `math.lerp`). |
| `math.ln(value)` | Natural logarithm of value |
| `math.max(A, B)` | Return highest value of A or B |
| `math.min(A, B)` | Return lowest value of A or B |
| `math.min_angle(value)` | Minimize angle magnitude (in degrees) into the range [-180, 180) |
| `math.mod(value, denominator)` | Return the remainder of value / denominator |
| `math.pi` | Returns the float representation of the constant pi. |
| `math.pow(base, exponent)` | Elevates `base` to the `exponent`'th power |
| `math.random(low, high)` | Random value between low and high inclusive |
| `math.random_integer(low, high)` | Random integer value between low and high inclusive |
| `math.round(value)` | Round value to nearest integral number |
| `math.sign(value)` | Returns 1 if value is positive, -1 otherwise |
| `math.sin(value)` | Sine (in degrees) of value |
| `math.sqrt(value)` | Square root of value |
| `math.trunc(value)` | Round value towards zero |

## 相关参考

- [Molang](../../docs/general/molang.md)
- [Molang查询函数](molang-query-function.md)
