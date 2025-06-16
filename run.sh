#!/bin/bash

# Check if .env.docker file exists
if [ ! -f .env.docker.enc ]; then
    echo "Error: .env.docker file not found"
    exit 1
fi

#Decrytp.env.enc file
ENC_FILE="backend/.env.enc"
DEC_FILE="backend/.env"
openssl enc -d -aes-256-cbc -salt -in "$ENC_FILE" -out "$DEC_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to decrypt $ENC_FILE"
    exit 1
fi

# Decrypt.env.docker file
ENC_FILE=.env.docker.enc
DEC_FILE=.env.docker
openssl enc -d -aes-256-cbc -salt -in "$ENC_FILE" -out "$DEC_FILE"
if [ $? -ne 0 ]; then
    echo "Error: Failed to decrypt $ENC_FILE"
    exit 1
fi

# Read each line from .env.docker and export variables
while IFS= read -r line || [ -n "$line" ]; do
    # Skip empty lines and comments
    if [[ -z "$line" || "$line" =~ ^# ]]; then
        continue
    fi
    
    # Remove any trailing comments
    line=$(echo "$line" | sed 's/#.*$//')
    
    # Trim whitespace
    line=$(echo "$line" | xargs)
    
    # Export the variable
    if [[ "$line" =~ ^[A-Za-z_][A-Za-z0-9_]*= ]]; then
        export "$line"
        echo "Exported: $line"
    fi
done < .env.docker

docker compose build --no-cache

docker compose up -d

rm .env.docker

rm "backend/.env"