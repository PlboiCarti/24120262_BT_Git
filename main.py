print("Hello Github")

# 2. Hàm thống kê dãy số nguyên tố
def analyze_primes(numbers):
    """Thống kê số lượng, tổng và danh sách các số nguyên tố"""
    prime_list = [num for num in numbers if is_prime(num)]
    count = len(prime_list)
    total = sum(prime_list)
    
    return {
        "prime_numbers": prime_list,
        "count": count,
        "total": total
    }