from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os
import json

def transactions_list(request):
    """
    returns a list of transactions
    """
    base = settings.BASE_DIR
    file_path = os.path.join(base, "data", "transactions.json")

    if not os.path.exists(file_path):
        return JsonResponse({
            "error": "transactions.json not found. Put the file in data/transactions.json"
        }, status=404)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return JsonResponse({"transactions": data})