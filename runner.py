def run():
    from transformers import pipeline, set_seed
    generator = pipeline('text-generation', model='openai-gpt')
    set_seed(42)
    x = generator("The man worked as a", max_length=10, num_return_sequences=5)
    return x