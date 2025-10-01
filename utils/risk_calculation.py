# diabetic - 1 | 0
# spo2 - (90%-100%) | (85%-89%) | Below 85%
# temp - 36.1–37.2°C (97–99°F) | 35.0–35.9°C (95–96.6°F) or 37.3–39.0°C (99.1–102.2°F) | < 35.0°C (95.0°F) or > 39.0°C (102.2°F)
# age               Heart Rate
# (0–11 month)	    70–190
# (1–5 years)	    80–130
# (6–11 years)	    75–120
# (12+ years)	    60–100


def risk_calculation(dbt, spo2, temp, age, hrate):
    score = 0
    match dbt:
        case 1:
            score+=1
            match spo2:
                case _ if spo2 not in range(90, 101):
                    score+=1
                    match temp:
                        case _ if temp not in range(97, 100):
                            score+=1
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                        case _ if temp in range(97, 100):
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                case _ if spo2 in range(90, 101):
                    match temp:
                        case _ if temp not in range(97, 100):
                            score+=1
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                        case _ if temp in range(97, 100):
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
        case 0:
            match spo2:
                case _ if spo2 not in range(90, 101):
                    score+=1
                    match temp:
                        case _ if temp not in range(97, 100):
                            score+=1
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                        case _ if temp in range(97, 100):
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                case _ if spo2 in range(90, 101):
                    match temp:
                        case _ if temp not in range(97, 100):
                            score+=1
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
                        case _ if temp in range(97, 100):
                            match age:
                                case _ if age < 1:
                                    if hrate not in range(70, 191):
                                        score+=1
                                case _ if age in range(1, 6):
                                    if hrate not in range(80, 131):
                                        score+=1
                                case _ if age in range(6, 12):
                                    if hrate not in range(75, 121):
                                        score+=1
                                case _ if age >= 12:
                                    if hrate not in range(60, 101):
                                        score+=1
    probability = (score/4)
    label = ""
    match probability:
        case _ if probability < 0.5:
            label = "Low"
        case _ if 0.5 <= probability < 0.75:
            label = "Medium"
        case _ if probability >= 0.75:
            label = "High"
        
    return probability, label
