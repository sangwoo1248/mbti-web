from typing import List


def calculate_mbti(answers: List[str]) -> str:
    """
    답변 리스트를 받아서 MBTI 유형을 계산합니다.
    
    answers 예시: ["E", "N", "F", "P", "E", "S", ...]
    각 답변은 E/I, S/N, T/F, J/P 중 하나
    """
    if not answers:
        return "INFP"  # 기본값
    
    # 각 지표별 카운트
    counts = {
        "E": 0, "I": 0,
        "S": 0, "N": 0,
        "T": 0, "F": 0,
        "J": 0, "P": 0,
    }
    
    for answer in answers:
        answer = answer.upper().strip()
        if answer in counts:
            counts[answer] += 1
    
    # 각 축에서 더 높은 쪽 선택
    ei = "E" if counts["E"] >= counts["I"] else "I"
    sn = "S" if counts["S"] >= counts["N"] else "N"
    tf = "T" if counts["T"] >= counts["F"] else "F"
    jp = "J" if counts["J"] >= counts["P"] else "P"
    
    return f"{ei}{sn}{tf}{jp}"
