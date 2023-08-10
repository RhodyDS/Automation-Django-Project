# from unfefoll import unfandfol
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

# unfandfol( 1, ['rhodyds', 'valsaciones_cestas'], ['boatelevelfortaleza', 'vall_santhos'], 4,  0,  200,'fol', 'n')
event = {
    "notification": "Sua mensagem de notificação aqui"
}
notification = "trabalho diario já iniciado0000." 
channel_layer = get_channel_layer()
async_to_sync(channel_layer.group_send)('DashboardConsumer', {'type': 'send_notification', 'message': json.dumps(event)})

# async_to_sync(channel_layer.group_send)(
#     "DashboardConsumer",
#     {
#         "type": "send_notification",
#         "notification": notification,
#     },
# )