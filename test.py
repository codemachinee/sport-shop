from yoomoney import Authorize
from yoomoney import Client

#Authorize(
 #   client_id='C0D4E2EB774D66707295C5BAC236D4203CF5920F2181E54418AFAFA1A8CC9879',
  #  redirect_uri='https://t.me/lemonaade_bot',
   # scope=["account-info",
    #       "operation-history",
     #      "incoming-transfers",
      #     "payment-p2p",
       #    "payment-shop",
   # ]
#)


#token = "4100116460956966.47E0EA43A8D91E10F709F2EB8566AF852B8A37BB682D92179C76F70872D7BCB47F1649F0F31CC6B2AB4D4F33EFCB9FD6200045936DD3CDFE5E9E70B7CBA5AFF18056C02C1EAA8630938EDCFA04D8A11CA5AA70775A9CFD95CD82A1CA82DF5851C66DC4A2522C1FBD01F16CDF5AADD56E55081CC2CD8A0360CC353103964BED59"
#client = Client(token)
#user = client.account_info()
#print("Account number:", user.account)
#print("Account balance:", user.balance)
#print("Account currency code in ISO 4217 format:", user.currency)
#print("Account status:", user.account_status)
#print("Account type:", user.account_type)
#print("Extended balance information:")
#for pair in vars(user.balance_details):
 #   print("\t-->", pair, ":", vars(user.balance_details).get(pair))
#print("Information about linked bank cards:")
#cards = user.cards_linked
#if len(cards) != 0:
  #  for card in cards:
 #       print(card.pan_fragment, " - ", card.type)
#else:
#    print("No card is linked to the account")

from yoomoney import Quickpay
quickpay = Quickpay(
            receiver="4100116460956966",
            quickpay_form="shop",
            targets="payment",
            paymentType="SB",
            sum=150,
            label=15
            )
print(quickpay.base_url)
print(quickpay.redirected_url)