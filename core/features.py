import re

def extract_features(comment):
    """
    Convert comment into a feature dict for spam detection
    """
    features = {}
    features['length'] = len(comment)
    features['has_url'] = int(bool(re.search(r'http[s]?://', comment)))
    features['has_keywords'] = int(bool(re.search(r'(earn money|DM me|WhatsApp|free)', comment, re.IGNORECASE)))
    features['all_caps'] = int(comment.isupper())
    return features
