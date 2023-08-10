from django.shortcuts import render
from datetime import datetime
from pymongo import MongoClient
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
from django.http import JsonResponse
import json
from automations.unfefoll import unfandfol
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

def home_Dashboard(request):
    client = MongoClient("localhost", 27017)

    db = client["Rengage"]
    collection = db["workday"]
    clientes = db["clientes"]
    packs = db["packfollowers"]
    print('here')
    # event = {"notification": "Sua mensagem de notificação aquicvdc"}
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {"type": "send_notification", "message": "testando"},
    )

    all_packs = packs.distinct("user")
    all_clients = clientes.distinct("user")

    today_date = datetime.now().strftime("%Y-%m-%d")

    actual_work = collection.find_one({"data": today_date})

    return render(
        request,
        "dashboard/home_dashboard.html",
        {"actualWork": actual_work, "allClients": all_clients, "allPack": all_packs},
    )


def automation_function(request):
    channel_layer = get_channel_layer()
    for i in range(5):
        notification = f"Automação em andamento - Iteração {i}"
        async_to_sync(channel_layer.group_send)(
            "receive",
            {
                "type": "send_notification",
                "notification": notification,
            },
        )
        time.sleep(2)
    return render(request, "dashboard.html")


def automacao_view(request):
    if request.method == "POST":
        event = {"notification": "Sua mensagem de notificação aqui"}
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "test_consumer_group",
            {"type": "send_notification", "value": json.dumps(event)},
        )
        data = json.loads(request.body)
        print(data)
        dispositivo = data.get("dispositivo")
        group = data.get("group")
        pacote = data.get("pacote")
        rodadas = int(data.get("rodadas"))
        timebreak = int(data.get("tempo"))
        quantseguir = int(data.get("quantseguir"))
        func = data.get("func")
        continuar = data.get("cont")

        unfandfol(
            dispositivo, group, pacote, rodadas, timebreak, quantseguir, func, continuar
        )

        return JsonResponse(
            {"success": True, "message": "Automação concluída com sucesso!"}
        )

    return JsonResponse(
        {"success": False, "message": "Método não permitido."}, status=405
    )
