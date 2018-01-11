import sys
import json
from struct import Struct
import random

class th123_packet():
    def __init__(self, rand=random.randint(0, 2147483647)):
        self._rand = rand
        self._sendcount = 0

    def next(self):
        data = bytearray([
            0x01, # 固定 1byte
            0x02, 0x00, 0x2a, 0x30, # 固定 4bytes
            0x7f, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00, 0x80, 0x69, 0x00, 0x69, 0x00, # バージョン情報 12bytes
            0x02, 0x00, 0x2a, 0x30, # 固定 4bytes
            0x7f, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00, 0x80, 0x69, 0x00, 0x69, 0x00, # バージョン情報 12bytes
        ])

        data += bytes(
            self._get_sendcount(self._sendcount)
            .to_bytes(4, byteorder="little") # 送信回数
        )

        self._sendcount += 1
        return data

    def _get_sendcount(self, sendcount):
        if sendcount % 5 < 2:
            return 0
        if sendcount % 5 < 4:
            return int(sendcount / 5)

        return int(self._rand + sendcount / 5)

    def end(self):
        return self._sendcount >= 170


class th123_imitation_packet():
    def __init__(self):
        with open("sample.json", "r") as f:
            self._buffers = json.load(f)
            print(len(self._buffers))
            self._count = 0

    def next(self):
        data = self._buffers[self._count]
        self._count += 1
        return data

    def end(self):
        return len(self._buffers) >= self._count