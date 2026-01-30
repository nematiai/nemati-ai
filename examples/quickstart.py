"""
Nemati AI SDK Examples

This file contains example usage of the Nemati AI Python SDK.
"""

from nemati import NematiAI

# Initialize client
client = NematiAI(api_key="nai_live_your_api_key_here")


# ============================================================
# CHAT EXAMPLES
# ============================================================

def chat_example():
    """Basic chat completion example."""
    response = client.chat.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is machine learning?"}
        ],
        model="gpt-4",
        max_tokens=500,
    )
    
    print("Chat Response:")
    print(response.content)
    print(f"Tokens used: {response.usage.total_tokens}")


def chat_streaming_example():
    """Streaming chat example."""
    print("Streaming Response:")
    
    for chunk in client.chat.create(
        messages=[{"role": "user", "content": "Write a haiku about coding."}],
        stream=True,
    ):
        print(chunk.content, end="", flush=True)
    
    print()


# ============================================================
# AI WRITER EXAMPLES
# ============================================================

def writer_example():
    """AI Writer content generation example."""
    content = client.writer.generate(
        prompt="Write a product description for a smart home assistant",
        content_type="product_description",
        tone="professional",
        max_tokens=300,
    )
    
    print("Generated Content:")
    print(content.text)
    print(f"Word count: {content.word_count}")


def writer_template_example():
    """Using templates example."""
    # List available templates
    templates = client.writer.templates.list()
    print("Available Templates:")
    for t in templates[:5]:
        print(f"  - {t.id}: {t.name}")
    
    # Generate from template
    if templates:
        content = client.writer.templates.generate(
            template_id=templates[0].id,
            variables={"topic": "AI in healthcare"}
        )
        print(f"\nGenerated from template:\n{content.text}")


# ============================================================
# IMAGE GENERATION EXAMPLES
# ============================================================

def image_example():
    """Image generation example."""
    image = client.image.generate(
        prompt="A serene mountain lake at sunset, photorealistic",
        size="1024x1024",
        quality="hd",
    )
    
    print(f"Image URL: {image.url}")
    # Save the image
    # image.save("mountain_lake.png")


def image_edit_example():
    """Image editing example."""
    # with open("input.jpg", "rb") as f:
    #     edited = client.image.edit(
    #         image=f,
    #         prompt="Add a rainbow in the sky",
    #         strength=0.5,
    #     )
    #     edited.save("edited.jpg")
    pass


# ============================================================
# TREND DISCOVERY EXAMPLES
# ============================================================

def trends_example():
    """Trend discovery example."""
    trends = client.trends.search(
        query="artificial intelligence",
        platforms=["youtube", "reddit"],
        timeframe="7d",
        limit=10,
    )
    
    print(f"Found {len(trends.items)} trends:")
    for trend in trends.items[:5]:
        print(f"  [{trend.platform}] {trend.title}")
        print(f"    Engagement: {trend.engagement}, Growth: {trend.growth_rate}%")


def youtube_trends_example():
    """YouTube-specific trends example."""
    trends = client.trends.youtube.search(
        query="programming tutorials",
        timeframe="30d",
        sort_by="views",
    )
    
    print("Top YouTube videos:")
    for trend in trends[:5]:
        print(f"  - {trend.title} ({trend.views} views)")


# ============================================================
# MARKET INTELLIGENCE EXAMPLES
# ============================================================

def stock_example():
    """Stock market data example."""
    stock = client.market.stocks.get("AAPL")
    
    print(f"Apple Inc. (AAPL)")
    print(f"  Price: ${stock.price}")
    print(f"  Change: {stock.change_percent}%")
    print(f"  Market Cap: ${stock.market_cap:,.0f}")


def crypto_example():
    """Cryptocurrency data example."""
    btc = client.market.crypto.get("BTC")
    
    print(f"Bitcoin (BTC)")
    print(f"  Price: ${btc.price:,.2f}")
    print(f"  24h Change: {btc.change_percent_24h}%")
    print(f"  24h Volume: ${btc.volume_24h:,.0f}")


# ============================================================
# DOCUMENT EXAMPLES
# ============================================================

def document_example():
    """Document upload and chat example."""
    # Upload document
    # with open("report.pdf", "rb") as f:
    #     doc = client.documents.upload(
    #         file=f,
    #         name="Q4 Report"
    #     )
    # 
    # # Chat with document
    # response = client.documents.chat(
    #     document_id=doc.id,
    #     message="What are the key findings?"
    # )
    # 
    # print(response.answer)
    # for source in response.sources:
    #     print(f"  Source: Page {source.page}")
    pass


# ============================================================
# ACCOUNT EXAMPLES
# ============================================================

def account_example():
    """Account information example."""
    # Get account info
    account = client.account.me()
    print(f"Account: {account.email}")
    print(f"Plan: {account.plan.name}")
    
    # Check credits
    credits = client.account.credits()
    print(f"Credits: {credits.remaining}/{credits.total}")
    
    # Get limits
    limits = client.account.limits()
    print(f"Chat limit: {limits.chat.max_per_day}/day")


# ============================================================
# ASYNC EXAMPLE
# ============================================================

async def async_example():
    """Async client example."""
    from nemati import AsyncNematiAI
    
    async with AsyncNematiAI(api_key="nai_live_xxx") as client:
        response = await client.chat.create(
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.content)


# ============================================================
# RUN EXAMPLES
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Nemati AI SDK Examples")
    print("=" * 50)
    
    # Uncomment to run examples:
    # chat_example()
    # chat_streaming_example()
    # writer_example()
    # image_example()
    # trends_example()
    # stock_example()
    # crypto_example()
    # account_example()
    
    print("\nEdit this file and uncomment examples to run them.")
