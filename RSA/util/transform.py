import math


def bytes2int(raw_bytes: bytes) -> int:
    # When using unicode strings, encode it to some encoding like UTF8 first.
    # List -> 8-bit string
    #   >>> bytes2int(b'\x80@\x0f')
    #   8405007

    #    >>> (((128 * 256) + 64) * 256) + 15
    #    8405007
    return int.from_bytes(raw_bytes, "big", signed=False)


def int2bytes(number: int, fill_size: int = 0) -> bytes:
    if number < 0:
        raise ValueError("Number must be an unsigned integer: %d" % number)

    bytes_required = max(1, math.ceil(number.bit_length() / 8))

    if fill_size > 0:
        return number.to_bytes(fill_size, "big")

    return number.to_bytes(bytes_required, "big")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
