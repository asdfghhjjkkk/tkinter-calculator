import os
import random
import time

FILE_NAME = "test_file.bin"
FILE_SIZE_MB = 100
BLOCK_SIZES = [2048, 4096, 8192]

results = {}

def sequential_write(file_name, block_size, num_blocks, data):
    start = time.time()
    with open(file_name, "wb") as f:
        for _ in range(num_blocks):
            f.write(data)
    end = time.time()
    return end - start

def sequential_read(file_name, block_size):
    start = time.time()
    with open(file_name, "rb") as f:
        while f.read(block_size):
            pass
    end = time.time()
    return end - start

def random_write(file_name, block_size, num_blocks, data):
    start = time.time()
    with open(file_name, "r+b") as f:
        for _ in range(num_blocks):
            pos = random.randint(0, num_blocks - 1) * block_size
            f.seek(pos)
            f.write(data)
    end = time.time()
    return end - start

def random_read(file_name, block_size, num_blocks):
    start = time.time()
    with open(file_name, "rb") as f:
        for _ in range(num_blocks):
            pos = random.randint(0, num_blocks - 1) * block_size
            f.seek(pos)
            f.read(block_size)
    end = time.time()
    return end - start


for bs in BLOCK_SIZES:
    print(f"\nBLOCK SIZE = {bs} bytes")

    file_size_bytes = FILE_SIZE_MB * 1024 * 1024
    num_blocks = file_size_bytes // bs
    data = os.urandom(bs)


    with open(FILE_NAME, "wb") as f:
        f.write(b'\x00' * file_size_bytes)


    sw_time = sequential_write(FILE_NAME, bs, num_blocks, data)
    sr_time = sequential_read(FILE_NAME, bs)
    rw_time = random_write(FILE_NAME, bs, num_blocks, data)
    rr_time = random_read(FILE_NAME, bs, num_blocks)

    results[bs] = {
        "seq_write": FILE_SIZE_MB / sw_time,
        "seq_read": FILE_SIZE_MB / sr_time,
        "rand_write": FILE_SIZE_MB / rw_time,
        "rand_read": FILE_SIZE_MB / rr_time,
        "sw_time": sw_time,
        "sr_time": sr_time,
        "rw_time": rw_time,
        "rr_time": rr_time
    }

    print(f"Ketma-ket yozish: {results[bs]['seq_write']:.2f} MB/s  | vaqt: {sw_time:.2f} s")
    print(f"Ketma-ket o‘qish: {results[bs]['seq_read']:.2f} MB/s  | vaqt: {sr_time:.2f} s")
    print(f"Tasodifiy yozish: {results[bs]['rand_write']:.2f} MB/s | vaqt: {rw_time:.2f} s")
    print(f"Tasodifiy o‘qish: {results[bs]['rand_read']:.2f} MB/s | vaqt: {rr_time:.2f} s")

print("\nEng yaxshi natijalar")

best_seq_write = max(results, key=lambda b: results[b]["seq_write"])
best_seq_read = max(results, key=lambda b: results[b]["seq_read"])
best_rand_write = max(results, key=lambda b: results[b]["rand_write"])
best_rand_read = max(results, key=lambda b: results[b]["rand_read"])

print(f"Eng tez ketma-ket yozish: {best_seq_write} bytes "
      f"({results[best_seq_write]['seq_write']:.2f} MB/s, vaqt: {results[best_seq_write]['sw_time']:.2f} s)")

print(f"Eng tez ketma-ket o‘qish: {best_seq_read} bytes "
      f"({results[best_seq_read]['seq_read']:.2f} MB/s, vaqt: {results[best_seq_read]['sr_time']:.2f} s)")

print(f"Eng tez random yozish: {best_rand_write} bytes "
      f"({results[best_rand_write]['rand_write']:.2f} MB/s, vaqt: {results[best_rand_write]['rw_time']:.2f} s)")

print(f"Eng tez random o‘qish: {best_rand_read} bytes "
      f"({results[best_rand_read]['rand_read']:.2f} MB/s, vaqt: {results[best_rand_read]['rr_time']:.2f} s)")
