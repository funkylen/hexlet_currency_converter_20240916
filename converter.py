def convert(original_currency, result_currency, original_amount, currencies):
    original_currency_value = currencies[original_currency]
    result_currency_value = currencies[result_currency]
    coefficient = result_currency_value / original_currency_value
    result_amount = coefficient * original_amount

    return round(result_amount, 2)
