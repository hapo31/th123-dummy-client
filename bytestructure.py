import sys
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
        if sendcount % 5 < 3:
            return 0
        if sendcount % 5 < 4:
            return int(sendcount * 7)

        return int(self._rand + sendcount * 7)

    def end(self):
        return self._sendcount >= 170