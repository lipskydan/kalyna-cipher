from kalyna import Kalyna, KALYNA_TYPE
from tools import string2bytes, bytes2string
import time

if __name__ == "__main__":
    time_before = time.time()

    input_data = string2bytes("101112131415161718191A1B1C1D1E1F")
    key = string2bytes("000102030405060708090A0B0C0D0E0F")

    encrypted_input = Kalyna(key, KALYNA_TYPE.KALYNA_128_128).encrypt(input_data)
    decrypted_input = Kalyna(key, KALYNA_TYPE.KALYNA_128_128).decrypt(encrypted_input)

    print(f'input_data: {bytes2string(input_data)}')
    print(f'encrypted_input: {bytes2string(encrypted_input)}')
    print(f'decrypted_input: {bytes2string(decrypted_input)}')

    time_after = time.time()
    print(' working time is ', time_after - time_before, ' seconds')

    print(decrypted_input == input_data)
