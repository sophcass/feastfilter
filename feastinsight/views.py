from django.shortcuts import render
from .forms import TextInputForm
from feastinsight.ai_functions import openai_functions, anthropic_functions

def chat_bot_view(request):
    result = None
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            model_choice = request.POST.get('model_choice')

            # Call the appropriate function based on model choice
            if model_choice == 'openai':
                result = openai_functions.get_restaurant_recommendation(input_text)
            elif model_choice == 'anthropic':
                result = anthropic_functions.get_restaurant_recommendation(input_text)
    else:
        form = TextInputForm()
    return render(request, "feastinsight/chat_bot.html", {'form': form, 'result': result})

def home_view(request):
    return render(request, "feastinsight/home.html")