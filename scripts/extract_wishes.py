#!/usr/bin/env python3
"""
Extract "Dear #Internet" tweets from Will's Twitter archive.
Appends to existing WISHES.md file.
"""

import json
import re
from datetime import datetime

def extract_wishes(tweets_file, output_file):
    """Extract tweets containing 'Dear' wishes."""
    with open(tweets_file, 'r') as f:
        tweets = json.load(f)
    
    wishes = []
    patterns = [
        r'Dear #?\w+:',  # Dear #Internet: / Dear Internet:
        r'Dear \w+,',     # Dear Internet,
    ]
    
    for item in reversed(tweets):  # Oldest first
        tweet = item.get('tweet', {})
        text = tweet.get('full_text') or tweet.get('text', '')
        created_at = tweet.get('created_at', '')
        
        # Check if tweet matches wish pattern
        if any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns):
            # Parse date
            try:
                dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
                year = dt.year
            except:
                year = 'unknown'
            
            wishes.append({
                'text': text,
                'date': created_at,
                'year': year
            })
    
    # Group by year
    wishes_by_year = {}
    for wish in wishes:
        year = wish['year']
        if year not in wishes_by_year:
            wishes_by_year[year] = []
        wishes_by_year[year].append(wish)
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write("# Dear #Internet — Extended Archive (2018-2025)\\n\\n")
        f.write("**Source:** wbic16 Twitter archive\\n")
        f.write("**Extracted:** 2026-02-08\\n")
        f.write("**Tool:** extract_wishes.py\\n\\n")
        f.write("---\\n\\n")
        
        for year in sorted(wishes_by_year.keys()):
            f.write(f"## {year}\\n\\n")
            for wish in wishes_by_year[year]:
                f.write(f"* {wish['text']}\\n\\n")
    
    print(f"Extracted {len(wishes)} wishes")
    print(f"Years covered: {sorted(wishes_by_year.keys())}")
    print(f"Output: {output_file}")

if __name__ == '__main__':
    extract_wishes(
        '/source/exo-archives/wbic16/tweets.json',
        '/source/exo-archives/WISHES_2018_2025.md'
    )
