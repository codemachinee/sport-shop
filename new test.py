from passwords import *
from yoomoney import Client, Quickpay
from datetime import *

token = "4100116460956966.47E0EA43A8D91E10F709F2EB8566AF852B8A37BB682D92179C76F70872D7BCB47F1649F0F31CC6B2AB4" \
                "D4F33EFCB9FD6200045936DD3CDFE5E9E70B7CBA5AFF18056C02C1EAA8630938EDCFA04D8A11CA5AA70775A9CFD95CD82A1C" \
                "A82DF5851C66DC4A2522C1FBD01F16CDF5AADD56E55081CC2CD8A0360CC353103964BED59"
client = Client(token)
history = client.operation_history(label='127154290')
print(history.operations[0].datetime.date())
print(datetime.now().date())
print((datetime.now().time().hour * 3600 + datetime.now().time().minute * 60 + datetime.now().time().second) - (history.operations[0].datetime.time().hour * 3600 + history.operations[0].datetime.minute * 60 +
      history.operations[0].datetime.time().second))
print(history.operations[0].datetime)
print(history.operations[0].datetime.time().hour * 3600 + history.operations[0].datetime.minute * 60 +
      history.operations[0].datetime.time().second)
print(history.operations)

str(history.operations[0].datetime).find(str(datetime.now().date()))