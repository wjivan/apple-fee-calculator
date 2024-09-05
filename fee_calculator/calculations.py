# fee_calculator/calculations.py
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import io

def calculate_fees(
    annual_revenue,
    total_installs,
    is_small_business,
    global_revenue,
    third_party_commission_rate,
    apple_revenue_percentage
):
    annual_revenue = float(annual_revenue)
    total_installs = int(total_installs)
    global_revenue = float(global_revenue)
    third_party_commission_rate = float(third_party_commission_rate)
    apple_revenue_percentage = float(apple_revenue_percentage) / 100  # Convert to decimal

    results = {
        'existing_terms': calculate_existing_terms(annual_revenue, is_small_business),
        'existing_terms_link_out': calculate_existing_terms_link_out(annual_revenue, is_small_business, third_party_commission_rate, apple_revenue_percentage),
        'alternative_terms': calculate_alternative_terms(
            annual_revenue, 
            total_installs, 
            is_small_business, 
            global_revenue, 
            third_party_commission_rate,
            apple_revenue_percentage
        ),
        'alternative_terms_link_out': calculate_alternative_terms_link_out(
            annual_revenue, 
            total_installs, 
            is_small_business, 
            global_revenue, 
            third_party_commission_rate,
            apple_revenue_percentage
        )
    }
    
    results['most_cost_effective'] = min(results, key=lambda k: results[k]['total'])
    
    return results

def calculate_existing_terms(annual_revenue, is_small_business):
    rate = 0.15 if is_small_business else 0.30
    fee = annual_revenue * rate
    return {
        'apple_fee': round(fee),
        'third_party_fee': 0,
        'ctf': 0,
        'total': round(fee)
    }

def calculate_existing_terms_link_out(annual_revenue, is_small_business, third_party_commission_rate, apple_revenue_percentage):
    apple_rate = 0.12 if is_small_business else 0.25
    apple_fee = annual_revenue * apple_revenue_percentage * apple_rate
    third_party_fee = annual_revenue * (1 - apple_revenue_percentage) * (third_party_commission_rate / 100)
    total_fee = apple_fee + third_party_fee
    return {
        'apple_fee': round(apple_fee),
        'third_party_fee': round(third_party_fee),
        'ctf': 0,
        'total': round(total_fee)
    }

def calculate_alternative_terms(annual_revenue, total_installs, is_small_business, global_revenue, third_party_commission_rate, apple_revenue_percentage):
    apple_rate = 0.13 if is_small_business else 0.20
    apple_fee = annual_revenue * apple_revenue_percentage * apple_rate
    third_party_fee = annual_revenue * (1 - apple_revenue_percentage) * (third_party_commission_rate / 100)
    ctf = calculate_ctf(total_installs, global_revenue)
    total = apple_fee + third_party_fee + ctf
    return {
        'apple_fee': round(apple_fee),
        'third_party_fee': round(third_party_fee),
        'ctf': round(ctf),
        'total': round(total)
    }

def calculate_alternative_terms_link_out(annual_revenue, total_installs, is_small_business, global_revenue, third_party_commission_rate, apple_revenue_percentage):
    apple_rate = 0.10 if is_small_business else 0.15
    apple_fee = annual_revenue * apple_revenue_percentage * apple_rate
    third_party_fee = annual_revenue * (1 - apple_revenue_percentage) * (third_party_commission_rate / 100)
    ctf = calculate_ctf(total_installs, global_revenue)
    total = apple_fee + third_party_fee + ctf
    return {
        'apple_fee': round(apple_fee),
        'third_party_fee': round(third_party_fee),
        'ctf': round(ctf),
        'total': round(total)
    }

def calculate_ctf(total_installs, global_revenue):
    if global_revenue < 10000000:  # Less than €10M
        return 0  # 3-year exemption
    else:
        ctf = max(0, (total_installs - 1000000) * 0.5)
        if global_revenue < 50000000:  # Between €10M and €50M
            return min(ctf, 1000000)  # Capped at €1M
        else:
            return ctf  # No cap for global revenue >= €50M
        
def generate_chart(results):
    fee_structures = [k for k in results.keys() if k != 'most_cost_effective']
    apple_fees = [results[k]['apple_fee'] for k in fee_structures]
    third_party_fees = [results[k]['third_party_fee'] for k in fee_structures]
    ctf_fees = [results[k]['ctf'] for k in fee_structures]

    fig = go.Figure(data=[
        go.Bar(name='Apple Fee', x=fee_structures, y=apple_fees),
        go.Bar(name='Third Party Fee', x=fee_structures, y=third_party_fees),
        go.Bar(name='CTF', x=fee_structures, y=ctf_fees)
    ])

    fig.update_layout(
        barmode='stack',
        title='Fee Comparison',
        xaxis_title='Fee Structure',
        yaxis_title='Fee Amount (€)',
        height=500
    )

    # Convert plot to static image
    img_bytes = fig.to_image(format="png")
    encoding = base64.b64encode(img_bytes).decode()
    img_b64 = "data:image/png;base64," + encoding

    return img_b64