from .converter import convert

class TemperatureRecord:
    def __init__(self, date, readings, scale):
        self.date = date
        self.readings = readings
        self.scale = scale

    def convert_to(self, target_scale):
        if self.scale != target_scale:
            self.readings = [
                convert(temp, self.scale, target_scale)
                for temp in self.readings
            ]
            self.scale = target_scale

    def get_summary(self):
        if not self.readings:
            return {'date': self.date, 'scale': self.scale, 'min': 0, 'max': 0, 'avg': 0}
        return {
            'date': self.date,
            'scale': self.scale,
            'min': round(min(self.readings), 2),
            'max': round(max(self.readings), 2),
            'avg': round(sum(self.readings) / len(self.readings), 2)
        }

    def is_above_threshold(self, threshold):
        return all(temp > threshold for temp in self.readings)
