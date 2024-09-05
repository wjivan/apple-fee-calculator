# App Store Fee Calculator

Live Demo: https://apple-fee-calculator-90781680a2e3.herokuapp.com/

This project provides a web-based calculator to help developers estimate and compare fees under different Apple App Store commission structures, including the new terms introduced in 2024.

## Project Overview

The App Store Fee Calculator allows developers to input their app's financial details and receive a breakdown of fees under various scenarios. It takes into account different fee structures, including existing terms, alternative terms, and their variations with link-out options.

## Features

- Calculate fees under four different scenarios:
  1. Existing terms
  2. Existing terms with link-out
  3. Alternative terms
  4. Alternative terms with link-out
- Consider Small Business Program eligibility
- Account for Core Technology Fee (CTF) in alternative terms
- Visualize fee breakdowns with a stacked bar chart
- Responsive web design for ease of use on various devices

## Calculations

The calculator performs the following fee calculations:

1. Existing Terms:
   - Standard: 30% of developer's in-app revenue
   - Small Business Program: 15% of developer's in-app revenue

2. Existing Terms + Link Out:
   - First year:
     * Standard: 25% of developer's in-app revenue
     * Small Business Program: 12% of developer's in-app revenue

3. Alternative Terms:
   - Standard: 20% of developer's in-app revenue
   - Small Business Program: 13% of developer's in-app revenue
   - Includes Core Technology Fee (CTF) calculation

4. Alternative Terms + Link Out:
   - First year:
     * Standard: 15% of developer's in-app revenue
     * Small Business Program: 10% of developer's in-app revenue
   - Includes Core Technology Fee (CTF) calculation

Core Technology Fee (CTF) Calculation:
- €0.50 per install over 1 million
- Exemption for developers with less than €10M in annual revenue
- Cap of €1M for developers with €10M-€50M in annual revenue

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- Plotly (for chart generation)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/app-store-fee-calculator.git
   ```

2. Navigate to the project directory:
   ```
   cd app-store-fee-calculator
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open a web browser and navigate to `http://localhost:8000`

## Usage

1. Enter your app's financial details in the provided form.
2. Click "Calculate Fees" to see the breakdown of fees under different scenarios.
3. View the stacked bar chart for a visual comparison of fee structures.

## Contributing

Contributions to improve the calculator or extend its functionality are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

[MIT License](LICENSE)

## Disclaimer

This calculator is for informational purposes only and should not be considered as financial advice. Always refer to official Apple documentation and consult with a professional for accurate financial planning.
