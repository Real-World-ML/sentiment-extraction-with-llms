## How to build a crypto sentiment parser in 2025

With BAML, of course!

- Add it to the project
```sh
uv add baml-py
```

- Generate some starter `*.baml` files
```sh
uv run baml-cli init
```


- Generate the baml client python files in `baml_client`
```sh
uv run baml-cli generate
```

Use the `resume.baml` as inspiration to build our crypto sentiment parser

```baml
class CryptoSentiment {
  coin Coin
  score Score
  reason string
}

enum Coin {
  Bitcoin
  Ethereum
}

enum Score {
  Positive @description("Positive sentiment")
  Negative @description("Negative sentiment")
  Neutral @description("Neutral sentiment")
}

function ExtractCryptoSentiment(news: string) -> CryptoSentiment[] {
  
  client CustomSonnet // Set ANTRHOPIC_API_KEY to use this client.
  prompt #"
    You are an expert crypto financial analyst with deep knowledge of market dynamics and sentiment analysis.
    Analyze the following news story and determine its potential impact on crypto asset prices.
    Focus on both direct mentions and indirect implications for each asset.

    Do not output data for a given coin if the news is not relevant to it.
    
    Provide a reason behind each score, in one straightforward sentence.
    {{ news }}

    {{ ctx.output_format }}
  "#
}

test news_1 {
  functions [ExtractCryptoSentiment]
  args {
    news #"
      Fed Chair Jerome Powell said in a recent speech that the central bank is closely monitoring inflation and may consider further rate hikes if necessary. This has led to speculation about the potential impact on Bitcoin and Ethereum prices.
      Additionally, the recent partnership between Visa and a leading blockchain platform has sparked interest in the future of digital payments and their implications for cryptocurrencies.
      Bitcoin has seen a surge in interest from institutional investors, while Ethereum's transition to proof-of-stake is expected to enhance its scalability and security.
    "#
  }
}

test news_2 {
  functions [ExtractCryptoSentiment]
  args {
    news #"
      FED will raise interest rates.
    "#
  }
}
```