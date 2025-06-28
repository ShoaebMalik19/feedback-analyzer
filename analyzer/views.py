from django.shortcuts import render                     # For rendering HTML templates
from transformers import pipeline                       # For loading pre-trained AI model
from .models import Feedback                            # Importing our database model

# Load sentiment analysis model only once (faster performance)
sentiment_model = pipeline("sentiment-analysis")

# Main function to handle homepage and form submission
def home(request):
    result = None  # This will store the result to show in the HTML

    if request.method == 'POST':  # If user submits the form
        text = request.POST.get('feedback')  # Get the feedback text from the form

        # Run sentiment analysis on the input text
        ai_result = sentiment_model(text)[0]  # Returns a dictionary like {'label': 'POSITIVE', 'score': 0.98}

        label = ai_result['label']  # Extract the sentiment label
        score = round(ai_result['score'] * 100, 2)  # Convert score to a percentage and round it

        # Save this feedback and result to the database
        Feedback.objects.create(
            text=text,               # Save the original feedback
            sentiment=label,         # Save the predicted sentiment
            confidence=score         # Save the confidence score
        )

        # Final result string to display on the webpage
        result = f"Sentiment: {label} ({score}%)"

    # Render the result to the webpage
    return render(request, 'home.html', {'result': result})