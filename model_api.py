from transformers import pipeline
import gradio as gr

# Загружаем предобученную модель, явно указываем PyTorch
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", framework="pt")

# Функция для предсказания
def predict_sentiment(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    return f"Настроение: {label}, Уверенность: {score:.2f}"

# Создаем Gradio-интерфейс
iface = gr.Interface(fn=predict_sentiment, inputs="text", outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860, share=False)