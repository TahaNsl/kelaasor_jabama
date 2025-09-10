from django.http import JsonResponse
from datetime import datetime, date


MY_RESERVATIONS = [
    {"name":"ویلا در شمال", "date": "2025-09-06"},
    {"name":"سوئیت در تهران", "date": "2025-09-19"},
    {"name":"کلبه جنگلی", "date": "2025-09-10"},
]

def parse_iso(dstr):
    """
    converts date string to ISO date
    """
    return datetime.strptime(dstr, "%Y-%m-%d").date()

def my_reservations_list(request):
    """
    returns a list of the user reservations
    """
    today = date.today()
    result = []
    for r in MY_RESERVATIONS:
        rdate = parse_iso(r["date"])
        if rdate == today:
            status = 0
        elif rdate < today:
            status = -1
        else:
            status = 1
        result.append({
            "name": r["name"],
            "reservation_date": r["date"],
            "status": status
        })
    return JsonResponse({"today": today.isoformat(), "reservations": result})