from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from myapp.models import TestModel
from django.http import JsonResponse

# Create your views here.
def example_view(request):
    template = loader.get_template('myTemplate.html')
    return HttpResponse(template.render())

def store_text(request):
    if request.method == 'POST':
        # Retrieve the text to be stored (You mentioned you have the text already)
        text_to_store =  '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''
        # Example: text_to_store = request.POST.get('text_to_store', '')
        
        # Here you would write code to store the text in your database
        # For demonstration, let's just print it
        print("Text to store:", text_to_store)
        try:
            # Create a new instance of TestModel and save the text data to the database
            test_instance = TestModel.objects.create(text_data=text_to_store)
            # Optionally, you can perform additional operations here

            # Return a JSON response indicating the success of the operation
            return JsonResponse({'message': 'Text stored successfully.'})
        except Exception as e:
            # If an error occurs during database operations, return an error response
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # If the request method is not POST, return a method not allowed response
        return JsonResponse({'error': 'Method not allowed.'}, status=405)
    

def display_data(request):
    # Retrieve data from the TestModel model
    data = TestModel.objects.all()
    return render(request, 'display_data.html', {'data': data})