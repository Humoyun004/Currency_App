from django.shortcuts import render
import requests
from .models import History

def home(request):
    return render(request, 'transferer/index.html')

def transaction(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get('amount'))
            transferTo = request.POST.get("transferTo")
            fromTransfer = request.POST.get("fromTransfer")
        except ValueError:
            return render(request, 'transferer/transfer.html')

        url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{fromTransfer.lower()}/{transferTo.lower()}.json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            transfered_result = amount * data[transferTo.lower()]
            History.objects.create(
                amount=amount,
                fromTransfer=fromTransfer,
                transfered_result=transfered_result,
                transferTo=transferTo,
            )
            return render(request, 'transferer/transfer.html', {'result': transfered_result, 'transferTo': transferTo})
        else:
            return render(request, 'transferer/transfer.html')
    return render(request, 'transferer/transfer.html')



def transaction_history(request):
    return render(request, 'transferer/history.html', {'transactions': History.objects.all()})

