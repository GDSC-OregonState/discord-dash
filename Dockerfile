FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot code into the container
COPY . .

# Set environment variables (optional, can be overridden at runtime)
ENV TOKEN="your-discord-bot-token-here"

# Run the bot
CMD ["python", "bot.py"]