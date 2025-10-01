import re

class Normalizer:
    @staticmethod
    def normalize_values(dbt, spo2, temp, age, hrate):
        
        # normalizing Diabetic
        dbt_map = {"YES": 1, "TRUE": 1, "NO": 0, "FALSE": 0}
        if dbt not in (0, 1):
            dbt = dbt_map.get(str(dbt).upper(), None)

        # normalizing SpO2
        try:
            val = float(spo2)
            spo2 = round(val * 100) if val <= 1 else round(val)
            spo2 = max(0, min(100, spo2))
        except (ValueError, TypeError):
            spo2 = None

        # normalizing Temperature
        try:
            t = float(temp)
            if 30 <= t <= 45:      # Celsius
                t = (t * 9/5) + 32
            temp = max(80, min(110, round(t, 1)))
        except (ValueError, TypeError):
            temp = None

        # normalizing Age
        try:
            if isinstance(age, str):
                val_lower = age.strip().lower()
                if val_lower in ["newborn", "infant", "baby"]:
                    age = 0
                elif m := re.search(r"(\d+(\.\d+)?)\s*month", val_lower):
                    age = float(m.group(1)) / 12
                elif m := re.search(r"(\d+(\.\d+)?)\s*week", val_lower):
                    age = float(m.group(1)) / 52
                elif m := re.search(r"(\d+(\.\d+)?)\s*day", val_lower):
                    age = float(m.group(1)) / 365
                elif m := re.search(r"(\d+(\.\d+)?)", val_lower):
                    age = float(m.group(1))
                else:
                    age = None
            else:
                age = float(age)

            if age is not None:
                age = round(age)
                age = None if age < 0 else min(120, age)
        except (ValueError, TypeError):
            age = None

        # normalizing Heart Rate
        try:
            hr = float(hrate)
            if hr <= 0:
                hrate = None
            else:
                if hr <= 10:  # Hz → bpm
                    hr *= 60
                hrate = max(30, min(220, round(hr)))
        except (ValueError, TypeError):
            hrate = None

        return dbt, spo2, temp, age, hrate