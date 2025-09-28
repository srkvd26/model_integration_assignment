class normalize_time:
    @staticmethod
    def normalize_time_string(time_str):

        # Convert a numeric or colon-separated string into a normalized 12-hour clock time with AM/PM.
        # Handles:
        #   - HH, HHMM, HHMMSS formats
        #   - Colon-separated inputs (H:M, H:M:S)
        #   - Missing leading zeros (e.g., '7:5' -> '7:05 AM')
        #   - Auto-corrects invalid inputs by wrapping into valid time

        # Examples:
        #     '105620'   -> '10:56:20 AM'
        #     '15:30'    -> '3:30 PM'
        #     '07'       -> '7:00 AM'
        #     '7:5'      -> '7:05 AM'
        #     '9:5:7'    -> '9:05:07 AM'
        #     '2500'     -> '1:00 AM'
        #     '99:99:99' -> '3:40:39 AM'
        #     '1261'     -> '1:01 PM'
        #     '10:56:20' -> '10:56:20 AM'

        time_str = time_str.strip()
        
        #Step 1: Split if colons exist, else treat as plain string
        if ":" in time_str:
            parts = time_str.split(":")
            parts = [int(p) if p else 0 for p in parts]  # convert to int safely

            # Normalize to always have [HH, MM, SS]
            if len(parts) == 1:
                hh, mm, ss = parts[0], 0, 0
            elif len(parts) == 2:
                hh, mm, ss = parts[0], parts[1], 0
            elif len(parts) == 3:
                hh, mm, ss = parts
            else:
                raise ValueError("Too many parts in time string")
        else:
            clean_str = time_str
            if len(clean_str) == 2:
                hh, mm, ss = int(clean_str), 0, 0
            elif len(clean_str) == 4:
                hh, mm, ss = int(clean_str[:2]), int(clean_str[2:]), 0
            elif len(clean_str) == 6:
                hh, mm, ss = int(clean_str[:2]), int(clean_str[2:4]), int(clean_str[4:])
            else:
                raise ValueError("Unsupported time format. Use HH, HHMM, HHMMSS, or colon-separated forms.")
        
        #Step 2: Auto-correct invalid values (wrap into valid time)
        ss_over, ss = divmod(ss, 60)
        mm += ss_over
        mm_over, mm = divmod(mm, 60)
        hh += mm_over
        hh = hh % 24  # wrap around 24 hours
        
        #Step 3: Format into 12-hour
        suffix = "AM" if hh < 12 else "PM"
        display_hour = hh % 12
        if display_hour == 0:
            display_hour = 12
        
        if ss > 0 or (":" in time_str and time_str.count(":") == 2) or len(time_str) == 6:
            return f"{display_hour}:{mm:02d}:{ss:02d} {suffix}"
        else:
            return f"{display_hour}:{mm:02d} {suffix}"