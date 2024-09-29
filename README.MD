![image](https://github.com/acrobyte007/movie_recommendation/blob/main/Movie.PNG)

# Movie Recommendation System
[http://52.66.197.41:8501/]

This project is deployed on an AWS EC2 instance running on a Linux operating system.



## Project Overview
This project is a Movie Recommendation System that leverages advanced Natural Language Processing (NLP) techniques to analyze movie descriptions and reviews, providing personalized movie suggestions based on user preferences.

## Features

### NLP and Text Processing
- Applied advanced NLP techniques to extract insights from movie descriptions and reviews.
- Processed and cleaned text data to prepare it for the recommendation engine.

### Recommendation Engine
- Built a content-based recommendation system using cosine similarity to suggest movies that align with user preferences.

### Multi-feature Selection
- Implemented interactive UI components that allow users to explore movie recommendations based on:
  - Genres
  - Cast members
  - Crew roles

### Data Handling
- Processed movie metadata from CSV files.
- Handled similarity scores from pickle files to ensure efficient retrieval and display of recommendations.

### User Interface
- Designed a user-friendly interface with Streamlit.
- Enhanced visual appeal and usability with customized CSS.

## Skills Demonstrated
- **Python**: Core programming language used for developing the recommendation engine.
- **Pandas**: Utilized for data manipulation and analysis.
- **Machine Learning**: Applied for developing the recommendation algorithms.
- **Streamlit**: Used for creating the interactive web application.
- **Git**: Employed for version control and project management.

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/acrobyte007/movie_recommendation/tree/main
   cd movie-recommendation-system
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## File Structure

- `app.py`: Main application file containing the Streamlit app code.
- `data/`: Directory containing movie metadata CSV files and similarity score pickle files.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation file.

## Usage

1. Open the application link in your web browser.
2. Use the interactive UI components to filter and explore movie recommendations based on your preferences.

## Contributing

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.


---

