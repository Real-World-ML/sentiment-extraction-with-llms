# Let's build an Agentic Trading Platform. Together

I want to write a blog post title "Let's build an Agentic Trading Platform. Together"

I want it to have 3 sections.

In the first section I want to explain the context. Basically, how it all started 13 years ago, when I landed my first job as a quant analyst.

Then I want to fast forward 13 years to today, where sentiment extraction is a solved problem thanks to LLMs. I now go over the code explanation.
At the end of this section, I ask myself if we could go further than just
sentiment extraction, and I start to think about the whole trading desk.

Can we use semi-autonomous agentic workflows to emulate and outperform the 
trading desks I used to work on 13 years ago?

Invitation to the course.

-----

## How it all started?

It all started 13 years ago, when I landed my first job as a quant analyst.

My role?

Basically building mathematical models to estimate market risk for all financial derivatives at a major
European bank.

Was it exciting?
Yes, of course! It was my dream job back then (the fact that it was the first job out of Maths school probabably helped).

I spent my days fitting stastical models before Machine Learning was cool.
It was all about MATLAB (not my cup of tea, but my best friend at the time).

And it was a lot about talking to traders, the guys at the bank that were using these models
to make trading decisions that fit their (and the bank's) risk appetite.

I entered a trading floor for the first time in my life, and I got a glimpse of what
actual trading looks like.

Bloomberg terminals, fax machines, phone booths.
Risk management, portfolio construction, and of course trading.
One of the things that caught my attention, was the amount of screens showing Bloomberg news 24/7.

Traders would constantly have one eye on their Bloomberg terminal, and the other on Bloomberg news.

Why?

Becuase they knew that some news can really move the market.
So they wanted to be the first to know. Take action and profit.

Back then there was no such thing as Large Language Models. But there were a lot of smart tricks
to extract sentiment from news.

Simple regular expressions, helped quant traders build C++ functions running on Bloomberg terminals,
generating numeric scores for potential market moves.

These inputs were then used to make trading decisions (by traders), that had to be approved by risk management.

That was the Prehistory of my career.

Fast forward 13 years.


## Sentiment extraction is a solved problem

Large Language Models are universal function that can make any given text to any structured output you want.

For example, mapping a piece of market news to a JSON formated list of sentiment scores.

Of course, you need to wrestle a bit with your prompts to get there.

And this is something I want to quickly show you today.

### The tools

We will be using BAML (Basically a Made up Language) to ensure our LLM generate the type of structured output we want.

I personally prefer BAML to all-in-one frameworks like LangChain, as it makes
fast prompt experimentation (the key to success for 99% of LLM problems) easier.

I also strongly recommend you use `uv` to package your project.

For example, to create the project you just need to run:
```sh
uv init crypto-sentiment-parser
```

Nice, let's now install the BAML client and the BAML cli.

```sh
uv add baml-py
```

To generat some boilerplate BAML code under `baml_src` run:

```sh
uv run baml-cli init
```

From this `*.baml` typed files, you can generate the equivalent Python code with:

```sh
uv run baml-cli generate
```

In the BAML language a prompt is a function with strict types. 

You define your types in BAML

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
```

And from there, you prompt becomes a stricly typed function (why on Earth it took so long for some to realize this?).

For example, here is the `ExtractCryptoSentiment` function, that maps a string to a list
of `CryptoSentiment` objects.

```baml
// Create a function to extract the resume from a string.
function ExtractCryptoSentiment(news: string) -> CryptoSentiment[] {
  
  client CustomSonnet // Set ANTHROPIC_API_KEY to use this client.
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
```

From here, the BAML client will generate the Python code for you and put it in the `baml_client` folder.

So, whenver you need to invoke this very simple sentiment extraction agent, you just need to do:

```python
from baml_client.sync_client import b
from baml_client.types import CryptoSentiment

def get_sentiment(news: str) -> list[CryptoSentiment]: 
  return b.ExtractCryptoSentiment(news)
```

If you want to play around, check out this repository


## What's next?

Building a sentiment extraction parser is very cool and all that.
But this is just one piece of the trading puzzle.

Tradins smartly is all about:

> Finding a trading idea
> Testing with hard data if this idea is really a goo idea
> Executing the idea

So my next question is:

Can we solve this hard problem by building a semi-autonomous agentic platform?

And you know what?

I think WE can.

And I want you to join me in this journey.


## Want to build an agentic trading platform, together?

On October 6th, I will start the first cohort of my new live course "Let's build an agentic trading platform. Together".

We will work super hard for 8-weeks and live code together 50+ hours, to build from scratch
a semi-autonomous production-ready agentic system for trading, that we will deploy and operate on Kubernetes.

Along this 8-week journey, you will learn how to:

> Map a business problem to an AI system solution with a real world example.
> Universal design patterns for building real time agentic systems.
> Real time data processing, transport (Kafka), and storage (Real time DBs and VectorDBs).
> Structured output generation and tool usage to guide agents to success.
> Vanilla, RAG and Agentic RAG to increase model output quality.
> Tool server design and implementation.
> Containerization with Docker and deployment with Kubernetes.
> Continuous Integration and Continuous Deployment with Kubernetes.
> Production-ready LLM serving with Nvidia NIM.

And you know what?

We won't be alone. Marius Rugan, the most talented Infrastructure engineer I have met in my life, will be in charge of the Ops part of the course. He brings to the table 20 years of experience building, operating and scaling infrastructure for top tier companies, both in finance and in retail.

I will lead the Software/AI/LLM/however-this-this-will-be-called in 2026 engineering.

We are **not** here to teach you how to trade and earn money - we are here to teach you how to build production-ready agentic systems (in this case a semi-autonomous agentic trading system that assists the end user in the decision-making process and execution).

This is not a course for AI tourists.
This is a course for AI hard-core builders who want to understand both the big picture and the million low-level details to implement, deploy and operate a production-ready cost-effective agentic system on Kubernetes.

Do you want to join us in this journey?

[testimonial]

## Gift 🎁
As a subscriber to the Real World ML Newsletter you have exclusive access to a 50% discount if you enroll in the following 72 hours.

It will never get cheaper than this, so grab it before I change my mind. 😉

[Get 50% OFF TODAY]

See you on the other side,

Pau