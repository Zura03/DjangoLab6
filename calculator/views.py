from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'calculator/index.html')

def calculate(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operation = request.POST.get('operation')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return HttpResponse("Cannot divide by zero.")
            result = num1 / num2
        else:
            return HttpResponse("Invalid operation selected.")
        
        return render(request, 'calculator/result.html', {'result': result})
    else:
        return HttpResponse("Method not allowed.")
