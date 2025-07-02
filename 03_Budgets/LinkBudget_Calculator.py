import numpy as np

# Constants
c = 3e8
frequency = 437e6
distance = 1200e3

Pt_dBm = 30
Gt_dBi = 0
Gr_dBi = 5
L_misc_dB = 2

fspl_dB = 20 * np.log10(distance) + 20 * np.log10(frequency) - 147.55
Pr_dBm = Pt_dBm + Gt_dBi + Gr_dBi - fspl_dB - L_misc_dB

print(f"Free-space path loss: {fspl_dB:.2f} dB")
print(f"Received power: {Pr_dBm:.2f} dBm")
