def average_temperature_across_days(records):
    temps = [temp for record in records for temp in record.readings]
    return round(sum(temps) / len(temps), 2) if temps else 0

def hottest_day(records):
    if not records:
        return ""
    return max(records, key=lambda r: sum(r.readings) / len(r.readings)).date

def detect_extreme_days(records, threshold):
    return [r.date for r in records if any(t > threshold for t in r.readings)]

def temperature_range_for_each_day(records):
    return {
        r.date: (min(r.readings), max(r.readings)) if r.readings else (0, 0)
        for r in records
    }

def temperature_trend(temps):
    if not temps or len(temps) < 2:
        return []
    return [
        'up' if temps[i] > temps[i-1] else 'down' if temps[i] < temps[i-1] else 'same'
        for i in range(1, len(temps))
    ]

def detect_spike(temps, *, threshold=5):
    return any(abs(temps[i] - temps[i - 1]) >= threshold for i in range(1, len(temps)))
