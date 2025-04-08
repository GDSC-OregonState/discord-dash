# Discord Dash

A Discord bot built with `discord.py`, designed to be deployed using Docker for easy setup and management.

## Features

- Automated moderation
- Custom commands
- Integration with third-party APIs
- More features coming soon!

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Setting Up Docker and Docker Compose

### 1. Install Docker

Follow the official installation guide for your operating system:

- **Windows & macOS**: Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- **Linux**: Install Docker using your package manager:
  ```sh
  sudo apt-get update && sudo apt-get install -y docker.io
  ```

### 2. Install Docker Compose

Docker Compose is included with Docker Desktop. On Linux, install it separately:

```sh
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Verify the installation:

```sh
docker-compose --version
```

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/discord-dash.git
cd discord-dash
```

### 2. Create a `.env` file

Inside the project directory, create a `.env` file and add the following:

```env
DISCORD_TOKEN=your-bot-token
```

Replace `your-bot-token` with your actual Discord bot token.

### 3. Running the bot

## Docker Compose (Recommended Setup)

Since the repository already contains the `Dockerfile` and `docker-compose.yml`, you can start the bot easily using Docker Compose.

1. Ensure your `.env` file is set up.
2. Start the bot with:

```sh
docker-compose up -d
```

3. To stop the bot:

```sh
docker-compose down
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, reach out via GitHub Issues or Discord.
