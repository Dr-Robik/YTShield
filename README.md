# YTShield

YTShield is a Python-based security and machine learning tool designed to analyze YouTube video comments and detect spam or potentially malicious content. The goal of the project is to simulate a lightweight content moderation and threat detection system using NLP techniques.

From a security perspective, the tool demonstrates how machine learning can be used to identify common spam patterns such as phishing attempts, promotional abuse, bot-generated messages, and suspicious external links in comment sections.

---

## What the tool does 

YouTube comment sections are often abused for:

- phishing links
    
- fake giveaways
    
- channel hijacking attempts
    
- automated bot promotion
    
- malicious redirects
    
- scam advertisements
    

YTShield attempts to detect these behaviors by analyzing text patterns in comments and classifying them as either normal or spam.

It does not understand intent like a human, but instead relies on learned statistical patterns from previously labeled datasets.

---

## How it works

The system follows a typical security analysis pipeline:

1. **Data collection**  
    Comments are fetched from YouTube using the official API. This simulates real-world threat intelligence gathering from a live platform.
    
2. **Preprocessing**  
    Raw comment text is cleaned by removing URLs, special characters, and noise. This is important because attackers often try to bypass filters using obfuscation techniques.
    
3. **Feature extraction**  
    Text is converted into numerical representations using TF-IDF, which captures the importance of words and word combinations in spam detection.
    
4. **Classification model**  
    A Logistic Regression model is trained to distinguish between legitimate and spam-like behavior based on historical labeled data.
    
5. **Decision output**  
    Each comment is assigned a probability score indicating how likely it is to be spam.
    

---

## Security relevance

Although this is a lightweight ML project, it reflects real-world security concepts:

- Content moderation systems used by social media platforms
    
- Anti-spam filtering engines used in messaging systems
    
- Threat intelligence classification pipelines
    
- Pattern recognition systems for abuse detection
    

The same approach can be extended to detect:

- phishing URLs in comments
    
- social engineering attempts
    
- coordinated bot activity
    
- scam campaigns across platforms
    

---

## Current state 

YTShield is still in an early development stage and is not yet 100% ready. While it can detect many obvious spam patterns, it also produces false positives in some cases, especially with legitimate promotional content or ambiguous messages.

We are actively working on improving model accuracy, reducing false positives, and enhancing the system with more advanced detection techniques.
