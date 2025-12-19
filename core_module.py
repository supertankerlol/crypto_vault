import struct

def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

def sha256_simplified(data: bytes) -> str:
    # Initial Hash Values (First 32 bits of fractional parts of square roots of first 8 primes)
    h0, h1, h2, h3, h4, h5, h6, h7 = (
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    )

    # Pre-processing: Padding
    orig_len_bits = (len(data) * 8) & 0xffffffffffffffff
    data += b'\x80'
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'
    data += struct.pack('>Q', orig_len_bits)

    # Process in 512-bit chunks
    for i in range(0, len(data), 64):
        chunk = data[i:i+64]
        w = list(struct.unpack('>16L', chunk)) + [0]*48
        for j in range(16, 64):
            s0 = rotr(w[j-15], 7) ^ rotr(w[j-15], 18) ^ (w[j-15] >> 3)
            s1 = rotr(w[j-2], 17) ^ rotr(w[j-2], 19) ^ (w[j-2] >> 10)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xFFFFFFFF

        # Compression loop logic omitted for brevity in this snippet,
        # but follows the standard Sigma/Choice/Majority functions.
        # Student should be able to explain the 64 rounds of mixing.

    return f"{h0:08x}{h1:08x}{h2:08x}{h3:08x}{h4:08x}{h5:08x}{h6:08x}{h7:08x}"