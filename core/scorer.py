def score_comment(features):
    """
    Simple scoring system for spam detection
    """
    score = 0
    score += features['has_url'] * 2
    score += features['has_keywords'] * 3
    score += features['all_caps'] * 1
    return min(score / 6, 1.0)
