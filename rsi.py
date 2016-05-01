#!/usr/bin/env python3
class Piece():
    def __init__(self, rsi_value, area):
        self.rsi_value = rsi_value  # m^2*K/W
        self.area = area  # m^2


def watts_lost_from(piece, temperature_delta):
    """
    Calculates heat loss from area, rsi value and temperature delta

    temperature_delta: K

    Returns heat loss in Watts
    """
    return temperature_delta / piece.rsi_value * piece.area


def main():
    total_loss_watts = 0
    temperature_delta = 10

    pieces = [Piece(2, 10)]

    for p in pieces:
        piece_loss = watts_lost_from(p, temperature_delta)
        total_loss_watts += piece_loss

    print('Total heat loss %d Watts' % total_loss_watts)

if __name__ == '__main__':
    main()
