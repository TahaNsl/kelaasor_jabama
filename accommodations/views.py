from django.http import JsonResponse
from datetime import date
import jdatetime
from iranholidays import off_occasion_solar



ACCOMMODATIONS = [
    {"name": "ویلا در شمال", "address": "مازندران", "price": 100_0000},
    {"name": "سوئیت در تهران", "address": "سعادت آباد", "price": 50_0000},
    {"name": "کلبه جنگلی", "address": "گیلان", "price": 80_0000},
]


def today_is_persian_holiday() -> bool:
    """
    returns True if today is persian holiday
    """
    jdt = jdatetime.date.today()
    occasion = off_occasion_solar(jdt)
    return occasion is not None

def accommodations_list(request):
    """
    returns a list of the accommodations
    """
    today = date.today()
    is_holiday = today_is_persian_holiday()
    weekday = today.weekday()
    is_weekend = (weekday == 5 or weekday == 6)

    result = []
    for a in ACCOMMODATIONS:
        base = a['price']
        price = base
        if is_holiday:
            price = int(round(base * 1.20))
        elif is_weekend:
            price = int(round(base * 0.80))
        result.append({
            "name": a['name'],
            "address": a['address'],
            "price": price
        })
    return JsonResponse({"date": today.isoformat(), "is_holiday": is_holiday, "accommodations": result})