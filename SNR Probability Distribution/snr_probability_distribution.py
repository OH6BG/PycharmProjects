import math

"""
Calculate REL for an array of REQ. (required) SNR values
© Jari Perkiömäki OH6BG, 15 July 2019
"""


def cdf(z_index):
    return (1.0 + math.erf(z_index / math.sqrt(2.0))) / 2.0


SNR10 = 85.0  # for 10% of days, or 3 days, in a month
SNR = 75.0    # for median or 50% of days, or 14 days, in a month
SNR90 = 60.0  # for 90% of days, or 27 days, in a month

sigma_up = abs(SNR - SNR10) / 1.28
sigma_lw = abs(SNR - SNR90) / 1.28

# Calculate REL for REQ.SNR range of 50 to 95 dB-Hz
for y in range(50, 96, 5):

    if y <= SNR:
        z = abs(SNR - y) / sigma_lw
        zp = cdf(z)
    else:
        z = abs(SNR - y) / sigma_up
        zp = 1.0 - cdf(z)

    print("SNR %3d: z = %.2f => REL %5.2f%%" % (y, z, zp * 100))
