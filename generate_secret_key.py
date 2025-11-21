#!/usr/bin/env python
"""
Quick script to generate a Django secret key for production use.
Run: python generate_secret_key.py
"""
from django.core.management.utils import get_random_secret_key

if __name__ == '__main__':
    secret_key = get_random_secret_key()
    print("\n" + "="*60)
    print("Generated Django Secret Key:")
    print("="*60)
    print(secret_key)
    print("="*60)
    print("\nCopy this key and add it to your environment variables as SECRET_KEY")
    print("Never commit this key to version control!\n")

