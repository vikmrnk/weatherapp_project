# Weather App

A feature-rich Django weather application that allows users to check current weather conditions and forecasts for cities around the world.


## Features

- **Current Weather Data**: Temperature, humidity, wind speed, pressure, and "feels like" temperature
- **5-Day Forecast**: View weather predictions for the next 5 days
- **City Background Images**: Dynamic background images that match the searched city
- **Favorites System**: Save and manage your favorite cities for quick access
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Fallback Data**: Provides sample data when API limits are reached or connections fail
- **Error Handling**: Graceful error display with helpful messages

## Technology Stack

- **Backend**: Django 3.2+
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenWeatherMap API, Google Custom Search API
- **Database**: SQLite (easily upgradeable to PostgreSQL for production)
- **Deployment**: Ready for deployment on any Django-compatible hosting platform

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/weather_app.git
   cd weather_app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a .env file for your environment variables:
   ```
   WEATHER_API_KEY=your_openweathermap_api_key
   GOOGLE_API_KEY=your_google_api_key
   GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser

## API Keys Setup

### OpenWeatherMap API
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)
2. Generate an API key from your account dashboard
3. Add it to your .env file as `WEATHER_API_KEY`

### Google Custom Search API (for city images)
1. Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the Custom Search API
3. Generate an API key
4. Create a Custom Search Engine at [Programmable Search Engine](https://programmablesearchengine.google.com/about/)
5. Add both the API key and Search Engine ID to your .env file

## Project Structure

```
weather_app/
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── static/                 # Static assets
│   └── style.css           # CSS styles
├── templates/              # HTML templates
│   └── index.html          # Main page template
└── weatherapp/             # Main Django app
    ├── admin.py            # Admin panel configuration
    ├── models.py           # Database models
    ├── urls.py             # URL routing
    ├── views.py            # View functions
    └── ...                 # Other Django files
```

## Learning Outcomes

This project was developed to learn and practice:

- Django framework fundamentals (models, views, templates, URLs)
- API integration with multiple fallback strategies
- Caching system implementation for optimization
- Multi-layered error handling
- User session management
- Responsive front-end design
- Environment variables management
- Git version control system

## Author

Viktoriia Kamarenko - [https://github.com/vikmrnk](https://github.com/vikmrnk)