# isValidNumber
This project implements a Deterministic Finite Automaton (DFA) to check whether a given string is a valid number or not. The problem can be found on LeetCode under the name "Valid Number." Difficulty : Hard

---
[Video](https://drive.google.com/drive/folders/1usDtiu5BoR-dehTT_N-e-xcZPz_qoMJY?usp=sharing)

## FSM Overview
- **q0**: Start state.
- **q1**: Sign state (after reading `+` or `-`).
- **q2**: Integer part (digits before a decimal or exponent).
- **q3**: Decimal point state.
- **q4**: Fractional part (digits after the decimal).
- **q5**: Exponent state (after reading `e` or `E`).
- **q6**: Sign for exponent (after reading `+` or `-` in the exponent).
- **q7**: Exponent number (digits in the exponent).
- **q_dead**: Dead state (invalid input).

## FSM Transition Table

| Current State | Input          | Next State  |
|----------------|----------------|--------------|
| `q0`           | `+`, `-`       | `q1`        |
| `q0`           | Digit          | `q2`        |
| `q0`           | `.`            | `q3`        |
| `q0`           | Any other      | `q_dead`    |
| `q1`           | Digit          | `q2`        |
| `q1`           | `.`            | `q3`        |
| `q1`           | Any other      | `q_dead`    |
| `q2`           | Digit          | `q2`        |
| `q2`           | `.`            | `q3`        |
| `q2`           | `e`, `E`       | `q5`        |
| `q2`           | Any other      | `q_dead`    |
| `q3`           | Digit          | `q4`        |
| `q3`           | Any other      | `q_dead`    |
| `q4`           | Digit          | `q4`        |
| `q4`           | `e`, `E`       | `q5`        |
| `q4`           | Any other      | `q_dead`    |
| `q5`           | `+`, `-`       | `q6`        |
| `q5`           | Digit          | `q7`        |
| `q5`           | Any other      | `q_dead`    |
| `q6`           | Digit          | `q7`        |
| `q6`           | Any other      | `q_dead`    |
| `q7`           | Digit          | `q7`        |
| `q7`           | Any other      | `q_dead`    |
| `q_dead`       | Any input      | `q_dead`    |



