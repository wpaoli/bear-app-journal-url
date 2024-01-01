from flask import Flask, redirect
from datetime import datetime, timedelta

app = Flask(__name__)

def get_current_week_dates():
    current_date = datetime.now()
    start_of_week = current_date - timedelta(days=current_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

@app.route('/generate-bear-url')
def generate_bear_url():
    start_of_week, end_of_week = get_current_week_dates()
    year_str = start_of_week.strftime("%Y")
    week_number = start_of_week.isocalendar()[1]
    url = f"bear://x-callback-url/create?title=Week%20{week_number}%2C%20{start_of_week.strftime('%b %d')}%20-%20{end_of_week.strftime('%b %d')}&tags={year_str}%2Fweek%2F{week_number}"
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
