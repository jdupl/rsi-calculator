#!/usr/bin/env python3
import yaml


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


def load_yaml(f):
    pieces = []
    sun_power = 500  # Watt/m^2

    with open(f, 'r') as stream:
        yaml_data = yaml.load(stream)

        power = yaml_data['collectable_width'] * \
            yaml_data['collectable_length'] * sun_power

        for piece in yaml_data['pieces']:
            if 'rsi' in piece:
                rsi = piece['rsi']
            elif 'rimp' in piece:
                rsi = piece['rimp'] * 0.1761101838
            else:
                raise Exception('Invalid YAML')

            area = piece['width'] * piece['length']
            pieces.append(Piece(rsi, area))
    return power, pieces


def main():
    power, pieces = load_yaml('panel_2_4.yaml')

    for t in range(1, 10):
        total_loss_watts = 0
        temperature_delta = t * 10

        for p in pieces:
            piece_loss = watts_lost_from(p, temperature_delta)
            total_loss_watts += piece_loss

        efficiency = (power - total_loss_watts) / power * 100.0
        print('Total heat loss %d Watts @ %d K delta. Eff %d%%' %
              (total_loss_watts, temperature_delta, efficiency))

if __name__ == '__main__':
    main()
