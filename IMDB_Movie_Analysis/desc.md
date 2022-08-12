# IMDB_Movie_Analysis

### Table of Contents
1. [About](#about)
2. [Execution](#execution)
3. [Conclusion](#conclusion)

### About

#### Background

This is my submission to the final project in course provided by the Developer Students Club, Al-Azhar University.  

#### Description

I was provided a dataset with information about movies from the Internet Movie Database, along with a few simple tasks.  
The columns of the data are:  
- Title  
- Release Date
- Color
- Genre
- Language
- Country
- Rating
- Lead Actor
- Director Name
- Lead Actor Facebook Likes
- Cast Facebook Likes (ambiguous)
- Director Facebook Likes
- Movie Facebook Likes
- IMDB Score
- Total Reviews
- Duration in mins
- Gross Revenue
- Budget

#### Objective

The instructions given by the instructors were as follows:  
1. Solve The Provided Tasks in the Notebook
2. Clean the Data
3. Visualize the insights using Tableau

As an analyst I dealed with it as if I am trying to help a new movie producer with a few decisions like choosing the genre, actor, manage expectation of budget, etc...

### Execution

When starting any new Data Analysis project, I like to define the end targets ahead, The Questions!  
The questions I need to answer using the dataset are what help pave the way for the project, in this case they were:  
- What are the most trending Ratings?  
- is Revenue related to Budget?  
- which lead actors or directors to consider?  
- how long should the movie be?  
- what is the range of revenues to be expected nowadays?  
- does doing a movie with more age restriction decrease its score?  

The Next step is usually Wrangling the data, but for this project I had to answer the questions provided first,  
Then comes the wrangling part, which expands to 3 successive steps:  
1. Gather
2. Assess
3. Clean

After Assessing the Data, I found a few missing data, a few outliers, columns with the wrong type, but those were easy fixes,  
The 2 big problems I faced were:  
- The currency was different for each movie  
- The data spanned a lot of years, a lot of countries, with different rating standards.

The currency problem, I discovered it from an outlier (The host's movie budget) that taught me to check outliers before dealing with them :)  
I ended up scraping the currency of each country, then the exchange rate of each currency to euro.  
The code for this can be found in a seperate notebook.

I believe this method is problematic because the exchange rates obviously changed drastically over the past 100 years, besides, the values are not adjusted, meaning it's not fair to compare $10 in 2020 to $10 in 1920, but it should give a general idea.  
and since the main focus is to create a movie now, we won't bother much with old movies :D

The Ratings problem required a little bit of research, and I ended up grouping all similar ratings into one.

And with a few more cleaning, the data is finally ready for EDA and visualizations :D  
You can find the results for that in the conclusion part.

Although the notebook includes visualizations, I also Created a few charts using Tableau Public, you can check them [Here](https://public.tableau.com/profile/khaled.basiony#!/), and swipe through them from the metadata part down the page.

### Code

I used python 3 for this project along with the following libraries:
- pandas
- numpy
- matplotlib
- seaborn
- requests
- beautiful soup 4
- pickle
- Scikit-Learn

At the time of creating this project I was unaware of virtual envs or the command `pip freeze` So unfortunately I can't get the exact versions.

### Conclusion

The insights I was able to get from there are:  
- Half the Revenues fall between 5 Millions and 54 Millions Euros, with an average of 41 Millions.
- Increasing the budget might increase the Revenue, but I wouldn't go crazy with it.
- Increasing the duration doesn't always mean higher score.
- Most age restrictions of the modern era are PG-13 and R which have almost no effect on score apparently.
- A more Popular director is more likely to get a higher score for the movie.
- Actors are generally more popular than directors.

Didn't find the answer to any of the proposed questions? kindly check the notebook for more info.
