def sum_multiples(num):
    m_5 = (i for i in range(5, num, 5))
    m_3 = (i for i in range(3, num, 3))
    m_15 = (i for i in range(15, num, 15))

    return sum(set(m_15).symmetric_difference(m_3) | set(m_15).symmetric_difference(m_5))


print(sum_multiples(1000))
