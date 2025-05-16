from sentiment import get_sentiment

def main():
    print("Hello from baml-101!")

    news = """
    MicroStrategy to let employees invest in crypto through 401(k) retirement plans
    """

    # Call the example function with the raw resume
    sentiment = get_sentiment(news)
    
    # Print the extracted resume
    print(sentiment)


if __name__ == "__main__":
    main()
